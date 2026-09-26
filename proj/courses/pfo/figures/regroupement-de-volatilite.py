#!/usr/bin/env python3
r"""
regroupement-de-volatilite.svg — les fortes variations arrivent groupées.

Ce que la figure doit faire voir : un écart type unique, calculé sur toute la période,
trace une bande fixe ; les rendements qui en sortent ne sont pas répartis au hasard, ils
se concentrent dans un épisode agité, entre deux épisodes calmes.

La série est simulée [ajout] : 250 jours de rendements tirés d'une loi normale (graine 9),
d'écart type 0,6 % par jour du jour 1 au jour 100, 1,9 % du jour 101 au jour 150, puis
0,6 % à nouveau, de sorte que l'écart type de toute la série vaille environ 1 % par jour.
La bande est ± 2 fois cet écart type empirique. Les nombres qu'écrit la fiche sont ceux
qu'imprime l'option --resume.

Usage : python courses/pfo/figures/regroupement-de-volatilite.py > regroupement-de-volatilite.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, PALE      # noqa: E402

N, A, B = 250, 100, 150                   # l'épisode agité va du jour A+1 au jour B
rng = random.Random(9)
vol = [0.019 if A < k <= B else 0.006 for k in range(1, N + 1)]
r = [100 * rng.gauss(0.0, v) for v in vol]                 # en pour cent
m = sum(r) / N
s = math.sqrt(sum((x - m) ** 2 for x in r) / (N - 1))       # un seul nombre, fixe
hors = [k for k, x in enumerate(r, start=1) if abs(x) > 2 * s]


def resume():
    dedans = sum(1 for k in hors if A < k <= B)
    return "écart type %.2f %% ; %d jours hors bande, dont %d dans l'épisode agité" % (
        s, len(hors), dedans)


fr = lambda v: ("%+.0f %%" % v).replace("+0 ", "0 ") if v else "0"
g = Figure(xmin=0, xmax=N + 2, ymin=-6.5, ymax=7.5, w=600, h=300, marges=(46, 12, 38, 10),
           titre="Les fortes variations arrivent groupées")
g.axes(xlab="jours", xticks=(1, 50, 100, 150, 200, 250), yticks=(-5, 0, 5),
       fmt=lambda t: "%d" % t, fmt_y=fr, croix=(0, -6.5))

# la bande fixe : ± 2 écarts types de toute la période
for y in (-2 * s, 2 * s):
    g.segment(0, y, N + 2, y, couleur=AJOUT, epaisseur=1.3, pointilles="6 4")
g.texte(N + 2, 2 * s, "± 2 écarts types de toute la période", couleur=AJOUT, taille=11.5,
        ancre="end", dy=-5, fond=True)

# les rendements du jour : en couleur ceux qui sortent de la bande
for k, x in enumerate(r, start=1):
    dehors = abs(x) > 2 * s
    g.barre(k, x, 0.75, couleur=ACCENT if dehors else DOUX, opacite=1 if dehors else 0.55,
            y0=0)

# les trois épisodes
g.segment(A + 0.5, -6.5, A + 0.5, 7.5, couleur=PALE, epaisseur=1.0, pointilles="2 3")
g.segment(B + 0.5, -6.5, B + 0.5, 7.5, couleur=PALE, epaisseur=1.0, pointilles="2 3")
g.texte(A / 2, 7.5, "calme", couleur=DOUX, ancre="middle", dy=12)
g.texte((A + B) / 2, 7.5, "agité", couleur=ACCENT, ancre="middle", dy=12, gras=True)
g.texte((B + N) / 2, 7.5, "calme", couleur=DOUX, ancre="middle", dy=12)

if __name__ == "__main__" and "--resume" in sys.argv:
    print(resume())
else:
    sys.stdout.write(g.svg())
