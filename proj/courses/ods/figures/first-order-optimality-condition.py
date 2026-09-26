#!/usr/bin/env python3
r"""
first-order-optimality-condition.svg — flat in every direction, or rising in every allowed one.

Ce que la figure doit faire voir : sans contrainte, le minimiseur est là où la tangente
est plate ; sur un intervalle, la pente peut ne pas s'annuler au minimiseur, pourvu
qu'elle monte dans toutes les directions permises.

Gauche : f(x) = x² − cos x, tangente plate en x* = 0. Droite : l'exemple des notes,
f(x) = x sur [0, 1] : le minimiseur est 0, où f'(0) = 1 ; la seule direction qui
descend, vers la gauche, sort du domaine.

Usage : python courses/ods/figures/first-order-optimality-condition.py > first-order-optimality-condition.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = lambda x: x * x - math.cos(x)
g1 = Figure(xmin=-1.8, xmax=1.8, ymin=-1.5, ymax=2.0, w=300, h=240, marges=(8, 8, 8, 8))
g1.axes(croix=(0, 0))
g1.fonction(f, -1.62, 1.62, couleur=ACCENT, epaisseur=2.3)
g1.courbe([(-1.2, -1), (1.2, -1)], couleur=AJOUT, epaisseur=2)
g1.point(0, -1, couleur=ACCENT, r=4.6)
g1.texte(0.1, -1.35, "∇f(x*) = 0 at x* = 0", couleur=AJOUT, taille=12, gras=True, fond=True,
         ancre="middle")
g1.texte(-1.75, 1.82, "unconstrained", couleur=ENCRE, taille=12.5, gras=True)

g2 = Figure(xmin=-0.6, xmax=1.6, ymin=-0.5, ymax=1.5, w=300, h=240, marges=(8, 8, 8, 8))
g2.axes(croix=(0, 0))
g2.fonction(lambda x: x, -0.5, 1.5, couleur=PALE, epaisseur=1.4)
g2.fonction(lambda x: x, 0, 1, couleur=ACCENT, epaisseur=3)
g2.point(0, 0, couleur=ACCENT, r=4.6)
g2.point(1, 1, couleur=ACCENT, r=3)
g2.fleche(0.05, 0.1, 0.45, 0.1, couleur=ENCRE)
g2.texte(0.5, 0.05, "allowed: f goes up", couleur=ENCRE, taille=11.5)
g2.fleche(-0.05, -0.25, -0.45, -0.25, couleur=AJOUT)
g2.texte(-0.05, -0.43, "f goes down, but leaves [0, 1]", couleur=AJOUT, taille=11.5, fond=True)
g2.texte(-0.55, 1.35, "on [0, 1]: f(x) = x, f′(0) = 1", couleur=ENCRE, taille=12.5, gras=True, fond=True)
sys.stdout.write(Planche([g1, g2], ecart=22,
                         titre="At a minimizer, no allowed direction goes downhill").svg())
