#!/usr/bin/env python3
r"""
volatilite.svg — même moyenne, écarts différents.

Ce que la figure doit faire voir : la volatilité ne dit pas combien un titre rapporte,
mais de combien son rendement s'écarte de sa moyenne. Deux titres rapportent en moyenne
5 % par an ; chaque année, l'un rapporte 5 % ± 10 points, l'autre 5 % ± 20 points, à
parts égales. Leurs écarts types, 10 % et 20 %, sont la demi-largeur de chaque ligne.

Usage : python courses/fpp/figures/volatilite.py > volatilite.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

MOY = 5.0


def ecart_type(valeurs):
    m = sum(valeurs) / len(valeurs)
    return math.sqrt(sum((v - m) ** 2 for v in valeurs) / len(valeurs))


lignes = [(2.2, 10.0, AJOUT), (0.9, 20.0, ACCENT)]     # (hauteur, écart, couleur)
g = Figure(xmin=-22, xmax=46, ymin=-0.35, ymax=3.25, w=640, h=250, marges=(8, 8, 8, 8),
           titre="Même moyenne, écarts différents : la volatilité mesure l'écart")

g.courbe([(MOY, -0.1), (MOY, 2.85)], couleur=PALE, epaisseur=1.2)
g.texte(MOY, 2.85, "moyenne 5 %", couleur=DOUX, taille=12, ancre="middle", dy=-6)

for y, s, c in lignes:
    bas, haut = MOY - s, MOY + s
    sd = ecart_type([bas, haut])                        # vaut s : rien n'est écrit en dur
    g.courbe([(bas, y), (haut, y)], couleur=c, epaisseur=1.4, pointilles="4 3")
    g.point(bas, y, couleur=c, r=5)
    g.point(haut, y, couleur=c, r=5)
    g.texte(bas, y, ("%+.0f %%" % bas).replace("-", "−"), couleur=c, taille=12.5, ancre="middle", dy=-11)
    g.texte(haut, y, "%+.0f %%" % haut, couleur=c, taille=12.5, ancre="middle", dy=-11)
    g.texte((MOY + haut) / 2, y, "écart %.0f" % sd, couleur=c, taille=11.5,
            ancre="middle", dy=17)
    g.texte(haut, y, "volatilité %.0f %%" % sd, couleur=c, gras=True, taille=13, dx=14, dy=4)

g.courbe([(-22, -0.1), (46, -0.1)], couleur=DOUX, epaisseur=1.2)
g.texte(46, -0.1, "rendement de l'année, en %", couleur=DOUX, taille=11.5, ancre="end",
        dy=16)

sys.stdout.write(g.svg())
