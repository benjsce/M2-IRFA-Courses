#!/usr/bin/env python3
"""
validate.py — vérifie les axiomes A1–A13 de SPEC-MODELE.md sur courses/.

Usage : python tools/validate.py [--root .] [--json]
Sortie : liste des erreurs (E) et avertissements (W), dette, code de retour 1 si E.

Dépendance : pyyaml.
"""
from __future__ import annotations
import argparse, json, re, sys, unicodedata
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("pyyaml manquant : pip install pyyaml", file=sys.stderr)
    sys.exit(2)

TYPES = {"principe", "notion", "abstraite"}
STATUTS = {"source", "ajout", "retiree"}

RUBRIQUES = [  # (titre, obligatoire pour quels types, condition)
    "Ce que c'est",
    "Forme",
    "Ce qui la définit",
    "Ce que les membres partagent",
    "Pourquoi ce niveau existe",
    "Le chemin jusqu'ici",
    "Exemple minimal",
    "Geste de calcul type",
    "Ce qui reste libre",
    "Cesse d'être valide quand",
    "Origine",
]
ORDRE = {t: i for i, t in enumerate(RUBRIQUES)}
DERIVEES = {"Sert ensuite à", "Membres", "Socle", "Socle complet", "Niveau",
            "Le paramètre qui les distingue", "Cas particulier de", "Construite à partir de"}

MARKER = re.compile(r"\[([^\[\]]+)\]\s*$")

# Un nombre écrit en toutes lettres devant une quantité que le générateur calcule :
# « treize notions au socle », « quatre membres ». Vrai le jour où on l'écrit, faux la
# semaine d'après, et rien ne le signale. CLAUDE.md, interdictions absolues.
# « un/une » et « niveaux » sont hors du motif : ce sont presque toujours des articles
# ou des tournures ordinaires (« deux niveaux de richesse », « pas une notion »).
NOMBRE_DERIVE = re.compile(
    r"\b(deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|quatorze|quinze"
    r"|\d+)\s+(notions?|membres?|prérequis|fiches?)\b", re.I)


class Rapport:
    def __init__(self):
        self.E, self.W = [], []
        self.dette = defaultdict(int)

    def e(self, ax, ou, msg): self.E.append((ax, ou, msg))
    def w(self, ax, ou, msg): self.W.append((ax, ou, msg))


# ---------------------------------------------------------------- lecture

def lire_fiche(path: Path):
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---\n"):
        raise ValueError("en-tête YAML absent")
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


def blocs(texte: str):
    """Paragraphes séparés par une ligne vide ; une table est un seul bloc."""
    out, cur = [], []
    for line in texte.splitlines():
        if line.strip() == "":
            if cur: out.append("\n".join(cur)); cur = []
        else:
            cur.append(line)
    if cur: out.append("\n".join(cur))
    return out


# ---------------------------------------------------------------- validation

