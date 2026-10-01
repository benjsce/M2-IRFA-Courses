#!/usr/bin/env python3
r"""
esperance-conditionnelle-gaussienne.svg — la droite des milieux.

Ce que la figure doit faire voir : sachant X₁ = x₁, la loi de X₂ est une gaussienne dont
le centre est le milieu de la coupe verticale de chaque ellipse ; ces milieux sont
alignés sur une droite, a + b x₁. L'espérance conditionnelle est cette droite.

Le couple du cours : m = (0, 1), variances 1, covariance ½. Alors b = cov/Var X₁ = ½ et
a = E[X₂] − b E[X₁] = 1 : E[X₂|X₁] = 1 + X₁/2. Trois coupes, en x₁ = −1,5, 0 et 1,5, de
l'ellipse où (x − m)ᵗΣ⁻¹(x − m) = 4 ; leurs milieux sont calculés comme milieux des deux
points de la coupe, et le script vérifie qu'ils tombent sur la droite. Le grand axe de
l'ellipse, de pente 1, est en pointillé : la droite des milieux n'est pas lui.

Usage : python courses/cs/figures/esperance-conditionnelle-gaussienne.py > esperance-conditionnelle-gaussienne.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

M = (0.0, 1.0)
S11, S12, S22 = 1.0, 0.5, 1.0
DET = S11 * S22 - S12 ** 2
B = S12 / S11
A = M[1] - B * M[0]
assert (A, B) == (1.0, 0.5)
C2 = 4.0                                            # niveau de l'ellipse
A11, A21 = math.sqrt(S11), S12 / math.sqrt(S11)
A22 = math.sqrt(S22 - A21 ** 2)


def ellipse(c, n=160):
    return [(M[0] + c * A11 * math.cos(2 * math.pi * k / n),
             M[1] + c * (A21 * math.cos(2 * math.pi * k / n) + A22 * math.sin(2 * math.pi * k / n)))
            for k in range(n + 1)]


def coupe(x1):
    """Les deux x₂ où la verticale x₁ coupe l'ellipse : racines en x₂ de
    S11 d2² − 2 S12 d1 d2 + S22 d1² = C2 · DET, avec d = x − m."""
    d1 = x1 - M[0]
    a, b, c = S11, -2 * S12 * d1, S22 * d1 * d1 - C2 * DET
    r = math.sqrt(b * b - 4 * a * c)
    return M[1] + (-b - r) / (2 * a), M[1] + (-b + r) / (2 * a)


ent = lambda t: ("%d" % t).replace("-", "−")
f = Figure(-3.0, 3.0, -1.6, 3.8, w=560, h=380, marges=(34, 20, 34, 16),
           titre="E(X₂|X₁) = a + b X₁ passe par le milieu de chaque coupe verticale")
f.axes(xlab="X₁", xticks=(-2, -1, 1, 2), yticks=(-1, 1, 2, 3), fmt=ent, croix=(0, 0))
f.texte(0, 3.8, "X₂", couleur=DOUX, dx=8, dy=8)
f.courbe(ellipse(1), couleur=PALE, epaisseur=1.4)
f.courbe(ellipse(2), couleur=ACCENT, epaisseur=2.2)
f.segment(-2.0, -1.0, 2.0, 3.0, couleur=DOUX, epaisseur=1.2)
f.texte(2.0, 3.0, "grand axe, pente 1", couleur=DOUX, dx=6, dy=4, taille=11.5)

for x1 in (-1.5, 0.0, 1.5):
    bas, haut = coupe(x1)
    mil = (bas + haut) / 2
    assert abs(mil - (A + B * x1)) < 1e-12
    f.segment(x1, bas, x1, haut, couleur=ENCRE, epaisseur=1.4, pointilles=None)
    f.point(x1, bas, couleur=ENCRE, r=2.6)
    f.point(x1, haut, couleur=ENCRE, r=2.6)
    f.point(x1, mil, couleur=AJOUT, r=4.6)

f.courbe([(-2.8, A + B * -2.8), (2.8, A + B * 2.8)], couleur=AJOUT, epaisseur=2.6)
f.texte(2.98, 1.0, "E(X₂|X₁)", couleur=AJOUT, ancre="end", gras=True)
f.texte(2.98, 1.0, "= 1 + ½ X₁", couleur=AJOUT, ancre="end", dy=17, gras=True)
f.texte(-2.9, 3.8, "a = E(X₂) − b E(X₁) = 1", couleur=ENCRE, dy=8)
f.texte(-2.9, 3.8, "b = cov(X₁, X₂) / Var X₁ = ½", couleur=ENCRE, dy=26)

sys.stdout.write(f.svg())
