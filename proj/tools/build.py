#!/usr/bin/env python3
"""
build.py — génère site/ depuis courses/ selon SPEC-SITE.md.

Contrat (rappel du gabarit d'origine) :
  1. exécute tools/validate.py ; échoue si une erreur E est présente ;
  2. charge toutes les fiches, calcule les dérivés (A9) : D^-1, A^-1, socle D^+, niveau ;
  3. exécute tools/tests/test_layout.py ; échoue si un test échoue ;
  4. produit les pages listées dans SPEC-SITE.md §3, autonomes, ouvrables en file:// ;
  5. options : --offline (copie MathJax dans site/vendor/), --course <code>.

Dépendances : pyyaml uniquement. Aucune requête réseau au build hors --offline.

Rien n'est écrit dans courses/ : ce programme ne fait que lire.
"""
from __future__ import annotations
import argparse, html, importlib.util, json, re, shutil, subprocess, sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml manquant : pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# PowerShell rend la sortie en cp1252 : on force UTF-8 pour que le build soit
# identique sur macOS et sur Windows 11.
for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

RACINE = Path(__file__).resolve().parent.parent
MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
MAX_LISTE = 7          # SPEC-SITE §2 règle 4
TAILLE_MAX = 300_000   # SPEC-SITE §4 : une page ≤ 300 ko hors MathJax

# l'algorithme de l'arbre vit dans le test ; on en importe les constantes (SPEC-SITE §5)
_spec = importlib.util.spec_from_file_location("test_layout", RACINE / "tools" / "tests" / "test_layout.py")
_tl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tl)
CARTE_W, COL_C, ECART_G = _tl.W, _tl.C, _tl.G


# ================================================================ 1. chargement

def lire_fiche(path: Path):
    """Même découpage que validate.py : en-tête YAML, puis sections « ## »."""
    txt = path.read_text(encoding="utf-8")
    _, fm, body = txt.split("---\n", 2)
    meta = yaml.safe_load(fm) or {}
    sections, cur, buf = [], None, []
    for line in body.splitlines():
        if line.startswith("## "):
            if cur is not None:
                sections.append((cur, "\n".join(buf).strip()))
            cur, buf = line[3:].strip(), []
        else:
            buf.append(line)
    if cur is not None:
        sections.append((cur, "\n".join(buf).strip()))
    return meta, sections


def charger(root: Path):
    m = dict(cours={}, N={}, a_venir={}, exercices={}, rapports=[])
    for cdir in sorted(p for p in (root / "courses").iterdir() if p.is_dir()):
        code = cdir.name
        meta = yaml.safe_load((cdir / "course.yml").read_text(encoding="utf-8")) or {}
        nota = yaml.safe_load((cdir / "notation.yml").read_text(encoding="utf-8")) if (cdir / "notation.yml").exists() else {}
        inv = yaml.safe_load((cdir / "inventaire.yml").read_text(encoding="utf-8")) if (cdir / "inventaire.yml").exists() else {}
        av = yaml.safe_load((cdir / "a-venir.yml").read_text(encoding="utf-8")) if (cdir / "a-venir.yml").exists() else []
        m["cours"][code] = dict(
            code=code, meta=meta, notions=[],
            notation=(nota or {}).get("symboles", []) or [],
            collisions=(nota or {}).get("collisions", []) or [],
            inventaire=(inv or {}).get("elements", []) or [],
            exercices=[],
        )
        for it in av or []:
            m["a_venir"][it["id"]] = it
        for f in sorted((cdir / "notions").glob("*.md")):
            fm, secs = lire_fiche(f)
            if fm.get("statut") == "retiree":       # SPEC-INGESTION : sort du site, reste au dépôt
                continue
            fm.setdefault("statut", "source")
            m["N"][fm["id"]] = dict(meta=fm, sections=secs, cours=code, fichier=str(f.relative_to(root)))
            m["cours"][code]["notions"].append(fm["id"])
        edir = cdir / "exercices"
        if edir.is_dir():
            for f in sorted(edir.glob("*.md")):
                fm, secs = lire_fiche(f)
                m["exercices"][fm["id"]] = dict(meta=fm, sections=secs, cours=code, slug=f.stem)
                m["cours"][code]["exercices"].append(fm["id"])
    rdir = root / "rapports"
    if rdir.is_dir():
        for f in sorted(rdir.glob("*.md")):
            m["rapports"].append(dict(slug=f.stem, texte=f.read_text(encoding="utf-8")))
    return m


# ================================================================ 2. dérivés (A9)

def deriver(m):
    N = m["N"]
    D = {i: [x for x in (n["meta"].get("construite_a_partir_de") or []) if isinstance(x, str)] for i, n in N.items()}
    A = {i: n["meta"].get("cas_de") for i, n in N.items()}
    D_inv, A_inv = defaultdict(list), defaultdict(list)
    for x, ys in D.items():
        for y in ys:
            D_inv[y].append(x)
    for x, y in A.items():
        if y:
            A_inv[y].append(x)
    for d in (D_inv, A_inv):
        for k in d:
            d[k].sort(key=lambda i: nom_de(m, i).lower())

    # niveau : longueur du plus long chemin vers une source de D.
    # Un identifiant « à venir » n'a pas de dépendance connue : il compte pour un niveau 0.
    niveau, encours = {}, set()
    def ell(i):
        if i not in N:
            return 0
        if i in niveau:
            return niveau[i]
        if i in encours:       # A3 garantit l'absence de cycle ; garde-fou
            return 0
        encours.add(i)
        v = 0 if not D[i] else 1 + max(ell(y) for y in D[i])
        encours.discard(i)
        niveau[i] = v
        return v
    for i in N:
        ell(i)

    def socle(i):
        """D^+ : la fermeture transitive des dépendances, ordonnée par niveau croissant."""
        vus, pile = [], list(D.get(i, []))
        seen = set()
        while pile:
            y = pile.pop()
            if y in seen:
                continue
            seen.add(y)
            vus.append(y)
            pile.extend(D.get(y, []))
        return sorted(vus, key=lambda y: (ell(y), nom_de(m, y).lower()))

    m["D"], m["A"], m["D_inv"], m["A_inv"] = D, A, dict(D_inv), dict(A_inv)
    m["niveau"] = niveau
    m["socle"] = {i: socle(i) for i in N}
    return m


def nom_de(m, i):
    if i in m["N"]:
        return m["N"][i]["meta"].get("nom", i)
    return i.split("/", 1)[-1].replace("-", " ")


def est_ajout(m, i):
    return i in m["N"] and m["N"][i]["meta"].get("statut") == "ajout"


# ================================================================ 3. Markdown

def esc(s: str) -> str:
    return html.escape(s, quote=False)


MARQUEUR = re.compile(r"\[([^\[\]]+)\]\s*$")
_MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$|`[^`\n]+`", re.S)
_ID = re.compile(r"(?<![\w/-])([a-z]{2,8}/[a-z0-9][a-z0-9-]*)(?![\w/-])")


def _proteger(txt, bac):
    def r(mo):
        bac.append(mo.group(0))
        return "\x00%d\x00" % (len(bac) - 1)
    return _MATH.sub(r, txt)


def _restaurer(txt, bac):
    def r(mo):
        brut = bac[int(mo.group(1))]
        if brut.startswith("`"):
            return "<code>" + esc(brut[1:-1]) + "</code>"
        return esc(brut)          # les maths restent du texte : MathJax les lira
    return re.sub("\x00(\\d+)\x00", r, txt)


def enligne(txt, ctx=None):
    """Inline Markdown, maths et code protégés, identifiants connus transformés en liens."""
    bac = []
    t = _proteger(txt, bac)
    t = esc(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
    if ctx:
        t = _ID.sub(lambda mo: _lien_id(mo.group(1), ctx) or mo.group(1), t)
    return _restaurer(t, bac)


def _lien_id(ident, ctx):
    m, rel = ctx["m"], ctx["rel"]
    if ident in m["N"]:
        c, s = ident.split("/", 1)
        return '<a href="%s%s/n/%s.html">%s</a>' % (rel, c, s, esc(nom_de(m, ident)))
    if ident in m["exercices"]:
        c, s = ident.split("/", 1)
        return '<a href="%s%s/exercices/%s.html">%s</a>' % (rel, c, s, esc(ident))
    return None


def _marqueur_html(marq):
    toks = [t.strip() for t in marq.split(",")]
    if all(t == "ajout" for t in toks):
        return '<span class="marq marq-ajout" title="assertion de l\'opérateur, absente de la source">ajout</span>', True
    return '<span class="marq" title="référence à la source">' + esc("[" + ", ".join(toks) + "]") + "</span>", False


def _decouper(texte):
    """Blocs séparés par une ligne vide — même découpage que validate.blocs()."""
    out, cur = [], []
    for line in texte.splitlines():
        if line.strip() == "":
            if cur:
                out.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        out.append(cur)
    return out


def _table(lignes, ctx, fiche):
    marq = ""
    if not lignes[-1].lstrip().startswith("|"):
        mo = MARQUEUR.search(lignes[-1])
        if mo and fiche:
            marq = mo.group(1)
        lignes = lignes[:-1]
    cells = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lignes]
    cells = [c for c in cells if not all(re.fullmatch(r":?-{2,}:?", x or "-") for x in c)]
    if not cells:
        return ""
    chip, aj = _marqueur_html(marq) if marq else ("", False)
    out = ['<div class="tablebloc%s">' % (" is-ajout" if aj else ""), "<table><thead><tr>"]
    out += ["<th>" + enligne(c, ctx) + "</th>" for c in cells[0]]
    out.append("</tr></thead><tbody>")
    for row in cells[1:]:
        out.append("<tr>" + "".join("<td>" + enligne(c, ctx) + "</td>" for c in row) + "</tr>")
    out.append("</tbody></table>")
    if chip:
        out.append('<p class="marqligne">' + chip + "</p>")
    out.append("</div>")
    return "".join(out)


