#!/usr/bin/env python3
r"""
compte-capitalise.svg — deux façons d'aller d'aujourd'hui à dans un an. En haut, un seul
zéro-coupon, P(t, t+1) = 0,9608, connu. En bas, deux placements de six mois : le premier,
P(t, t+½) = 0,9802, est connu ; le second ne le sera que dans six mois.

Usage : python courses/fpp/figures/compte-capitalise.py > compte-capitalise.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.35, xmax=2.3, ymin=-1.6, ymax=2.35, w=560, h=340, marges=(10, 10, 10, 10),
           titre="Le zéro-coupon fixe le trajet d'avance ; le compte capitalisé le découvre pas à pas")
f.axe_temps(1.3, -0.1, 2.2, [(0, "t₀"), (1, "t₁"), (2, "t₂")])
f.fleche(1.95, 1.55, 0.05, 1.55, couleur=ACCENT, courbure=26)
f.texte(1.0, 1.55, "P(t_{0},t_{2}) : connu aujourd'hui", couleur=ACCENT, ancre="middle", dy=-44, gras=True)
f.axe_temps(-0.5, -0.1, 2.2, [(0, "t₀"), (1, "t₁"), (2, "t₂")])
f.fleche(1.95, -0.25, 1.05, -0.25, couleur=AJOUT, courbure=16, pointilles="5 4")
f.fleche(0.95, -0.25, 0.05, -0.25, couleur=ACCENT, courbure=16)
f.texte(1.5, -0.25, "P(t_{1},t_{2}) : inconnu en t_{0}", couleur=AJOUT, ancre="middle", dy=-30, taille=12, gras=True)
f.texte(0.5, -0.25, "P(t_{0},t_{1}) : connu", couleur=ACCENT, ancre="middle", dy=-30, taille=12, gras=True)
f.texte(1.0, -1.45, "B(t_{0},t_{2}) = P(t_{0},t_{1}) × P(t_{1},t_{2})", couleur=ENCRE, ancre="middle", taille=12.5)
sys.stdout.write(f.svg())
