#!/usr/bin/env python3
r"""
probabilite-risque-neutre.svg — deux états du monde en T, S_d et S_u. Sous la probabilité
historique P, la hausse a la probabilité p et la moyenne vaut E^P(S_T). Sous la probabilité
risque-neutre Q, elle a la probabilité q = (F − S_d) / (S_u − S_d), choisie pour que la
moyenne tombe sur le prix forward : E^Q(S_T) = F(0,T). Puis, sur un échéancier, cette
moyenne d'un paiement g(S_T), reçue en T, revient en 0 multipliée par P(0,T) : c'est le prix,
Price = P(0,T) E^Q(g(S_T)). Les deux égalités de la Forme, dans l'ordre.

Usage : python courses/fpp/figures/probabilite-risque-neutre.py > probabilite-risque-neutre.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
F = 100 / math.exp(-0.04)
Q = (F - 80) / (130 - 80)


def cadre(titre, p, moyenne, couleur, lab_bas, lab_haut, lab_moy):
    f = Figure(xmin=60, xmax=150, ymin=0, ymax=0.85, w=310, h=320, marges=(20, 30, 58, 10))
    f.axes(xlab="S(T)", xticks=(80, 130), fmt=lambda t: "")
    f.texte(80, 0, "S_{d}", couleur=DOUX, ancre="middle", dy=19, taille=12)
    f.texte(130, 0, "S_{u}", couleur=DOUX, ancre="middle", dy=19, taille=12)
    f.barre(80, 1 - p, 9, couleur=couleur, opacite=0.8)
    f.barre(130, p, 9, couleur=couleur, opacite=0.8)
    f.texte(80, 1 - p, lab_bas, ancre="middle", dy=-6, taille=12)
    f.texte(130, p, lab_haut, ancre="middle", dy=-6, taille=12)
    f.segment(moyenne, 0, moyenne, 0.78, couleur=ENCRE, pointilles="5 3", epaisseur=1.4)
    f.texte(moyenne, 0.78, lab_moy, ancre="middle", dy=-6, gras=True, taille=12)
    f.texte(105, 0.85, titre, ancre="middle", dy=-14, couleur=couleur, gras=True)
    return f


g = cadre("probabilité historique P", 0.6, 110, AJOUT, "1 − p", "p", "E^{P}(S_{T})")
d = cadre("probabilité risque-neutre Q", Q, F, ACCENT, "1 − q", "q", "E^{Q}(S_{T}) = F(0,T)")
d.texte(105, 0.0, "q = (F − S_{d}) / (S_{u} − S_{d})", couleur=ACCENT, ancre="middle", dy=38, taille=12)
# Troisième temps, la première égalité de la Forme : la moyenne sous Q, reçue en T,
# revient en 0 multipliée par le zéro-coupon, et c'est le prix.
e = Figure(xmin=-0.35, xmax=1.35, ymin=-0.2, ymax=0.85, w=250, h=320, marges=(10, 30, 58, 10))
e.axe_temps(0, -0.3, 1.3, [(0, "0"), (1, "T")])
e.fleche(1, 0.02, 1, 0.5, couleur=ACCENT, epaisseur=2.2)
e.texte(1, 0.5, "E^{Q}(g(S_{T}))", couleur=ACCENT, ancre="middle", dy=-8, gras=True, taille=12)
e.fleche(0.95, 0.62, 0.05, 0.62, couleur=DOUX, courbure=12, epaisseur=1.2)
e.texte(0.5, 0.62, "× P(0,T)", couleur=DOUX, ancre="middle", dy=-20, taille=12)
e.fleche(0, 0.02, 0, 0.4, couleur=ENCRE, epaisseur=2.2)
e.texte(0, 0.4, "prix de g(S_{T})", couleur=ENCRE, ancre="middle", dy=-8, gras=True, taille=12)
e.texte(0.5, -0.2, "Price = P(0,T) E^{Q}(g(S_{T}))", couleur=ENCRE, ancre="middle", dy=38,
        gras=True, taille=12)
e.texte(0.5, 0.85, "le prix", couleur=ENCRE, ancre="middle", dy=-14, gras=True)
sys.stdout.write(Planche([g, d, e], signes=("", "→"), ecart=30,
                 titre="Q choisit les poids pour que la moyenne tombe sur le prix forward ; "
                       "le prix est cette moyenne ramenée en 0").svg())
