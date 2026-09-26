#!/usr/bin/env python3
r"""
logistic-regression.svg — the logistic loss never reaches zero.

Ce que la figure doit faire voir : la perte d'une fleur, log(1 + e^{−m}), en fonction de
sa marge m = y xᵀw ; elle décroît vers 0 sans l'atteindre. Quand toutes les marges
peuvent être rendues positives, doubler w double chaque marge et fait baisser chaque
perte : la somme descend sans fin, et aucun w ne l'atteint. Deux marges, 1 et 2, et
leurs doubles, 2 et 4, sont marquées.

log(1 + e^{−1}) ≈ 0,313 ; log(1 + e^{−2}) ≈ 0,127 ; log(1 + e^{−4}) ≈ 0,018.

Usage : python courses/ods/figures/logistic-regression.py > logistic-regression.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

perte = lambda m: math.log(1 + math.exp(-m))

g = Figure(xmin=-3.2, xmax=6.2, ymin=-0.35, ymax=3.4, w=560, h=330, marges=(40, 24, 36, 12),
           titre="The logistic loss goes down to 0 without reaching it")
g.fonction(perte, -3, 6, couleur=ACCENT, epaisseur=2.4)
g.segment(-3.2, 0, 6.2, 0, couleur=PALE)
for m, c in ((1, AJOUT), (2, AJOUT), (4, ENCRE)):
    g.point(m, perte(m), couleur=c, r=3.8)
g.fleche(1, perte(1) + 0.12, 2 - 0.08, perte(2) + 0.14, couleur=AJOUT, courbure=10)
g.fleche(2, perte(2) + 0.12, 4 - 0.1, perte(4) + 0.12, couleur=AJOUT, courbure=10)
g.texte(1.05, perte(1) + 0.55, "double w: margins 1 → 2 → 4,", couleur=AJOUT, taille=12, fond=True)
g.texte(1.05, perte(1) + 0.3, "losses 0.31 → 0.13 → 0.02", couleur=AJOUT, taille=12, fond=True)
g.texte(-3.0, 3.1, "loss of one flower: log(1 + e^{−m})", couleur=ACCENT, taille=12.5, gras=True, fond=True)
g.texte(-2.9, 0.5, "wrong side", couleur=DOUX, taille=11.5)
g.texte(4.5, 0.5, "right side", couleur=DOUX, taille=11.5)
g.axes(xlab="margin m = y xᵀw", xticks=[-2, 0, 2, 4, 6], yticks=[0, 1, 2, 3], croix=(0, 0),
       fmt=lambda t: ("%d" % t).replace("-", "−"))
sys.stdout.write(g.svg())
