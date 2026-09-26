#!/usr/bin/env python3
r"""
taux-forward-instantane.svg — un taux forward instantané de 4 % la première année et de
6 % la seconde : l'aire sous la courbe sur deux ans vaut 0,04 + 0,06 = 0,10, et le
zéro-coupon à deux ans vaut e^{−0,10} = 0,9048.

Usage : python courses/fpp/figures/taux-forward-instantane.py > taux-forward-instantane.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=0, xmax=2.35, ymin=0, ymax=0.08, w=560, h=320,
           titre="L'aire sous f de t à T vaut −ln P(t,T) : 0,04 + 0,06 = 0,10")
f.axes(xlab="date u − t, en années", ylab="f(t,u)", xticks=(0, 1, 2), yticks=(0.04, 0.06),
       fmt=lambda t: "%g" % t, fmt_y=lambda t: ("%g %%" % (100 * t)).replace(".", ","))
f.barre(0.5, 0.04, 1.0, couleur=AJOUT, opacite=0.22)
f.barre(1.5, 0.06, 1.0, couleur=ACCENT, opacite=0.22)
f.courbe([(0, 0.04), (1, 0.04), (1, 0.06), (2, 0.06)], couleur=ENCRE, epaisseur=2.4)
f.texte(0.5, 0.02, "aire 0,04", couleur=AJOUT, ancre="middle", gras=True)
f.texte(1.5, 0.03, "aire 0,06", couleur=ACCENT, ancre="middle", gras=True)
f.texte(1.0, 0.072, "P(t, t+2) = e^{−(0,04 + 0,06)} = 0,9048", couleur=ENCRE, ancre="middle", gras=True)
sys.stdout.write(f.svg())