def _liste(lignes, ctx, fiche):
    out = ["<ul>"]
    for l in lignes:
        item = l.strip()[2:] if l.strip().startswith(("- ", "* ")) else l.strip()
        chip, aj = "", False
        if fiche:
            mo = MARQUEUR.search(item)
            if mo:
                chip, aj = _marqueur_html(mo.group(1))
                item = item[: mo.start()].rstrip()
        out.append('<li%s>%s%s</li>' % (' class="is-ajout"' if aj else "", enligne(item, ctx), (" " + chip) if chip else ""))
    out.append("</ul>")
    return "".join(out)


def rendre(texte, ctx=None, fiche=False, niveau_titre=3):
    """Markdown minimal : titres, tables, listes, paragraphes. fiche=True extrait les
    marqueurs de traçabilité (A11) en fin de bloc et marque les blocs « ajout »."""
    out = []
    for lignes in _decouper(texte):
        prem = lignes[0].lstrip()
        if prem.startswith("#"):
            n = len(prem) - len(prem.lstrip("#"))
            t = min(6, niveau_titre + n - 1)
            out.append("<h%d>%s</h%d>" % (t, enligne(prem[n:].strip(), ctx), t))
            if len(lignes) > 1:
                out.append(rendre("\n".join(lignes[1:]), ctx, fiche, niveau_titre))
            continue
        if prem.startswith("|"):
            out.append(_table(lignes, ctx, fiche))
            continue
        if prem.startswith(("- ", "* ")):
            out.append(_liste(lignes, ctx, fiche))
            continue
        chip, aj = "", False
        corps = list(lignes)
        if fiche:
            mo = MARQUEUR.search(corps[-1])
            if mo:
                chip, aj = _marqueur_html(mo.group(1))
                corps[-1] = corps[-1][: mo.start()].rstrip()
        txt = "\n".join(corps).strip()
        cls = ' class="is-ajout"' if aj else ""
        if not txt and chip:
            out.append("<p%s>%s</p>" % (cls, chip))
        elif txt:
            out.append("<p%s>%s%s</p>" % (cls, enligne(txt, ctx), (" " + chip) if chip else ""))
    return "".join(out)


# ================================================================ 4. ressources

CSS = """
:root{
  --bg:#fbfaf7; --bg2:#f3f0ea; --fg:#1b1a17; --mut:#6c675d; --fai:#8e887c;
  --li:#e0dbd1; --li2:#cdc6b8; --card:#ffffff; --acc:#8a4f23; --acc2:#f3e7dc;
  --ajo:#6d5a8c; --ajo2:#efe9f5; --lim:#9a3a2e; --ok:#3f6b46; --faute:#a8631a;
  --r:8px; --w:min(72rem,100%);
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --serif:ui-serif,Georgia,"Iowan Old Style","Times New Roman",serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#16161a; --bg2:#1e1e23; --fg:#e9e6e0; --mut:#a49e94; --fai:#837d73;
  --li:#32323a; --li2:#45454f; --card:#1c1c21; --acc:#e0a078; --acc2:#332720;
  --ajo:#b6a2d6; --ajo2:#2a2333; --lim:#e08d80; --ok:#8fbf98; --faute:#e2a457;
}}
:root[data-theme="dark"]{
  --bg:#16161a; --bg2:#1e1e23; --fg:#e9e6e0; --mut:#a49e94; --fai:#837d73;
  --li:#32323a; --li2:#45454f; --card:#1c1c21; --acc:#e0a078; --acc2:#332720;
  --ajo:#b6a2d6; --ajo2:#2a2333; --lim:#e08d80; --ok:#8fbf98; --faute:#e2a457;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--serif);
  font-size:17px;line-height:1.62;overflow-wrap:break-word}
a{color:var(--acc);text-decoration-thickness:1px;text-underline-offset:2px}
a:hover{text-decoration-style:dotted}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px;border-radius:3px}
.wrap{width:var(--w);margin:0 auto;padding:0 1rem}

/* ---- barre du haut ---- */
header.top{position:sticky;top:0;z-index:40;background:var(--bg2);
  border-bottom:1px solid var(--li);font-family:var(--sans)}
.topin{width:var(--w);margin:0 auto;padding:.45rem 1rem;display:flex;gap:.6rem;align-items:center;flex-wrap:wrap}
.brand{font-weight:600;font-size:.95rem;text-decoration:none;color:var(--fg);letter-spacing:.02em}
.fil{color:var(--mut);font-size:.82rem;flex:1 1 8rem;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fil a{color:var(--mut)}
.btn{font:inherit;font-size:.78rem;font-family:var(--sans);background:var(--card);color:var(--fg);
  border:1px solid var(--li2);border-radius:var(--r);padding:.2rem .55rem;cursor:pointer}
.btn:hover{border-color:var(--acc)}
.btn[aria-pressed="true"]{background:var(--acc2);border-color:var(--acc);color:var(--fg)}
.rech{position:relative;flex:0 1 16rem;min-width:9rem}
.rech input{width:100%;font:inherit;font-size:.84rem;font-family:var(--sans);padding:.25rem .5rem;
  border:1px solid var(--li2);border-radius:var(--r);background:var(--card);color:var(--fg)}
.res{position:absolute;top:calc(100% + 4px);left:0;right:0;background:var(--card);border:1px solid var(--li2);
  border-radius:var(--r);box-shadow:0 6px 24px rgba(0,0,0,.14);max-height:60vh;overflow:auto;padding:.2rem;margin:0;
  list-style:none;display:none;z-index:50;min-width:18rem}
.res.on{display:block}
.res li a{display:block;padding:.3rem .45rem;border-radius:6px;text-decoration:none;color:var(--fg);font-size:.86rem}
.res li a:hover,.res li.sel a{background:var(--acc2)}
.res .sub{color:var(--mut);font-size:.76rem;font-family:var(--sans)}
.res .vide{padding:.4rem .5rem;color:var(--mut);font-size:.84rem}

main{padding:1.4rem 0 4rem}
h1{font-size:1.75rem;line-height:1.24;margin:.2rem 0 .3rem}
h2{font-size:1.06rem;font-family:var(--sans);font-weight:600;letter-spacing:.01em;margin:0}
h3{font-size:.95rem;font-family:var(--sans);margin:1.2rem 0 .3rem}
p{margin:.55rem 0}
.ptag{font-family:var(--sans);font-size:.74rem;color:var(--mut);text-transform:uppercase;letter-spacing:.08em;margin:0 0 .5rem}

/* ---- métadonnées de fiche ---- */
.meta{display:flex;flex-wrap:wrap;gap:.35rem;align-items:center;font-family:var(--sans);font-size:.75rem;color:var(--mut);margin:.4rem 0 1.1rem}
.pill{border:1px solid var(--li2);border-radius:99px;padding:.06rem .5rem;background:var(--card);white-space:nowrap}
.pill.ajout{color:var(--ajo);border-color:var(--ajo);background:var(--ajo2)}
.pill.typ{background:var(--acc2);border-color:var(--acc)}
.sym{font-family:var(--serif);font-size:1rem;color:var(--fg)}

/* ---- sections ---- */
.sec{border-top:1px solid var(--li);padding:.85rem 0}
.sec.vide{display:none}
details.sec>summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:.45rem;padding:.1rem 0}
details.sec>summary::-webkit-details-marker{display:none}
details.sec>summary::before{content:"›";color:var(--fai);font-family:var(--sans);display:inline-block;
  transition:transform .12s ease;transform:rotate(0deg);width:.7em}
details.sec[open]>summary::before{transform:rotate(90deg)}
details.sec>summary .cnt{font-family:var(--sans);font-size:.74rem;color:var(--fai);font-weight:400}
.corps{padding-top:.25rem}
.gen{border-left:2px solid var(--li2);padding-left:.7rem}
.note{font-family:var(--sans);font-size:.76rem;color:var(--mut);margin:.2rem 0 .4rem}
.sec.lim{border-left:3px solid var(--lim);padding-left:.7rem;background:linear-gradient(90deg,var(--acc2),transparent 60%)}
.sec.faute{border-left:3px solid var(--faute);padding-left:.7rem}
.sec.abs{border-left:3px solid var(--ajo);padding-left:.7rem}
.note.avert{color:var(--ajo);font-weight:600}
.sec.faute>summary h2{color:var(--faute)}
.faute-b{border:1px solid var(--faute);border-left-width:3px;border-radius:var(--r);padding:.5rem .7rem;
  margin:.4rem 0;background:var(--bg2);font-family:var(--sans);font-size:.85rem}
.faute-b strong{color:var(--faute)}
.sec.lim>summary h2{color:var(--lim)}
.sec.lim>h2{color:var(--lim)}

/* ---- marqueurs de traçabilité ---- */
.marq{font-family:var(--sans);font-size:.7rem;color:var(--fai);white-space:nowrap;vertical-align:.12em}
.marq-ajout{color:var(--ajo);background:var(--ajo2);border:1px solid var(--ajo);border-radius:99px;padding:0 .35rem}
.marqligne{margin:.15rem 0 0}
html.sans-ajouts .is-ajout{display:none!important}
.masq{font-family:var(--sans);font-size:.78rem;color:var(--ajo);background:var(--ajo2);border:1px dashed var(--ajo);border-radius:var(--r);padding:.3rem .5rem;margin:.3rem 0}
.sec.estmasq>summary h2,.sec.estmasq>h2{opacity:.65}
.bandeau{font-family:var(--sans);font-size:.8rem;border:1px dashed var(--ajo);background:var(--ajo2);
  color:var(--fg);border-radius:var(--r);padding:.4rem .6rem;margin:.6rem 0}

/* ---- pastilles ---- */
.pasts{display:flex;flex-wrap:wrap;gap:.35rem;margin:.35rem 0;padding:0;list-style:none}
.past{display:inline-block;font-family:var(--sans);font-size:.82rem;text-decoration:none;color:var(--fg);
  background:var(--card);border:1px solid var(--li2);border-radius:99px;padding:.12rem .6rem}
.past:hover{border-color:var(--acc);color:var(--acc)}
.past .cc{color:var(--fai);font-size:.74rem}
.past.ajout{border-color:var(--ajo);color:var(--ajo)}
.past.venir{border-style:dashed;color:var(--fai);text-decoration:line-through;cursor:default}
.past .nv{color:var(--fai);font-size:.7rem;margin-left:.25rem}

/* ---- socle ---- */
.socle{list-style:none;padding:0;margin:.3rem 0}
.socle li{display:flex;gap:.5rem;align-items:baseline;padding:.12rem 0;font-size:.92rem}
.socle input{margin:0;accent-color:var(--ok)}
.socle li.su a{color:var(--fai);text-decoration:line-through}
.compteur{font-family:var(--sans);font-size:.78rem;color:var(--mut)}
.grp{margin:.5rem 0}
.grp>summary{cursor:pointer;font-family:var(--sans);font-size:.8rem;color:var(--mut)}

table{border-collapse:collapse;margin:.5rem 0;font-size:.9rem;display:block;overflow-x:auto;max-width:100%}
th,td{border:1px solid var(--li);padding:.25rem .55rem;text-align:left;vertical-align:top}
th{background:var(--bg2);font-family:var(--sans);font-size:.78rem;font-weight:600}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.86em;
  background:var(--bg2);border:1px solid var(--li);border-radius:4px;padding:0 .25em}
ul{padding-left:1.1rem}
hr{border:0;border-top:1px solid var(--li);margin:1.4rem 0}

/* ---- cartes d'accueil / carte du cours ---- */
.cartes{display:grid;gap:.7rem;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));padding:0;list-style:none;margin:.6rem 0}
.carte{background:var(--card);border:1px solid var(--li);border-radius:var(--r);padding:.65rem .8rem}
.carte h3{margin:0 0 .2rem}
.carte p{margin:.2rem 0;font-size:.88rem;color:var(--mut)}
.carte a.tit{text-decoration:none;font-size:1.02rem;font-weight:600}
.dette{border:1px solid var(--li2);border-radius:var(--r);padding:.6rem .8rem;background:var(--bg2);font-family:var(--sans);font-size:.85rem}
.dette ul{margin:.3rem 0 0}
footer{border-top:1px solid var(--li);color:var(--mut);font-family:var(--sans);font-size:.76rem;padding:1rem 0 2rem}

/* ---- arbre ---- */
.barre{display:flex;gap:.4rem;flex-wrap:wrap;align-items:center;margin:.5rem 0}
#scene{position:relative;border:1px solid var(--li);border-radius:var(--r);background:var(--bg2);
  height:min(74vh,720px);overflow:hidden;touch-action:none;cursor:grab}
#scene.drag{cursor:grabbing}
#pan{position:absolute;transform-origin:0 0;top:0;left:0}
#aretes{position:absolute;top:0;left:0;overflow:visible;pointer-events:none}
#aretes path{fill:none;stroke:var(--li2);stroke-width:1.5}
.noeud{position:absolute;background:var(--card);border:1px solid var(--li2);border-radius:var(--r);
  padding:.35rem .5rem;font-family:var(--sans);font-size:.8rem;line-height:1.3}
.noeud.aj{border-color:var(--ajo)}
.noeud .nm{font-weight:600}
.noeud .nm a{text-decoration:none;color:var(--fg)}
.noeud .nm a:hover{color:var(--acc)}
.noeud .pa{color:var(--mut);font-size:.72rem;display:block;margin-top:.1rem}
.noeud .pli{font:inherit;font-size:.72rem;background:none;border:1px solid var(--li2);border-radius:4px;
  color:var(--mut);cursor:pointer;padding:0 .3rem;margin-right:.25rem}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media (max-width:640px){
  body{font-size:16px}
  h1{font-size:1.4rem}
  .rech{flex:1 1 100%;order:9}
  #scene{height:66vh}
}
@media print{header.top,.barre,.btn{display:none}details.sec{display:block}details.sec>summary{font-weight:700}}
"""

