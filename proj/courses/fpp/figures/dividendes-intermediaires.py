#!/usr/bin/env python3
r"""
dividendes-intermediaires.svg — le portage de l'action avec un dividende en T₁. Le
dividende, d₁ S_t / P(t,T₁), placé jusqu'à T, devient d₁ S_t / P(t,T) et rembourse d'autant
l'emprunt S_t / P(t,T) : le prix forward tombe à S_t / P(t,T) × (1 − d₁).

Usage : python courses/fpp/figures/dividendes-intermediaires.py > dividendes-intermediaires.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.35, xmax=2.55, ymin=-2.1, ymax=1.35, w=580, h=360, marges=(10, 10, 10, 10),
           titre="Le dividende touché en route allège le portage : F = S_t / P(t,T) × (1 − d₁)")
f.axe_temps(0, -0.2, 2.4, [(0, "t"), (0.9, "T₁ : dividende"), (1.8, "T")])
f.fleche(0.9, 0.1, 0.9, 0.55, couleur=ACCENT, epaisseur=2)
f.texte(0.9, 0.35, "+ d_{1} S_{t} / P(t,T_{1})", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.fleche(0.95, 0.7, 1.72, 0.7, couleur=ACCENT, courbure=14, epaisseur=1.4)
f.texte(1.33, 0.7, "placé jusqu'à T : × P(t,T_{1}) / P(t,T)", couleur=ACCENT, ancre="middle", dy=-24, taille=12)
f.fleche(1.72, 0.1, 1.72, 0.58, couleur=ACCENT, epaisseur=2)
f.texte(1.72, 0.35, "d_{1} S_{t} / P(t,T)", couleur=ACCENT, dx=8, taille=12)
f.fleche(1.88, -0.45, 1.88, -1.6, couleur=AJOUT, epaisseur=2.4)
f.texte(1.88, -1.0, "− S_{t} / P(t,T) :", couleur=AJOUT, dx=8, gras=True)
f.texte(1.88, -1.0, "l'emprunt qui a", couleur=AJOUT, dx=8, dy=17, taille=12)
f.texte(1.88, -1.0, "payé l'action", couleur=AJOUT, dx=8, dy=32, taille=12)
f.texte(0.7, -1.3, "reste à couvrir en T, le prix forward :", couleur=ENCRE, ancre="middle", taille=12.5)
f.texte(0.7, -1.3, "S_{t} / P(t,T) − d_{1} S_{t} / P(t,T) = S_{t} / P(t,T) × (1 − d_{1})", couleur=ENCRE, ancre="middle", dy=20, gras=True, taille=12.5)
sys.stdout.write(f.svg())
