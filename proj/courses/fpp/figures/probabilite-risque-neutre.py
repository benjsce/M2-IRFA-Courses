#!/usr/bin/env python3
r"""
probabilite-risque-neutre.svg — deux états du monde dans un an, l'action à 80 ou à 130.
Sous la probabilité historique (hausse 60 %), la moyenne vaut 110. Sous la probabilité
risque-neutre, la hausse a q = (104,08 − 80)/(130 − 80) ≈ 48 % de chances : la moyenne
tombe sur le prix forward, 104,08.

Usage : python courses/fpp/figures/probabilite-risque-neutre.py > probabilite-risque-neutre.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

F = 100 / math.exp(-0.04)
Q = (F - 80) / (130 - 80)


def cadre(titre, p, moyenne, couleur, etiquette):
    f = Figure(xmin=60, xmax=150, ymin=0, ymax=0.85, w=300, h=300, marges=(40, 30, 40, 10))
    f.axes(xlab="action dans un an", xticks=(80, 130), yticks=(0.2, 0.4, 0.6),
           fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d %%" % round(100 * t))
    f.barre(80, 1 - p, 9, couleur=couleur, opacite=0.8)
    f.barre(130, p, 9, couleur=couleur, opacite=0.8)
    f.texte(80, 1 - p, "%d %%" % round(100 * (1 - p)), ancre="middle", dy=-6, taille=12)
    f.texte(130, p, "%d %%" % round(100 * p), ancre="middle", dy=-6, taille=12)
    f.segment(moyenne, 0, moyenne, 0.78, couleur=ENCRE, pointilles="5 3", epaisseur=1.4)
    f.texte(moyenne, 0.78, etiquette, ancre="middle", dy=-6, gras=True, taille=12)
    f.texte(105, 0.85, titre, ancre="middle", dy=-14, couleur=couleur, gras=True)
    return f


gauche = cadre("probabilité historique P", 0.6, 110, AJOUT, "moyenne 110")
droite = cadre("probabilité risque-neutre Q", Q, F, ACCENT, "moyenne 104,08 = F")
sys.stdout.write(Planche([gauche, droite], ecart=30,
                 titre="Q choisit les poids pour que la moyenne tombe sur le prix forward").svg())
