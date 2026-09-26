#!/usr/bin/env python3
r"""
quadratic-lower-bound.svg — room for a parabola between the curve and its tangent.

Ce que la figure doit faire voir : pour une fonction fortement convexe, il n'y a pas
seulement la tangente sous la courbe ; la tangente augmentée de la parabole (μ/2)(x − x̄)²
y tient encore. C'est la figure 2.4 (b) des notes, sur f(x) = x² − cos x, μ = 1, x̄ = 1.

f(1) ≈ 0,46, f'(1) ≈ 2,84. En x = −1 : tangente ≈ −5,22, tangente + parabole ≈ −3,22,
courbe ≈ 0,46.

Usage : python courses/ods/figures/quadratic-lower-bound.py > quadratic-lower-bound.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
xb, mu = 1.0, 1.0
fb, p = f(xb), 2 * xb + math.sin(xb)
tan = lambda x: fb + p * (x - xb)
bas = lambda x: tan(x) + mu / 2 * (x - xb) ** 2

g = Figure(xmin=-1.9, xmax=2.3, ymin=-6.2, ymax=4.2, w=560, h=380, marges=(10, 10, 10, 10),
           titre="Strong convexity: between the curve and its tangent there is room for a parabola")
g.axes(croix=(0, 0))
g.fonction(tan, -1.25, 2.2, couleur=PALE, epaisseur=1.6)
g.fonction(bas, -1.6, 2.2, couleur=AJOUT, epaisseur=2.2)
g.fonction(f, -1.8, 2.15, couleur=ACCENT, epaisseur=2.4)
g.point(xb, fb)
g.segment(xb, 0, xb, fb, couleur=PALE)
g.texte(xb + 0.08, -0.55, "x̄ = 1", couleur=DOUX, taille=12)
g.mesure(-1, bas(-1), f(-1), couleur=ENCRE, etiquette="still ≈ %.2f of room" % (f(-1) - bas(-1)))
g.texte(-1.3, 3.85, "f(x) = x² − cos x, μ = 1", couleur=ACCENT, taille=12.5, gras=True, fond=True)
g.texte(-1.85, -4.1, "tangent + ½μ(x − x̄)²", couleur=AJOUT, taille=12.5, gras=True, fond=True)
g.texte(0.1, -4.9, "tangent alone", couleur=DOUX, taille=12, fond=True)
sys.stdout.write(g.svg())
