#!/usr/bin/env python3
r"""
vecteur-gaussien.svg — des composantes gaussiennes ne font pas un vecteur gaussien.

Ce que la figure doit faire voir : la définition porte sur toutes les combinaisons
⟨x,X⟩, et une seule combinaison non gaussienne suffit à la faire tomber.

Deux couples, en colonnes, et pour chacun la loi de la même combinaison x = (1, 1),
c'est-à-dire de la somme des deux composantes :
- à gauche, le couple du cours, de moyenne m = (0, 1) et de covariance ½ entre deux
  variances 1 ; ses lignes de niveau sont des ellipses, et X₁ + X₂ suit une N(1, 3)
  (moyenne 0 + 1, variance 1 + 1 + 2 × ½) ;
- à droite, (X, εX) avec X de loi N(0, 1) et ε = ±1 indépendant, chaque signe avec
  probabilité ½ : εX est encore N(0, 1), mais le couple vit sur les deux diagonales, et
  X + εX vaut 0 dès que ε = −1, avec probabilité ½. Le reste du temps il vaut 2X, de loi
  N(0, 4) : une demi-cloche et une masse ponctuelle, ce qui n'est pas une gaussienne.

Les deux lignes de niveau sont celles où (x − m)ᵗΣ⁻¹(x − m) vaut 1 et 4, tracées comme
m + c·A(cos θ, sin θ), où A est la racine de Cholesky de Σ.

Usage : python courses/cs/figures/vecteur-gaussien.py > vecteur-gaussien.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, Colonne, ACCENT, AJOUT, DOUX, ENCRE, PALE   # noqa: E402

M = (0.0, 1.0)
S11, S12, S22 = 1.0, 0.5, 1.0
A11, A21 = math.sqrt(S11), S12 / math.sqrt(S11)            # Cholesky : Σ = A Aᵗ
A22 = math.sqrt(S22 - A21 ** 2)
VAR_SOMME = S11 + S22 + 2 * S12                              # 3
assert abs(VAR_SOMME - 3) < 1e-12


def ellipse(c, n=120):
    return [(M[0] + c * A11 * math.cos(2 * math.pi * k / n),
             M[1] + c * (A21 * math.cos(2 * math.pi * k / n) + A22 * math.sin(2 * math.pi * k / n)))
            for k in range(n + 1)]


def normale(mu, var):
    return lambda s: math.exp(-(s - mu) ** 2 / (2 * var)) / math.sqrt(2 * math.pi * var)


ent = lambda t: ("%d" % t).replace("-", "−")
W, H = 290, 230

# -- ligne 1 : les deux couples ------------------------------------------------
g = Figure(-3.2, 3.2, -2.2, 4.2, w=W, h=H, marges=(30, 14, 42, 10))
g.axes(xlab="X₁", ylab="X₂", xticks=(-2, 0, 2), yticks=(-2, 0, 2, 4), fmt=ent, croix=(0, 0))
for c in (1, 2):
    g.courbe(ellipse(c), couleur=ACCENT, epaisseur=2.0)
g.point(*M, couleur=ACCENT)
g.texte(0.25, 3.9, "le couple du cours", couleur=ENCRE, gras=True)

d = Figure(-3.2, 4.0, -3.2, 3.2, w=W, h=H, marges=(30, 14, 42, 10))
d.axes(xlab="X", ylab="εX", xticks=(-2, 0, 2), yticks=(-2, 0, 2), fmt=ent, croix=(0, 0))
d.segment(-2.4, -2.4, 2.4, 2.4, couleur=AJOUT, epaisseur=3.0, pointilles=None)
d.segment(-2.4, 2.4, 2.4, -2.4, couleur=AJOUT, epaisseur=3.0, pointilles=None)
d.texte(-3.0, 2.95, "(X, εX)", couleur=ENCRE, gras=True)
d.texte(2.4, 2.4, "ε = 1", couleur=AJOUT, dx=6, dy=4)
d.texte(2.4, -2.4, "ε = −1", couleur=AJOUT, dx=6, dy=4)

# -- ligne 2 : la loi de X₁ + X₂ -------------------------------------------------
YM = 0.27
b = Figure(-5, 7, 0, YM, w=W, h=H, marges=(30, 14, 42, 10))
b.axes(xlab="X₁ + X₂", xticks=(-4, 0, 1, 4), fmt=ent, croix=(-5, 0))
b.fonction(normale(1, VAR_SOMME), -5, 7, n=200, couleur=ACCENT, epaisseur=2.4)
b.segment(1, 0, 1, normale(1, VAR_SOMME)(1), couleur=PALE)
b.texte(-4.8, 0.245, "N(1, 3) : gaussienne", couleur=ACCENT, gras=True)

c = Figure(-6, 6, 0, YM, w=W, h=H, marges=(30, 14, 42, 10))
c.axes(xlab="X + εX", xticks=(-4, 0, 4), fmt=ent, croix=(-6, 0))
c.fonction(lambda s: 0.5 * normale(0, 4)(s), -6, 6, n=200, couleur=AJOUT, epaisseur=2.4)
c.fleche(0, 0, 0, 0.215, couleur=AJOUT, epaisseur=3.0)
c.texte(0, 0.215, "masse ½ en 0", couleur=AJOUT, dx=8, dy=4, gras=True)
c.texte(3.0, 0.07, "½ N(0, 4)", couleur=AJOUT, dx=0, dy=0)
c.texte(-5.8, 0.245, "pas gaussienne", couleur=AJOUT, gras=True)

sys.stdout.write(Colonne(
    [Planche([g, d], ecart=24), Planche([b, c], ecart=24)],
    intitules=["Deux couples aux composantes de loi gaussienne",
               "La combinaison ⟨x,X⟩ pour x = (1, 1) : la somme des composantes"],
    titre="Le couple du cours est gaussien ; (X, εX) ne l'est pas, sa somme a une masse en 0").svg())
