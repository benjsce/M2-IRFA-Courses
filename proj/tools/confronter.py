#!/usr/bin/env python3
"""
confronter.py — l'étape 2 de SPEC-INGESTION, calculée.

« Le danger de ce projet n'est pas l'erreur ponctuelle, c'est la réécriture zélée de ce
qui existe déjà. » L'étape 2 demande de chercher, pour chaque élément d'une source
nouvelle, s'il correspond à une notion existante — par `nom`, par `alias`, par `symbole`,
et par le sens. Les trois premières routes se calculent ; la quatrième, non.

Cet outil ne décide rien et n'écrit rien. Il imprime une **liste de travail** : les
rapprochements à examiner, et rien de plus. Un rapprochement qu'il signale peut être une
homonymie légitime ; un rapprochement qu'il manque reste possible, parce que deux cours
peuvent nommer différemment la même chose. Il réduit la surface à lire, il ne la supprime
pas.

Quatre usages, un par question de l'étape 2 :

  python tools/confronter.py --refs fpp refs.txt
      « Ce matériau est la suite d'un cours déjà ouvert : qu'est-ce que l'inventaire
        connaît déjà ? » Route exacte, par référence de source. C'est la seule fiable.

  python tools/confronter.py --noms "Régression ridge" "Sélection pas à pas"
      « Ces noms candidats existent-ils déjà, ailleurs ? » Route approchée, par nom et
        par alias, avant qu'aucune fiche ne soit écrite.

  python tools/confronter.py --cours dss
      « Ce cours-ci, une fois écrit, recouvre-t-il un autre ? » Le même calcul sur les
        fiches déjà en place, plus les symboles partagés avec les autres registres.

  python tools/confronter.py --aval dss/bootstrap
      « Si j'insère quelque chose sous ces notions, quels chemins déjà écrits devrai-je
        relire ? » Descendance par D^-1. Le validateur signale le cas une fois l'arête
        posée ; cette liste se lit avant.

Usage : python tools/confronter.py [--root .] <un des quatre modes> [--seuil 0.45]
Sortie : une liste de travail, sur la sortie standard. Code de retour toujours 0 :
         cet outil ne juge pas.

Dépendance : pyyaml.
"""
from __future__ import annotations
import argparse, difflib, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml manquant : pip install pyyaml", file=sys.stderr)
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import lire_fiche              # noqa: E402

for _f in (sys.stdout, sys.stderr):          # cp1252 sous PowerShell
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

# Mots trop fréquents pour rapprocher quoi que ce soit : « fonction de répartition » et
# « fonction d'utilité » ne se ressemblent que par « fonction ». Ils comptent dans la
# similarité de chaîne, pas dans celle des mots.
VIDES = {"de", "du", "des", "la", "le", "les", "l", "d", "un", "une", "a", "au", "aux",
         "et", "ou", "en", "par", "pour", "sur", "the", "of", "a", "an"}


def aplat(x):
    """Chaîne comparable : sans accent, sans casse, sans ponctuation."""
    x = unicodedata.normalize("NFD", str(x).lower().replace("’", "'"))
    x = "".join(ch for ch in x if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]", " ", x)).strip()


def mots(x):
    return {m for m in aplat(x).split() if m not in VIDES}


RACINE = 5      # longueur du préfixe qui fait considérer deux mots comme apparentés


def meme_racine(a, b):
    """Deux chaînes partagent-elles une racine de mot ? « régression ridge » et
    « régression sur composantes principales », oui. « arbre de décision » et
    « invariance de description », non : « déci » et « descr » divergent au troisième
    caractère."""
    ta = [t for t in aplat(a).split() if len(t) >= RACINE]
    tb = [t for t in aplat(b).split() if len(t) >= RACINE]
    return any(x[:RACINE] == y[:RACINE] for x in ta for y in tb)


def proximite(a, b):
    """Deux mesures, on garde la plus favorable. Les mots communs rattrapent l'ordre
    inversé (« aversion au risque » / « risque et aversion ») ; la similarité de chaîne
    rattrape les variantes d'une même racine (« régularisation » / « régulariser »).

    La seconde ne compte que si les deux chaînes partagent une racine : sans ce filtre,
    la similarité de caractères rapproche n'importe quels noms français de même longueur.
    Mesuré sur le corpus du 2026-09-20 : 1610 paires inter-cours au-dessus du seuil sans
    le filtre, 71 avec, et aucun rapprochement vrai perdu."""
    ma, mb = mots(a), mots(b)
    j = len(ma & mb) / len(ma | mb) if ma | mb else 0.0
    r = difflib.SequenceMatcher(None, aplat(a), aplat(b)).ratio()
    if not meme_racine(a, b):
        r = 0.0
    return max(j, r), j, r


