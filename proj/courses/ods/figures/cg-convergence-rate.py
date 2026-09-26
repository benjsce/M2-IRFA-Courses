#!/usr/bin/env python3
r"""
cg-convergence-rate.svg — √κ against κ: the gap widens with the conditioning.

Ce que la figure doit faire voir : le nombre d'itérations pour diviser l'erreur par 10⁶
(bornes du pire cas, slide 24), en fonction du conditionnement κ, sur deux axes
logarithmiques : une droite de pente ½ pour le gradient conjugué, de pente 1 pour la
descente de gradient ; l'écart entre les deux grandit avec κ. Les points sont ceux du
tableau de la slide 25.

Gradient conjugué : 2((√κ − 1)/(√κ + 1))^k ≤ 10⁻⁶, k ≈ (√κ/2) ln(2·10⁶).
Descente de gradient : ((κ − 1)/(κ + 1))^k ≤ 10⁻⁶, k ≈ (κ/2) ln(10⁶).

Usage : python courses/ods/figures/cg-convergence-rate.py > cg-convergence-rate.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

eps = 1e-6


def k_cg(kappa):
    r = (math.sqrt(kappa) - 1) / (math.sqrt(kappa) + 1)
    return math.log(eps / 2) / math.log(r)


def k_gd(kappa):
    r = (kappa - 1) / (kappa + 1)
    return math.log(eps) / math.log(r)


g = Figure(xmin=1.6, xmax=6.4, ymin=1, ymax=7.3, w=560, h=380, marges=(58, 26, 40, 16),
           titre="Iterations to divide the error by a million: √κ for conjugate gradient, κ for gradient descent")
lx = [2 + 4 * i / 80 for i in range(81)]
g.courbe([(x, math.log10(k_gd(10 ** x))) for x in lx], couleur=AJOUT, epaisseur=2.2)
g.courbe([(x, math.log10(k_cg(10 ** x))) for x in lx], couleur=ACCENT, epaisseur=2.4)
for x in (2, 4, 6):
    kc, kg = k_cg(10 ** x), k_gd(10 ** x)
    g.point(x, math.log10(kc), couleur=ACCENT)
    g.point(x, math.log10(kg), couleur=AJOUT)
    g.segment(x, math.log10(kc), x, math.log10(kg), couleur=PALE)
g.texte(2.05, math.log10(k_cg(100)) - 0.35, "≈ 70", couleur=ACCENT, taille=12, fond=True)
g.texte(4.05, math.log10(k_cg(1e4)) - 0.35, "≈ 730", couleur=ACCENT, taille=12, fond=True)
g.texte(5.95, math.log10(k_cg(1e6)) - 0.35, "≈ 7 300", couleur=ACCENT, taille=12, ancre="end", fond=True)
g.texte(2.05, math.log10(k_gd(100)) + 0.2, "≈ 700", couleur=AJOUT, taille=12, fond=True)
g.texte(4.05, math.log10(k_gd(1e4)) + 0.2, "≈ 69 000", couleur=AJOUT, taille=12, fond=True)
g.texte(5.95, math.log10(k_gd(1e6)) + 0.12, "≈ 6 900 000", couleur=AJOUT, taille=12, ancre="end", fond=True)
g.texte(3.0, 5.8, "gradient descent", couleur=AJOUT, taille=12.5, gras=True)
g.texte(4.6, 2.3, "conjugate gradient", couleur=ACCENT, taille=12.5, gras=True)
g.axes(xlab="condition number κ", ylab="iterations",
       xticks=[2, 3, 4, 5, 6], yticks=[1, 2, 3, 4, 5, 6, 7],
       fmt=lambda t: "10" + "⁰¹²³⁴⁵⁶⁷⁸⁹"[t])
sys.stdout.write(g.svg())
