#!/usr/bin/env python3
r"""
convex-function.svg — the chord passes above the graph.

Ce que la figure doit faire voir : entre deux points du graphe de f(x) = x² − cos x, la
corde passe au-dessus du graphe ; au milieu, la corde vaut la moyenne des deux valeurs,
et le graphe est plus bas. C'est l'inégalité (2.1) des notes, à λ = ½.

x = −1 : f = 1 − cos 1 ≈ 0,46 ; y = 2 : f = 4 − cos 2 ≈ 4,42. Au milieu, 0,5 :
f(0,5) = 0,25 − cos 0,5 ≈ −0,63, et la corde vaut (0,46 + 4,42)/2 ≈ 2,44.

Usage : python courses/ods/figures/convex-function.py > convex-function.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
x, y = -1.0, 2.0
m = (x + y) / 2
fx, fy, fm = f(x), f(y), f(m)
corde = (fx + fy) / 2
v = lambda t: ("%.2f" % t).replace("-", "−")

g = Figure(xmin=-1.8, xmax=2.7, ymin=-1.5, ymax=5.0, w=560, h=360, marges=(10, 10, 10, 10),
           titre="Between any two points of the graph, the chord passes above it")
g.axes(croix=(0, 0))
g.fonction(f, -1.6, 2.28, couleur=ACCENT, epaisseur=2.4)
g.courbe([(x, fx), (y, fy)], couleur=AJOUT, epaisseur=2)
g.point(x, fx); g.point(y, fy)
g.segment(m, fm, m, corde, couleur=ENCRE, epaisseur=1.4, pointilles=None)
g.point(m, fm, couleur=ACCENT); g.point(m, corde, couleur=AJOUT)
for t, s in ((x, "x = −1"), (m, "½x + ½y"), (y, "y = 2")):
    g.segment(t, 0, t, min(f(t), 0) if t == m else 0, couleur=PALE)
    g.texte(t, -0.45 if t != m else 0.3, s, couleur=DOUX, taille=12, ancre="middle", fond=True)
g.texte(x - 0.1, fx + 0.15, "f(x) ≈ " + v(fx), taille=12.5, ancre="end", fond=True)
g.texte(y - 0.12, fy + 0.2, "f(y) ≈ " + v(fy), taille=12.5, ancre="end", fond=True)
g.texte(m + 0.12, corde + 0.12, "chord: ½f(x) + ½f(y) ≈ " + v(corde), couleur=AJOUT, taille=12.5,
        gras=True, fond=True)
g.texte(m + 0.12, fm - 0.35, "graph: f(½x + ½y) ≈ " + v(fm), couleur=ACCENT, taille=12.5, gras=True,
        fond=True)
sys.stdout.write(g.svg())
