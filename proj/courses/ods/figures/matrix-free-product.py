#!/usr/bin/env python3
r"""
matrix-free-product.svg — computing Aw without ever forming A.

Ce que la figure doit faire voir : le vecteur w passe par X, puis par Xᵀ, et on lui
ajoute λw ; chaque passage coûte deux opérations par non-nul de X, soit 2 × 10⁶, et ne
garde en mémoire que des vecteurs. La matrice A = XᵀX + λI, 10⁶ × 10⁶, n'apparaît jamais.
Slide 13 : n = 10⁵, p = 10⁶, nnz(X) = 10⁶, coût total ≈ 4 nnz(X) = 4 × 10⁶ opérations.

Usage : python courses/ods/figures/matrix-free-product.py > matrix-free-product.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

g = Figure(xmin=0, xmax=14, ymin=0, ymax=5.4, w=640, h=250, marges=(8, 8, 8, 8),
           titre="Never form the matrix: Aw is two sparse products and one vector sum")


def boite(x, y, l, h, titre, sous, c=ENCRE, barree=False):
    X0, Y0, X1, Y1 = g.px(x), g.py(y + h), g.px(x + l), g.py(y)
    g._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.1" '
           'stroke="%s" stroke-width="1.5" rx="4"%s/>'
           % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), c, c,
              ' stroke-dasharray="5 4"' if barree else ""))
    g.texte(x + l / 2, y + h * 0.58, titre, couleur=c, taille=13, ancre="middle", gras=True)
    g.texte(x + l / 2, y + h * 0.2, sous, couleur=DOUX, taille=11.5, ancre="middle")


boite(0.2, 2.6, 2.4, 1.5, "w", "10⁶ numbers", c=ACCENT)
boite(4.0, 2.6, 2.6, 1.5, "Xw", "10⁵ numbers", c=ACCENT)
boite(8.0, 2.6, 2.6, 1.5, "Xᵀ(Xw)", "10⁶ numbers", c=ACCENT)
boite(11.6, 2.6, 2.2, 1.5, "Aw", "10⁶ numbers", c=ENCRE)
g.fleche(2.65, 3.35, 3.95, 3.35)
g.fleche(6.65, 3.35, 7.95, 3.35)
g.fleche(10.65, 3.35, 11.55, 3.35)
g.texte(3.3, 3.55, "× X", taille=12, ancre="middle")
g.texte(3.3, 2.75, "2·10⁶ ops", taille=11, ancre="middle", couleur=DOUX)
g.texte(7.3, 3.55, "× Xᵀ", taille=12, ancre="middle")
g.texte(7.3, 2.75, "2·10⁶ ops", taille=11, ancre="middle", couleur=DOUX)
g.texte(11.1, 3.55, "+ λw", taille=12, ancre="middle")
boite(3.2, 0.2, 7.6, 1.6, "A = XᵀX + λI, 10⁶ × 10⁶", "8 TB: never built", c=AJOUT, barree=True)
sys.stdout.write(g.svg())
