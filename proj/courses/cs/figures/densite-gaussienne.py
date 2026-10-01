#!/usr/bin/env python3
r"""
densite-gaussienne.svg — Σ inversible : une densité ; Σ singulière : une droite.

Ce que la figure doit faire voir : la densité est constante sur les ellipses où la forme
quadratique (x − m)ᵗΣ⁻¹(x − m) est constante, et elle n'existe plus quand det Σ = 0,
parce que toute la masse tient alors sur une droite, de surface nulle.

À gauche, le couple du cours : m = (0, 1), variances 1, covariance ½, det Σ = ¾. Les
ellipses tracées sont celles où la forme quadratique vaut 1 et 4. À droite, le même
couple avec une covariance 1 : Σ = (1 1 ; 1 1), det Σ = 0, et Var(X₁ − X₂) = 1 + 1 − 2 = 0,
donc X₁ − X₂ = −1 avec probabilité un — la combinaison c = (1, −1) de la Prop. 0.3.2.

Usage : python courses/cs/figures/densite-gaussienne.py > densite-gaussienne.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE   # noqa: E402

M = (0.0, 1.0)
S11, S12, S22 = 1.0, 0.5, 1.0
DET = S11 * S22 - S12 ** 2
assert abs(DET - 0.75) < 1e-12
A11, A21 = math.sqrt(S11), S12 / math.sqrt(S11)
A22 = math.sqrt(S22 - A21 ** 2)


def ellipse(c, n=120):
    """(x − m)ᵗΣ⁻¹(x − m) = c² : l'image du cercle de rayon c par la racine A de Σ."""
    pts = []
    for k in range(n + 1):
        u, v = c * math.cos(2 * math.pi * k / n), c * math.sin(2 * math.pi * k / n)
        x1, x2 = M[0] + A11 * u, M[1] + A21 * u + A22 * v
        # contrôle : la forme quadratique vaut bien c² sur la courbe
        d1, d2 = x1 - M[0], x2 - M[1]
        q = (S22 * d1 * d1 - 2 * S12 * d1 * d2 + S11 * d2 * d2) / DET
        assert abs(q - c * c) < 1e-9
        pts.append((x1, x2))
    return pts


ent = lambda t: ("%d" % t).replace("-", "−")
W, H = 300, 320

g = Figure(-3.2, 3.2, -2.2, 4.2, w=W, h=H, marges=(30, 34, 60, 10))
g.axes(xlab="X₁", xticks=(-2, 2), yticks=(-2, 2, 4), fmt=ent, croix=(0, 0))
for c, lab in ((1, "= 1"), (2, "= 4")):
    g.courbe(ellipse(c), couleur=ACCENT, epaisseur=2.2)
g.texte(M[0] + A11 * 1 * math.cos(-0.6), M[1] + A21 * math.cos(-0.6) + A22 * math.sin(-0.6),
        "1", couleur=ACCENT, dx=4, dy=4, gras=True)
g.texte(M[0] + A11 * 2 * math.cos(-0.6), M[1] + 2 * (A21 * math.cos(-0.6) + A22 * math.sin(-0.6)),
        "4", couleur=ACCENT, dx=4, dy=4, gras=True)
g.point(*M, couleur=ACCENT)
g.texte(0, 4.2, "X₂", couleur=DOUX, dx=8, dy=6)
g.texte(-3.1, 4.2, "det Σ = ¾ : une densité", couleur=ACCENT, gras=True, dy=-16)
g.texte(-3.1, -2.2, "densité = c × e^{−½ (x−m)ᵗΣ⁻¹(x−m)} : constante", couleur=ENCRE, dy=36, taille=12)
g.texte(-3.1, -2.2, "sur chaque ellipse, où la forme vaut 1, puis 4", couleur=ENCRE, dy=53, taille=12)

d = Figure(-3.2, 3.2, -2.2, 4.2, w=W, h=H, marges=(30, 34, 60, 10))
d.axes(xlab="X₁", xticks=(-2, 2), yticks=(-2, 2, 4), fmt=ent, croix=(0, 0))
d.segment(-3.0, -2.0, 3.0, 4.0, couleur=AJOUT, epaisseur=3.4, pointilles=None)
d.point(*M, couleur=AJOUT)
d.texte(0, 4.2, "X₂", couleur=DOUX, dx=8, dy=6)
d.texte(-3.1, 4.2, "det Σ = 0 : pas de densité", couleur=AJOUT, gras=True, dy=-16)
d.texte(0.3, -1.0, "toute la masse est", couleur=AJOUT)
d.texte(0.3, -1.0, "sur X₁ − X₂ = −1", couleur=AJOUT, dy=16, gras=True)
d.texte(-3.1, -2.2, "le facteur 1 / det(Σ)^{1/2} n'existe plus :", couleur=ENCRE, dy=36, taille=12)
d.texte(-3.1, -2.2, "une droite n'a pas de surface", couleur=ENCRE, dy=53, taille=12)

sys.stdout.write(Planche([g, d], ecart=26,
                         titre="Σ inversible : densité constante sur des ellipses ; Σ singulière : une droite").svg())
