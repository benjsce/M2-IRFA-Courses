#!/usr/bin/env python3
r"""
transformee-de-laplace-gaussienne.svg — la courbe exponentielle et deux valeurs d'une
variable de moyenne nulle, −0,2 et +0,2 : la moyenne des deux exponentielles,
(e^{−0,2} + e^{0,2})/2 ≈ 1,0201, est au-dessus de e^0 = 1. Pour une gaussienne d'écart type
0,2, le théorème donne e^{0,02} ≈ 1,0202.

Usage : python courses/fpp/figures/transformee-de-laplace-gaussienne.py > transformee-de-laplace-gaussienne.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

a = 0.2
m = (math.exp(-a) + math.exp(a)) / 2
f = Figure(xmin=-0.3, xmax=0.3, ymin=0.76, ymax=1.28, w=560, h=320,
           titre="La moyenne de l'exponentielle dépasse l'exponentielle de la moyenne")
f.axes(xlab="x", ylab="exp(x)", xticks=(-0.2, 0, 0.2), yticks=(0.8, 0.9, 1.0, 1.1, 1.2),
       fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: ("%.1f" % t).replace(".", ","),
       croix=(-0.3, 0.76))
f.fonction(math.exp, -0.29, 0.29, couleur=ACCENT, epaisseur=2.6)
f.courbe([(-a, math.exp(-a)), (a, math.exp(a))], couleur=AJOUT, epaisseur=1.8)
f.segment(-a, 0.76, -a, math.exp(-a))
f.segment(a, 0.76, a, math.exp(a))
f.segment(0, 0.76, 0, 1)
for x in (-a, a):
    f.point(x, math.exp(x), couleur=ACCENT)
f.point(0, 1, couleur=ENCRE)
f.point(0, m, couleur=AJOUT, r=4.5)
f.texte(0, m, "moyenne des exp : 1,0201", couleur=AJOUT, dx=-8, dy=-10, ancre="end", gras=True)
f.texte(0, 1, "exp(0) = 1", couleur=ENCRE, dx=8, dy=16)
f.mesure(0.035, 1, m, couleur=AJOUT, etiquette="+0,02")
sys.stdout.write(f.svg())
