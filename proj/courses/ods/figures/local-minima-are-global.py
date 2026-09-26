#!/usr/bin/env python3
r"""
local-minima-are-global.svg — a descent can be trapped by a non-convex f, never by a convex one.

Ce que la figure doit faire voir : à gauche, une fonction non convexe a deux creux ; un
point qui descend depuis la droite s'arrête dans le creux le plus haut, un minimum local
qui n'est pas global. À droite, f(x) = x² − cos x n'a qu'un creux, et il est global.

Fonction de gauche : h(x) = (x² − 1)² + 0,3x. Ses creux se trouvent en résolvant
h'(x) = 4x³ − 4x + 0,3 = 0 ; le script les calcule par dichotomie.

Usage : python courses/ods/figures/local-minima-are-global.py > local-minima-are-global.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

h = lambda x: (x * x - 1) ** 2 + 0.3 * x
dh = lambda x: 4 * x ** 3 - 4 * x + 0.3


def racine(a, b):
    for _ in range(60):
        m = (a + b) / 2
        if dh(a) * dh(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


gauche, droite = racine(-1.5, -0.5), racine(0.5, 1.5)

g1 = Figure(xmin=-1.8, xmax=1.8, ymin=-0.8, ymax=2.3, w=300, h=240, marges=(8, 8, 8, 8))
g1.axes(croix=(0, 0))
g1.fonction(h, -1.6, 1.5, couleur=AJOUT, epaisseur=2.3)
g1.point(droite, h(droite), couleur=AJOUT, r=4.6)
g1.point(gauche, h(gauche), couleur=ENCRE, r=4.6)
g1.fleche(1.42, h(1.42) + 0.25, droite + 0.1, h(droite) + 0.2, couleur=ENCRE)
g1.texte(droite, h(droite) - 0.33, "trapped: local", couleur=AJOUT, taille=12, ancre="middle",
         gras=True, fond=True)
g1.texte(gauche, h(gauche) - 0.33, "global", couleur=ENCRE, taille=12, ancre="middle", fond=True)
g1.texte(-1.2, 2.12, "not convex", couleur=AJOUT, taille=12.5, gras=True, fond=True)

f = lambda x: x * x - math.cos(x)
g2 = Figure(xmin=-1.8, xmax=1.8, ymin=-1.4, ymax=2.4, w=300, h=240, marges=(8, 8, 8, 8))
g2.axes(croix=(0, 0))
g2.fonction(f, -1.5, 1.5, couleur=ACCENT, epaisseur=2.3)
g2.point(0, -1, couleur=ACCENT, r=4.6)
g2.fleche(1.2, f(1.2) + 0.25, 0.35, f(0.35) + 0.22, couleur=ENCRE)
g2.texte(0.12, -1.28, "the only local minimum is global", couleur=ACCENT, taille=12, gras=True,
         fond=True, ancre="middle")
g2.texte(-1.75, 2.22, "convex: x² − cos x", couleur=ACCENT, taille=12.5, gras=True, fond=True)

sys.stdout.write(Planche([g1, g2], ecart=22,
                         titre="Walking downhill can stop in a trap, unless f is convex").svg())
