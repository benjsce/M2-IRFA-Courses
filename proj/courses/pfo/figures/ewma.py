#!/usr/bin/env python3
r"""
ewma.svg — le poids de chaque rendement passé dans la variance du jour.

La forme développée de la fiche donne au carré du rendement d'il y a $k$ jours le poids
$\alpha(1-\alpha)^{k-1}$, avec $\alpha=1-\lambda=0{,}06$ pour la valeur de RiskMetrics.
Les barres sont ces poids : le rendement de la veille pèse 6 %, et le poids est divisé
par deux environ tous les 11 jours. Les vingt derniers jours portent ensemble
$1-0{,}94^{20}\approx71\,\%$ du poids.

Usage : python courses/pfo/figures/ewma.py > ewma.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, ENCRE      # noqa: E402

LAM = 0.94
ALPHA = 1 - LAM
N = 60
poids = [ALPHA * LAM ** (k - 1) for k in range(1, N + 1)]
VINGT = 1 - LAM ** 20

f = Figure(xmin=0, xmax=N + 1, ymin=0, ymax=0.068, w=560, h=320,
           titre="Les rendements récents pèsent le plus, et le poids décroît géométriquement")
f.axes(xlab="il y a k jours", ylab="poids", xticks=(1, 10, 20, 30, 40, 50, 60),
       yticks=(0.03, 0.06), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%g" % (t * 100)).replace(".", ",") + " %")

for k, w in enumerate(poids, start=1):
    f.barre(k, w, 0.72, couleur=ACCENT if k <= 20 else DOUX, opacite=1 if k <= 20 else 0.5)

f.texte(8, 0.061, "← la veille : 6 %", couleur=ENCRE, taille=11.5, fond=True)
f.texte(40, 0.042, "les 20 derniers jours : %d %% du poids" % round(100 * VINGT),
        couleur=ACCENT, ancre="middle", gras=True, fond=True)
f.texte(45, 0.015, "λ = 0,94", couleur=DOUX, ancre="middle", taille=11.5)

sys.stdout.write(f.svg())
