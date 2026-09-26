#!/usr/bin/env python3
r"""
taux-forward.svg — le taux long comme moyenne des forwards, lue en aires.

L'identité de la fiche : $R(t,S)(S-t)=R(t,T)(T-t)+F(t,T,S)(S-T)$. Chaque produit taux ×
durée est une aire. Sur l'exemple : 4 % sur la première année et 6 % sur la seconde font
les deux rectangles pleins ; le taux à deux ans, 5 %, est la hauteur du rectangle
pointillé de même aire. Le forward est donc le taux qui complète l'aire du taux court pour
atteindre celle du taux long.

Usage : python courses/fpp/figures/taux-forward.py > taux-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

P1, P2 = 0.9608, 0.9048
R1 = -math.log(P1) * 100                 # 4 %
R2 = -math.log(P2) / 2 * 100             # 5 %
F12 = math.log(P1 / P2) * 100            # 6 %
fr = lambda v: ("%.0f" % v)

f = Figure(xmin=0, xmax=2.35, ymin=0, ymax=7.6, w=560, h=320,
           titre="4 % × 1 an + 6 % × 1 an = 5 % × 2 ans : le forward complète l'aire")
f.axes(xlab="années", ylab="taux, en %", xticks=(0, 1, 2), yticks=(4, 5, 6),
       fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d" % t)

f.barre(0.5, R1, 1.0, couleur=DOUX, opacite=0.45)
f.barre(1.5, F12, 1.0, couleur=ACCENT, opacite=0.45)
f.courbe([(0, R2), (2, R2), (2, 0)], couleur=AJOUT, epaisseur=2.2, pointilles="6 4")
f.texte(0.5, R1 / 2, "R(0,1) = 4 %", couleur=ENCRE, ancre="middle", gras=True)
f.texte(0.5, R1 / 2, "aire 4", couleur=ENCRE, ancre="middle", dy=16, taille=11.5)
f.texte(1.5, F12 / 2, "F(0,1,2) = 6 %", couleur=ENCRE, ancre="middle", gras=True)
f.texte(1.5, F12 / 2, "aire 6", couleur=ENCRE, ancre="middle", dy=16, taille=11.5)
f.texte(0.04, R2, "R(0,2) = 5 % sur deux ans, aire 10", couleur=AJOUT, dy=-8, gras=True, fond=True)

sys.stdout.write(f.svg())
