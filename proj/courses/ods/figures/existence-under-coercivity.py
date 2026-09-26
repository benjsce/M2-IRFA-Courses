#!/usr/bin/env python3
r"""
existence-under-coercivity.svg — coercivity builds the compact set that the plane lacks.

Ce que la figure doit faire voir : sur tout le plan, aucun domaine compact n'est donné ;
mais hors d'un disque, la perte dépasse sa valeur en 0, donc le meilleur point, s'il
existe, est dans le disque — et le disque est compact.

Les quatre observations du cours : lignes (1, 1), (1, 0), (1, 0), (0, 1), réponses
b = (1, 0, 0, 1), perte f(x) = ½‖Ax − b‖². AᵀA = [[3, 1], [1, 2]], le minimiseur est
x* = (0, 1) et l'ajustement y est exact, donc f(x) = ½ (x − x*)ᵀ AᵀA (x − x*) ; f(0) = 1.
Le plus petit facteur d'étirement de A est c = √((5 − √5)/2) ≈ 1,176, et
‖Ax − b‖ ≥ c‖x‖ − ‖b‖, avec ‖b‖ = √2 : f(x) > 1 dès que ‖x‖ > 2√2/c ≈ 2,41.
La courbe tracée est la ligne de niveau f = f(0) = 1, qui passe par l'origine.

Usage : python courses/ods/figures/existence-under-coercivity.py > existence-under-coercivity.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

H = ((3.0, 1.0), (1.0, 2.0))                      # AᵀA
XS = (0.0, 1.0)                                   # le minimiseur
c = math.sqrt((5 - math.sqrt(5)) / 2)
M = 2 * math.sqrt(2) / c                          # ≈ 2,41

# ligne de niveau ½ (x − x*)ᵀ H (x − x*) = 1 : x = x* + √2 · (vecteurs propres / √valeurs propres)
l1, l2 = (5 + math.sqrt(5)) / 2, (5 - math.sqrt(5)) / 2
def vp(l):                                        # vecteur propre de H pour la valeur l
    v = (1.0, l - 3.0)
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)
v1, v2 = vp(l1), vp(l2)
def niveau(t):
    a, b = math.sqrt(2 / l1) * math.cos(t), math.sqrt(2 / l2) * math.sin(t)
    return (XS[0] + a * v1[0] + b * v2[0], XS[1] + a * v1[1] + b * v2[1])

g = Figure(xmin=-3.3, xmax=5.6, ymin=-2.9, ymax=2.9, w=600, h=390, marges=(10, 10, 10, 10),
           titre="Outside the disk the loss exceeds its value at 0: the best point can only be inside")
g.axes(croix=(0, 0))
g.courbe([(M * math.cos(2 * math.pi * k / 200), M * math.sin(2 * math.pi * k / 200))
          for k in range(201)], couleur=ENCRE, epaisseur=1.6, pointilles="6 4")
g.courbe([niveau(2 * math.pi * k / 200) for k in range(201)], couleur=ACCENT, epaisseur=2.2)
g.point(0, 0, couleur=ENCRE)
g.point(*XS, couleur=ACCENT, r=4.6)
g.texte(-0.18, 0.93, "x* = (0, 1)", couleur=ACCENT, gras=True, taille=12.5, ancre="end", fond=True)
g.texte(-0.15, -0.28, "0", couleur=DOUX, taille=12, ancre="end")
g.texte(1.2, 0.62, "level f = f(0) = 1", couleur=ACCENT, taille=12, fond=True)
g.segment(0, 0, M * math.cos(-0.75), M * math.sin(-0.75), couleur=DOUX, pointilles=None)
g.texte(0.45, -1.25, "M ≈ 2.41", couleur=ENCRE, taille=12, fond=True)
g.texte(2.75, 2.3, "outside the disk:", couleur=ENCRE, taille=12.5, gras=True)
g.texte(2.75, 1.85, "f > f(0) = 1,", couleur=ENCRE, taille=12.5)
g.texte(2.75, 1.4, "no point there can win", couleur=DOUX, taille=12)
g.texte(2.75, -1.6, "inside: a closed, bounded", couleur=ENCRE, taille=12.5)
g.texte(2.75, -2.05, "disk, where a minimizer", couleur=ENCRE, taille=12.5)
g.texte(2.75, -2.5, "exists (Theorem 1.1)", couleur=ENCRE, taille=12.5)
sys.stdout.write(g.svg())
