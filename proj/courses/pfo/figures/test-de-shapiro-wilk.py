#!/usr/bin/env python3
r"""
test-de-shapiro-wilk.svg — l'échantillon rangé, face aux positions attendues d'une loi normale.

L'échantillon de la fiche, $\{3, -1, 2, 5, -2\}$ en %, rangé : $-2, -1, 2, 3, 5$. En
abscisse, les positions $m_i$ qu'occuperaient en moyenne les cinq observations rangées
d'un échantillon normal centré réduit de taille 5 : $-1{,}163$, $-0{,}495$, 0, $0{,}495$,
$1{,}163$ (valeurs tabulées). Le test compare ces deux colonnes : pour un échantillon
normal, les points s'aligneraient sur une droite. La droite tracée est celle des moindres
carrés, pour guider l'œil.

Usage : python courses/pfo/figures/test-de-shapiro-wilk.py > test-de-shapiro-wilk.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

X = sorted([3, -1, 2, 5, -2])
M = [-1.16296, -0.49502, 0.0, 0.49502, 1.16296]
xm = sum(X) / len(X)
pente = sum(m * x for m, x in zip(M, X)) / sum(m * m for m in M)
droite = lambda m: xm + pente * m

f = Figure(xmin=-1.5, xmax=1.5, ymin=-4, ymax=7, w=480, h=360, marges=(54, 16, 40, 18),
           titre="Chaque observation rangée, face à la position qu'elle aurait sous une loi normale")
f.axes(xlab="position attendue mi", ylab="X(i), en %", xticks=(-1.163, -0.495, 0, 0.495, 1.163),
       yticks=(-2, 0, 2, 4, 6), fmt=lambda t: ("%g" % round(t, 3)).replace(".", ","),
       fmt_y=lambda t: "%d" % t, croix=(-1.5, -4))

f.fonction(droite, -1.4, 1.4, couleur=DOUX, epaisseur=1.4, pointilles="5 4")
for i, (m, x) in enumerate(zip(M, X), start=1):
    f.point(m, x, couleur=ACCENT, r=4.5)
    f.texte(m, x, "X(%d) = %d %%" % (i, x), couleur=ACCENT, dx=-8, dy=-8, ancre="end",
            taille=11, fond=True)

sys.stdout.write(f.svg())
