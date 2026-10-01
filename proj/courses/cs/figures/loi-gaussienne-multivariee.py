#!/usr/bin/env python3
r"""
loi-gaussienne-multivariee.svg — la fonction caractéristique lue sur une seule cloche.

Ce que la figure doit faire voir : pour un x fixé, ⟨x,X⟩ est une gaussienne réelle ; son
centre est ⟨x,m⟩ et sa variance xᵗΣx, et ce sont exactement les deux facteurs de Φ_X(x).

Le couple du cours : m = (0, 1), variances 1, covariance ½ ; x = (1, 1). Alors
⟨x,m⟩ = 1 et xᵗΣx = 1 + 2 × ½ + 1 = 3. La cloche est celle de N(1, 3) ; une flèche
mène de son centre au facteur e^{i⟨x,m⟩}, une mesure de sa largeur (un écart type de part
et d'autre) au facteur e^{−xᵗΣx/2}. La Forme est écrite dessous.

Usage : python courses/cs/figures/loi-gaussienne-multivariee.py > loi-gaussienne-multivariee.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

M = (0.0, 1.0)
SIGMA = ((1.0, 0.5), (0.5, 1.0))
X = (1.0, 1.0)
CENTRE = X[0] * M[0] + X[1] * M[1]                                   # ⟨x,m⟩ = 1
VAR = sum(X[i] * SIGMA[i][j] * X[j] for i in range(2) for j in range(2))   # xᵗΣx = 3
assert abs(CENTRE - 1) < 1e-12 and abs(VAR - 3) < 1e-12
ET = math.sqrt(VAR)
dens = lambda s: math.exp(-(s - CENTRE) ** 2 / (2 * VAR)) / math.sqrt(2 * math.pi * VAR)
ent = lambda t: ("%d" % t).replace("-", "−")

f = Figure(-5, 7, -0.13, 0.27, w=600, h=330, marges=(14, 16, 10, 14),
           titre="La loi de ⟨x,X⟩ : centre ⟨x,m⟩, variance xᵗΣx ; Φ_X(x) en découle")
# l'axe des valeurs seul : la Forme s'écrit dessous, dans le cadre
f.courbe([(-5, 0), (7, 0)], couleur=DOUX, epaisseur=1.2)
for t in (-4, -2, 0, 1, 2, 4, 6):
    f.segment(t, 0, t, -0.006, couleur=DOUX, epaisseur=1.2, pointilles=None)
    f.texte(t, 0, ent(t), couleur=DOUX, taille=11.5, ancre="middle", dy=17)
f.texte(7, 0, "⟨x,X⟩ = X₁ + X₂", couleur=DOUX, ancre="end", dy=-8)
f.fonction(dens, -5, 7, n=220, couleur=ACCENT, epaisseur=2.6)

# le centre
f.segment(CENTRE, 0, CENTRE, dens(CENTRE), couleur=AJOUT, epaisseur=1.6)
f.texte(CENTRE, dens(CENTRE), "centre ⟨x,m⟩ = 0 + 1", couleur=AJOUT, dx=8, dy=-6, gras=True)

# la largeur : un écart type de part et d'autre, à mi-hauteur de la cloche
h = dens(CENTRE + ET)
f.fleche(CENTRE, h, CENTRE + ET, h, couleur=ENCRE, epaisseur=1.6)
f.fleche(CENTRE, h, CENTRE - ET, h, couleur=ENCRE, epaisseur=1.6)
f.texte(CENTRE + ET, h, "écart type √(xᵗΣx)", couleur=ENCRE, dx=10, dy=-6, gras=True)
f.texte(CENTRE + ET, h, "xᵗΣx = 1 + 2 × ½ + 1 = 3", couleur=ENCRE, dx=22, dy=-26)

# la Forme, dessous : chaque facteur sous ce qui le porte
f.texte(-0.4, -0.07, "Φ_{X}(x) = E(e^{i⟨x,X⟩})  =", couleur=ENCRE, taille=15, ancre="end")
f.texte(CENTRE, -0.07, "e^{i⟨x,m⟩}", couleur=AJOUT, taille=15, gras=True, ancre="middle")
f.texte(CENTRE + ET + 0.4, -0.07, "e^{−xᵗΣx/2}", couleur=ENCRE, taille=15, gras=True, ancre="middle")
f.texte(CENTRE, -0.115, "le centre", couleur=AJOUT, ancre="middle")
f.texte(CENTRE + ET + 0.4, -0.115, "la largeur", couleur=ENCRE, ancre="middle")

sys.stdout.write(f.svg())
