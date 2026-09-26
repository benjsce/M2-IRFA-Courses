#!/usr/bin/env python3
r"""
score-z.svg — la loi normale graduée en scores, et le rendement de l'exemple.

La fiche énonce la règle pour une loi normale : environ 68 % des observations entre $-1$
et $+1$, environ 95 % entre $-2$ et $+2$, et un score au-delà de 3 en valeur absolue très
rare. Les bandes montrent ces deux proportions, les verticales le seuil de 3. Le point est
l'exemple : un rendement de $-4\,\%$ dans un groupe de moyenne nulle et d'écart type 1 %,
soit un score de $-4$, hors du seuil.

Usage : python courses/pfo/figures/score-z.py > score-z.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

phi = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)

f = Figure(xmin=-5, xmax=5, ymin=0, ymax=0.47, w=560, h=320,
           titre="Au-delà de trois écarts types, une observation est suspecte")
f.axes(xlab="score Z", xticks=(-4, -3, -2, -1, 0, 1, 2, 3, 4), fmt=lambda t: "%d" % t)

PAS = 0.05
for k in range(-40, 40):
    z = (k + 0.5) * PAS
    op = 0.40 if abs(z) < 1 else 0.18
    f.barre(z, phi(z), PAS, couleur=ACCENT, opacite=op)
f.fonction(phi, -4.8, 4.8, n=300, couleur=ENCRE, epaisseur=2.0)
for s in (-3, 3):
    f.segment(s, 0, s, 0.30, couleur=AJOUT, epaisseur=1.6)
f.texte(0, 0.18, "68 %", couleur=ENCRE, ancre="middle", gras=True)
f.texte(0, 0.43, "95 % entre −2 et +2", couleur=ACCENT, ancre="middle", taille=11.5)
f.texte(3, 0.30, "seuil 3", couleur=AJOUT, ancre="middle", dy=-6, taille=11.5, gras=True)
f.point(-4, 0, couleur=AJOUT, r=5)
f.texte(-4, 0, "−4 % : Z = −4", couleur=AJOUT, ancre="middle", dy=-12, gras=True, fond=True)

sys.stdout.write(f.svg())
