#!/usr/bin/env python3
r"""
modele-black-scholes.svg — la densité du prix de l'action en T sous Q dans le modèle de
Black et Scholes : ln S_T suit N(ln S₀ + (r − σ²/2)T, σ²T). La médiane vaut
S₀ e^{(r − σ²/2)T}, la moyenne S₀ e^{rT}, le prix forward. Tracé avec σ = 20 %, r = 4 %.

Usage : python courses/fpp/figures/modele-black-scholes.py > modele-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
S0, R, SIG, T = 100, 0.04, 0.2, 1
MU = math.log(S0) + (R - SIG ** 2 / 2) * T
SD = SIG * math.sqrt(T)


def dens(s):
    return math.exp(-(math.log(s) - MU) ** 2 / (2 * SD ** 2)) / (s * SD * math.sqrt(2 * math.pi))


med, moy = math.exp(MU), S0 * math.exp(R * T)
top = dens(math.exp(MU - SD ** 2))
f = Figure(xmin=40, xmax=200, ymin=0, ymax=top * 1.3, w=560, h=320,
           titre="Sous Q, S_T est log-normal : la moyenne, le prix forward, dépasse la médiane")
f.axes(xlab="S(T)")
f.fonction(dens, 41, 199, n=300, couleur=ACCENT, epaisseur=2.6)
f.segment(med, 0, med, dens(med))
f.segment(moy, 0, moy, top * 1.15, couleur=AJOUT, pointilles="5 3", epaisseur=1.5)
f.texte(med, dens(med) * 0.45, "médiane S_{0} e^{(r − σ²/2)T}", couleur=ENCRE, ancre="end", dx=-8, taille=12, fond=True)
f.texte(moy, top * 1.15, "moyenne S_{0} e^{rT} = F(0,T)", couleur=AJOUT, dx=6, dy=4, gras=True, taille=12)
sys.stdout.write(f.svg())
