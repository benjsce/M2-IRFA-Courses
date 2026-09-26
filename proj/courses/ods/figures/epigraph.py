#!/usr/bin/env python3
r"""
epigraph.svg — the epigraph turns a function into a set, and its shape into convexity.

Ce que la figure doit faire voir : l'épigraphe est tout ce qui est au-dessus du
graphe ; pour une fonction à bosse, un segment entre deux points de l'épigraphe passe
sous la bosse et en sort ; pour f(x) = x² − cos x, tout segment reste dedans. C'est la
figure 2.3 des notes, avec la fonction du cours à droite.

À gauche, la fonction à bosse est g(x) = 1,6 exp(−1,2 x²) : elle n'est pas convexe. Les
deux points (±1,5 ; 1,0) sont dans son épigraphe, puisque g(1,5) ≈ 0,11 ; le milieu de
leur segment, (0 ; 1,0), est sous g(0) = 1,6, donc hors de l'épigraphe. À droite, les
points (−1,4 ; 2,4) et (1,2 ; 1,5) sont au-dessus de f, et tout le segment aussi.

Usage : python courses/ods/figures/epigraph.py > epigraph.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, _n      # noqa: E402


def epi(g, f, x0, x1, haut, couleur, n=120):
    pts = [(x0 + (x1 - x0) * k / n, f(x0 + (x1 - x0) * k / n)) for k in range(n + 1)]
    d = ("M" + " L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in pts)
         + " L%s %s L%s %s Z" % (_n(g.px(x1)), _n(g.py(haut)), _n(g.px(x0)), _n(g.py(haut))))
    g._add('<path d="%s" fill="%s" fill-opacity="0.16" stroke="none"/>' % (d, couleur))
    g.courbe(pts, couleur=couleur, epaisseur=2.2)


def bosse(x):
    return 1.6 * math.exp(-1.2 * x * x)


g1 = Figure(xmin=-2, xmax=2, ymin=-0.9, ymax=3.2, w=290, h=240, marges=(8, 8, 8, 8))
g1.axes(croix=(0, 0))
epi(g1, bosse, -1.75, 1.75, 3.2, AJOUT)
p, q = (-1.5, 1.0), (1.5, 1.0)
g1.courbe([p, q], couleur=ENCRE, epaisseur=1.8)
g1.point(*p); g1.point(*q)
g1.texte(-1.9, 2.95, "a bump: epi f not convex", couleur=AJOUT, gras=True, taille=12.5, fond=True)
g1.texte(0, -0.65, "the segment passes under the bump", couleur=ENCRE, taille=11.5, ancre="middle",
         fond=True)
g1.texte(0.3, 2.3, "epi f", couleur=AJOUT, taille=12.5)

g2 = Figure(xmin=-2, xmax=2, ymin=-1.5, ymax=3.2, w=290, h=240, marges=(8, 8, 8, 8))
g2.axes(croix=(0, 0))
f = lambda x: x * x - math.cos(x)
epi(g2, f, -1.74, 1.74, 3.2, ACCENT)
p, q = (-1.4, 2.4), (1.2, 1.5)
g2.courbe([p, q], couleur=ENCRE, epaisseur=1.8)
g2.point(*p); g2.point(*q)
g2.texte(0, -1.28, "f(x) = x² − cos x: convex", couleur=ACCENT, gras=True, taille=12.5, ancre="middle", fond=True)
g2.texte(-0.2, 0.9, "epi f", couleur=ACCENT, taille=12.5, ancre="end")
g2.texte(0.35, 2.75, "every segment stays inside", couleur=ENCRE, taille=11.5, ancre="middle", fond=True)

sys.stdout.write(Planche([g1, g2], ecart=22,
                         titre="The epigraph is everything on or above the graph").svg())
