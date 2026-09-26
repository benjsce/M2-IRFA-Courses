#!/usr/bin/env python3
r"""
dividendes-intermediaires.svg — le portage de l'action avec un dividende de 2 % de la
valeur forward dans six mois. Le dividende, 2 % × 102,02 = 2,04, placé jusqu'à l'échéance,
devient 2,04 × 0,9802 / 0,9608 = 2,08 et rembourse d'autant l'emprunt de 104,08 : le prix
forward tombe à 102,00.

Usage : python courses/fpp/figures/dividendes-intermediaires.py > dividendes-intermediaires.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.35, xmax=2.55, ymin=-1.95, ymax=1.35, w=560, h=340, marges=(10, 10, 10, 10),
           titre="Le dividende touché en route allège le portage : 104,08 − 2,08 = 102,00")
f.axe_temps(0, -0.2, 2.4, [(0, "t"), (0.9, "t + ½ : dividende"), (1.8, "T")])
f.fleche(0.9, 0.1, 0.9, 0.55, couleur=ACCENT, epaisseur=2)
f.texte(0.9, 0.35, "+2,04", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.fleche(0.95, 0.7, 1.72, 0.7, couleur=ACCENT, courbure=14, epaisseur=1.4)
f.texte(1.33, 0.7, "placé six mois : 2,08", couleur=ACCENT, ancre="middle", dy=-24, taille=12)
f.fleche(1.72, 0.1, 1.72, 0.58, couleur=ACCENT, epaisseur=2)
f.fleche(1.88, -0.45, 1.88, -1.6, couleur=AJOUT, epaisseur=2.4)
f.texte(1.88, -1.0, "−104,08 : l'emprunt", couleur=AJOUT, dx=8, gras=True)
f.texte(1.88, -1.28, "qui a payé l'action", couleur=AJOUT, dx=8, taille=12)
f.texte(0.6, -1.25, "reste à couvrir en T :", couleur=ENCRE, ancre="middle", taille=12.5)
f.texte(0.6, -1.25, "104,08 − 2,08 = 102,00", couleur=ENCRE, ancre="middle", dy=18, gras=True)
f.texte(0.6, -1.25, "le prix forward", couleur=DOUX, ancre="middle", dy=35, taille=12)
sys.stdout.write(f.svg())
