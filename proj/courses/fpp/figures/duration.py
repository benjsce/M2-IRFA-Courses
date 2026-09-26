#!/usr/bin/env python3
r"""
duration.svg — un point de taux se paie une fois par année d'attente.

Ce que la figure doit faire voir : un zéro-coupon qui paie 1 dans cinq ans revient en t
année par année ; quand le taux monte d'un point, chacune des cinq années d'actualisation
coûte environ 1 % de valeur de plus, et le titre perd donc environ 5 %, autant de pour
cent que d'années. Les prix sont ceux du cours : au taux continu de 4 %, $e^{-0,20}$ ;
à 5 %, $e^{-0,25}$ ; la perte exacte, $e^{-0,05}-1$, est de 4,9 %.

Usage : python courses/fpp/figures/duration.py > duration.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

R0, DR, MAT = 0.04, 0.01, 5
P0, P1 = math.exp(-R0 * MAT), math.exp(-(R0 + DR) * MAT)
v4 = lambda v: ("%.4f" % v).replace(".", ",")
pc = lambda v: ("%.1f %%" % v).replace(".", ",").replace("-", "−")

x0, pas = 1.3, 1.65                          # t, puis une année tous les 1,65
X = [x0 + k * pas for k in range(MAT + 1)]

g = Figure(xmin=0, xmax=10.6, ymin=-2.1, ymax=4.0, w=640, h=300, marges=(8, 8, 8, 8),
           titre="Un point de taux de plus coûte environ 1 % par année d'attente : 5 % sur cinq ans")
g.axe_temps(0, 0.4, 10.3, [(X[0], "t")] + [(X[k], "t+%d" % k) for k in range(1, MAT + 1)])

# le flux : 1 payé dans cinq ans
g.fleche(X[-1], 0.35, X[-1], 1.75, couleur=ENCRE, epaisseur=2.2)
g.texte(X[-1], 1.0, "1", couleur=ENCRE, gras=True, taille=14, dx=9)

# il revient en t année par année ; chaque année coûte environ 1 % de plus
ya = 2.15
for k in range(MAT, 0, -1):
    g.fleche(X[k] - 0.06, ya, X[k - 1] + 0.06, ya, couleur=ACCENT, epaisseur=1.6, courbure=14)
    g.texte((X[k] + X[k - 1]) / 2, ya + 0.72, "−1 %", couleur=ACCENT, gras=True,
            taille=12.5, ancre="middle")
g.texte(X[0], ya + 1.45, "le taux passe de 4 % à 5 % : chaque année d'attente coûte 1 % de plus",
        couleur=ENCRE, taille=12.5)
g.texte(X[0], 1.0, "−5 %", couleur=AJOUT, gras=True, taille=15, ancre="middle")
g.texte(X[0], 0.45, "environ", couleur=AJOUT, taille=11.5, ancre="middle")

# les chiffres exacts, sous l'axe
g.texte(X[0], -1.5, "prix aujourd'hui : %s à 4 %%, %s à 5 %%, soit %s, environ 5 × 1 %%"
        % (v4(P0), v4(P1), pc((P1 / P0 - 1) * 100)), couleur=DOUX, taille=12)

sys.stdout.write(g.svg())
