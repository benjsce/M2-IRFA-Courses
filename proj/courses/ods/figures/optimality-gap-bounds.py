#!/usr/bin/env python3
r"""
optimality-gap-bounds.svg — the gap to the minimum, squeezed by the gradient and the distance.

Ce que la figure doit faire voir : en z = 1, l'écart f(z) − f(x*) se lit comme une
hauteur ; la pente en z en donne un minorant, la distance à x* un majorant, et l'écart
vrai tombe entre les deux.

f(x) = x² − cos x, L = 3, x* = 0, f(x*) = −1. En z = 1 : écart 1 − cos 1 + 1 ≈ 1,46 ;
minorant f'(1)²/(2L) ≈ 2,84²/6 ≈ 1,35 ; majorant (L/2)·1² = 1,5.

Usage : python courses/ods/figures/optimality-gap-bounds.py > optimality-gap-bounds.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
L, z = 3.0, 1.0
fs = -1.0
bas = (2 * z + math.sin(z)) ** 2 / (2 * L)
haut = L / 2 * z * z
ecart = f(z) - fs

g = Figure(xmin=-1.5, xmax=2.7, ymin=-1.45, ymax=1.65, w=560, h=340, marges=(10, 10, 10, 10),
           titre="The gap f(z) − f(x*) lies between the two bounds")
g.axes(croix=(0, 0))
g.fonction(f, -1.25, 1.25, couleur=ACCENT, epaisseur=2.4)
g.segment(-1.3, fs, 2.35, fs, couleur=PALE)
g.point(0, fs, couleur=ACCENT, r=4.2)
g.point(z, f(z))
g.segment(z, f(z), 2.35, f(z), couleur=PALE)
g.texte(0.1, fs - 0.22, "x* = 0, f(x*) = −1", couleur=ACCENT, taille=12, fond=True)
g.texte(z - 0.08, f(z) + 0.12, "z = 1", taille=12, ancre="end", fond=True)
for x, h, c, s in ((1.6, bas, AJOUT, "%.2f" % bas), (1.95, ecart, ENCRE, "%.2f" % ecart),
                   (2.3, haut, AJOUT, "%.2f" % haut)):
    g.mesure(x, fs, fs + h, couleur=c)
    g.texte(x, fs - 0.22, s, couleur=c, taille=12, ancre="middle", gras=(c == ENCRE))
g.texte(1.775, fs - 0.22, "≤", couleur=DOUX, taille=12, ancre="middle")
g.texte(2.125, fs - 0.22, "≤", couleur=DOUX, taille=12, ancre="middle")
g.texte(1.15, 1.45, "left: (slope at z)² / 2L", couleur=AJOUT, taille=12)
g.texte(1.15, 1.2, "middle: the gap itself", couleur=ENCRE, taille=12)
g.texte(1.15, 0.95, "right: (L/2) × (distance to x*)²", couleur=AJOUT, taille=12)
sys.stdout.write(g.svg())
