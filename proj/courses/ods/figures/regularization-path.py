#!/usr/bin/env python3
r"""
regularization-path.svg — the ridge solutions as λ decreases, solved from the easy end.

Ce que la figure doit faire voir : dans le plan des poids, les solutions ŵ(λ) des quatre
observations forment une courbe qui part de 0 (λ → ∞) et arrive à l'ajustement exact
(0, 1) (λ = 0) ; on la parcourt dans ce sens : chaque solution sert de point de départ à
la suivante, et la première, à λ grand, est presque 0.

ŵ(λ) = (XᵀX + λI)⁻¹ Xᵀy, XᵀX = [[3, 1], [1, 2]], Xᵀy = (1, 2) : ŵ(10) = (2/31, 5/31),
ŵ(2) = (2/19, 9/19), ŵ(1) = (1/11, 7/11), ŵ(0) = (0, 1).

Usage : python courses/ods/figures/regularization-path.py > regularization-path.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def w(lam):
    a, b, d = 3 + lam, 1.0, 2 + lam
    det = a * d - b * b
    return ((d * 1 - b * 2) / det, (a * 2 - b * 1) / det)


g = Figure(xmin=-0.08, xmax=0.36, ymin=-0.06, ymax=1.1, w=420, h=470, marges=(46, 26, 36, 12),
           titre="The ridge path, from λ large (near 0) to λ = 0 (the exact fit)")
lams = [10 ** (3 - 5 * i / 200) for i in range(201)] + [0.0]
g.courbe([w(l) for l in lams], couleur=PALE, epaisseur=2)
grille = [100, 10, 3, 1, 0.3, 0.1, 0.0]
pts = [w(l) for l in grille]
for a, b in zip(pts, pts[1:]):
    g.fleche(a[0], a[1], b[0], b[1], couleur=ACCENT, epaisseur=1.6)
for l, p in zip(grille, pts):
    g.point(*p, couleur=ACCENT, r=3.8)
    g.texte(p[0] + 0.012, p[1] - 0.005, "λ = %g" % l, taille=11.5, couleur=ENCRE, fond=True)
g.point(0, 0, couleur=DOUX)
g.texte(0.01, -0.035, "0", taille=11.5, couleur=DOUX)
g.texte(0.12, 0.2, "solve λ = 100 first, from w⁰ = 0;", taille=12, couleur=ACCENT, gras=True)
g.texte(0.12, 0.14, "then warm-start each next λ", taille=12, couleur=ACCENT, gras=True)
g.axes(xlab="w₁", ylab="w₂", xticks=[0, 0.1, 0.2, 0.3], yticks=[0, 0.5, 1],
       fmt=lambda t: ("%g" % t))
sys.stdout.write(g.svg())
