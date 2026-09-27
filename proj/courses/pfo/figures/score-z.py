#!/usr/bin/env python3
r"""
score-z.svg — la loi normale graduée en scores, et le rendement de l'exemple.

La fiche énonce la règle pour une loi normale : environ 68 % des observations entre $-1$
et $+1$, environ 95 % entre $-2$ et $+2$, et un score au-delà de 3 en valeur absolue très
rare. Les bandes montrent ces deux proportions, les verticales le seuil de 3. Le point est
l'exemple : un rendement de $-4\,\%$ dans un groupe de moyenne nulle et d'écart type 1 %,
soit un score de $-4$, hors du seuil. Sous l'axe des scores, l'axe des rendements, gradué
en $\mu$, $\mu\pm\sigma$… : chaque rendement $x$ tombe au score $Z=(x-\mu)/\sigma$, ce que
la flèche de l'exemple fait lire, et c'est la Forme de la fiche.

Usage : python courses/pfo/figures/score-z.py > score-z.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

phi = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)

f = Figure(xmin=-6, xmax=6, ymin=-0.2, ymax=0.52, w=560, h=420,
           titre="Au-delà de trois écarts types, une observation est suspecte")
f.axes(xlab="score Z", xticks=(-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5), fmt=lambda t: "%d" % t,
       croix=(-6, 0))

PAS = 0.05
for k in range(-40, 40):
    z = (k + 0.5) * PAS
    op = 0.40 if abs(z) < 1 else 0.18
    f.barre(z, phi(z), PAS, couleur=ACCENT, opacite=op, y0=0)
f.fonction(phi, -5.6, 5.6, n=300, couleur=ENCRE, epaisseur=2.0)
f.texte(0, 0.18, "68 %", couleur=ENCRE, ancre="middle", gras=True)

# 95 % : une accolade de −2 à +2, reliée à la bande claire par deux verticales
HAUT = 0.445
for s_ in (-2, 2):
    f.segment(s_, phi(s_), s_, HAUT, couleur=ACCENT, epaisseur=1.0, pointilles="3 3")
f.courbe([(-2, HAUT - 0.012), (-2, HAUT), (2, HAUT), (2, HAUT - 0.012)], couleur=ACCENT,
         epaisseur=1.4)
f.texte(0, HAUT, "95 % entre −2 et +2", couleur=ACCENT, ancre="middle", dy=-7, taille=11.5)

# le seuil de 3, des deux côtés
for s_ in (-3, 3):
    f.segment(s_, 0, s_, 0.14, couleur=AJOUT, epaisseur=1.6)
f.texte(3, 0.14, "seuil 3", couleur=AJOUT, ancre="middle", dy=-6, taille=11.5, gras=True)

# le rendement de l'exemple : un trait le relie à son étiquette, posée au-dessus du seuil
f.point(-4, 0, couleur=AJOUT, r=5)
f.segment(-4, 0.012, -4, 0.19, couleur=AJOUT, epaisseur=1.0, pointilles="2 3")
f.texte(-4, 0.19, "−4 % : Z = −4", couleur=AJOUT, ancre="middle", dy=-6, gras=True)

# L'axe des rendements, sous celui des scores : x = μ + Zσ, donc Z = (x − μ)/σ.
YR = -0.13
f.courbe([(-6, YR), (6, YR)], couleur=DOUX, epaisseur=1.2)
for z, s_ in ((-4, "μ − 4σ"), (-2, "μ − 2σ"), (0, "μ"), (2, "μ + 2σ"), (4, "μ + 4σ")):
    f.courbe([(z, YR - 0.008), (z, YR + 0.008)], couleur=DOUX, epaisseur=1.2)
    f.texte(z, YR, s_, couleur=DOUX, ancre="middle", dy=18, taille=11.5)
f.texte(6, YR, "rendement x", couleur=DOUX, ancre="end", dy=-8, taille=12)
f.fleche(-4, YR + 0.012, -4, -0.035, couleur=AJOUT, epaisseur=1.6)
f.texte(-4, (YR - 0.035) / 2 + 0.004, "Z = (x − μ) / σ = (−4 % − 0) / 1 %", couleur=AJOUT, dx=8,
        dy=4, taille=12, gras=True)
sys.stdout.write(f.svg())
