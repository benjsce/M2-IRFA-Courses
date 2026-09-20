#!/usr/bin/env python3
"""
test_layout.py — test de propriété de la disposition de l'arbre (SPEC-SITE.md §5).

Ce module est la *référence* de l'algorithme de placement : le JavaScript embarqué dans
`<code>/arbre.html` en est la transcription ligne à ligne, et `build.py` importe d'ici les
constantes W, C, G pour les injecter dans la page. Toute modification faite ici doit être
reportée dans `JS_LAYOUT` de `build.py`, et réciproquement.

Usage : python tools/tests/test_layout.py [--root .] [--configs 1000] [--seed 20260920]
Sortie : une ligne par arbre testé ; code de retour ≠ 0 si une propriété est violée.

Dépendance : pyyaml.
"""
from __future__ import annotations
import argparse, random, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml manquant : pip install pyyaml", file=sys.stderr)
    sys.exit(2)

for _f in (sys.stdout, sys.stderr):      # cp1252 sous PowerShell
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

# --- géométrie (SPEC-SITE §5) ; c > w est la condition de disjonction des colonnes ---
W = 220.0   # largeur d'une carte
C = 320.0   # espacement des colonnes
G = 16.0    # écart vertical
EPS = 1e-7

assert C > W, "SPEC-SITE §5 exige c > w"


# ---------------------------------------------------------------- l'algorithme

def disposer(racines, enfants, deplies, hauteurs):
    """Placement en colonnes par profondeur (SPEC-SITE §5).

    racines  : liste ordonnée d'identifiants
    enfants  : id -> liste ordonnée d'identifiants
    deplies  : ensemble des identifiants dont les enfants sont visibles
    hauteurs : id -> hauteur mesurée (une carte masquée n'est jamais mesurée)

    Retourne (tops, prof) pour les seuls nœuds visibles.
    """
    tops, prof, ynext = {}, {}, {}
    plancher = 0.0

    def yn(d):
        return max(ynext.get(d, 0.0), plancher)

    def sous_arbre(n, d, acc):
        acc.append((n, d))
        if n in deplies:
            for k in enfants.get(n, ()):
                sous_arbre(k, d + 1, acc)
        return acc

    def placer(n, d):
        prof[n] = d
        kids = enfants.get(n, ()) if n in deplies else ()
        if not kids:
            tops[n] = yn(d)                                    # 1.
        else:
            for k in kids:                                     # 2. les enfants d'abord
                placer(k, d + 1)
            pr, de = kids[0], kids[-1]
            m = (tops[pr] + hauteurs[pr] / 2 + tops[de] + hauteurs[de] / 2) / 2
            vise = m - hauteurs[n] / 2
            haut = max(yn(d), vise)
            if haut > vise:                                    # le maximum a joué
                delta = haut - vise
                colonnes = set()
                for k in kids:
                    for (x, dx) in sous_arbre(k, d + 1, []):
                        tops[x] += delta
                        colonnes.add(dx)
                for dx in colonnes:
                    ynext[dx] = yn(dx) + delta
            tops[n] = haut
        ynext[d] = tops[n] + hauteurs[n] + G                   # 3.

    for i, r in enumerate(racines):
        if i:
            plancher = max([plancher] + list(ynext.values()))
        placer(r, 0)

    return tops, prof


def visibles(racines, enfants, deplies):
    out = []
    def descendre(n):
        out.append(n)
        if n in deplies:
            for k in enfants.get(n, ()):
                descendre(k)
    for r in racines:
        descendre(r)
    return out


def aretes_visibles(racines, enfants, deplies):
    out = []
    def descendre(n):
        if n in deplies:
            for k in enfants.get(n, ()):
                out.append((n, k))
                descendre(k)
    for r in racines:
        descendre(r)
    return out


# ---------------------------------------------------------------- les propriétés

def bezier_x(x0, x1, t):
    """Abscisse de la Bézier cubique dont les deux points de contrôle sont au milieu."""
    xm = (x0 + x1) / 2
    u = 1 - t
    return u ** 3 * x0 + 3 * u ** 2 * t * xm + 3 * u * t ** 2 * xm + t ** 3 * x1


