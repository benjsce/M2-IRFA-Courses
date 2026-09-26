#!/usr/bin/env python3
r"""
sparse-storage-format.svg — a CSR matrix is three arrays.

Ce que la figure doit faire voir : la matrice 3 × 3 du carnet 3, [[1, 2, 0], [0, 0, 3],
[4, 0, 5]], et sa forme CSR : les valeurs non nulles ligne par ligne (data), leur
colonne (indices), et, pour chaque ligne, l'endroit où elle commence dans ces deux
tableaux (indptr). La ligne i occupe les cases indptr[i] à indptr[i+1] − 1.

data = [1, 2, 3, 4, 5], indices = [0, 1, 2, 0, 2], indptr = [0, 2, 3, 5].

Usage : python courses/ods/figures/sparse-storage-format.py > sparse-storage-format.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

M = [[1, 2, 0], [0, 0, 3], [4, 0, 5]]
data = [v for ligne in M for v in ligne if v]
indices = [j for ligne in M for j, v in enumerate(ligne) if v]
indptr = [0]
for ligne in M:
    indptr.append(indptr[-1] + sum(1 for v in ligne if v))
couleur_ligne = [ACCENT, AJOUT, ENCRE]

g = Figure(xmin=0, xmax=14.6, ymin=0, ymax=6.4, w=680, h=300, marges=(8, 8, 8, 8),
           titre="Compressed sparse row: values, their columns, and where each row starts")


def case(x, y, s, c=ENCRE, plein=False, pale=False):
    X0, Y0, X1, Y1 = g.px(x), g.py(y + 0.8), g.px(x + 0.8), g.py(y)
    g._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="%s" '
           'stroke="%s" stroke-width="1.2" rx="2"/>'
           % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), c, "0.14" if plein else "0",
              PALE if pale else c))
    g.texte(x + 0.4, y + 0.26, s, couleur=DOUX if pale else c, taille=13, ancre="middle",
            gras=not pale)


# la matrice
g.texte(0.3, 5.9, "the matrix (notebook 3)", taille=12.5, gras=True)
for i, ligne in enumerate(M):
    for j, v in enumerate(ligne):
        case(1.3 + 0.9 * j, 4.5 - 0.9 * i, str(v), c=couleur_ligne[i], plein=bool(v), pale=not v)
    g.texte(0.1, 4.76 - 0.9 * i, "row %d" % i, taille=11.5, couleur=couleur_ligne[i])

# les trois tableaux
x0 = 5.8
g.texte(x0, 5.9, "its CSR form", taille=12.5, gras=True)
k = 0
for i in range(3):
    for _ in range(indptr[i + 1] - indptr[i]):
        case(x0 + 1.4 + 0.9 * k, 4.5, str(data[k]), c=couleur_ligne[i], plein=True)
        case(x0 + 1.4 + 0.9 * k, 3.1, str(indices[k]), c=couleur_ligne[i])
        k += 1
g.texte(x0 + 1.25, 4.76, "data", taille=12.5, ancre="end")
g.texte(x0 + 1.25, 3.36, "indices", taille=12.5, ancre="end")
g.texte(x0 + 1.4 + 0.9 * 5, 4.76, "non-zeros, row by row", taille=11.5, couleur=DOUX)
g.texte(x0 + 1.4 + 0.9 * 5, 3.36, "their columns", taille=11.5, couleur=DOUX)
for m, v in enumerate(indptr):
    case(x0 + 1.4 + 0.9 * v - 0.4, 1.2, str(v), c=ENCRE)
    if m < 3:
        g.fleche(x0 + 1.4 + 0.9 * v, 2.0, x0 + 1.4 + 0.9 * v + 0.05, 3.0, couleur=couleur_ligne[m],
                 epaisseur=1.3)
g.texte(x0 + 1.25, 1.46, "indptr", taille=12.5, ancre="end", dx=-18)
g.texte(x0 + 1.0, 0.4, "row i starts at indptr[i] and stops before indptr[i+1]", taille=11.5,
        couleur=DOUX)
sys.stdout.write(g.svg())
