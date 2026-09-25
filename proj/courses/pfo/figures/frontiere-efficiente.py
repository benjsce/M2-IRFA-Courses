#!/usr/bin/env python3
r"""
frontiere-efficiente.svg — la courbe des portefeuilles, et sa seule partie efficiente.

La fiche dit que faire varier le rendement cible trace une courbe, dont seule la branche
située au-dessus du portefeuille de variance minimale globale est efficiente. Avec les
deux actifs non corrélés de l'exemple (6 % et 10 % de rendement, 10 % et 20 % de
volatilité), chaque poids du premier actif entre 0 et 1 donne un point ; le point le
plus à gauche place 80 % dans le premier actif, à 8,94 % de volatilité pour 6,8 %.

Usage : python courses/pfo/figures/frontiere-efficiente.py > frontiere-efficiente.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

MU = (6.0, 10.0)             # rendements espérés, en %
SIG = (10.0, 20.0)           # volatilités, en %, corrélation nulle


def point(a):
    """(volatilité, rendement) du portefeuille qui place a dans le premier actif."""
    m = a * MU[0] + (1 - a) * MU[1]
    s = math.sqrt((a * SIG[0]) ** 2 + ((1 - a) * SIG[1]) ** 2)
    return s, m


A_GMV = SIG[1] ** 2 / (SIG[0] ** 2 + SIG[1] ** 2)          # 0,8
S_GMV, M_GMV = point(A_GMV)

f = Figure(xmin=0, xmax=22, ymin=5, ymax=10.8, w=560, h=330,
           titre="Seule la branche au-dessus du portefeuille de variance minimale est efficiente")
f.axes(xlab="risque σp, en %", ylab="rendement μp, en %",
       xticks=(0, 5, 10, 15, 20), yticks=(6, 7, 8, 9, 10), fmt=lambda t: str(int(t)))

N = 200
haut = [point(A_GMV * k / N) for k in range(N + 1)]                    # de B au GMV
bas = [point(A_GMV + (1 - A_GMV) * k / N) for k in range(N + 1)]       # du GMV à A
f.courbe(bas, couleur=DOUX, epaisseur=1.8, pointilles="5 4")
f.courbe(haut, couleur=ACCENT, epaisseur=2.4)

f.segment(0, M_GMV, S_GMV, M_GMV, couleur=PALE)
f.point(S_GMV, M_GMV, couleur=ENCRE, r=4)
f.texte(S_GMV, M_GMV, "variance minimale globale", couleur=ENCRE, dx=-8, dy=-9,
        ancre="end", taille=11.5, gras=True, fond=True)

sa, ma = point(1.0)
sb, mb = point(0.0)
f.point(sa, ma, couleur=DOUX)
f.point(sb, mb, couleur=DOUX)
f.texte(sa, ma, "actif 1", couleur=DOUX, dx=8, dy=4, taille=11.5)
f.texte(sb, mb, "actif 2", couleur=DOUX, dx=7, dy=4, taille=11.5)
f.texte(15.2, 8.6, "branche efficiente", couleur=ACCENT, taille=11.5, gras=True, fond=True)
f.texte(12.5, 5.6, "branche inefficiente", couleur=DOUX, taille=11.5, fond=True)

sys.stdout.write(f.svg())
