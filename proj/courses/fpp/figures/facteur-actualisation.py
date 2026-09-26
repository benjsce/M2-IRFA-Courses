#!/usr/bin/env python3
r"""
facteur-actualisation.svg — ce qu'il faut placer en t pour avoir un euro en T.

Ce que la figure doit faire voir : l'euro payé en T est connu, ce qu'il vaut en t est
cherché ; et la réponse est ce qu'il faut placer aujourd'hui pour l'obtenir. En haut,
un euro payé en T revient en t, où il vaut $P(t,T)$ : on actualise en multipliant par
$P(t,T)$. En bas, placer $P(t,T)$ en t donne exactement 1 en T : on capitalise en
divisant par $P(t,T)$. L'exemple de la fiche, 4 % continu sur un an : $P=e^{-0,04}$,
soit 0,9608, et $0{,}9608\times e^{0,04}=1$.

Usage : python courses/fpp/figures/facteur-actualisation.py > facteur-actualisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

r, duree = 0.04, 1.0
P = math.exp(-r * duree)                     # 0,9608
C = math.exp(r * duree)                      # 1,0408
v = lambda x: ("%.4f" % x).replace(".", ",")

t, T = 2.6, 8.2
g = Figure(xmin=0, xmax=10, ymin=-4.6, ymax=4.6, w=620, h=330, marges=(8, 8, 8, 8),
           titre="Un euro payé en T vaut en t ce qu'il faut placer en t pour l'obtenir")
g.axe_temps(0, 1.2, 9.7, [(t, "t"), (T, "T")])

# actualiser : 1 payé en T (connu) vaut P(t,T) en t (cherché)
g.texte(0.05, 3.3, "actualiser", taille=12, gras=True, couleur=ACCENT)
g.fleche(T, 0.45, T, 2.3, couleur=ACCENT, epaisseur=2)
g.texte(T, 1.55, "1", couleur=ACCENT, gras=True, taille=14, dx=10)
g.texte(T, 0.95, "connu", couleur=DOUX, taille=11.5, dx=10)
g.fleche(T - 0.25, 2.8, t + 0.9, 2.8, couleur=ACCENT, courbure=22)
g.texte(t, 2.7, "P(t,T) = " + v(P), couleur=ACCENT, gras=True, taille=13.5, ancre="middle")
g.texte(t, 2.1, "cherché", couleur=DOUX, taille=11.5, ancre="middle")
g.texte((t + T) / 2, 4.15, "× P(t,T)", couleur=ENCRE, taille=12.5, ancre="middle")

# capitaliser : placer P(t,T) en t rapporte exactement 1 en T
g.texte(0.05, -3.6, "capitaliser", taille=12, gras=True, couleur=AJOUT)
g.fleche(t, -0.85, t, -2.55, couleur=AJOUT, epaisseur=2)
g.texte(t, -1.75, "placer " + v(P), couleur=AJOUT, gras=True, taille=13.5, dx=10)
g.fleche(t + 0.35, -3.3, T - 1.15, -3.3, couleur=AJOUT, courbure=-20)
g.texte(T, -3.2, v(P) + " × " + v(C) + " = %.0f" % (P * C), couleur=AJOUT, gras=True,
        taille=13, ancre="middle")
g.texte((t + T) / 2, -4.45, "÷ P(t,T)", couleur=ENCRE, taille=12.5, ancre="middle")

sys.stdout.write(g.svg())
