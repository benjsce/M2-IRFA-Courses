#!/usr/bin/env python3
r"""
taux-forward.svg — le FRA ramené en t, en trois étapes numérotées.

① La jambe variable : recevoir en S l'intérêt au taux R(T,S), c'est exactement ce que
   donne 1 reçu en T et placé de T à S au taux du moment. Elle vaut donc 1 en T.
② Chaque jambe revient en t par son zéro-coupon : 1 en T vaut P(t,T) = 0,9608 ;
   e^{K(S−T)} payé en S vaut P(t,S)·e^{K} = 0,9048·e^{K}.
③ Le contrat ne coûte rien : 0,9608 = 0,9048·e^{K}, donc K = 6 %.
Courbe du cours : 4 % à un an, 5 % à deux ans ; T = t + 1, S = t + 2.

Usage : python courses/fpp/figures/taux-forward.py > taux-forward.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

f = Figure(xmin=-1.25, xmax=3.05, ymin=-2.45, ymax=2.45, w=660, h=470, marges=(10, 10, 10, 10),
           titre="Taux forward : chaque jambe du FRA ramenée en t, puis égalées parce que le contrat est gratuit")
f.axe_temps(0, -0.05, 2.9, [(0, "t"), (1, "T = t + 1"), (2, "S = t + 2")])
f.texte(-1.2, 1.9, "on reçoit", couleur=ACCENT, gras=True, taille=12)
f.texte(-1.2, -1.95, "on paie", couleur=AJOUT, gras=True, taille=12)

# ① la jambe variable équivaut à 1 en T
f.fleche(1, 0.12, 1, 0.85, couleur=ACCENT, epaisseur=2.2)
f.texte(1, 0.45, "1", couleur=ACCENT, dx=8, gras=True)
f.fleche(1.06, 0.95, 1.96, 0.95, couleur=ACCENT, courbure=12, epaisseur=1.4)
f.fleche(2, 0.12, 2, 0.85, couleur=ACCENT, epaisseur=2.2, pointilles="5 4")
f.texte(2, 0.62, "e^{R(T,S)(S−T)}", couleur=ACCENT, dx=8, gras=True)
f.texte(2, 0.62, "inconnu aujourd'hui", couleur=ACCENT, dx=8, dy=16, taille=11.5)
f.texte(1.5, 0.95, "① 1 placé de T à S au taux du moment", couleur=ACCENT, ancre="middle", dy=-30, taille=12)
f.texte(1.5, 0.95, "donne exactement ce montant", couleur=ACCENT, ancre="middle", dy=-15, taille=12)

# ② chaque jambe revient en t
f.fleche(0.95, 1.05, 0.12, 1.55, couleur=ACCENT, courbure=26, epaisseur=1.8)
f.texte(0.55, 1.55, "② × P(t,T)", couleur=ACCENT, ancre="middle", dy=-26, gras=True, taille=12)
f.texte(0, 1.55, "0,9608", couleur=ACCENT, ancre="end", dx=-8, dy=5, gras=True)

f.fleche(2, -0.45, 2, -1.15, couleur=AJOUT, epaisseur=2.2)
f.texte(2, -0.75, "e^{K(S−T)}", couleur=AJOUT, dx=8, gras=True)
f.texte(2, -0.75, "fixé aujourd'hui", couleur=AJOUT, dx=8, dy=16, taille=11.5)
f.fleche(1.95, -1.3, 0.12, -1.55, couleur=AJOUT, courbure=-30, epaisseur=1.8)
f.texte(1.2, -1.45, "② × P(t,S)", couleur=AJOUT, ancre="middle", gras=True, taille=12)
f.texte(0, -1.55, "0,9048 × e^{K}", couleur=AJOUT, ancre="end", dx=-8, dy=5, gras=True)

# ③ les deux valeurs sont égales
f.courbe([(-0.4, 1.3), (-0.4, 0.4)], couleur=ENCRE, epaisseur=1.4)
f.courbe([(-0.4, -0.45), (-0.4, -1.3)], couleur=ENCRE, epaisseur=1.4)
f.texte(-0.4, 0.0, "③ égales :", couleur=ENCRE, ancre="middle", dy=-3, gras=True, taille=13)
f.texte(-0.4, 0.0, "le contrat est gratuit", couleur=DOUX, ancre="middle", dy=13, taille=11)
f.texte(0.85, -2.33, "0,9608 = 0,9048 × e^{K}, d'où K = F(t,T,S) = ln(0,9608 / 0,9048) = 6 %",
        couleur=ENCRE, ancre="middle", gras=True, taille=12.5)
sys.stdout.write(f.svg())
