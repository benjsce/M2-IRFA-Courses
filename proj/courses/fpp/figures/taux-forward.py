#!/usr/bin/env python3
r"""
taux-forward.svg — le FRA ramené en t. La jambe fixe paie e^{K(S−T)} en S, fixé
aujourd'hui, qui vaut P(t,S)·e^{K(S−T)} en t. La jambe variable reçoit e^{R(T,S)(S−T)}
en S, qui vaut 1 en T quel que soit le taux, donc P(t,T) en t. Le contrat ne coûtant rien,
les deux valeurs sont égales, et K est le taux forward : 6 % avec la courbe du cours.

Usage : python courses/fpp/figures/taux-forward.py > taux-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-1.0, xmax=2.95, ymin=-2.0, ymax=2.0, w=600, h=400, marges=(10, 10, 10, 10),
           titre="P(t,T) = P(t,S)·e^{K(S−T)} : le FRA ne coûte rien, K est le taux forward")
f.axe_temps(0, -0.6, 2.8, [(0, "t"), (1, "T"), (2, "S")])
# jambe variable, en haut
f.fleche(2, 0.1, 2, 1.0, couleur=ACCENT, epaisseur=2, pointilles="5 4")
f.texte(2, 0.8, "e^{R(T,S)(S−T)}", couleur=ACCENT, dx=10, gras=True)
f.texte(2, 0.52, "inconnu aujourd'hui", couleur=ACCENT, dx=10, taille=12)
f.fleche(1.95, 1.15, 1.06, 1.15, couleur=ACCENT, courbure=14, pointilles="5 4")
f.point(1, 1.15, couleur=ACCENT)
f.texte(1, 1.15, "vaut 1 en T,", couleur=ACCENT, ancre="end", dx=-8, dy=-4, taille=12)
f.texte(1, 1.15, "quel que soit R(T,S)", couleur=ACCENT, ancre="end", dx=-8, dy=11, taille=12)
f.fleche(0.95, 1.62, 0.45, 1.62, couleur=ACCENT, courbure=10)
f.texte(0, 1.62, "P(t,T)", couleur=ACCENT, ancre="middle", dy=4, gras=True)
# jambe fixe, en bas
f.fleche(2, -0.42, 2, -1.25, couleur=AJOUT, epaisseur=2.2)
f.texte(2, -0.7, "e^{K(S−T)}", couleur=AJOUT, dx=10, gras=True)
f.texte(2, -0.98, "fixé aujourd'hui", couleur=AJOUT, dx=10, taille=12)
f.fleche(2, -1.45, 0.65, -1.45, couleur=AJOUT, courbure=-22)
f.texte(0, -1.45, "P(t,S)·e^{K(S−T)}", couleur=AJOUT, ancre="middle", dy=4, gras=True)
# égalité, dans la colonne de t
f.courbe([(0, 1.42), (0, 0.3)], couleur=DOUX, epaisseur=1.3)
f.courbe([(0, -0.45), (0, -1.22)], couleur=DOUX, epaisseur=1.3)
f.texte(0, 0.95, "égales :", couleur=ENCRE, ancre="end", dx=-8, dy=-2, gras=True)
f.texte(0, 0.95, "le contrat", couleur=DOUX, ancre="end", dx=-8, dy=14, taille=12)
f.texte(0, 0.95, "ne coûte rien", couleur=DOUX, ancre="end", dx=-8, dy=29, taille=12)
f.texte(0, -0.85, "0,9608 = 0,9048·e^{K}", couleur=DOUX, ancre="end", dx=-8, taille=12)
f.texte(1.0, -1.9, "K = F(t,T,S) = ln(0,9608 / 0,9048) = 6 %", couleur=ENCRE, ancre="middle", gras=True)
sys.stdout.write(f.svg())
