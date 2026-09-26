#!/usr/bin/env python3
r"""
valeur-actuelle-nette.svg — un titre qui paie 5 dans un an et 105 dans deux ans : chaque
flux revient en t par son zéro-coupon, 5 × 0,9608 = 4,80 et 105 × 0,9048 = 95,01 ; leur
somme, 99,81, est la valeur actuelle nette.

Usage : python courses/fpp/figures/valeur-actuelle-nette.py > valeur-actuelle-nette.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.75, xmax=2.35, ymin=-0.35, ymax=2.1, w=560, h=300, marges=(10, 10, 10, 10),
           titre="Valeur actuelle nette : 4,80 + 95,01 = 99,81")
f.axe_temps(0, -0.1, 2.3, [(0, "t"), (1, "t + 1"), (2, "t + 2")])
f.fleche(1, 0.08, 1, 0.45, couleur=AJOUT, epaisseur=2)
f.texte(1, 0.3, "5", couleur=AJOUT, dx=8, gras=True)
f.fleche(2, 0.08, 2, 1.25, couleur=AJOUT, epaisseur=2.4)
f.texte(2, 0.7, "105", couleur=AJOUT, dx=8, gras=True)
f.fleche(1, 0.6, 0.12, 0.62, couleur=ACCENT, courbure=12)
f.fleche(2, 1.4, 0.12, 1.2, couleur=ACCENT, courbure=30)
f.texte(0, 0.62, "4,80", couleur=ACCENT, ancre="end", dx=-6, dy=4, gras=True)
f.texte(0, 1.2, "95,01", couleur=ACCENT, ancre="end", dx=-6, dy=4, gras=True)
f.texte(0, 1.75, "NPV = 99,81", couleur=ENCRE, ancre="end", dx=-6, dy=4, gras=True)
f.segment(0, 0.08, 0, 1.7)
f.texte(1.55, 0.95, "× 0,9048", couleur=DOUX, taille=11.5, ancre="middle", dy=-28)
f.texte(0.55, 0.62, "× 0,9608", couleur=DOUX, taille=11.5, ancre="middle", dy=-16)
sys.stdout.write(f.svg())
