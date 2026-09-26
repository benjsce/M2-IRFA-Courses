#!/usr/bin/env python3
r"""
fonction-d-activation.svg — le seuil du perceptron, puis la sigmoïde.

La fiche : le passage du seuil à une fonction non linéaire dérivable a rendu possible
l'apprentissage multicouche. À gauche, le seuil saute de 0 à 1 en zéro : sa pente est
nulle partout ailleurs, et l'on ne peut rien en dériver. À droite, la sigmoïde
$1/(1+e^{-a})$ passe continûment de 0 à 1, et sa pente existe partout ; elle vaut
$o(1-o)$, le facteur de la rétropropagation.

Usage : python courses/dss/figures/fonction-d-activation.py > fonction-d-activation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402


def cadre(titre, trace, couleur):
    g = Figure(xmin=-6, xmax=6, ymin=-0.1, ymax=1.2, w=270, h=240, marges=(30, 30, 36, 10))
    g.axes(xlab="a", xticks=(0,), yticks=(0.5, 1), fmt=lambda t: "0",
           fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(0, 0))
    trace(g, couleur)
    g.texte(0, 1.2, titre, couleur=couleur, ancre="middle", dy=-10, gras=True)
    return g


def seuil(g, c):
    g.courbe([(-6, 0), (0, 0)], couleur=c, epaisseur=2.6)
    g.courbe([(0, 1), (6, 1)], couleur=c, epaisseur=2.6)
    g.courbe([(0, 0), (0, 1)], couleur=c, epaisseur=1.2, pointilles="3 3")


def sigmoide(g, c):
    s = lambda a: 1 / (1 + math.exp(-a))
    g.fonction(s, -6, 6, n=200, couleur=c, epaisseur=2.6)
    g.fonction(lambda a: 0.5 + 0.25 * a, -1.6, 1.6, couleur=AJOUT, epaisseur=1.4)
    g.texte(1.6, 0.9, "pente o(1 − o)", couleur=AJOUT, dx=4, taille=11)


p = Planche([cadre("seuil : un saut", seuil, DOUX), cadre("sigmoïde : dérivable", sigmoide, ACCENT)],
            signes=("→",), ecart=34,
            titre="Remplacer le saut par une pente : c'est ce qui permet de dériver l'erreur")
sys.stdout.write(p.svg())