# ---------------------------------------------------------------- lecture du dépôt

def charger(root: Path):
    fiches, registres, inventaires = {}, {}, {}
    cdir = root / "courses"
    if not cdir.is_dir():
        sys.exit("courses/ introuvable — lancer depuis la racine du dépôt, ou passer --root")
    for d in sorted(p for p in cdir.iterdir() if p.is_dir()):
        code = d.name
        for f in sorted((d / "notions").glob("*.md")) if (d / "notions").is_dir() else []:
            try:
                meta, _ = lire_fiche(f)
            except Exception:
                continue
            if meta.get("id"):
                meta["_cours"] = code
                fiches[meta["id"]] = meta
        nf = d / "notation.yml"
        if nf.exists():
            nd = yaml.safe_load(nf.read_text(encoding="utf-8")) or {}
            registres[code] = {str(s.get("symbole", "")).strip(): s
                               for s in (nd.get("symboles") or [])}
        inv = d / "inventaire.yml"
        if inv.exists():
            nd = yaml.safe_load(inv.read_text(encoding="utf-8")) or {}
            inventaires[code] = nd.get("elements") or []
    return fiches, registres, inventaires


def appellations(fiches):
    """id -> liste des chaînes sous lesquelles la fiche peut être cherchée."""
    out = {}
    for nid, m in fiches.items():
        out[nid] = [m.get("nom", "")] + [a for a in (m.get("alias") or [])
                                         if isinstance(a, str)]
    return out


# ---------------------------------------------------------------- les quatre modes

def mode_refs(code, source, inventaires):
    elems = inventaires.get(code)
    if elems is None:
        sys.exit("pas d'inventaire pour le cours « %s »" % code)
    connu = {}
    for el in elems:
        r = str(el.get("ref", "")).strip()
        img = next((f"{k} → {el[k]}" for k in ("notion", "absorbe", "exclu", "a_venir")
                    if k in el), "sans image")
        connu.setdefault(aplat(r), (r, el.get("intitule", ""), img))
    lignes = [l.strip() for l in source if l.strip()]
    print("Confrontation à l'inventaire de « %s » — route exacte, par référence.\n" % code)
    deja, neuf = [], []
    for l in lignes:
        (deja if aplat(l) in connu else neuf).append(l)
    print("  DÉJÀ DANS L'INVENTAIRE (%d) — ne pas réécrire :" % len(deja))
    for l in deja:
        r, intitule, img = connu[aplat(l)]
        print("    %-14s %s" % (r, img) + (("  — " + intitule) if intitule else ""))
    print("\n  ABSENT DE L'INVENTAIRE (%d) — à inventorier à l'étape 1 :" % len(neuf))
    for l in neuf:
        print("    " + l)
    print("\n  Rappel : une référence déjà inventoriée peut malgré tout apporter du contenu")
    print("  nouveau. « Déjà inventoriée » veut dire « la source l'a déjà dite », pas")
    print("  « la fiche est complète ».")


def mode_noms(candidats, fiches, seuil, k):
    noms = appellations(fiches)
    print("Confrontation par nom et par alias — route approchée.\n")
    for c in candidats:
        scores = []
        for nid, formes in noms.items():
            best = max(((proximite(c, f)[0], f) for f in formes if f), default=(0.0, ""))
            if best[0] >= seuil:
                scores.append((best[0], nid, best[1]))
        scores.sort(reverse=True)
        print("  « %s »" % c)
        if not scores:
            print("      rien de proche — candidat à une fiche nouvelle")
        for sc, nid, forme in scores[:k]:
            via = "nom" if aplat(forme) == aplat(fiches[nid].get("nom", "")) else "alias"
            print("      %.2f  %-42s %s « %s »" % (sc, nid, via, forme))
        print()