JS_TETE = """
(function(){try{var t=localStorage.getItem('notions.theme');if(t){document.documentElement.setAttribute('data-theme',t);}
var a=localStorage.getItem('notions.ajouts');if(a==='0'){document.documentElement.classList.add('sans-ajouts');}}catch(e){}})();
"""

JS_COMMUN = """
var LS={g:function(k,d){try{var v=localStorage.getItem(k);return v===null?d:v}catch(e){return d}},
        s:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
function majAjouts(on){var h=document.documentElement;h.classList.toggle('sans-ajouts',!on);
  var b=document.getElementById('bajout');if(b){b.setAttribute('aria-pressed',on?'false':'true');
  b.textContent=on?'masquer les ajouts':'ajouts masqués';}
  document.querySelectorAll('.sec').forEach(function(s){
    var c=s.querySelector('.corps');if(!c)return;var n=0;
    c.querySelectorAll(':scope>*').forEach(function(el){
      if(el.classList.contains('is-ajout'))return;
      if(el.classList.contains('note'))return;          /* commentaire du générateur */
      if(el.tagName==='UL'){var v=0;el.querySelectorAll(':scope>li').forEach(function(li){if(!li.classList.contains('is-ajout'))v++});if(!v)return;}
      n++;});
    var vide=!on&&n===0, oblig=s.hasAttribute('data-oblig');
    s.classList.toggle('vide',vide&&!oblig);
    var msg=c.querySelector('.masq');
    if(vide&&oblig){
      if(!msg){msg=document.createElement('p');msg.className='masq';
        msg.textContent='Rubrique obligatoire dont tout le contenu est un ajout de l’opérateur : masquée par le filtre, mais elle existe dans la fiche.';
        c.appendChild(msg);}
      s.classList.add('estmasq');
    } else {if(msg)msg.remove();s.classList.remove('estmasq');}});
  if(window.ARBRE&&window.ARBRE.redessiner)window.ARBRE.redessiner();
}
document.addEventListener('DOMContentLoaded',function(){
  var bt=document.getElementById('btheme');
  if(bt)bt.addEventListener('click',function(){
    var cur=document.documentElement.getAttribute('data-theme');
    var sys=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
    var nx=(cur||sys)==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',nx);LS.s('notions.theme',nx);});
  var ba=document.getElementById('bajout');
  if(ba)ba.addEventListener('click',function(){var on=document.documentElement.classList.contains('sans-ajouts');
    LS.s('notions.ajouts',on?'1':'0');majAjouts(on);});
  majAjouts(LS.g('notions.ajouts','1')!=='0');
  /* --- recherche instantanée (règle 9) --- */
  var inp=document.getElementById('q'),res=document.getElementById('qres');
  if(!inp||!res||!window.SEARCH_INDEX)return;
  var REL=document.documentElement.getAttribute('data-rel')||'';
  var sel=-1,items=[];
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}
  function cherche(q){
    var n=norm(q);if(!n)return [];
    var out=[];
    SEARCH_INDEX.forEach(function(e){
      var sc=-1,ch=e.h||[];
      for(var i=0;i<ch.length;i++){var p=norm(ch[i]).indexOf(n);
        if(p===0){sc=Math.max(sc,3-(i>0?1:0))}else if(p>0){sc=Math.max(sc,1)}}
      if(sc>=0)out.push([sc,e]);});
    out.sort(function(a,b){return b[0]-a[0]||a[1].n.localeCompare(b[1].n)});
    return out.slice(0,9).map(function(x){return x[1]});}
  function rendre(){
    items=cherche(inp.value);sel=-1;res.innerHTML='';
    if(!inp.value){res.classList.remove('on');return}
    if(!items.length){res.innerHTML='<li class="vide">rien</li>';res.classList.add('on');return}
    items.forEach(function(e,i){
      var li=document.createElement('li');
      var a=document.createElement('a');a.href=REL+e.u;a.id='qr'+i;
      a.innerHTML='<span>'+e.n+'</span> <span class="sub">'+e.s+'</span>';
      li.appendChild(a);res.appendChild(li);});
    res.classList.add('on');}
  function bouge(d){if(!items.length)return;sel=(sel+d+items.length)%items.length;
    Array.prototype.forEach.call(res.children,function(li,i){li.classList.toggle('sel',i===sel)});
    inp.setAttribute('aria-activedescendant','qr'+sel);}
  inp.addEventListener('input',rendre);
  inp.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();bouge(1)}
    else if(e.key==='ArrowUp'){e.preventDefault();bouge(-1)}
    else if(e.key==='Enter'){var a=res.querySelector(sel>=0?'li.sel a':'li a');if(a){e.preventDefault();location.href=a.href}}
    else if(e.key==='Escape'){inp.value='';res.classList.remove('on')}});
  document.addEventListener('click',function(e){if(!res.contains(e.target)&&e.target!==inp)res.classList.remove('on')});
  document.addEventListener('keydown',function(e){
    if((e.key==='/'||((e.ctrlKey||e.metaKey)&&e.key==='k'))&&document.activeElement!==inp){e.preventDefault();inp.focus();inp.select()}});
});
"""

