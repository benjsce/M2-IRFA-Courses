#!/usr/bin/env python3
r"""
conjugate-gradient.svg — two steps for conjugate gradient, an approach for gradient descent.

Ce que la figure doit faire voir : sur les lignes de niveau de q pour le système du
cours, A = [[4, 1], [1, 3]], b = (1, 2), le gradient conjugué part de 0, passe par
(1/4, 1/2) et arrive exactement en x* = (1/11, 7/11) au deuxième pas ; la descente de
gradient de pas 1/L, partie du même point, s'en approche sans l'atteindre en six pas.

Usage : python courses/ods/figures/conjugate-gradient.py > conjugate-gradient.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402
from _quadratique import XS, L1, niveau, gradient_conjugue, descente, ecart      # noqa: E402

g = Figure(xmin=-0.62, xmax=0.78, ymin=-0.12, ymax=1.28, w=470, h=470, marges=(10, 10, 10, 10),
           titre="Conjugate gradient lands on the minimizer at step two; gradient descent only approaches it")
g.axes(croix=(0, 0))
for t in (0.5, 0.3, 0.1, 0.02):
    g.courbe(niveau(t), couleur=PALE, epaisseur=1.2)
gd = descente(1 / L1, 6)
g.courbe(gd, couleur=AJOUT, epaisseur=1.6, pointilles="5 3")
for p in gd[1:]:
    g.point(*p, couleur=AJOUT, r=2.6)
cg, _ = gradient_conjugue()
g.courbe(cg, couleur=ACCENT, epaisseur=2.6)
for p in cg:
    g.point(*p, couleur=ACCENT, r=4)
g.point(*XS, couleur=ENCRE, r=4.5)
g.texte(0.02, -0.07, "w⁰ = 0", taille=12, fond=True)
g.texte(cg[1][0] + 0.03, cg[1][1] - 0.02, "w¹ = (1/4, 1/2)", couleur=ACCENT, taille=12, gras=True,
        fond=True)
g.texte(XS[0] - 0.03, XS[1] + 0.05, "w² = w* = (1/11, 7/11)", couleur=ACCENT, taille=12, gras=True,
        ancre="end", fond=True)
g.texte(-0.58, 1.18, "conjugate gradient: 2 steps", couleur=ACCENT, taille=12.5, gras=True)
g.texte(-0.58, 1.1, "gradient descent, step 1/L: 6 steps, not there yet", couleur=AJOUT, taille=12.5)
sys.stdout.write(g.svg())
