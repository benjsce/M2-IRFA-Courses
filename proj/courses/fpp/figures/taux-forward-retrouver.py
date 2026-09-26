#!/usr/bin/env python3
r"""
taux-forward-retrouver.svg — un euro placé de t à S, d'un coup ou en deux temps.

La fiche : $F(t,T,S)=\frac{1}{S-T}\ln\frac{P(t,T)}{P(t,S)}$. En haut, l'euro placé d'un
coup jusqu'en S devient $1/P(t,S)$. En bas, placé jusqu'en T il devient $1/P(t,T)$, puis
replacé de T à S au taux F il devient $e^{F(S-T)}/P(t,T)$. Le taux forward est celui qui
fait arriver les deux chemins au même montant : c'est la formule, lue sur le dessin.
Aucun contrat ici : les flèches vont vers l'avenir, alors que celles du FRA reviennent en t.

Usage : python courses/fpp/figures/taux-forward-retrouver.py > taux-forward-retrouver.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE      # noqa: E402

t, T, S = 1.6, 5.0, 8.4
g = Figure(xmin=0, xmax=10, ymin=-2.9, ymax=3.4, w=640, h=260, marges=(8, 8, 8, 8),
           titre="Taux forward : deux façons de placer un euro jusqu'en S")
g.axe_temps(0, 0.6, 9.8, [(t, "t"), (T, "T"), (S, "S")])
g.texte(t, 0.55, "1", couleur=ENCRE, gras=True, taille=14, ancre="middle")

# d'un coup, de t à S
g.fleche(t + 0.25, 0.9, S - 0.25, 0.9, couleur=AJOUT, epaisseur=1.8, courbure=40)
g.texte((t + S) / 2, 2.7, "placé d'un coup jusqu'en S", couleur=AJOUT, taille=12,
        ancre="middle")
g.texte(S, 1.25, "1 / P(t,S)", couleur=AJOUT, gras=True, taille=13.5, ancre="middle")

# en deux temps : jusqu'en T, puis de T à S au taux F
g.fleche(t + 0.25, -0.55, T - 0.25, -0.55, couleur=ACCENT, epaisseur=1.8, courbure=-25)
g.texte((t + T) / 2, -2.15, "placé jusqu'en T", couleur=ACCENT, taille=12, ancre="middle")
g.texte(T, 0.45, "1 / P(t,T)", couleur=ACCENT, gras=True, taille=13, ancre="middle")
g.fleche(T + 0.25, -0.55, S - 0.25, -0.55, couleur=ACCENT, epaisseur=1.8, courbure=-25)
g.texte((T + S) / 2, -2.15, "replacé au taux F", couleur=ACCENT, taille=12, ancre="middle")
g.texte(S, -1.05, "e^{F(S−T)} / P(t,T)", couleur=ACCENT, gras=True, taille=13.5,
        ancre="middle", dy=16)


sys.stdout.write(g.svg())
