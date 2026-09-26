#!/usr/bin/env python3
r"""
valeur-actuelle-nette.svg — un titre qui paie X₁ en t₁ et X₂ en t₂ : chaque flux revient
en t multiplié par le zéro-coupon de sa date ; leur somme est la valeur actuelle nette,
NPV(t) = P(t,t₁)X₁ + P(t,t₂)X₂.

Usage : python courses/fpp/figures/valeur-actuelle-nette.py > valeur-actuelle-nette.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-1.05, xmax=2.35, ymin=-0.35, ymax=2.1, w=580, h=300, marges=(10, 10, 10, 10),
           titre="NPV(t) = Σ P(t,t_i) X_i : chaque flux ramené en t par son zéro-coupon, puis la somme")
f.axe_temps(0, -0.1, 2.3, [(0, "t"), (1, "t₁"), (2, "t₂")])
f.fleche(1, 0.08, 1, 0.45, couleur=AJOUT, epaisseur=2)
f.texte(1, 0.3, "X_{1}", couleur=AJOUT, dx=8, gras=True)
f.fleche(2, 0.08, 2, 1.25, couleur=AJOUT, epaisseur=2.4)
f.texte(2, 0.7, "X_{2}", couleur=AJOUT, dx=8, gras=True)
f.fleche(1, 0.6, 0.12, 0.62, couleur=ACCENT, courbure=12)
f.fleche(2, 1.4, 0.12, 1.2, couleur=ACCENT, courbure=30)
f.texte(0, 0.62, "P(t,t_{1}) X_{1}", couleur=ACCENT, ancre="end", dx=-6, dy=4, gras=True)
f.texte(0, 1.2, "P(t,t_{2}) X_{2}", couleur=ACCENT, ancre="end", dx=-6, dy=4, gras=True)
f.texte(-1.0, 1.95, "NPV(t) = P(t,t_{1}) X_{1} + P(t,t_{2}) X_{2}", couleur=ENCRE, dy=4, gras=True)
f.segment(0, 0.08, 0, 1.4)
f.texte(1.55, 0.95, "× P(t,t_{2})", couleur=DOUX, taille=11.5, ancre="middle", dy=-28)
f.texte(0.55, 0.62, "× P(t,t_{1})", couleur=DOUX, taille=11.5, ancre="middle", dy=-16)
sys.stdout.write(f.svg())
