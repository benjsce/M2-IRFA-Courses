#!/usr/bin/env python3
r"""
portefeuille-tangent.svg — la droite la plus pentue issue de l'actif sans risque.

La fiche dit que maximiser le ratio de Sharpe revient à chercher, parmi les droites
issues du point (0, R_f), la plus pentue qui touche encore la frontière : elle la touche
au portefeuille tangent. Mêmes deux actifs que l'exemple, R_f = 2 % ; le point tangent
place deux tiers dans le premier actif, à 9,43 % de volatilité pour 7,33 %, et la pente
vaut 0,566.

Usage : python courses/pfo/figures/portefeuille-tangent.py > portefeuille-tangent.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

MU = (6.0, 10.0)             # rendements espérés, en %
SIG = (10.0, 20.0)           # volatilités, en %, corrélation nulle
RF = 2.0


def point(a):
    m = a * MU[0] + (1 - a) * MU[1]
    s = math.sqrt((a * SIG[0]) ** 2 + ((1 - a) * SIG[1]) ** 2)
    return s, m


# poids tangents ∝ Σ⁻¹(μ − R_f) : Σ est diagonale
z = [(MU[i] - RF) / SIG[i] ** 2 for i in range(2)]
A_T = z[0] / (z[0] + z[1])                                  # 2/3
S_T, M_T = point(A_T)
PENTE = (M_T - RF) / S_T                                    # 0,566

f = Figure(xmin=0, xmax=22, ymin=0, ymax=11.5, w=560, h=330,
           titre="La droite la plus pentue issue de l'actif sans risque touche la frontière en T")
f.axes(xlab="risque σp, en %", ylab="rendement μp, en %",
       xticks=(0, 5, 10, 15, 20), yticks=(0, 2, 4, 6, 8, 10), fmt=lambda t: str(int(t)))

N = 300
f.courbe([point(k / N) for k in range(N + 1)], couleur=ENCRE, epaisseur=2.0)
f.segment(0, RF, 15.5, RF + PENTE * 15.5, couleur=ACCENT, epaisseur=2.0, pointilles=None)

f.point(0, RF, couleur=ACCENT, r=4)
f.texte(0, RF, "actif sans risque", couleur=ACCENT, dx=8, dy=16, taille=11.5)
f.point(S_T, M_T, couleur=ACCENT, r=4.5)
f.texte(S_T, M_T, "T", couleur=ACCENT, dx=-10, dy=-8, ancre="end", taille=13, gras=True, fond=True)
f.texte(4.5, RF + PENTE * 4.5, "pente = ratio de Sharpe maximal", couleur=ACCENT,
        dx=6, dy=18, taille=11.5, fond=True)
f.texte(20, 10, "frontière", couleur=ENCRE, dx=-2, dy=20, ancre="end", taille=11.5, fond=True)

sys.stdout.write(f.svg())
