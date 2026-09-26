#!/usr/bin/env python3
r"""
convex-set.svg — a convex set keeps every segment, a non-convex one lets one escape.

Ce que la figure doit faire voir : deux points pris dans chaque ensemble et le segment
qui les joint ; dans l'ensemble convexe il reste dedans, dans le croissant il traverse
le creux. C'est la figure 2.2 des notes, redessinée.

Le croissant est un disque de rayon 1,6 centré en 0, privé du disque de rayon 1,3 centré
en (0,8 ; 0) ; les deux points (0,2 ; ±1,45) sont dans ses deux cornes, et le milieu du
segment, (0,2 ; 0), est dans le disque retiré.

Usage : python courses/ods/figures/convex-set.py > convex-set.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, _n      # noqa: E402


def surface(g, pts, couleur):
    d = "M" + " L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in pts) + " Z"
    g._add('<path d="%s" fill="%s" fill-opacity="0.16" stroke="%s" stroke-width="1.8" '
           'stroke-linejoin="round"/>' % (d, couleur, couleur))


def arc(cx, cy, r, a0, a1, n=80):
    return [(cx + r * math.cos(a0 + (a1 - a0) * k / n), cy + r * math.sin(a0 + (a1 - a0) * k / n))
            for k in range(n + 1)]


def cadre():
    return Figure(xmin=-2.2, xmax=2.2, ymin=-2.0, ymax=2.1, w=290, h=250, marges=(8, 8, 8, 8))


# convexe : une ellipse inclinée
g1 = cadre()
t = math.radians(20)
ell = [(1.9 * math.cos(s) * math.cos(t) - 1.1 * math.sin(s) * math.sin(t),
        1.9 * math.cos(s) * math.sin(t) + 1.1 * math.sin(s) * math.cos(t))
       for s in [2 * math.pi * k / 120 for k in range(120)]]
surface(g1, ell, ACCENT)
x, y = (-1.3, -0.1), (1.2, 0.75)
g1.courbe([x, y], couleur=ENCRE, epaisseur=2)
g1.point(*x); g1.point(*y)
g1.texte(x[0] - 0.1, x[1] + 0.2, "x", taille=13, ancre="end")
g1.texte(y[0] + 0.1, y[1] + 0.15, "y", taille=13)
g1.texte(-2.1, 1.85, "C: convex", couleur=ACCENT, gras=True, taille=13)
g1.texte(-2.1, -1.85, "the segment stays inside", couleur=DOUX, taille=12)

# non convexe : un croissant
g2 = cadre()
xi = (2.56 - 1.69 + 0.64) / 1.6                    # abscisse des deux points d'intersection
yi = math.sqrt(2.56 - xi * xi)
a_ext = math.atan2(yi, xi)                          # ≈ 53,8°
a_int = math.atan2(yi, xi - 0.8)                    # ≈ 83,6°
bord = arc(0, 0, 1.6, a_ext, 2 * math.pi - a_ext) + arc(0.8, 0, 1.3, 2 * math.pi - a_int, a_int)
surface(g2, bord, AJOUT)
x, y = (0.2, 1.45), (0.2, -1.45)
g2.courbe([x, y], couleur=ENCRE, epaisseur=2)
g2.point(*x); g2.point(*y)
g2.texte(x[0] + 0.12, x[1] + 0.1, "x", taille=13)
g2.texte(y[0] + 0.12, y[1] - 0.25, "y", taille=13)
g2.texte(-2.1, 1.85, "D: not convex", couleur=AJOUT, gras=True, taille=13)
g2.texte(0.35, 0.05, "the segment", couleur=ENCRE, taille=12)
g2.texte(0.35, -0.35, "leaves D here", couleur=ENCRE, taille=12)

sys.stdout.write(Planche([g1, g2], ecart=20,
                         titre="A convex set contains every segment between two of its points").svg())