JS_FICHE = """
document.addEventListener('DOMContentLoaded',function(){
  /* pliage mémorisé par rubrique (règle 5) */
  document.querySelectorAll('details.sec[data-k]').forEach(function(d){
    var k='notions.pli.'+d.getAttribute('data-k');
    var v=LS.g(k,null);if(v!==null)d.open=(v==='1');
    d.addEventListener('toggle',function(){LS.s(k,d.open?'1':'0')});});
  /* amont et aval : même état « déjà su », un compteur par liste (règle 6) */
  var su={};try{su=JSON.parse(localStorage.getItem('notions.su')||'{}')||{}}catch(e){su={}}
  function compte(){
    document.querySelectorAll('.sec').forEach(function(s){
      var cpt=s.querySelector('[data-cpt]');if(!cpt)return;
      var l=s.querySelectorAll('input[data-su]'),k=0;
      l.forEach(function(c){if(c.checked)k++});
      cpt.textContent=l.length+' notion'+(l.length>1?'s':'')+', '+(l.length-k)+' à voir';});}
  document.querySelectorAll('input[data-su]').forEach(function(c){
    var id=c.getAttribute('data-su');c.checked=!!su[id];
    c.closest('li').classList.toggle('su',c.checked);
    c.addEventListener('change',function(){
      su[id]=c.checked;if(!c.checked)delete su[id];
      try{localStorage.setItem('notions.su',JSON.stringify(su))}catch(e){}
      document.querySelectorAll('input[data-su="'+id+'"]').forEach(function(o){
        o.checked=c.checked;o.closest('li').classList.toggle('su',c.checked);});
      compte();});});
  compte();
});
"""


# JS_ARBRE est la transcription de tools/tests/test_layout.py::disposer. Toute
# modification de l'un doit être reportée dans l'autre ; les constantes W, C, G sont
# injectées depuis le test pour qu'elles ne puissent pas diverger.
JS_ARBRE = """
(function(){
var W=__W__,C=__C__,G=__G__;
var noeuds=ARBRE_DATA.noeuds, H={}, deplies=new Set(), pan={x:40,y:24,s:1};
var scene=document.getElementById('scene'),plan=document.getElementById('pan'),svg=document.getElementById('aretes');

function structure(){
  var sans=document.documentElement.classList.contains('sans-ajouts');
  var gardes={},ordre=[];
  noeuds.forEach(function(n){if(!(sans&&n.aj)){gardes[n.id]=n;ordre.push(n.id)}});
  var enfants={},parent={};
  ordre.forEach(function(i){enfants[i]=[]});
  ordre.forEach(function(i){
    var p=gardes[i].pa;
    while(p&&!gardes[p]){var q=null;noeuds.forEach(function(n){if(n.id===p)q=n.pa});p=q}
    parent[i]=(p&&gardes[p])?p:null;
    if(parent[i])enfants[parent[i]].push(i);});
  var racines=ordre.filter(function(i){return !parent[i]&&(enfants[i].length||gardes[i].pr)});
  return {gardes:gardes,enfants:enfants,racines:racines};
}

/* --- SPEC-SITE §5 : miroir exact de test_layout.disposer --- */
function disposer(racines,enfants,deplies,hauteurs){
  var tops={},prof={},ynext={},plancher=0;
  function yn(d){var v=ynext[d];return Math.max(v===undefined?0:v,plancher)}
  function sousArbre(n,d,acc){acc.push([n,d]);
    if(deplies.has(n))(enfants[n]||[]).forEach(function(k){sousArbre(k,d+1,acc)});return acc}
  function placer(n,d){
    prof[n]=d;
    var kids=deplies.has(n)?(enfants[n]||[]):[];
    if(!kids.length){tops[n]=yn(d);}
    else{
      kids.forEach(function(k){placer(k,d+1)});
      var pr=kids[0],de=kids[kids.length-1];
      var m=(tops[pr]+hauteurs[pr]/2+tops[de]+hauteurs[de]/2)/2;
      var vise=m-hauteurs[n]/2, haut=Math.max(yn(d),vise);
      if(haut>vise){
        var delta=haut-vise, cols={};
        kids.forEach(function(k){sousArbre(k,d+1,[]).forEach(function(p){tops[p[0]]+=delta;cols[p[1]]=1})});
        Object.keys(cols).forEach(function(dx){ynext[dx]=yn(dx)+delta});}
      tops[n]=haut;}
    ynext[d]=tops[n]+hauteurs[n]+G;}
  racines.forEach(function(r,i){
    if(i){var mx=plancher;Object.keys(ynext).forEach(function(d){if(ynext[d]>mx)mx=ynext[d]});plancher=mx;}
    placer(r,0);});
  return {tops:tops,prof:prof};
}

function visibles(racines,enfants,deplies){
  var out=[];
  function desc(n){out.push(n);if(deplies.has(n))(enfants[n]||[]).forEach(desc)}
  racines.forEach(desc);return out;
}

function verifier(vis,tops,prof,haut){ /* propriété (i), écrite en console (SPEC-SITE §5) */
  var r=vis.map(function(n){return [n,prof[n]*C,tops[n],prof[n]*C+W,tops[n]+haut[n]]}),ko=0;
  for(var i=0;i<r.length;i++)for(var j=i+1;j<r.length;j++){
    var a=r[i],b=r[j];
    if(a[1]<b[3]-1e-7&&b[1]<a[3]-1e-7&&a[2]<b[4]-1e-7&&b[2]<a[4]-1e-7){ko++;
      console.error('arbre : chevauchement '+a[0]+' / '+b[0]);}}
  console.log('arbre : '+vis.length+' cartes visibles, '+ko+' chevauchement(s)');
}

function creerCartes(){
  noeuds.forEach(function(n){
    var d=document.createElement('div');
    d.className='noeud'+(n.aj?' aj':'');d.id='nd-'+n.k;d.style.width=W+'px';
    var pli=(n.en&&n.en.length)?'<button class="pli" data-n="'+n.id+'" aria-label="plier ou déplier">–</button>':'';
    d.innerHTML='<span class="nm">'+pli+'<a href="'+n.u+'">'+n.nom+'</a></span>'+
                (n.pa2?'<span class="pa">'+n.pa2+'</span>':'');
    plan.appendChild(d);});
  noeuds.forEach(function(n){H[n.id]=document.getElementById('nd-'+n.k).offsetHeight});
}

function redessiner(){
  var st=structure(),vis=visibles(st.racines,st.enfants,deplies);
  var r=disposer(st.racines,st.enfants,deplies,H);
  var visSet=new Set(vis),maxx=0,maxy=0;
  noeuds.forEach(function(n){
    var el=document.getElementById('nd-'+n.k);
    if(!visSet.has(n.id)){el.style.display='none';return}
    el.style.display='';el.style.left=(r.prof[n.id]*C)+'px';el.style.top=(r.tops[n.id])+'px';
    var b=document.querySelector('#nd-'+n.k+' .pli');
    if(b){var ouvert=deplies.has(n.id);b.textContent=ouvert?'–':'+';b.setAttribute('aria-expanded',ouvert?'true':'false');}
    maxx=Math.max(maxx,r.prof[n.id]*C+W);maxy=Math.max(maxy,r.tops[n.id]+H[n.id]);});
  var d='';
  vis.forEach(function(n){
    if(!deplies.has(n))return;
    (st.enfants[n]||[]).forEach(function(k){
      var x0=r.prof[n]*C+W,y0=r.tops[n]+H[n]/2,x1=r.prof[k]*C,y1=r.tops[k]+H[k]/2,xm=(x0+x1)/2;
      d+='M'+x0+','+y0+'C'+xm+','+y0+' '+xm+','+y1+' '+x1+','+y1+' ';});});
  svg.setAttribute('width',maxx+10);svg.setAttribute('height',maxy+10);
  svg.innerHTML='<path d="'+d+'"/>';
  plan.style.width=(maxx+10)+'px';plan.style.height=(maxy+10)+'px';
  verifier(vis,r.tops,r.prof,H);
  var c=document.getElementById('nbvis');if(c)c.textContent=vis.length+' noeuds affichés';
}
function transformer(){plan.style.transform='translate('+pan.x+'px,'+pan.y+'px) scale('+pan.s+')'}

document.addEventListener('DOMContentLoaded',function(){
  creerCartes();
  noeuds.forEach(function(n){if(n.en&&n.en.length&&n.pf<1)deplies.add(n.id)});  /* replié > 2 niveaux */
  redessiner();transformer();
  plan.addEventListener('click',function(e){
    var b=e.target.closest('.pli');if(!b)return;e.preventDefault();
    var i=b.getAttribute('data-n');if(deplies.has(i))deplies.delete(i);else deplies.add(i);redessiner();});
  document.getElementById('tout').addEventListener('click',function(){
    noeuds.forEach(function(n){if(n.en&&n.en.length)deplies.add(n.id)});redessiner();});
  document.getElementById('rien').addEventListener('click',function(){deplies.clear();redessiner();});
  document.getElementById('zp').addEventListener('click',function(){pan.s=Math.min(2,pan.s*1.2);transformer()});
  document.getElementById('zm').addEventListener('click',function(){pan.s=Math.max(.3,pan.s/1.2);transformer()});
  document.getElementById('zr').addEventListener('click',function(){pan={x:40,y:24,s:1};transformer()});
  var dr=null;
  scene.addEventListener('pointerdown',function(e){
    if(e.target.closest('a')||e.target.closest('button'))return;
    dr={x:e.clientX-pan.x,y:e.clientY-pan.y};scene.setPointerCapture(e.pointerId);scene.classList.add('drag');});
  scene.addEventListener('pointermove',function(e){if(!dr)return;pan.x=e.clientX-dr.x;pan.y=e.clientY-dr.y;transformer()});
  ['pointerup','pointercancel'].forEach(function(t){scene.addEventListener(t,function(){dr=null;scene.classList.remove('drag')})});
  scene.addEventListener('keydown',function(e){
    var p={ArrowLeft:[60,0],ArrowRight:[-60,0],ArrowUp:[0,60],ArrowDown:[0,-60]}[e.key];
    if(!p)return;e.preventDefault();pan.x+=p[0];pan.y+=p[1];transformer();});
});
window.ARBRE={redessiner:function(){if(Object.keys(H).length)redessiner()}};
})();
"""


