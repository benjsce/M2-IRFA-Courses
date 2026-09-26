#!/usr/bin/env python3
r"""
conjugate-directions.svg — conjugate directions are perpendicular once A is made round.

Ce que la figure doit faire voir : à gauche, les deux pas du gradient conjugué sur les
ellipses de q ne sont pas perpendiculaires ; à droite, dans les coordonnées z = A^{1/2} w,
les ellipses deviennent des cercles et les deux mêmes pas se coupent à angle droit :
⟨d¹, A d⁰⟩ = 0 est une perpendicularité, pour le produit scalaire de A.

A^{1/2} = V diag(√λ) Vᵀ, avec les vecteurs propres V de A = [[4, 1], [1, 3]].

Usage : python courses/ods/figures/conjugate-directions.py > conjugate-directions.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402
from _quadratique import XS, L1, L2, V1, V2, niveau, gradient_conjugue, ecart      # noqa: E402

s1, s2 = math.sqrt(L1), math.sqrt(L2)


def racine(p):
    """z = A^{1/2} p."""
    a, b = p[0] * V1[0] + p[1] * V1[1], p[0] * V2[0] + p[1] * V2[1]
    return (s1 * a * V1[0] + s2 * b * V2[0], s1 * a * V1[1] + s2 * b * V2[1])


cg, _ = gradient_conjugue()
niveaux = (0.5, 0.2, 0.05)

g1 = Figure(xmin=-0.62, xmax=0.78, ymin=-0.12, ymax=1.28, w=330, h=330, marges=(8, 8, 8, 8))
for t in niveaux:
    g1.courbe(niveau(t), couleur=PALE, epaisseur=1.2)
g1.courbe(cg[:2], couleur=ACCENT, epaisseur=2.6)
g1.courbe(cg[1:], couleur=AJOUT, epaisseur=2.6)
for p in cg:
    g1.point(*p, couleur=ENCRE, r=3.6)
g1.texte(-0.58, 1.17, "weights w: not perpendicular", taille=12.5, gras=True, fond=True)
g1.texte(0.2, 0.2, "d⁰", couleur=ACCENT, taille=13, gras=True)
g1.texte(0.2, 0.6, "d¹", couleur=AJOUT, taille=13, gras=True)

zc = [racine(p) for p in cg]
cz = racine(XS)
xs_, ys_ = [p[0] for p in zc] + [cz[0] - 1.0, cz[0] + 1.0], [p[1] for p in zc] + [cz[1] + 1.0]
m_ = max(max(xs_) - min(xs_), max(ys_) - min(ys_)) / 2 + 0.1
cx_, cy_ = (max(xs_) + min(xs_)) / 2, (max(ys_) + min(ys_)) / 2
g2 = Figure(xmin=cx_ - m_, xmax=cx_ + m_, ymin=cy_ - m_, ymax=cy_ + m_, w=330, h=330,
            marges=(8, 8, 8, 8))
for t in niveaux:
    g2.courbe([racine(p) for p in niveau(t)], couleur=PALE, epaisseur=1.2)
g2.courbe(zc[:2], couleur=ACCENT, epaisseur=2.6)
g2.courbe(zc[1:], couleur=AJOUT, epaisseur=2.6)
for p in zc:
    g2.point(*p, couleur=ENCRE, r=3.6)
# l'équerre de l'angle droit en z¹
u = (zc[0][0] - zc[1][0], zc[0][1] - zc[1][1])
v = (zc[2][0] - zc[1][0], zc[2][1] - zc[1][1])
nu, nv = math.hypot(*u), math.hypot(*v)
e = 0.07
a = (zc[1][0] + e * u[0] / nu, zc[1][1] + e * u[1] / nu)
b = (zc[1][0] + e * u[0] / nu + e * v[0] / nv, zc[1][1] + e * u[1] / nu + e * v[1] / nv)
c = (zc[1][0] + e * v[0] / nv, zc[1][1] + e * v[1] / nv)
g2.courbe([a, b, c], couleur=ENCRE, epaisseur=1.3)
g2.texte(cx_ - m_ + 0.05, cy_ + m_ - 0.12, "z = A^{1/2}w: circles, right angle", taille=12.5, gras=True, fond=True)
sys.stdout.write(Planche([g1, g2], signes=("→",), ecart=40,
                         titre="Two directions are conjugate when they are perpendicular for the inner product of A").svg())
