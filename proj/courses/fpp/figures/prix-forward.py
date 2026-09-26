#!/usr/bin/env python3
r"""
prix-forward.svg — le prix forward est le prix comptant capitalisé jusqu'à l'échéance.
L'action vaut 100 en t ; livrée dans un an, elle se paie 100 / 0,9608 = 104,08 ; dans deux
ans, 100 / 0,9048 = 110,52. Le dépassement de 100, la base, est le coût du portage :
4,08 à un an, 10,52 à deux ans. Courbe du cours : 4 % à un an, 5 % à deux ans.

Usage : python courses/fpp/figures/prix-forward.py > prix-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

S = 100
P = {1: math.exp(-0.04), 2: math.exp(-0.10)}
F = {k: S / p for k, p in P.items()}
L = 0.22                                  # largeur des barres, en années

f = Figure(xmin=-0.6, xmax=2.75, ymin=-14, ymax=178, w=600, h=400, marges=(10, 10, 10, 10),
           titre="F(t,T) = S_{t} / P(t,T) : le prix comptant capitalisé jusqu'à la livraison")
f.axe_temps(0, -0.3, 2.65, [(0, "t : aujourd'hui"), (1, "livraison à t + 1"), (2, "livraison à t + 2")])
f.segment(-0.3, S, 2.45, S)
f.barre(0, S, L, couleur=DOUX, opacite=0.55, y0=0)
f.texte(0, S / 2, "S_{t} = 100", ancre="middle", dy=4, gras=True, fond=True)
for k in (1, 2):
    f.barre(k, S, L, couleur=DOUX, opacite=0.25, y0=0)
    f.barre(k, F[k], L, couleur=ACCENT, opacite=0.85, y0=S)
    f.texte(k, F[k], "F = %s" % ("%.2f" % F[k]).replace(".", ","), couleur=ACCENT,
            ancre="middle", dy=-8, gras=True)
    f.texte(k + L / 2, (S + F[k]) / 2, "base %s" % ("%.2f" % (F[k] - S)).replace(".", ","),
            couleur=ACCENT, dx=8, dy=4, taille=12)
f.fleche(0.13, S + 3, 0.86, F[1] + 16, couleur=ENCRE, courbure=18, epaisseur=1.5)
f.fleche(0.13, S + 5, 1.86, F[2] + 16, couleur=ENCRE, courbure=52, epaisseur=1.5)
f.texte(0.45, F[1] + 16, "÷ P(t, t+1), soit ÷ 0,9608", ancre="middle", dy=-24, taille=12, fond=True)
f.texte(1.0, F[2] + 16, "÷ P(t, t+2), soit ÷ 0,9048", ancre="middle", dy=-38, taille=12, fond=True)
f.texte(2.45, S, "100", couleur=DOUX, dx=6, dy=4, taille=11.5)
sys.stdout.write(f.svg())