# ================================================================ 5. gabarit de page

def page(m, *, titre, rel, fil, corps, js="", mathjax=True, index=True):
    mj = ""
    if mathjax:
        mj = ('<script>window.MathJax={tex:{inlineMath:[["$","$"]],displayMath:[["$$","$$"]],'
              'processEscapes:true},svg:{fontCache:"global"},'
              'options:{skipHtmlTags:["script","noscript","style","textarea","pre","code"]}};</script>'
              '<script id="MathJax-script" async src="' + m["mathjax_src"](rel) + '"></script>')
    return (
        "<!doctype html>\n"
        '<html lang="fr" data-rel="' + rel + '">\n<head>\n'
        '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>" + esc(titre) + " · notions</title>\n"
        "<script>" + JS_TETE + "</script>\n"
        "<style>" + CSS + "</style>\n" + mj + "\n</head>\n<body>\n"
        '<header class="top"><div class="topin">'
        '<a class="brand" href="' + rel + 'index.html">notions</a>'
        '<span class="fil">' + fil + "</span>"
        '<div class="rech"><label class="sr" for="q" hidden>chercher</label>'
        '<input id="q" type="search" autocomplete="off" role="combobox" aria-expanded="false" '
        'aria-controls="qres" placeholder="chercher  ( / )"><ul class="res" id="qres" role="listbox"></ul></div>'
        '<button class="btn" id="bajout" aria-pressed="false">masquer les ajouts</button>'
        '<button class="btn" id="btheme" title="thème clair / sombre">thème</button>'
        "</div></header>\n<main><div class=\"wrap\">" + corps + "</div></main>\n"
        '<footer><div class="wrap">Base de notions M2 IRFA · page générée par <code>tools/build.py</code> '
        "selon <code>SPEC-SITE.md</code> · les rubriques dérivées (socle, membres, sert ensuite à, niveau) "
        "sont calculées au build, jamais écrites dans les fiches (A9).</div></footer>\n"
        + ('<script src="' + rel + 'search-index.js"></script>\n' if index else "")
        + "<script>" + JS_COMMUN + "</script>\n"
        + ("<script>" + js + "</script>\n" if js else "")
        + "</body>\n</html>\n"
    )


# ---------------------------------------------------------------- pastilles et listes

def pastille(m, ident, rel, cours=None, niveau=False):
    if ident in m["N"]:
        c, s = ident.split("/", 1)
        cls = "past" + (" ajout" if est_ajout(m, ident) else "")
        pre = '<span class="cc">' + esc(c) + "·</span> " if cours and c != cours else ""
        nv = '<span class="nv">n' + str(m["niveau"][ident]) + "</span>" if niveau else ""
        return ('<li><a class="' + cls + '" href="' + rel + c + "/n/" + s + '.html">'
                + pre + esc(nom_de(m, ident)) + nv + "</a></li>")
    av = m["a_venir"].get(ident, {})
    t = esc(av.get("raison", "non encore écrite"))
    return ('<li><span class="past venir" title="à venir — ' + t + '">'
            + esc(ident) + ' <span class="nv">à venir</span></span></li>')


def liste_pastilles(m, ids, rel, cours=None, niveau=False, cle=None):
    """Règle 4 : au-delà de sept éléments, on regroupe et on replie les groupes."""
    if not ids:
        return ""
    if len(ids) <= MAX_LISTE or cle is None:
        return '<ul class="pasts">' + "".join(pastille(m, i, rel, cours, niveau) for i in ids) + "</ul>"
    groupes = defaultdict(list)
    for i in ids:
        groupes[cle(i)].append(i)
    out = []
    for k in sorted(groupes):
        out.append('<details class="grp"><summary>' + esc(str(k)) + " (" + str(len(groupes[k])) + ")</summary>"
                   + '<ul class="pasts">' + "".join(pastille(m, i, rel, cours, niveau) for i in groupes[k])
                   + "</ul></details>")
    return "".join(out)


# Rubriques obligatoires de SPEC-MODELE §2.1 : si le filtre « masquer les ajouts »
# les vide entièrement, elles ne disparaissent pas — elles le disent. Une fiche sans
# « Cesse d'être valide quand » se lirait comme une fiche sans limite de validité.
OBLIGATOIRES = {"Ce que c'est", "Forme", "Ce qui la définit", "Ce que les membres partagent",
                "Pourquoi ce niveau existe", "Exemple minimal", "Geste de calcul type",
                "Cesse d'être valide quand"}


def sec(titre, corps, *, cle=None, ouvert=False, classe="", compte=""):
    """Une rubrique. Sans clé : toujours visible (règle 5, les trois premières)."""
    if not corps:
        return ""
    ob = ' data-oblig="1"' if titre in OBLIGATOIRES else ""
    if cle is None:
        return ('<section class="sec ' + classe + '"' + ob + "><h2>" + esc(titre) + "</h2>"
                '<div class="corps">' + corps + "</div></section>")
    c = '<span class="cnt">' + esc(compte) + "</span>" if compte else ""
    return ('<details class="sec ' + classe + '" data-k="' + cle + '"' + ob + (" open" if ouvert else "") + ">"
            "<summary><h2>" + esc(titre) + "</h2>" + c + "</summary>"
            '<div class="corps">' + corps + "</div></details>")


# ================================================================ 6. la fiche (§3.1)

def bloc_liste(m, ids, rel, cle, note):
    """Liste de notions ordonnée par niveau, cases « déjà su » partagées, compteur.
    Même forme pour l'amont (socle, transitif) et pour l'aval (rayon 1) — SPEC-SITE
    §2 règle 6."""
    if not ids:
        return ""
    def item(y):
        if y not in m["N"]:
            av = m["a_venir"].get(y, {})
            return ('<li><span style="width:1em"></span><span class="past venir" title="%s">%s à venir</span></li>'
                    % (esc(av.get("raison", "")), esc(y)))
        c, s = y.split("/", 1)
        cls = ' class="is-ajout"' if est_ajout(m, y) else ""
        return ('<li%s><input type="checkbox" data-su="%s" aria-label="déjà su : %s">'
                '<a href="%s%s/n/%s.html">%s</a> <span class="marq">niveau %d%s</span></li>'
                % (cls, esc(y), esc(nom_de(m, y)), rel, c, s, esc(nom_de(m, y)),
                   m["niveau"][y], " · ajout" if est_ajout(m, y) else ""))
    out = ['<p class="note">' + note + "</p>", '<p class="compteur" data-cpt="' + cle + '"></p>']
    if len(ids) <= MAX_LISTE:
        out.append('<ul class="socle">' + "".join(item(y) for y in ids) + "</ul>")
    else:
        grp = defaultdict(list)
        for y in ids:
            grp[m["niveau"].get(y, 0)].append(y)
        for nv in sorted(grp):
            out.append('<details class="grp" open><summary>niveau %d (%d)</summary>'
                       '<ul class="socle">%s</ul></details>'
                       % (nv, len(grp[nv]), "".join(item(y) for y in grp[nv])))
    return "".join(out)