def verifier(racines, enfants, deplies, hauteurs, tops, prof):
    """Retourne la liste des violations (vide si tout va bien)."""
    fautes = []
    vis = visibles(racines, enfants, deplies)

    # (i) rectangles visibles deux à deux disjoints
    rects = [(n, prof[n] * C, tops[n], prof[n] * C + W, tops[n] + hauteurs[n]) for n in vis]
    for i in range(len(rects)):
        ni, ax0, ay0, ax1, ay1 = rects[i]
        for j in range(i + 1, len(rects)):
            nj, bx0, by0, bx1, by1 = rects[j]
            if ax0 < bx1 - EPS and bx0 < ax1 - EPS and ay0 < by1 - EPS and by0 < ay1 - EPS:
                fautes.append(f"(i) chevauchement {ni} / {nj}")

    # (ii) abscisse de chaque arête entre bord droit du parent et bord gauche de l'enfant
    for (p, k) in aretes_visibles(racines, enfants, deplies):
        xd = prof[p] * C + W
        xg = prof[k] * C
        if xg < xd - EPS:
            fautes.append(f"(ii) colonnes inversées {p} → {k}")
            continue
        for s in range(21):
            x = bezier_x(xd, xg, s / 20)
            if x < xd - EPS or x > xg + EPS:
                fautes.append(f"(ii) arête {p} → {k} sort de l'entre-colonne en t={s/20}")
                break

    # (iii) parent visible entre son premier et son dernier enfant visible
    for n in vis:
        kids = enfants.get(n, ()) if n in deplies else ()
        if not kids:
            continue
        cp = tops[n] + hauteurs[n] / 2
        c1 = tops[kids[0]] + hauteurs[kids[0]] / 2
        c2 = tops[kids[-1]] + hauteurs[kids[-1]] / 2
        lo, hi = min(c1, c2), max(c1, c2)
        if cp < lo - 1e-6 or cp > hi + 1e-6:
            fautes.append(f"(iii) {n} non centré : {cp:.3f} hors de [{lo:.3f}, {hi:.3f}]")

    return fautes


# ---------------------------------------------------------------- les arbres du dépôt

def arbre_du_cours(notions, strict=False):
    """(racines, enfants) de l'arbre d'abstraction. strict=True applique la projection
    A11 : les notions `ajout` disparaissent et leurs membres remontent en racine."""
    ids = {n["id"] for n in notions}
    if strict:
        gardes = {n["id"] for n in notions if n.get("statut", "source") != "ajout"}
    else:
        gardes = set(ids)

    parent = {}
    for n in notions:
        if n["id"] not in gardes:
            continue
        p = n.get("cas_de")
        while p in ids and p not in gardes:      # remontée au premier ancêtre gardé
            p = next((m.get("cas_de") for m in notions if m["id"] == p), None)
        parent[n["id"]] = p if p in gardes else None

    enfants = {i: [] for i in gardes}
    for i in sorted(gardes):
        p = parent.get(i)
        if p:
            enfants[p].append(i)
    racines = sorted(i for i in gardes
                     if not parent.get(i)
                     and (enfants[i] or next(m.get("type") for m in notions if m["id"] == i) == "principe"))
    return racines, enfants


def charger(root: Path):
    """Retourne [(libellé, racines, enfants), ...] pour tous les cours du dépôt."""
    arbres = []
    cdir = root / "courses"
    for d in sorted(p for p in cdir.iterdir() if p.is_dir()):
        notions = []
        for f in sorted((d / "notions").glob("*.md")):
            txt = f.read_text(encoding="utf-8")
            meta = yaml.safe_load(txt.split("---\n")[1]) or {}
            if meta.get("statut") == "retiree":
                continue
            notions.append(meta)
        if not notions:
            continue
        for libelle, strict in (("complet", False), ("ajouts masqués", True)):
            racines, enfants = arbre_du_cours(notions, strict)
            if racines:
                arbres.append((f"{d.name} ({libelle})", racines, enfants))
    return arbres


# ---------------------------------------------------------------- le test

def tester(libelle, racines, enfants, configs, jeux, rng):
    pliables = [n for n, ks in enfants.items() if ks]
    tous = visibles(racines, enfants, set(pliables))
    fautes = []
    for c in range(configs):
        if c == 0:
            deplies = set()                       # tout replié
        elif c == 1:
            deplies = set(pliables)               # tout déplié
        else:
            deplies = {n for n in pliables if rng.random() < rng.choice((0.2, 0.5, 0.8))}
        for _ in range(jeux):
            hauteurs = {n: rng.uniform(28.0, 140.0) for n in tous}
            tops, prof = disposer(racines, enfants, deplies, hauteurs)
            f = verifier(racines, enfants, deplies, hauteurs, tops, prof)
            if f:
                fautes.append((sorted(deplies), f[:3]))
                break
        if fautes:
            break
    return fautes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--configs", type=int, default=1000)
    ap.add_argument("--jeux", type=int, default=3)
    ap.add_argument("--seed", type=int, default=20260920)
    a = ap.parse_args()

    rng = random.Random(a.seed)
    arbres = charger(Path(a.root))
    if not arbres:
        print("aucun arbre d'abstraction à tester", file=sys.stderr)
        return 1
    ko = 0
    for libelle, racines, enfants in arbres:
        n = len(visibles(racines, enfants, {k for k, v in enfants.items() if v}))
        fautes = tester(libelle, racines, enfants, a.configs, a.jeux, rng)
        if fautes:
            ko += 1
            deplies, msgs = fautes[0]
            print(f"ÉCHEC  {libelle} · {n} nœuds · déplié = {deplies}")
            for m in msgs:
                print(f"       {m}")
        else:
            print(f"ok     {libelle} · {n} nœuds · {a.configs} configurations × {a.jeux} jeux de hauteurs")
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
