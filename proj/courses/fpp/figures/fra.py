#!/usr/bin/env python3
r"""
fra.svg — l'emprunt futur que le FRA verrouille, ses deux flux ramenés en t.

La fiche : $P(t,T)=P(t,S)e^{K(S-T)}$. On reçoit 1 en T, on rend $e^{K(S-T)}$ en S ;
chaque flux revient en t par le zéro-coupon de sa date. Le contrat ne coûte rien à la
signature, donc les deux valeurs en t sont égales : c'est la forme de la fiche, lue sur
le dessin.

Usage : python courses/fpp/figures/fra.py > fra.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

t, T, S = 2.4, 5.6, 8.6
g = Figure(xmin=0, xmax=10, ymin=-4.6, ymax=4.4, w=620, h=330, marges=(8, 8, 8, 8),
           titre="FRA : on reçoit 1 en T, on rend capital et intérêts en S")
g.axe_temps(0, 1.1, 9.7, [(t, "t"), (T, "T"), (S, "S")])

# on emprunte 1 en T
g.fleche(T, 0.45, T, 2.2, couleur=AJOUT, epaisseur=2)
g.texte(T, 1.3, "1", couleur=AJOUT, gras=True, taille=14, dx=10)
g.fleche(T - 0.2, 2.7, t + 0.8, 2.7, couleur=AJOUT, courbure=18)
g.texte(t, 2.6, "P(t,T)", couleur=AJOUT, gras=True, taille=13.5, ancre="middle")

# on rend capital et intérêts en S
g.fleche(S, -1.25, S, -3.0, couleur=ACCENT, epaisseur=2)
g.texte(S, -2.1, "e^{K(S−T)}", couleur=ACCENT, gras=True, taille=13.5, dx=10)
g.fleche(S - 0.2, -3.45, t + 1.75, -3.45, couleur=ACCENT, courbure=-20)
g.texte(t + 1.6, -3.35, "P(t,S)·e^{K(S−T)}", couleur=ACCENT, gras=True, taille=13.5,
        ancre="end")


sys.stdout.write(g.svg())