def mode_cours(code, fiches, registres, seuil, k):
    dedans = {i: m for i, m in fiches.items() if m["_cours"] == code}
    if not dedans:
        sys.exit("aucune fiche pour le cours « %s »" % code)
    dehors = {i: m for i, m in fiches.items() if m["_cours"] != code}
    noms = appellations(dehors)
    print("Recouvrement de « %s » avec les autres cours.\n" % code)
    print("  — par nom et par alias\n")
    vu = 0
    for nid, m in sorted(dedans.items()):
        formes = [m.get("nom", "")] + [a for a in (m.get("alias") or []) if isinstance(a, str)]
        scores = []
        for autre, fautres in noms.items():
            best = max(((proximite(x, y)[0], x, y)
                        for x in formes if x for y in fautres if y), default=(0.0, "", ""))
            if best[0] >= seuil:
                scores.append((best[0], autre, best[1], best[2]))
        if not scores:
            continue
        vu += 1
        scores.sort(reverse=True)
        print("    %s « %s »" % (nid, m.get("nom", "")))
        for sc, autre, ici, la in scores[:k]:
            print("        %.2f  %-40s « %s » ≈ « %s »" % (sc, autre, ici, la))
    if not vu:
        print("    aucun rapprochement au-dessus du seuil")

    print("\n  — par symbole, entre registres\n")
    mien = registres.get(code, {})
    n = 0
    for sym, s in sorted(mien.items()):
        ailleurs = [(c, r[sym]) for c, r in registres.items() if c != code and sym in r]
        if not ailleurs:
            continue
        n += 1
        print("    %-12s %s : %s" % (sym, code, s.get("sens", "?")))
        for c, o in ailleurs:
            print("    %-12s %s : %s" % ("", c, o.get("sens", "?")))
    if not n:
        print("    aucun symbole partagé")
    print("\n  Une collision de symbole se déclare dans « collisions » ; une homonymie de")
    print("  nom, dans « homonymes ». Le validateur exige l'une et l'autre.")


def mode_aval(ids, fiches):
    D_inv = defaultdict(set)
    for nid, m in fiches.items():
        for y in (m.get("construite_a_partir_de") or []):
            if isinstance(y, str):
                D_inv[y].add(nid)
    print("Chemins à relire si ces notions gagnent un amont.\n")
    for i in ids:
        if i not in fiches:
            print("  %s : identifiant inconnu" % i)
            continue
        vus, pile = set(), [i]
        while pile:
            x = pile.pop()
            for y in D_inv.get(x, ()):
                if y not in vus:
                    vus.add(y)
                    pile.append(y)
        print("  %s — %s en aval" % (i, len(vus) or "rien"))
        for y in sorted(vus):
            print("      %s" % y)
        print()
    print("  Le « chemin jusqu'ici » de chacune nomme son socle en entier ; le socle")
    print("  grandit, la prose ne suit pas. Le validateur le signale une fois l'arête")
    print("  posée — cette liste sert à le savoir avant.")


def main():
    ap = argparse.ArgumentParser(description="confrontation à l'existant (SPEC-INGESTION étape 2)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--seuil", type=float, default=0.45,
                    help="proximité minimale affichée (défaut 0.45)")
    ap.add_argument("--max", type=int, default=6, help="voisins affichés par candidat")
    ap.add_argument("--refs", nargs=2, metavar=("CODE", "FICHIER"),
                    help="références à confronter à l'inventaire ; « - » pour l'entrée standard")
    ap.add_argument("--noms", nargs="+", metavar="NOM")
    ap.add_argument("--fichier", metavar="FICHIER", help="un nom candidat par ligne")
    ap.add_argument("--cours", metavar="CODE")
    ap.add_argument("--aval", nargs="+", metavar="ID")
    a = ap.parse_args()

    root = Path(a.root)
    fiches, registres, inventaires = charger(root)

    if a.refs:
        code, f = a.refs
        src = sys.stdin if f == "-" else open(f, encoding="utf-8")
        mode_refs(code, src, inventaires)
    elif a.noms or a.fichier:
        cands = list(a.noms or [])
        if a.fichier:
            cands += [l.strip() for l in open(a.fichier, encoding="utf-8") if l.strip()]
        mode_noms(cands, fiches, a.seuil, a.max)
    elif a.cours:
        mode_cours(a.cours, fiches, registres, a.seuil, a.max)
    elif a.aval:
        mode_aval(a.aval, fiches)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
