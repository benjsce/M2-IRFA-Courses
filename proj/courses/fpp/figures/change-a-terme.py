#!/usr/bin/env python3
r"""
change-a-terme.svg — le contrat de change à terme sur deux lignes : la devise étrangère
(le dollar) en haut, la locale (l'euro) en bas. On paie 1 euro en T et on reçoit K dollars
en T. Chaque flux revient en t par le zéro-coupon de sa propre devise ; les dollars
passent en euros au change du jour. Le contrat ne coûte rien : K·P^f(t,T)/X_t = P(t,T).
Avec X_t = 1,10, 4 % sur l'euro et 5 % sur le dollar : K = 1,1111.

Usage : python courses/fpp/figures/change-a-terme.py > change-a-terme.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-1.35, xmax=2.3, ymin=-2.0, ymax=2.0, w=600, h=400, marges=(10, 10, 10, 10),
           titre="K·P^{f}(t,T) / X_t = P(t,T) : le contrat de change à terme ne coûte rien")
f.axe_temps(0, -0.4, 2.2, [(0, "t"), (1.6, "T")])
f.texte(-1.25, 1.2, "$", couleur=ACCENT, taille=18, gras=True)
f.texte(-1.25, 0.85, "étrangère", couleur=DOUX, taille=12)
f.texte(-1.25, -1.15, "€", couleur=AJOUT, taille=18, gras=True)
f.texte(-1.25, -1.5, "locale", couleur=DOUX, taille=12)
# jambe étrangère : on reçoit K dollars
f.fleche(1.6, 0.12, 1.6, 1.0, couleur=ACCENT, epaisseur=2, pointilles="5 4")
f.texte(1.6, 0.75, "K", couleur=ACCENT, dx=10, gras=True)
f.texte(1.6, 0.45, "cherché", couleur=ACCENT, dx=10, taille=12)
f.fleche(1.55, 1.25, 0.45, 1.25, couleur=ACCENT, courbure=18)
f.texte(1.0, 1.25, "actualisé au taux étranger", couleur=DOUX, ancre="middle", dy=-30, taille=11.5)
f.texte(0.0, 1.25, "K·P^{f}(t,T)", couleur=ACCENT, ancre="middle", dy=4, gras=True)
# passage au comptant, en deux morceaux pour laisser lire la date
f.courbe([(0.0, 1.02), (0.0, 0.3)], couleur=DOUX, epaisseur=1.3, pointilles="4 3")
f.fleche(0.0, -0.45, 0.0, -1.05, couleur=DOUX, epaisseur=1.3, pointilles="4 3")
f.texte(0.0, 0.65, "÷ X_{t} au comptant", couleur=DOUX, dx=8, taille=12)
# jambe locale : on paie 1 euro
f.fleche(1.6, -0.42, 1.6, -1.05, couleur=AJOUT, epaisseur=2.2)
f.texte(1.6, -0.75, "1", couleur=AJOUT, dx=10, gras=True)
f.fleche(1.55, -1.3, 0.75, -1.3, couleur=AJOUT, courbure=-16)
f.texte(1.15, -1.3, "actualisé au taux local", couleur=DOUX, ancre="middle", dy=34, taille=11.5)
f.texte(0.0, -1.3, "K·P^{f}(t,T) / X_{t} = P(t,T)", couleur=AJOUT, ancre="middle", dy=4, gras=True)
f.texte(0.0, -1.88, "1,10 × 0,9608 / 0,9512 = 1,1111", couleur=ENCRE, ancre="middle", taille=12.5)
sys.stdout.write(f.svg())
