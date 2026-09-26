#!/usr/bin/env python3
r"""
feynman-kac.svg — deux façons de boucher le même trou, et le même nombre au bout.

Ce que la figure doit faire voir : on connaît le paiement à l'échéance, F(x) = x², et la
façon dont X bouge, un mouvement brownien ; on cherche la valeur en t quand X vaut 0.
À gauche, par l'espérance : un éventail de trajectoires issues de (t, 0), chacune finit
en un point de la parabole des paiements, et la moyenne de ces paiements vaut 1, la
variance de X_T. À droite, par l'équation : partie de f(T, x) = x², la solution de
ℒf = 0 remonte le temps en se translatant, f(s, x) = x² + (T − s), et vaut 1 en (t, 0).

Une année entre t et T. Les trajectoires sont des ponts browniens tirés par un
générateur écrit ici, pour que la figure soit la même sur toute machine ; leurs points
d'arrivée sont les quantiles de la loi normale, et seule leur forme est illustrative.

Usage : python courses/fpp/figures/feynman-kac.py > feynman-kac.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, ENCRE, DOUX, PALE      # noqa: E402


def phi_inv(p):
    lo, hi = -8.0, 8.0
    for _ in range(80):
        m = (lo + hi) / 2
        if 0.5 * (1 + math.erf(m / math.sqrt(2))) < p:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


class Gen:
    """Un générateur congruentiel : le même tirage partout, quelle que soit la version
    de Python."""

    def __init__(self, graine):
        self.x = graine

    def u(self):
        self.x = (1664525 * self.x + 1013904223) % 2 ** 32
        return (self.x + 0.5) / 2 ** 32

    def gauss(self):
        return math.sqrt(-2 * math.log(self.u())) * math.cos(2 * math.pi * self.u())


NT, NP, C = 60, 11, 0.12          # pas de temps, trajectoires, échelle des paiements
gen = Gen(20260926)

# ---- à gauche : par l'espérance ----------------------------------------------
A = Figure(xmin=-0.62, xmax=1.72, ymin=-2.75, ymax=2.9, w=370, h=320,
           marges=(10, 26, 30, 10))
A.courbe([(0, -2.55), (0, 2.55)], couleur=DOUX, epaisseur=1.1)
A.courbe([(1, -2.55), (1, 2.55)], couleur=DOUX, epaisseur=1.1)
A.texte(0, -2.75, "t", couleur=DOUX, ancre="middle", dy=4)
A.texte(1, -2.75, "T", couleur=DOUX, ancre="middle", dy=4)
for k in range(NP):
    z = phi_inv((k + 0.5) / NP)
    w, pts = 0.0, []
    brut = [0.0]
    for i in range(NT):
        w += gen.gauss() / math.sqrt(NT)
        brut.append(w)
    for i in range(NT + 1):
        s = i / NT
        pts.append((s, brut[i] - s * brut[-1] + s * z))
    A.courbe(pts, couleur=PALE, epaisseur=1.1)
    A.segment(1, z, 1 + C * z * z, z, couleur=PALE)
    A.point(1 + C * z * z, z, couleur=ACCENT, r=2.8)
A.courbe([(1 + C * y * y, y) for y in [-2.5 + 5 * i / 100 for i in range(101)]],
         couleur=ACCENT, epaisseur=2.0)
A.texte(1.08, 2.62, "connu : F(x) = x²", couleur=ACCENT, taille=11.5, gras=True)
A.point(0, 0, couleur=ENCRE, r=4)
A.texte(-0.06, 0.25, "f(t, 0) = ?", ancre="end", taille=12, gras=True, dy=-4)
A.texte(0.5, 2.62, "par l'espérance", couleur=AJOUT, ancre="middle", taille=13, gras=True,
        dy=-14)
A.texte(0.72, -2.75, "moyenne des paiements : 1", couleur=ENCRE, ancre="middle",
        taille=12, gras=True, dy=22)

# ---- à droite : par l'équation -----------------------------------------------
B = Figure(xmin=-2.3, xmax=2.75, ymin=-0.6, ymax=5.6, w=330, h=320,
           marges=(10, 26, 30, 10))
B.courbe([(-2.2, 0), (2.2, 0)], couleur=DOUX, epaisseur=1.1)
B.texte(2.2, 0, "x", couleur=DOUX, ancre="end", dy=16)
B.fonction(lambda x: x * x + 0.5, -2.08, 2.08, couleur=PALE, epaisseur=1.3)
B.fonction(lambda x: x * x, -2.2, 2.2, couleur=ACCENT, epaisseur=2.0)
B.fonction(lambda x: x * x + 1, -1.97, 1.97, couleur=ENCRE, epaisseur=2.2)
B.fleche(1.62, 1.62 ** 2 + 0.06, 1.62, 1.62 ** 2 + 0.94, couleur=AJOUT, epaisseur=1.6)
B.texte(1.72, 2.05, "ℒf = 0", couleur=AJOUT, taille=12, gras=True)
B.texte(0, 3.7, "en T : x²", couleur=ACCENT, ancre="middle", taille=11.5, gras=True)
B.texte(0, 4.3, "en t : x² + 1", couleur=ENCRE, ancre="middle", taille=11.5, gras=True)
B.point(0, 1, couleur=ENCRE, r=4)
B.texte(0, 1.0, "f(t, 0) = 1", ancre="middle", taille=12, gras=True, dy=-12)
B.texte(0.2, 5.6, "par l'équation", couleur=AJOUT, ancre="middle", taille=13, gras=True,
        dy=-2)

p = Planche([A, B], signes=("=",), ecart=34,
            titre="La moyenne des paiements et la solution de l'équation donnent le même nombre")
sys.stdout.write(p.svg())