def page_fiche(m, i):
    n = m["N"][i]
    meta, S = n["meta"], dict(n["sections"])
    code = n["cours"]
    slug = i.split("/", 1)[1]
    rel = "../../"
    ctx = {"m": m, "rel": rel}
    ajout = meta.get("statut") == "ajout"
    parent = m["A"].get(i)
    membres = m["A_inv"].get(i, [])
    typ = meta.get("type")

    # 1. en-tête
    pills = ['<span class="pill typ">' + esc(typ) + "</span>",
             '<a class="pill" href="' + rel + code + '/index.html">' + esc(code) + "</a>",
             '<span class="pill" title="ordre de lecture : nombre de notions à traverser, au plus '
             'long, pour arriver jusqu’à celle-ci. Niveau 0 = ne dépend d’aucune autre.">'
             "niveau " + str(m["niveau"][i]) + "</span>"]
    if meta.get("symbole"):
        pills.insert(0, '<span class="pill sym">' + esc(str(meta["symbole"])) + "</span>")
    for r in meta.get("refs") or []:
        pills.append('<span class="pill">' + esc(str(r)) + "</span>")
    if ajout:
        pills.append('<span class="pill ajout">ajout de l’opérateur</span>')
    ent = ["<h1>" + esc(meta.get("nom", i)) + "</h1>", '<div class="meta">' + "".join(pills) + "</div>"]
    if meta.get("alias"):
        ent.append('<p class="note">aussi : ' + esc(", ".join(str(a) for a in meta["alias"])) + "</p>")
    if ajout:
        ent.append('<div class="bandeau is-ajout">Cette notion n’est pas dans la source : elle a été '
                   "ajoutée par l’opérateur. Le filtre « masquer les ajouts » la retire du site.</div>")

    c = list(ent)
    # 2–4
    c.append(sec("Ce que c'est", rendre(S.get("Ce que c'est", ""), ctx, fiche=True)))
    c.append(sec("Forme", rendre(S.get("Forme", ""), ctx, fiche=True)))
    for t in ("Ce qui la définit", "Ce que les membres partagent"):
        if t in S:
            c.append(sec(t, rendre(S[t], ctx, fiche=True)))
    # 5. paramètre (généré)
    if typ == "abstraite" and membres:
        li = ["<table><thead><tr><th>membre</th><th>valeur du paramètre</th></tr></thead><tbody>"]
        for x in membres:
            cx, sx = x.split("/", 1)
            li.append('<tr%s><td><a href="%s%s/n/%s.html">%s</a></td><td>%s</td></tr>'
                      % (' class="is-ajout"' if est_ajout(m, x) else "", rel, cx, sx,
                         esc(nom_de(m, x)), enligne(str(m["N"][x]["meta"].get("valeur", "—")), ctx)))
        li.append("</tbody></table>")
        corps = ('<p class="note">Paramètre : ' + enligne(str(meta.get("parametre", "")), ctx)
                 + " — table générée depuis les membres (A9).</p>" + "".join(li))
        c.append(sec("Le paramètre qui les distingue", corps, cle="param", classe="gen",
                     compte=str(len(membres)) + " membres"))
    # 6.
    if "Pourquoi ce niveau existe" in S:
        c.append(sec("Pourquoi ce niveau existe", rendre(S["Pourquoi ce niveau existe"], ctx, fiche=True), cle="pourquoi"))
    # 7. cas particulier de (généré) — A4 : « découle de » sous un principe
    if parent:
        pp = m["N"].get(parent, {}).get("meta", {})
        titre = "Découle de" if pp.get("type") == "principe" else "Cas particulier de"
        note = ("Un principe n’est pas une généralisation : cette arête se lit « découle directement de » (A4)."
                if pp.get("type") == "principe" else
                "Autre relation : ce n’est pas un prérequis. Le prérequis, c’est « construite à partir de ».")
        corps = '<p class="note avert">' + note + "</p>"
        corps += '<ul class="pasts">' + pastille(m, parent, rel, code) + "</ul>"
        if meta.get("valeur"):
            corps += '<p class="note">valeur pour le paramètre du parent : ' + enligne(str(meta["valeur"]), ctx) + "</p>"
        c.append(sec(titre, corps, cle="casde", classe="gen abs", compte="autre relation"))
    # 8. construite à partir de
    dep = m["D"].get(i) or []
    if dep:
        c.append(sec("Construite à partir de",
                     liste_pastilles(m, dep, rel, code, niveau=True,
                                     cle=lambda y: "niveau %d" % m["niveau"].get(y, 0))
                     + '<p class="note">Dépendances directes seulement (A8). Le socle ci-dessous '
                       "en est la fermeture : ces notions-ci s’y retrouvent, augmentées de tout ce dont "
                       "elles dépendent à leur tour.</p>",
                     cle="construite", compte=str(len(dep)) + (" prérequis direct" if len(dep) == 1 else " prérequis directs")))
    # 9. socle (amont transitif) puis 10. sert ensuite à (aval, rayon 1), de même forme
    so = bloc_liste(m, m["socle"][i], rel, "socle",
                    "Amont transitif : tout ce qu’il faut savoir avant, ordonné par niveau "
                    "croissant. Le niveau est le nombre de notions à traverser au plus long pour "
                    "atteindre celle-ci : niveau 0, elle ne dépend de rien. C’est un ordre de "
                    "lecture. Une case cochée le reste sur toutes les fiches, et sur celle-ci comme "
                    "ailleurs.")
    if so:
        c.append(sec("Socle complet", so, cle="socle", classe="gen",
                     compte=str(len(m["socle"][i])) + (" prérequis" if len(m["socle"][i]) == 1 else " prérequis en tout")))
    srt = m["D_inv"].get(i) or []
    if srt:
        av = sorted(srt, key=lambda y: (m["niveau"].get(y, 0), nom_de(m, y).lower()))
        c.append(sec("Sert ensuite à",
                     bloc_liste(m, av, rel, "aval",
                                "Aval à rayon 1 : ce que cette notion ouvre immédiatement. "
                                "Généré, l’inverse de « construite à partir de » (A9). Jamais "
                                "transitif : une notion fondamentale débloquerait tout le cours."),
                     cle="sert", classe="gen", compte=str(len(av))))
    # 10–12
    for t, k in (("Exemple minimal", "exemple"), ("Geste de calcul type", "geste"), ("Ce qui reste libre", "libre")):
        if t not in S:
            continue
        corps, cl, cpt = rendre(S[t], ctx, fiche=True), "", ""
        if t == "Exemple minimal" and "à venir" in S[t]:
            # SPEC-INGESTION étape 3 : un exemple minimal ne dépend d'aucun exercice.
            # Le laisser en dette n'est pas de la dette, c'est une faute de protocole.
            cl, cpt = "faute", "faute de protocole"
            corps += ('<p class="note">SPEC-INGESTION étape 3 : « Elle ne dépend d’aucun exercice '
                      "et s’écrit dès la création de la fiche ; la laisser en dette est une faute de "
                      "protocole. » À écrire depuis la source, sans attendre un exercice.</p>")
        c.append(sec(t, corps, cle=k, classe=cl, compte=cpt))
    # 13. limite
    if "Cesse d'être valide quand" in S:
        c.append(sec("Cesse d'être valide quand", rendre(S["Cesse d'être valide quand"], ctx, fiche=True),
                     cle="limite", classe="lim"))
    # 15. membres (généré)
    if membres:
        titre = "Membres" if typ == "abstraite" else "Premières constructions"
        note = ("Généré : l’inverse de « cas de » (A9)." if typ == "abstraite"
                else "Généré : les notions qui découlent directement de ce principe (A4, A9).")
        c.append(sec(titre, liste_pastilles(m, membres, rel, code, cle=lambda y: m["N"][y]["meta"]["type"])
                     + '<p class="note">' + note + "</p>",
                     cle="membres", classe="gen", compte=str(len(membres))))
    # 16–17
    if "Origine" in S:
        c.append(sec("Origine", rendre(S["Origine"], ctx, fiche=True), cle="origine"))
    fil = ('<a href="' + rel + code + '/index.html">' + esc(m["cours"][code]["meta"].get("titre", code))
           + "</a> › " + esc(meta.get("nom", i)))
    return page(m, titre=meta.get("nom", i), rel=rel, fil=fil, corps="".join(c), js=JS_FICHE)


# ================================================================ 7. les autres pages

def dette_du_cours(m, code):
    liens, gestes, exemples = [], [], []
    for i in m["cours"][code]["notions"]:
        for y in (m["D"].get(i) or []) + ([m["A"][i]] if m["A"].get(i) else []):
            if y not in m["N"]:
                liens.append((i, y))
        S = dict(m["N"][i]["sections"])
        if "à venir" in S.get("Geste de calcul type", ""):
            gestes.append(i)
        if "à venir" in S.get("Exemple minimal", ""):
            exemples.append(i)
    inv = [e for e in m["cours"][code]["inventaire"] if "a_venir" in e]
    return dict(liens=liens, gestes=gestes, exemples=exemples, inventaire=inv)


