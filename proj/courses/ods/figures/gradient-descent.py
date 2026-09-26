#!/usr/bin/env python3
r"""
gradient-descent.svg — the gradient step goes to the bottom of the upper parabola.

Ce que la figure doit faire voir : en x = 1, la parabole de courbure L = 3 qui touche f
passe au-dessus de toute la courbe ; aller à son sommet, c'est faire le pas de gradient
x − f'(x)/L, et f y est au moins aussi bas que le sommet.

f(x) = x² − cos x ; en 1 : f ≈ 0,46, f' ≈ 2,84. Sommet en 1 − 2,84/3 ≈ 0,053, à la
hauteur 0,46 − 2,84²/6 ≈ −0,89 ; f(0,053) ≈ −0,996.

Usage : python courses/ods/figures/gradient-descent.py > gradient-descent.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
x0, L = 1.0, 3.0
f0, d1 = f(x0), 2 * x0 + math.sin(x0)
m = lambda x: f0 + d1 * (x - x0) + L / 2 * (x - x0) ** 2
x1 = x0 - d1 / L
v = lambda t, n=2: ("%.*f" % (n, t)).replace("-", "−")

g = Figure(xmin=-1.6, xmax=2.3, ymin=-1.6, ymax=3.6, w=560, h=360, marges=(10, 10, 10, 10),
           titre="Gradient descent: jump to the bottom of the parabola of curvature L that sits above f")
g.axes(croix=(0, 0))
g.fonction(m, -0.45, 1.75, couleur=AJOUT, epaisseur=2)
g.fonction(f, -1.5, 1.8, couleur=ACCENT, epaisseur=2.4)
g.point(x0, f0)
g.point(x1, m(x1), couleur=AJOUT)
g.point(x1, f(x1), couleur=ACCENT)
g.segment(x1, m(x1), x1, f(x1), couleur=ENCRE, pointilles=None)
g.fleche(x0 - 0.02, f0 + 0.35, x1 + 0.08, m(x1) + 0.4, couleur=ENCRE, courbure=18)
g.texte(x0 + 0.1, f0, "x = 1", taille=12, fond=True)
g.texte(0.5, 1.55, "step −f′(1)/L ≈ −0.95", taille=12, fond=True)
g.texte(x1 + 0.12, m(x1) - 0.05, "bottom of the parabola ≈ " + v(m(x1)), couleur=AJOUT,
        taille=12, fond=True)
g.texte(x1 + 0.12, f(x1) - 0.3, "f(0.053) ≈ " + v(f(x1), 3), couleur=ACCENT, taille=12, fond=True)
g.texte(-1.45, 3.25, "f(x) = x² − cos x, L = 3", couleur=ACCENT, taille=12.5, gras=True, fond=True)
g.texte(1.25, 3.25, "f(1) + f′(1)h + (L/2)h²", couleur=AJOUT, taille=12.5, gras=True, fond=True,
        ancre="middle")
sys.stdout.write(g.svg())
