#!/usr/bin/env python3
r"""
volatilite.svg — vingt-quatre rendements annuels fictifs, de moyenne 6 % et d'écart type
4 % : la plupart restent dans la bande d'une volatilité autour de la moyenne.

Les rendements sont tirés par un générateur congruentiel fixe, puis centrés et réduits
pour avoir exactement la moyenne et l'écart type de la fiche.

Usage : python courses/fpp/figures/volatilite.py > volatilite.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, ENCRE, PALE      # noqa: E402

MOY, SIG, N = 6.0, 4.0, 24

x, bruts = 12345, []
for _ in range(N):                       # somme de trois uniformes : presque gaussien
    s = 0.0
    for _ in range(3):
        x = (1103515245 * x + 12345) % 2 ** 31
        s += x / 2 ** 31
    bruts.append(s)
m = sum(bruts) / N
e = math.sqrt(sum((b - m) ** 2 for b in bruts) / N)
rend = [MOY + SIG * (b - m) / e for b in bruts]

f = Figure(xmin=0, xmax=N + 1, ymin=-4, ymax=16, w=560, h=300,
           titre="Des rendements de moyenne 6 % qui s'en écartent d'ordinaire de 4 points")
f.axes(xlab="année", ylab="rendement, en %", xticks=(1, 6, 12, 18, 24),
       yticks=(-2, 2, 6, 10, 14), fmt=lambda t: "%d" % t)
f.segment(0, MOY + SIG, N + 1, MOY + SIG, couleur=PALE)
f.segment(0, MOY - SIG, N + 1, MOY - SIG, couleur=PALE)
f.courbe([(0, MOY), (N + 1, MOY)], couleur=DOUX, epaisseur=1.4)
for k, r in enumerate(rend, start=1):
    f.segment(k, MOY, k, r, couleur=PALE, pointilles=None, epaisseur=1)
    f.point(k, r, couleur=ACCENT, r=4)
f.mesure(N + 0.5, MOY, MOY + SIG, etiquette="σ = 4 %", cote="left")
f.texte(0.4, MOY, "moyenne 6 %", couleur=DOUX, taille=11.5, dy=-6, fond=True)

sys.stdout.write(f.svg())
