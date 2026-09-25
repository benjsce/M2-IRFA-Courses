#!/usr/bin/env python3
r"""
facteur-actualisation.svg — un euro qui recule, un euro qui avance.

La fiche dit qu'on capitalise en avançant dans le temps et qu'on actualise en reculant,
et que le facteur est le taux de change entre deux dates. Au-dessus de l'axe, un euro
payé en T revient en t et y vaut P(t,T) ; au-dessous, un euro placé en t arrive en T
et y vaut 1/P(t,T), c'est-à-dire $C_t$ par la forme $P=C_t^{-1}$. Même facteur, lu
dans les deux sens.

Usage : python courses/fpp/figures/facteur-actualisation.py > facteur-actualisation.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T = 2.6, 8.2
g = Figure(xmin=0, xmax=10, ymin=-4.4, ymax=4.4, w=620, h=320, marges=(8, 8, 8, 8),
           titre="Actualiser recule d'un facteur P(t,T), capitaliser avance du même")
g.axe_temps(0, 1.2, 9.7, [(t, "t"), (T, "T")])

# actualiser : 1 payé en T vaut P(t,T) en t
g.texte(0.05, 3.3, "actualiser", taille=12, gras=True, couleur=ACCENT)
g.fleche(T, 0.45, T, 2.3, couleur=ACCENT, epaisseur=2)
g.texte(T, 1.4, "1", couleur=ACCENT, gras=True, taille=14, dx=10)
g.fleche(T - 0.25, 2.8, t + 0.75, 2.8, couleur=ACCENT, courbure=22)
g.texte(t, 2.7, "P(t,T)", couleur=ACCENT, gras=True, taille=13.5, ancre="middle")
g.texte((t + T) / 2, 3.95, "× P(t,T)", couleur=ENCRE, taille=12.5, ancre="middle")

# capitaliser : 1 placé en t vaut 1/P(t,T) en T
g.texte(0.05, -3.5, "capitaliser", taille=12, gras=True, couleur=AJOUT)
g.fleche(t, -1.2, t, -2.9, couleur=AJOUT, epaisseur=2)
g.texte(t, -2.1, "1", couleur=AJOUT, gras=True, taille=14, dx=10)
g.fleche(t + 0.35, -3.3, T - 0.95, -3.3, couleur=AJOUT, courbure=-20)
g.texte(T, -3.2, "1 / P(t,T)", couleur=AJOUT, gras=True, taille=13.5, ancre="middle")
g.texte((t + T) / 2, -4.25, "÷ P(t,T)", couleur=ENCRE, taille=12.5, ancre="middle")

sys.stdout.write(g.svg())
