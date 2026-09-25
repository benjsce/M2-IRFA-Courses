#!/usr/bin/env python3
r"""
produit-a-capital-protege.svg — la mise coupée en deux : un zéro-coupon, des calls.

La fiche : placer $KP(t,T)$ en zéro-coupon garantit K en T ; le solde achète des calls,
qui donnent la hausse. Deux lignes, une par brique, sur le même axe du temps. La
hausse est en pointillé : elle est aléatoire, et peut être nulle. Aucun strike n'est
écrit pour les calls, la fiche n'en fixe pas.

Usage : python courses/fpp/figures/produit-a-capital-protege.py > produit-a-capital-protege.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T = 3.2, 8.0
g = Figure(xmin=0, xmax=10, ymin=-4.3, ymax=4.5, w=640, h=330, marges=(8, 8, 8, 8),
           titre="Capital protégé : un zéro-coupon rend la mise, le solde achète la hausse")

for y0, nom, coul in ((1.9, "zéro-coupon", ACCENT), (-2.6, "calls", AJOUT)):
    g.axe_temps(y0, 1.3, 9.7, [(t, "t"), (T, "T")])
    g.texte(0.05, y0 + 0.15, nom, taille=12, gras=True, couleur=coul)

# zéro-coupon : KP(t,T) payé, K reçu
g.fleche(t, 1.45, t, 0.25, couleur=ACCENT, epaisseur=2)
g.texte(t, 0.7, "K·P(t,T)", couleur=ACCENT, gras=True, taille=13.5, dx=9)
g.fleche(T, 2.35, T, 3.85, couleur=ACCENT, epaisseur=2)
g.texte(T, 3.0, "K : la mise rendue", couleur=ACCENT, gras=True, taille=13.5, dx=9)

# calls : le solde payé, la hausse reçue
g.fleche(t, -3.05, t, -4.2, couleur=AJOUT, epaisseur=2)
g.texte(t, -3.75, "K − K·P(t,T) : le solde", couleur=AJOUT, gras=True, taille=13.5, dx=9)
g.fleche(T, -2.15, T, -0.7, couleur=AJOUT, epaisseur=2, pointilles="5 4")
g.texte(T, -1.45, "la hausse, ou rien", couleur=AJOUT, gras=True, taille=13.5, dx=9)

sys.stdout.write(g.svg())
