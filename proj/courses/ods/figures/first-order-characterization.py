#!/usr/bin/env python3
r"""
first-order-characterization.svg — a convex function lies above each of its tangents.

Ce que la figure doit faire voir : la tangente en un seul point x̄ passe sous tout le
graphe, pas seulement près de x̄ ; en x = −1, loin de x̄ = 1, l'écart est de plus de 5.

f(x) = x² − cos x, x̄ = 1 : f(1) = 1 − cos 1 ≈ 0,46, f'(1) = 2 + sin 1 ≈ 2,84. La
tangente vaut 0,46 + 2,84 (x − 1), soit ≈ −5,22 en x = −1, où f(−1) ≈ 0,46.

Usage : python courses/ods/figures/first-order-characterization.py > first-order-characterization.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
xb = 1.0
fb, pente = f(xb), 2 * xb + math.sin(xb)
tan = lambda x: fb + pente * (x - xb)

g = Figure(xmin=-1.9, xmax=2.3, ymin=-6.2, ymax=4.2, w=560, h=380, marges=(10, 10, 10, 10),
           titre="One tangent, drawn at a single point, stays under the whole graph")
g.axes(croix=(0, 0))
g.fonction(f, -1.8, 2.15, couleur=ACCENT, epaisseur=2.4)
g.fonction(tan, -1.25, 2.2, couleur=AJOUT, epaisseur=2)
g.point(xb, fb)
g.segment(xb, 0, xb, fb, couleur=PALE)
g.texte(xb + 0.08, -0.55, "x̄ = 1", couleur=DOUX, taille=12)
g.texte(xb - 0.12, fb + 0.35, "f(x̄) ≈ %.2f" % fb, taille=12.5, ancre="end", fond=True)
g.mesure(-1, tan(-1), f(-1), couleur=ENCRE, etiquette="gap ≈ %.2f" % (f(-1) - tan(-1)))
g.texte(-1.3, 3.85, "f(x) = x² − cos x", couleur=ACCENT, taille=12.5, gras=True, fond=True)
g.texte(0.1, -4.9, "tangent at x̄: f(x̄) + f′(x̄)(x − x̄)", couleur=AJOUT, taille=12.5, gras=True,
        fond=True)
sys.stdout.write(g.svg())