def page_cours(m, code):
    cs = m["cours"][code]
    rel = "../"
    ctx = {"m": m, "rel": rel}
    ids = cs["notions"]
    principes = [i for i in ids if m["N"][i]["meta"].get("type") == "principe"]
    principes.sort(key=lambda i: nom_de(m, i).lower())
    c = ["<h1>" + esc(cs["meta"].get("titre", code)) + "</h1>",
         '<div class="meta"><span class="pill">' + esc(code) + "</span>"
         '<span class="pill">' + esc(str(cs["meta"].get("enseignant", ""))) + "</span>"
         '<span class="pill">' + esc(str(cs["meta"].get("annee", ""))) + "</span>"
         '<span class="pill">' + str(len(ids)) + " notions</span>"
         '<a class="pill" href="' + rel + code + '/arbre.html">arbre d’abstraction</a>'
         '<a class="pill" href="' + rel + code + '/inventaire.html">inventaire de la source</a></div>']

    c.append('<h2 class="ptag">Principes</h2>')
    li = []
    for p in principes:
        S = dict(m["N"][p]["sections"])
        cp, sp = p.split("/", 1)
        li.append('<li class="carte%s"><a class="tit" href="%s%s/n/%s.html">%s</a><p>%s</p></li>'
                  % (" is-ajout" if est_ajout(m, p) else "", rel, cp, sp, esc(nom_de(m, p)),
                     rendre(S.get("Ce que c'est", ""), ctx, fiche=True).replace("<p>", "").replace("</p>", "")))
    c.append('<ul class="cartes">' + "".join(li) + "</ul>")

    for p in principes:
        enf = m["A_inv"].get(p, [])
        if not enf:
            continue
        c.append("<h3>Découle de « " + esc(nom_de(m, p)) + " »</h3>")
        li = []
        for x in enf:
            cx, sx = x.split("/", 1)
            nb = len(m["A_inv"].get(x, []))
            li.append('<li class="carte%s"><a class="tit" href="%s%s/n/%s.html">%s</a>'
                      '<p>%s%s</p></li>'
                      % (" is-ajout" if est_ajout(m, x) else "", rel, cx, sx, esc(nom_de(m, x)),
                         esc(m["N"][x]["meta"].get("type", "")),
                         " · " + str(nb) + " membre" + ("s" if nb > 1 else "") if nb else ""))
        c.append('<ul class="cartes">' + "".join(li) + "</ul>")

    comp = sorted([i for i in ids if not m["A"].get(i) and m["N"][i]["meta"].get("type") != "principe"],
                  key=lambda i: (m["niveau"][i], nom_de(m, i).lower()))
    if comp:
        c.append('<h2 class="ptag">Composants</h2>'
                 '<p class="note">Notions sans généralisation : ce n’est pas un oubli, '
                 "c’est une information (règle 2 de SPEC-SITE §3.3).</p>"
                 '<p class="note">Les groupes sont des <strong>niveaux de dépendance</strong> : '
                 "le niveau d’une notion est le nombre de notions qu’il faut traverser, au plus "
                 "long, pour arriver jusqu’à elle. <strong>Niveau 0</strong> : elle ne dépend "
                 "d’aucune autre, on peut la lire en premier. <strong>Niveau 1</strong> : elle "
                 "dépend uniquement de notions de niveau 0. Et ainsi de suite : le niveau est "
                 "donc un ordre de lecture, pas un degré de difficulté ni d’importance.</p>")
        c.append(liste_pastilles(m, comp, rel, code, niveau=True, cle=lambda y: "niveau %d" % m["niveau"][y]))

    d = dette_du_cours(m, code)
    if d["exemples"]:
        items = "".join('<li><a href="%s%s/n/%s.html">%s</a></li>'
                        % (rel, code, i.split("/", 1)[1], esc(nom_de(m, i))) for i in d["exemples"])
        liste = ("<ul>" + items + "</ul>" if len(d["exemples"]) <= MAX_LISTE else
                 '<details class="grp"><summary>les %d fiches</summary><ul>%s</ul></details>'
                 % (len(d["exemples"]), items))
        c.append('<h2 class="ptag">Faute de protocole</h2><div class="faute-b">'
                 "<strong>%d exemples minimaux manquants.</strong> Ce n’est pas de la dette : "
                 "SPEC-INGESTION étape 3 exige qu’un exemple minimal s’écrive dès la création de la "
                 "fiche, sans dépendre d’un exercice.%s</div>" % (len(d["exemples"]), liste))
    c.append('<h2 class="ptag">Dette</h2><div class="dette"><ul>')
    c.append("<li>liens à venir : <strong>" + str(len(d["liens"])) + "</strong>"
             + (" — " + ", ".join(esc(y) + " (depuis " + esc(nom_de(m, x)) + ")" for x, y in d["liens"][:MAX_LISTE])
                if d["liens"] else "") + "</li>")
    for lab, k in (("gestes de calcul à venir", "gestes"),):
        items = "".join('<li><a href="%s%s/n/%s.html">%s</a></li>'
                        % (rel, code, i.split("/", 1)[1], esc(nom_de(m, i))) for i in d[k])
        if not d[k]:
            detail = ""
        elif len(d[k]) <= MAX_LISTE:                      # règle 4 : sept au plus, sinon on replie
            detail = "<ul>" + items + "</ul>"
        else:
            detail = ('<details class="grp"><summary>les %d fiches</summary><ul>%s</ul></details>'
                      % (len(d[k]), items))
        c.append("<li>" + lab + " : <strong>" + str(len(d[k])) + "</strong>" + detail + "</li>")
    c.append('<li>éléments d’inventaire à venir : <strong>' + str(len(d["inventaire"]))
             + '</strong> — <a href="' + rel + code + '/inventaire.html">voir l’inventaire</a></li>')
    c.append("</ul></div>")
    return page(m, titre=cs["meta"].get("titre", code), rel=rel,
                fil=esc(cs["meta"].get("titre", code)), corps="".join(c))


def page_arbre(m, code):
    rel = "../"
    ids = m["cours"][code]["notions"]
    prof = {}
    def p_of(i):
        if i in prof:
            return prof[i]
        p = m["A"].get(i)
        prof[i] = 0 if not p or p not in m["N"] else p_of(p) + 1
        return prof[i]
    noeuds = []
    for k, i in enumerate(sorted(ids, key=lambda x: (p_of(x), nom_de(m, x).lower()))):
        meta = m["N"][i]["meta"]
        enf = m["A_inv"].get(i, [])
        if not enf and not m["A"].get(i) and meta.get("type") != "principe":
            continue                      # notions sans généralisation : listées sous l'arbre
        noeuds.append(dict(id=i, k=k, nom=nom_de(m, i).replace("$", ""), aj=est_ajout(m, i),
                           pa=m["A"].get(i), pa2=meta.get("type"), pf=p_of(i),
                           pr=meta.get("type") == "principe", en=enf,
                           u=rel + i.split("/", 1)[0] + "/n/" + i.split("/", 1)[1] + ".html"))
    data = "var ARBRE_DATA=" + json.dumps(dict(noeuds=noeuds), ensure_ascii=False) + ";"
    js = data + JS_ARBRE.replace("__W__", repr(CARTE_W)).replace("__C__", repr(COL_C)).replace("__G__", repr(ECART_G))
    seuls = sorted([i for i in ids if not m["A"].get(i) and not m["A_inv"].get(i)
                    and m["N"][i]["meta"].get("type") != "principe"],
                   key=lambda i: nom_de(m, i).lower())
    c = ["<h1>Arbre d’abstraction — " + esc(code) + "</h1>",
         '<p class="note">Une seule relation ici : « cas de » (et « découle de » sous un principe). '
         "Aucune arête de dépendance (règle 7). Replié au-delà de deux niveaux ; le canevas se déplace "
         "au glisser ou aux flèches.</p>",
         '<div class="barre">'
         '<button class="btn" id="tout">tout déplier</button>'
         '<button class="btn" id="rien">tout replier</button>'
         '<button class="btn" id="zp">zoom +</button>'
         '<button class="btn" id="zm">zoom −</button>'
         '<button class="btn" id="zr">recentrer</button>'
         '<span class="compteur" id="nbvis"></span></div>',
         '<div id="scene" tabindex="0" aria-label="arbre d’abstraction, déplaçable aux flèches">'
         '<div id="pan"><svg id="aretes"></svg></div></div>',
         '<p class="note">Avec « masquer les ajouts », une abstraction ajoutée disparaît et ses membres '
         "remontent en racine : c’est exactement la projection stricte d’A11.</p>"]
    if seuls:
        c.append("<h3>Notions sans généralisation (" + str(len(seuls)) + ")</h3>")
        c.append(liste_pastilles(m, seuls, rel, code, niveau=True, cle=lambda y: "niveau %d" % m["niveau"][y]))
    fil = ('<a href="' + rel + code + '/index.html">' + esc(m["cours"][code]["meta"].get("titre", code)) + "</a> › arbre")
    return page(m, titre="Arbre — " + code, rel=rel, fil=fil, corps="".join(c), js=js, mathjax=False)


def page_inventaire(m, code):
    rel = "../"
    ctx = {"m": m, "rel": rel}
    els = m["cours"][code]["inventaire"]
    groupes = [("notion", "Élément qui est une notion"), ("absorbe", "Élément absorbé dans une notion"),
               ("exclu", "Élément exclu, avec sa raison"), ("a_venir", "Élément pas encore traité (dette)")]
    c = ["<h1>Inventaire de la source — " + esc(code) + "</h1>",
         '<p class="note">A13 : chaque élément indexable de la source a exactement une image. '
         "C’est la liste que l’utilisateur audite — A13 garantit que rien d’inventorié n’est perdu, "
         "pas que l’inventaire est complet.</p>",
         '<div class="meta"><span class="pill">' + str(len(els)) + " éléments</span>"
         + "".join('<span class="pill">%s : %d</span>' % (k, sum(1 for e in els if k in e)) for k, _ in groupes)
         + "</div>"]
    for k, lab in groupes:
        sel = [e for e in els if k in e]
        if not sel:
            continue
        rows = []
        for e in sel:
            v = e[k]
            if k in ("notion", "absorbe"):
                cv, sv = str(v).split("/", 1)
                img = '<a href="%s%s/n/%s.html">%s</a>' % (rel, cv, sv, esc(nom_de(m, str(v))))
            else:
                img = esc(str(v))
            rows.append("<tr><td><code>%s</code></td><td>%s</td><td>%s</td></tr>"
                        % (esc(str(e.get("ref", "?"))), enligne(str(e.get("intitule", "")), ctx), img))
        c.append('<details class="grp"%s><summary>%s — %d</summary>'
                 "<table><thead><tr><th>réf.</th><th>intitulé</th><th>image</th></tr></thead>"
                 "<tbody>%s</tbody></table></details>"
                 % (" open" if k == "a_venir" else "", esc(lab), len(sel), "".join(rows)))
    fil = ('<a href="' + rel + code + '/index.html">' + esc(m["cours"][code]["meta"].get("titre", code))
           + "</a> › inventaire")
    return page(m, titre="Inventaire — " + code, rel=rel, fil=fil, corps="".join(c))


def page_exercice(m, xid):
    x = m["exercices"][xid]
    code = x["cours"]
    rel = "../../"
    ctx = {"m": m, "rel": rel}
    S = dict(x["sections"])
    c = ["<h1>" + esc(xid) + "</h1>",
         '<div class="meta"><span class="pill">exercice</span><a class="pill" href="'
         + rel + code + '/index.html">' + esc(code) + "</a>"
         '<span class="pill">' + esc(str(x["meta"].get("source", ""))) + "</span></div>"]
    for t in ("Énoncé", "Solution officielle", "Résolution", "Ce que l'exercice a révélé",
              "Contradiction avec la source"):
        if t in S and S[t].strip():
            c.append(sec(t, rendre(S[t], ctx), cle=None if t in ("Énoncé", "Résolution") else t[:6].lower(),
                         ouvert=True, classe="lim" if t.startswith("Contradiction") else ""))
    nts = [i for i in (x["meta"].get("notions") or []) if isinstance(i, str)]
    if nts:
        c.append(sec("Fiches touchées", liste_pastilles(m, nts, rel, code, niveau=True), cle="touchees", ouvert=True))
    fil = ('<a href="' + rel + code + '/index.html">' + esc(m["cours"][code]["meta"].get("titre", code))
           + "</a> › " + esc(xid))
    return page(m, titre=xid, rel=rel, fil=fil, corps="".join(c), js=JS_FICHE)


