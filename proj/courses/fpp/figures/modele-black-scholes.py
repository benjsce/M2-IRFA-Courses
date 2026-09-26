#!/usr/bin/env python3
r"""
modele-black-scholes.svg — la densité du prix de l'action dans un an sous Q, dans le
modèle de Black et Scholes : S_0 = 100, σ = 20 %, r = 4 %. ln S_1 suit une loi normale de
moyenne ln 100 + 0,04 − 0,02 et d'écart type 0,2 ; la médiane vaut 102,02, la moyenne 104,08.

Usage : python courses/fpp/figures/modele-black-scholes.py > modele-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

S0, R, SIG, T = 100, 0.04, 0.2, 1
MU = math.log(S0) + (R - SIG ** 2 / 2) * T
SD = SIG * math.sqrt(T)


def dens(s):
    return math.exp(-(math.log(s) - MU) ** 2 / (2 * SD ** 2)) / (s * SD * math.sqrt(2 * math.pi))


med, moy = math.exp(MU), S0 * math.exp(R * T)
top = dens(math.exp(MU - SD ** 2))
f = Figure(xmin=40, xmax=200, ymin=0, ymax=top * 1.25, w=560, h=320,
           titre="Sous Q, le prix dans un an : médiane 102,02, moyenne 104,08, étirée vers le haut")
f.axes(xlab="prix de l'action dans un an", xticks=(50, 100, 150, 200), yticks=(),
       fmt=lambda t: "%d" % t)
f.fonction(dens, 41, 199, n=300, couleur=ACCENT, epaisseur=2.6)
f.segment(med, 0, med, dens(med))
f.segment(moy, 0, moy, top * 1.12, couleur=AJOUT, pointilles="5 3", epaisseur=1.5)
f.texte(med, dens(med) * 0.45, "médiane 102,02", couleur=ENCRE, ancre="end", dx=-8, taille=12, fond=True)
f.texte(moy, top * 1.12, "moyenne 104,08 = prix forward", couleur=AJOUT, dx=6, dy=4, gras=True, taille=12)
sys.stdout.write(f.svg())