def valider(root: Path, rap: Rapport):
    courses_dir = root / "courses"
    if not courses_dir.is_dir():
        rap.e("A1", "courses/", "dossier absent"); return {}

    N = {}            # id -> dict(meta=..., sections=..., course=..., path=...)
    courses = {}      # code -> course.yml
    notations = {}    # code -> set(symboles)
    a_venir = {}      # id -> raison
    inventaires = {}  # code -> liste
    declarees = []    # (code, entrée collisions) — déclarations de collision de symbole
    homonymes = []    # (code, entrée homonymes) — déclarations d'homonymie de nom

    for cdir in sorted(p for p in courses_dir.iterdir() if p.is_dir()):
        code = cdir.name
        cy = cdir / "course.yml"
        if not cy.exists():
            rap.e("A1", str(cy), "course.yml absent"); continue
        courses[code] = yaml.safe_load(cy.read_text(encoding="utf-8")) or {}
        if courses[code].get("code") != code:
            rap.e("A1", str(cy), f"code '{courses[code].get('code')}' ≠ dossier '{code}'")

        # notations
        nf = cdir / "notation.yml"
        syms = set()
        if nf.exists():
            nd = yaml.safe_load(nf.read_text(encoding="utf-8")) or {}
            for s in nd.get("symboles", []) or []:
                syms.add(s.get("symbole", "").strip())
            for c in nd.get("collisions", []) or []:
                declarees.append((code, c))
            for h in nd.get("homonymes", []) or []:
                homonymes.append((code, h))
        notations[code] = syms

        # a-venir
        av = cdir / "a-venir.yml"
        if av.exists():
            for it in yaml.safe_load(av.read_text(encoding="utf-8")) or []:
                a_venir[it["id"]] = it.get("raison", "")

        # inventaire
        inv = cdir / "inventaire.yml"
        inventaires[code] = (yaml.safe_load(inv.read_text(encoding="utf-8")) or {}).get("elements", []) if inv.exists() else None

        # fiches
        ndir = cdir / "notions"
        if not ndir.is_dir():
            rap.e("A1", str(ndir), "dossier notions/ absent"); continue
        for f in sorted(ndir.glob("*.md")):
            try:
                meta, sections = lire_fiche(f)
            except Exception as ex:
                rap.e("A1", str(f), f"fiche illisible : {ex}"); continue
            nid = meta.get("id")
            if not nid:
                rap.e("A1", str(f), "id manquant"); continue
            if nid in N:
                rap.e("A1", str(f), f"id dupliqué : {nid} (déjà dans {N[nid]['path']})"); continue
            if nid != f"{code}/{f.stem}":
                rap.e("A1", str(f), f"id '{nid}' doit valoir '{code}/{f.stem}'")
            N[nid] = dict(meta=meta, sections=sections, course=code, path=str(f.relative_to(root)))

    # ---- champs et types
    for nid, n in N.items():
        m = n["meta"]
        t = m.get("type")
        if t not in TYPES:
            rap.e("A1", nid, f"type invalide : {t}")
        if m.get("statut", "source") not in STATUTS:
            rap.e("A11", nid, f"statut invalide : {m.get('statut')}")
        if not m.get("nom"):
            rap.e("A1", nid, "nom manquant")
        cap = m.get("construite_a_partir_de")
        if cap is not None and not isinstance(cap, list):
            rap.e("A1", nid, "construite_a_partir_de doit être une liste")
        if isinstance(m.get("cas_de"), list):
            rap.e("A4", nid, "cas_de doit être un identifiant unique, pas une liste")

    D = {nid: [x for x in (n["meta"].get("construite_a_partir_de") or []) if isinstance(x, str)] for nid, n in N.items()}
    A = {nid: n["meta"].get("cas_de") for nid, n in N.items()}
    A_inv = defaultdict(list)
    for x, y in A.items():
        if y: A_inv[y].append(x)

    # ---- A2 fermeture des références
    for nid in N:
        for y in D[nid] + ([A[nid]] if A[nid] else []):
            if y in N: continue
            if y in a_venir:
                rap.w("A2", nid, f"référence à venir : {y} ({a_venir[y]})"); rap.dette["liens à venir"] += 1
            else:
                rap.e("A2", nid, f"référence inconnue et non déclarée à venir : {y}")

    # ---- A3 acyclicité de D
    def cycles(G):
        WHITE, GREY, BLACK = 0, 1, 2
        col = {k: WHITE for k in G}; found = []
        def dfs(u, stack):
            col[u] = GREY; stack.append(u)
            for v in G.get(u, []):
                if v not in col: continue
                if col[v] == GREY: found.append(stack[stack.index(v):] + [v])
                elif col[v] == WHITE: dfs(v, stack)
            stack.pop(); col[u] = BLACK
        for k in G:
            if col[k] == WHITE: dfs(k, [])
        return found
    for cyc in cycles(D):
        rap.e("A3", " → ".join(cyc), "cycle de dépendance : ces notions sont probablement une seule, ou un principe manque")

    # ---- A4 forêt d'abstraction
    Ag = {k: ([v] if v in N else []) for k, v in A.items()}
    for cyc in cycles(Ag):
        rap.e("A4", " → ".join(cyc), "cycle d'abstraction")
    for x, y in A.items():
        if y in N:
            ty = N[y]["meta"].get("type")
            if ty not in {"abstraite", "principe"}:
                rap.e("A4", x, f"cas_de pointe vers '{y}' de type {ty} ; seuls abstraite ou principe sont admis")
            if N[x]["course"] != N[y]["course"]:
                rap.e("A10", x, f"cas_de vers un autre cours ({y}) : interdit")
    for y, members in A_inv.items():
        if y in N and A[y] is None and N[y]["meta"].get("type") != "principe":
            rap.e("A4", y, "racine de l'arbre d'abstraction avec des membres, mais pas de type principe")

    # ---- A5 règle des frères
    for nid, n in N.items():
        if n["meta"].get("type") != "abstraite": continue
        nb = len(A_inv.get(nid, []))
        parent = A[nid]
        freres = len(A_inv.get(parent, [])) if parent else 0
        if nb < 2 and freres < 2:
            rap.e("A5", nid, f"abstraite avec {nb} membre(s) et {freres} frère(s) : niveau non justifié")

    # ---- A6 paramètre générateur
    for nid, n in N.items():
        m = n["meta"]
        if m.get("type") == "abstraite" and not m.get("parametre"):
            rap.e("A6", nid, "abstraite sans 'parametre'")
        p = A[nid]
        if p in N and N[p]["meta"].get("type") == "abstraite" and not m.get("valeur"):
            rap.e("A6", nid, f"membre de l'abstraite {p} sans 'valeur'")
    for y, members in A_inv.items():
        if y in N and N[y]["meta"].get("type") == "abstraite":
            vals = defaultdict(list)
            for x in members:
                v = N[x]["meta"].get("valeur")
                if v: vals[str(v).strip()].append(x)
            for v, xs in vals.items():
                if len(xs) > 1:
                    rap.e("A6", y, f"valeur '{v}' partagée par {xs} : même cas, ou paramètre mal choisi")

    # ---- A7 disjonction ; A8 réduction transitive
    def anc_abs(x):
        s, p = set(), A.get(x)
        while p and p in N and p not in s:
            s.add(p); p = A.get(p)
        return s
    reach = {}
    def reach_of(x, seen=None):
        if x in reach: return reach[x]
        seen = seen or set()
        if x in seen: return set()
        seen.add(x)
        s = set()
        for y in D.get(x, []):
            s.add(y); s |= reach_of(y, seen)
        reach[x] = s; return s
    for nid in N:
        aa = anc_abs(nid)
        for y in D[nid]:
            if y in aa:
                rap.e("A7", nid, f"dépend de son ancêtre d'abstraction {y}")
        for y in D[nid]:
            if any(g != y and y in reach_of(g) for g in D[nid]):
                rap.w("A8", nid, f"dépendance redondante : {y} est déjà atteinte via une autre dépendance ; à retirer")

    # ---- « Le chemin jusqu'ici » : la prose qui raconte le socle
    # Le socle est dérivé, ce paragraphe est écrit : les deux peuvent diverger en
    # silence dès qu'une dépendance change en amont. Deux garde-fous : la rubrique est
    # exigée dès que le socle existe, et toute notion qu'elle nomme doit y être.
    for nid, n in N.items():
        S = dict(n["sections"])
        socle = reach_of(nid)
        txt = S.get("Le chemin jusqu'ici")
        if txt is None:
            if socle:
                rap.w("A1", nid, f"« Le chemin jusqu'ici » à écrire ({len(socle)} notions au socle)")
                rap.dette["chemin jusqu'ici à écrire"] += 1
            continue
        if not socle:
            rap.e("A1", nid, "« Le chemin jusqu'ici » sur une fiche sans socle : rien à raconter")
            continue
        cites = set(re.findall(r"\b([a-z][a-z0-9-]*/[a-z0-9-]+)\b", txt))
        for y in sorted(cites - socle - {nid}):
            if y in N:
                rap.e("A1", nid, f"« Le chemin jusqu'ici » cite {y}, qui n'est pas dans son socle")
        # Le paragraphe doit nommer CHAQUE notion du socle : sinon il explique une partie
        # du chemin et laisse le reste sans raison, ce qui est exactement la question que
        # la rubrique existe pour éviter. Signalé par l'utilisateur le 2026-09-20, sur
        # dup/assurance-probabiliste : 1 notion nommée sur 4.
        oublie = sorted(socle - cites)
        if oublie:
            rap.w("A1", nid, "« Le chemin jusqu'ici » ne nomme pas %d notion(s) de son socle : %s"
                  % (len(oublie), ", ".join(oublie[:4]) + (" …" if len(oublie) > 4 else "")))
            rap.dette["chemin jusqu'ici incomplet"] += 1

    # ---- nombres dérivés écrits en dur dans la prose
    for nid, n in N.items():
        for t, v in n["sections"]:
            for x in NOMBRE_DERIVE.finditer(v):
                rap.w("A1", nid, "[%s] nombre calculé écrit en dur : « %s » — le générateur "
                                 "l'affiche déjà, et la prose deviendra fausse" % (t, x.group(0)))
                rap.dette["nombre calculé en dur"] += 1

    # ---- ouvertures identiques du « chemin jusqu'ici »
    # Rédigées en série, ces proses convergent vers un gabarit : la même phrase
    # d'ouverture se retrouvait sur douze fiches le 2026-09-20, signalé par
    # l'utilisateur. Une phrase identique ne se justifie que par un socle identique ;
    # c'est le cas des grecques, qui partagent le socle de la formule.
    ouvertures = defaultdict(list)
    for nid, n in N.items():
        txt = dict(n["sections"]).get("Le chemin jusqu'ici")
        if not txt:
            continue
        tete = re.split(r"(?<=[.!?])\s", txt.strip().split("\n")[0])[0]
        cle = re.sub(r"\b[a-z][a-z0-9-]*/[a-z0-9-]+\b", "X", tete).strip()
        if len(cle) > 20:
            ouvertures[cle].append(nid)
    for cle, ids in sorted(ouvertures.items()):
        if len(ids) < 2:
            continue
        socles = {frozenset(reach_of(i)) for i in ids}
        if len(socles) == 1:
            continue          # même socle : la même phrase est honnête
        for nid in sorted(ids):
            rap.w("A1", nid, "« Le chemin jusqu'ici » ouvre comme %d autre(s) fiche(s) "
                             "de socle différent : « %s »" % (len(ids) - 1, cle[:60]))
            rap.dette["chemin sur gabarit"] += 1

    # ---- A9 sections interdites ; rubriques, ordre, obligations, marqueurs (A11)
    for nid, n in N.items():
        m, secs = n["meta"], n["sections"]
        titres = [t for t, _ in secs]
        for t in titres:
            if t in DERIVEES:
                rap.e("A9", nid, f"section dérivée écrite à la main : « {t} »")
            elif t not in ORDRE:
                rap.e("A1", nid, f"rubrique inconnue : « {t} »")
        idx = [ORDRE[t] for t in titres if t in ORDRE]
        if idx != sorted(idx):
            rap.e("A1", nid, f"rubriques dans le désordre : {titres}")
        if len(set(titres)) != len(titres):
            rap.e("A1", nid, "rubrique dupliquée")
        S = dict(secs)
        typ = m.get("type")
        if "Ce que c'est" not in S:
            rap.e("A1", nid, "« Ce que c'est » manquant")
        else:
            txt = MARKER.sub("", S["Ce que c'est"]).strip()
            if len(txt) > 220:
                rap.e("A1", nid, f"« Ce que c'est » trop long ({len(txt)} > 220) : le grain est mauvais, scinder")
            if ". " in txt:
                rap.w("A1", nid, "« Ce que c'est » semble contenir plusieurs phrases")
        if typ == "abstraite":
            if "Ce que les membres partagent" not in S: rap.e("A1", nid, "abstraite sans « Ce que les membres partagent »")
            if "Ce qui la définit" in S: rap.e("A1", nid, "abstraite avec « Ce qui la définit » (réservé aux notions et principes)")
            if "Pourquoi ce niveau existe" not in S: rap.e("A1", nid, "abstraite sans « Pourquoi ce niveau existe »")
        else:
            if "Ce qui la définit" not in S: rap.e("A1", nid, "« Ce qui la définit » manquant")
            if "Ce que les membres partagent" in S: rap.e("A1", nid, "« Ce que les membres partagent » réservé aux abstraites")
            if "Pourquoi ce niveau existe" in S: rap.e("A1", nid, "« Pourquoi ce niveau existe » réservé aux abstraites")
        if "Cesse d'être valide quand" not in S:
            rap.e("A1", nid, "« Cesse d'être valide quand » manquant")
        if "Forme" in S:
            for r in ("Exemple minimal", "Geste de calcul type"):
                if r not in S:
                    rap.e("A1", nid, f"« {r} » obligatoire quand « Forme » est présente")
                elif "à venir" in S[r]:
                    if r == "Exemple minimal":
                        # SPEC-INGESTION étape 3 : « Elle ne dépend d'aucun exercice et s'écrit
                        # dès la création de la fiche ; la laisser en dette est une faute de
                        # protocole. » Ce n'est donc pas de la dette, c'est une erreur.
                        rap.e("A1", nid, "« Exemple minimal » à venir : il ne dépend d'aucun "
                                         "exercice et s'écrit dès la création de la fiche "
                                         "(SPEC-INGESTION étape 3)")
                    else:
                        rap.w("A1", nid, f"« {r} » à venir"); rap.dette[f"{r} à venir"] += 1
        # marqueurs par bloc
        pat = courses[n["course"]].get("refs_pattern")
        rx = re.compile(pat) if pat else None
        for t, body in secs:
            for b in blocs(body):
                last = b.splitlines()[-1]
                mk = MARKER.search(last)
                if not mk:
                    rap.e("A11", nid, f"[{t}] bloc sans marqueur de référence : « {b[:60]}… »")
                    continue
                for tok in [x.strip() for x in mk.group(1).split(",")]:
                    if tok == "ajout": continue
                    if rx and not rx.match(tok):
                        rap.e("A11", nid, f"[{t}] référence hors grammaire : « {tok} »")

    # ---- A10 acyclicité entre cours
    Q = defaultdict(set)
    for x, ys in D.items():
        for y in ys:
            if y in N and N[y]["course"] != N[x]["course"]:
                Q[N[x]["course"]].add(N[y]["course"])
    Qg = {c: list(s) for c, s in Q.items()}
    for c in courses: Qg.setdefault(c, [])
    for cyc in cycles(Qg):
        rap.e("A10", " → ".join(cyc), "cycle de dépendance entre cours")

    # ---- A11 projection stricte
    for nid, n in N.items():
        if n["meta"].get("statut", "source") == "source":
            for y in D[nid]:
                if y in N and N[y]["meta"].get("statut") == "ajout":
                    rap.e("A11", nid, f"notion source dépendant d'un ajout : {y}")

    # ---- A12 registre de notations
    for nid, n in N.items():
        sym = (n["meta"].get("symbole") or "").strip()
        if not sym: continue
        reg = notations.get(n["course"], set())
        parts = [s.strip() for s in re.split(r"(?<=\$),\s*(?=\$)", sym)]
        for p in parts:
            if p and p not in reg:
                rap.e("A12", nid, f"symbole « {p} » absent du registre notation.yml")

    # ---- A12 collisions entre cours : déclarées, ou signalées
    # « deux cours peuvent donner deux sens au même symbole ; la collision est déclarée
    # dans notation.yml » (SPEC-MODELE A12). La règle était énoncée, rien ne la vérifiait :
    # cinq collisions inter-registres n'étaient pas déclarées le 2026-09-20.
    # Une déclaration couvre la collision quand elle nomme TOUS les cours concernés :
    # le lecteur doit trouver l'histoire entière au même endroit, pas un morceau par cours.
    couvert = defaultdict(set)     # symbole -> cours nommés par la déclaration la plus large
    for code, c in declarees:
        sym = str(c.get("symbole", "")).strip()
        ail = c.get("ailleurs") or {}
        if not isinstance(ail, dict):
            rap.e("A12", f"{code} notation.yml", f"collision « {sym} » : « ailleurs » doit être "
                                                 "une table <code de cours> : <sens>")
            continue
        for autre in ail:
            if autre not in courses:
                rap.e("A12", f"{code} notation.yml", f"collision « {sym} » : « ailleurs » nomme "
                                                     f"le cours « {autre} », qui n'existe pas")
        nommes = {code} | {a for a in ail if a in courses}
        if len(nommes) > len(couvert[sym]):
            couvert[sym] = nommes

    par_symbole = defaultdict(set)
    for code, syms in notations.items():
        for sym in syms:
            if sym:
                par_symbole[sym].add(code)
    for sym, cs_ in sorted(par_symbole.items()):
        if len(cs_) < 2:
            continue
        manque = cs_ - couvert.get(sym, set())
        if not manque:
            continue
        rap.w("A12", " ↔ ".join(sorted(cs_)),
              f"symbole « {sym} » dans plusieurs registres, collision non déclarée pour "
              f"{', '.join(sorted(manque))} : une entrée « collisions » doit nommer tous "
              "les cours concernés")
        rap.dette["collision de symbole non déclarée"] += 1

    # ---- A12 homonymie : deux fiches que le même mot désigne
    # SPEC-INGESTION étape 2 interdisait le nom ou l'alias en double et affirmait que le
    # validateur le refusait ; il ne le regardait pas. Et l'interdiction est trop forte :
    # « prime de risque » désigne deux grandeurs distinctes dans dup et dans fpp, et les
    # deux fiches doivent exister. Dans un même cours en revanche, c'est une faute.
    declares_hom = set()
    for code, h in homonymes:
        ids = [x for x in (h.get("entre") or []) if isinstance(x, str)]
        if len(ids) < 2:
            rap.e("A12", f"{code} notation.yml", f"homonymie « {h.get('nom')} » : « entre » doit "
                                                 "nommer au moins deux identifiants")
            continue
        for i in ids:
            if i not in N:
                rap.e("A12", f"{code} notation.yml", f"homonymie « {h.get('nom')} » : identifiant "
                                                     f"inconnu {i}")
        for a in ids:
            for b in ids:
                if a < b:
                    declares_hom.add(frozenset({a, b}))

    def aplat(x):
        """Nom comparable : sans accent, sans casse, sans ponctuation."""
        x = unicodedata.normalize("NFD", str(x).lower().replace("\u2019", "'"))
        x = "".join(ch for ch in x if unicodedata.category(ch) != "Mn")
        return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", x)).strip()

    appellations = defaultdict(set)
    for nid, n in N.items():
        m = n["meta"]
        for mot in [m.get("nom")] + list(m.get("alias") or []):
            if isinstance(mot, str) and aplat(mot):
                appellations[aplat(mot)].add(nid)
    vus = set()
    for mot, ids in sorted(appellations.items()):
        if len(ids) < 2:
            continue
        for a, b in ((x, y) for x in sorted(ids) for y in sorted(ids) if x < y):
            if N[a]["course"] == N[b]["course"]:
                rap.e("A12", a, f"« {mot} » désigne aussi {b} dans le même cours : "
                                "un cours ne nomme pas deux notions de la même façon")
            elif frozenset({a, b}) not in declares_hom and frozenset({a, b}) not in vus:
                vus.add(frozenset({a, b}))
                rap.w("A12", f"{a} ↔ {b}", f"« {mot} » désigne les deux, homonymie non déclarée : "
                                           "l'ajouter aux « homonymes » de l'un des deux registres")
                rap.dette["homonymie non déclarée"] += 1

    # ---- les documents de loi existent en double et se recopient à la main
    # Racine et proj/ portent les mêmes quatre documents. Rien ne garantissait qu'ils
    # restent identiques : une modification faite d'un côté se découvre le jour où les
    # deux textes se contredisent. Signalé cinq fois au rapport sans être vérifié.
    LOIS = ("CLAUDE.md", "SPEC-MODELE.md", "SPEC-INGESTION.md", "SPEC-SITE.md")
    abs_root = root.resolve()          # « . » n'a pas de parent utilisable
    for nom in LOIS:
        ici, la = abs_root / nom, abs_root.parent / nom
        if not ici.exists() or not la.exists():
            continue
        if ici.read_bytes() != la.read_bytes():
            rap.e("A1", nom, "les deux copies du document ont divergé : "
                             f"{ici.parent.name}/ et {la.parent.name}/ ne portent "
                             "plus le même texte")

    # ---- A13 couverture
    for code, elems in inventaires.items():
        if elems is None:
            rap.e("A13", code, "inventaire.yml absent"); continue
        for el in elems:
            keys = [k for k in ("notion", "absorbe", "exclu", "a_venir") if k in el]
            ref = el.get("ref", "?")
            if len(keys) != 1:
                rap.e("A13", f"{code} inventaire {ref}", f"exactement une image attendue, trouvé {keys}")
                continue
            k = keys[0]
            if k in ("notion", "absorbe") and el[k] not in N:
                rap.e("A13", f"{code} inventaire {ref}", f"{k} vers un id inconnu : {el[k]}")
            if k == "a_venir":
                rap.w("A13", f"{code} inventaire {ref}", f"à venir ({el[k]})"); rap.dette["inventaire à venir"] += 1
    return N


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rap = Rapport()
    N = valider(Path(a.root), rap)
    if a.json:
        print(json.dumps(dict(E=rap.E, W=rap.W, dette=dict(rap.dette), notions=len(N)), ensure_ascii=False, indent=1))
    else:
        for ax, ou, msg in rap.E: print(f"E {ax:4} {ou}: {msg}")
        for ax, ou, msg in rap.W: print(f"W {ax:4} {ou}: {msg}")
        print(f"\n{len(N)} notions · {len(rap.E)} erreur(s) · {len(rap.W)} avertissement(s)")
        if rap.dette:
            print("dette : " + ", ".join(f"{k} = {v}" for k, v in rap.dette.items()))
    sys.exit(1 if rap.E else 0)


if __name__ == "__main__":
    main()