def page_rapport(m, r):
    rel = "../"
    ctx = {"m": m, "rel": rel}
    return page(m, titre="Rapport " + r["slug"], rel=rel,
                fil="rapport d’ingestion › " + esc(r["slug"]),
                corps='<article class="rapport">' + rendre(r["texte"], ctx, niveau_titre=1) + "</article>")


def page_accueil(m):
    rel = ""
    c = ["<h1>Base de notions — M2 IRFA</h1>",
         '<p class="note">Une fiche par notion, deux relations, un validateur, un site généré. '
         "Les rubriques dérivées sont calculées au build et ne sont jamais écrites dans les fiches (A9).</p>",
         '<h2 class="ptag">Cours</h2><ul class="cartes">']
    for code, cs in sorted(m["cours"].items()):
        d = dette_du_cours(m, code)
        c.append('<li class="carte"><a class="tit" href="%s/index.html">%s</a>'
                 "<p>%s · %s</p><p>%d notions · %d exercices · dette : %d éléments d’inventaire, "
                 "%d gestes, %d liens%s</p>"
                 '<p><a href="%s/arbre.html">arbre</a> · <a href="%s/inventaire.html">inventaire</a></p></li>'
                 % (code, esc(cs["meta"].get("titre", code)), esc(str(cs["meta"].get("enseignant", ""))),
                    esc(str(cs["meta"].get("annee", ""))), len(cs["notions"]), len(cs["exercices"]),
                    len(d["inventaire"]), len(d["gestes"]), len(d["liens"]),
                    (" · <strong>%d exemples minimaux manquants</strong> (faute de protocole)"
                     % len(d["exemples"]) if d["exemples"] else ""), code, code))
    c.append("</ul>")
    if m["rapports"]:
        c.append('<h2 class="ptag">Rapports d’ingestion</h2><ul class="pasts">')
        for r in reversed(m["rapports"]):
            c.append('<li><a class="past" href="rapports/%s.html">%s</a></li>' % (r["slug"], esc(r["slug"])))
        c.append("</ul>")
    tot = len(m["N"])
    c.append('<h2 class="ptag">État</h2><div class="dette"><ul>'
             "<li>%d notions, %d cours</li>"
             "<li>recherche : touche <code>/</code> depuis n’importe quelle page</li>"
             "<li>« masquer les ajouts » donne la projection stricte du cours (A11)</li></ul></div>" % (tot, len(m["cours"])))
    return page(m, titre="Base de notions", rel=rel, fil="accueil", corps="".join(c), mathjax=False)


def index_recherche(m):
    ent = []
    for i, n in sorted(m["N"].items()):
        meta = n["meta"]
        c, s = i.split("/", 1)
        h = [str(meta.get("nom", i))] + [str(a) for a in (meta.get("alias") or [])]
        if meta.get("symbole"):
            h += [x.strip() for x in str(meta["symbole"]).split(",")]
        h.append(i)
        ent.append(dict(n=meta.get("nom", i), s=c + " · " + str(meta.get("type", "")),
                        u=c + "/n/" + s + ".html", h=h))
    for i, x in sorted(m["exercices"].items()):
        c, s = i.split("/", 1)
        ent.append(dict(n=i, s=c + " · exercice", u=c + "/exercices/" + s + ".html",
                        h=[i, str(x["meta"].get("source", ""))]))
    for code in sorted(m["cours"]):
        t = m["cours"][code]["meta"].get("titre", code)
        ent.append(dict(n="Carte du cours " + code, s=t, u=code + "/index.html", h=[code, t, "carte"]))
        ent.append(dict(n="Arbre " + code, s="abstraction", u=code + "/arbre.html", h=[code, "arbre", "abstraction"]))
        ent.append(dict(n="Inventaire " + code, s="couverture de la source", u=code + "/inventaire.html",
                        h=[code, "inventaire", "couverture"]))
    return "window.SEARCH_INDEX=" + json.dumps(ent, ensure_ascii=False) + ";\n"


# ================================================================ 8. écriture

def ecrire(chemin: Path, texte: str, tailles: list):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(texte, encoding="utf-8", newline="\n")
    tailles.append((chemin, len(texte.encode("utf-8"))))


def mathjax_offline(site: Path):
    import urllib.request
    dest = site / "vendor" / "mathjax" / "tex-svg.js"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        print("  MathJax déjà dans site/vendor/ (" + str(dest.stat().st_size // 1024) + " ko)")
        return
    print("  téléchargement de MathJax → " + str(dest.relative_to(site.parent)))
    with urllib.request.urlopen(MATHJAX_CDN, timeout=60) as r:
        dest.write_bytes(r.read())


def nettoyer(site: Path):
    """Idempotence : on efface ce que le build possède, jamais .nojekyll ni vendor/."""
    garde = {".nojekyll", "vendor"}
    if not site.is_dir():
        return
    for p in site.iterdir():
        if p.name in garde:
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()


def main():
    ap = argparse.ArgumentParser(description="génère site/ depuis courses/ (SPEC-SITE.md)")
    ap.add_argument("--root", default=str(RACINE))
    ap.add_argument("--offline", action="store_true", help="copie MathJax dans site/vendor/")
    ap.add_argument("--course", help="ne générer qu'un cours")
    ap.add_argument("--sans-test", action="store_true", help="(diagnostic) sauter test_layout.py")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    site = root / "site"

    # 1. le validateur fait foi
    print("1. validate.py")
    r = subprocess.run([sys.executable, str(root / "tools" / "validate.py"), "--root", str(root), "--json"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        print("build refusé : graphe invalide", file=sys.stderr)
        return 1
    v = json.loads(r.stdout)
    print("   %d notions · 0 erreur · %d avertissement(s) · dette : %s"
          % (v["notions"], len(v["W"]), ", ".join("%s = %d" % kv for kv in sorted(v["dette"].items())) or "aucune"))

    # 2. chargement et dérivés (A9)
    print("2. chargement et dérivés (A9)")
    m = deriver(charger(root))
    if a.course:
        if a.course not in m["cours"]:
            print("cours inconnu : " + a.course, file=sys.stderr)
            return 1
        codes = [a.course]
    else:
        codes = sorted(m["cours"])
    dt = {k: sum(len(dette_du_cours(m, c)[k]) for c in m["cours"]) for k in ("liens", "gestes", "exemples", "inventaire")}
    attendu = {"liens à venir": dt["liens"], "Geste de calcul type à venir": dt["gestes"],
               "Exemple minimal à venir": dt["exemples"], "inventaire à venir": dt["inventaire"]}
    for k, n in attendu.items():
        if v["dette"].get(k, 0) != n:
            print("   avertissement : dette « %s » = %d ici, %d pour le validateur"
                  % (k, n, v["dette"].get(k, 0)), file=sys.stderr)

    if dt["exemples"]:
        sys.stdout.flush()          # sinon l'avertissement stderr sort avant l'étape 1
        print("   faute de protocole : %d exemples minimaux à venir — SPEC-INGESTION étape 3 "
              "les exclut de la dette" % dt["exemples"], file=sys.stderr)

    # 3. le test de disposition (SPEC-SITE §5)
    if a.sans_test:
        print("3. test_layout.py SAUTÉ (--sans-test)")
    else:
        print("3. tools/tests/test_layout.py")
        t = subprocess.run([sys.executable, str(root / "tools" / "tests" / "test_layout.py"), "--root", str(root)],
                           capture_output=True, text=True)
        sys.stdout.write("".join("   " + l + "\n" for l in t.stdout.strip().splitlines() if l))
        if t.returncode != 0:
            sys.stderr.write(t.stderr)
            print("build refusé : la disposition de l'arbre viole une propriété de SPEC-SITE §5", file=sys.stderr)
            return 1

    # 4. génération
    print("4. site/")
    nettoyer(site)
    site.mkdir(parents=True, exist_ok=True)
    (site / ".nojekyll").touch()
    if a.offline:
        mathjax_offline(site)
        m["mathjax_src"] = lambda rel: rel + "vendor/mathjax/tex-svg.js"
    else:
        m["mathjax_src"] = lambda rel: MATHJAX_CDN

    tailles = []
    ecrire(site / "search-index.js", index_recherche(m), tailles)
    ecrire(site / "index.html", page_accueil(m), tailles)
    for r_ in m["rapports"]:
        ecrire(site / "rapports" / (r_["slug"] + ".html"), page_rapport(m, r_), tailles)
    for code in codes:
        ecrire(site / code / "index.html", page_cours(m, code), tailles)
        ecrire(site / code / "arbre.html", page_arbre(m, code), tailles)
        ecrire(site / code / "inventaire.html", page_inventaire(m, code), tailles)
        for i in m["cours"][code]["notions"]:
            ecrire(site / code / "n" / (i.split("/", 1)[1] + ".html"), page_fiche(m, i), tailles)
        for x in m["cours"][code]["exercices"]:
            ecrire(site / code / "exercices" / (m["exercices"][x]["slug"] + ".html"), page_exercice(m, x), tailles)

    # 5. contraintes de SPEC-SITE §4
    trop = [(p, n) for p, n in tailles if n > TAILLE_MAX]
    for p, n in trop:
        print("   page trop lourde : %s = %d ko > 300 ko" % (p.relative_to(root), n // 1024), file=sys.stderr)
    if trop:
        return 1
    plus = max(tailles, key=lambda x: x[1])
    print("   %d fichiers · la plus lourde : %s (%d ko) · limite 300 ko"
          % (len(tailles), plus[0].relative_to(root), plus[1] // 1024))
    print("   ouvrir : site/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
