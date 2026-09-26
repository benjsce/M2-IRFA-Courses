#!/usr/bin/env python3
r"""
composante-principale.svg — la direction de plus grande variance, et les distances à elle.

Un nuage de deux variables corrélées, construit pour le dessin avec une graine fixée (les
données de publicité du cours ne sont pas reproduites). La droite pleine est la première
composante : la direction le long de laquelle les points s'étalent le plus. Les petits
segments sont les distances perpendiculaires des points à cette droite ; la fiche dit
qu'elle en minimise la somme des carrés. La droite pointillée, orthogonale, est la seconde
composante, où il reste peu de variation.

Usage : python courses/dss/figures/composante-principale.py > composante-principale.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

rng = random.Random(11)
pts = []
for _ in range(30):
    t, e = rng.gauss(0, 1.6), rng.gauss(0, 0.45)
    pts.append((5 + 0.8 * t - 0.6 * e, 5 + 0.6 * t + 0.8 * e))
mx = sum(x for x, _ in pts) / len(pts)
my = sum(y for _, y in pts) / len(pts)
sxx = sum((x - mx) ** 2 for x, _ in pts)
syy = sum((y - my) ** 2 for _, y in pts)
sxy = sum((x - mx) * (y - my) for x, y in pts)
ang = 0.5 * math.atan2(2 * sxy, sxx - syy)           # direction propre principale
u = (math.cos(ang), math.sin(ang))
w = (-u[1], u[0])

f = Figure(xmin=0, xmax=10, ymin=0.5, ymax=9.5, w=480, h=420, marges=(40, 16, 36, 16),
           titre="La première composante suit l'étalement du nuage ; la seconde, ce qui reste")
f.axes(xlab="variable 1", ylab="variable 2", xticks=(), yticks=())
for x, y in pts:
    s = (x - mx) * u[0] + (y - my) * u[1]
    f.courbe([(x, y), (mx + s * u[0], my + s * u[1])], couleur=AJOUT, epaisseur=1.0)
f.courbe([(mx - 5.5 * u[0], my - 5.5 * u[1]), (mx + 5.5 * u[0], my + 5.5 * u[1])],
         couleur=ACCENT, epaisseur=2.6)
f.courbe([(mx - 2 * w[0], my - 2 * w[1]), (mx + 2 * w[0], my + 2 * w[1])], couleur=DOUX,
         epaisseur=1.6, pointilles="5 4")
for x, y in pts:
    f.point(x, y, couleur=ENCRE, r=3.2)
f.texte(mx + 4.6 * u[0], my + 4.6 * u[1], "1re composante", couleur=ACCENT, ancre="end", dx=-6,
        dy=-8, gras=True, fond=True)
f.texte(mx + 2 * w[0], my + 2 * w[1], "2e", couleur=DOUX, dx=6, gras=True)

sys.stdout.write(f.svg())
