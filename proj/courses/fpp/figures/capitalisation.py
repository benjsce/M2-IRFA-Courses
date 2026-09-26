#!/usr/bin/env python3
r"""
capitalisation.svg — 5 % par an pendant deux ans, selon le nombre n de versements
d'intérêts : (1 + 0,1/n)^n vaut 1,10 pour n = 1 (linéaire), 1,1025 pour n = 2, et tend
vers e^0,1 ≈ 1,1052, la capitalisation continue, quand n grandit.

Usage : python courses/fpp/figures/capitalisation.py > capitalisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

RT = 0.05 * 2
NS = [1, 2, 4, 12, 52, 365]
f = Figure(xmin=0.4, xmax=6.9, ymin=1.0985, ymax=1.1065, w=560, h=320,
           titre="Plus les intérêts sont versés souvent, plus 1 devient : la limite est e^{0,1} ≈ 1,1052")
f.axes(xlab="nombre de versements en 2 ans", ylab="ce que devient 1", xticks=(),
       yticks=(1.1, 1.1025, 1.105), fmt_y=lambda t: ("%.4f" % t).replace(".", ","))
lim = math.exp(RT)
f.segment(0.4, lim, 6.9, lim, couleur=ACCENT, pointilles="6 4", epaisseur=1.6)
f.texte(6.9, lim, "continu : e^{0,1} = 1,1052", couleur=ACCENT, ancre="end", dy=-8, gras=True)
pts = []
for k, n in enumerate(NS, start=1):
    v = (1 + RT / n) ** n
    pts.append((k, v))
    f.texte(k, 1.0985, "n = %d" % n, couleur=DOUX, ancre="middle", taille=11.5, dy=17)
f.courbe(pts, couleur=PALE, epaisseur=1.2)
for k, v in pts:
    f.point(k, v, couleur=AJOUT if k > 1 else DOUX, r=4.5)
f.texte(1, 1.1, "linéaire 1,10", couleur=DOUX, dx=10, dy=4, taille=12)
f.texte(2, (1 + RT / 2) ** 2, "1,1025", couleur=AJOUT, dx=10, dy=4, taille=12)
sys.stdout.write(f.svg())
