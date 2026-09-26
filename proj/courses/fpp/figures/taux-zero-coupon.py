#!/usr/bin/env python3
r"""
taux-zero-coupon.svg — moins le logarithme du prix du zéro-coupon en fonction de
l'échéance : le taux zéro-coupon est la pente de la corde issue de l'origine.
−ln 0,9608 = 0,04 à un an (pente 4 %), −ln 0,9048 = 0,10 à deux ans (pente 5 %).

Usage : python courses/fpp/figures/taux-zero-coupon.py > taux-zero-coupon.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=0, xmax=2.4, ymin=0, ymax=0.125, w=560, h=320,
           titre="R(t,T) = −ln P(t,T) / (T − t) : la pente de la corde depuis l'origine")
f.axes(xlab="échéance T − t, en années", ylab="− ln P(t,T)", xticks=(0, 1, 2),
       yticks=(0.04, 0.10), fmt=lambda t: "%g" % t, fmt_y=lambda t: ("%.2f" % t).replace(".", ","))
f.courbe([(0, 0), (2, 0.10)], couleur=ACCENT, epaisseur=2.4)
f.courbe([(0, 0), (1, 0.04)], couleur=AJOUT, epaisseur=2.4)
f.segment(1, 0, 1, 0.04)
f.segment(2, 0, 2, 0.10)
f.point(1, 0.04, couleur=AJOUT, r=4.5)
f.point(2, 0.10, couleur=ACCENT, r=4.5)
f.texte(1, 0.04, "P = 0,9608 : pente 4 %", couleur=AJOUT, dx=10, dy=14, gras=True)
f.texte(2, 0.10, "P = 0,9048 : pente 5 %", couleur=ACCENT, ancre="end", dx=-10, dy=-8, gras=True)
sys.stdout.write(f.svg())
