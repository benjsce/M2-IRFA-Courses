#!/usr/bin/env python3
r"""
fra.svg — un montant inconnu dont la valeur est connue.

Ce que la figure doit faire voir : en S, le FRA échange deux flux. Celui qui paie le fixe
paie $e^{K(S-T)}$, un montant fixé aujourd'hui ; il reçoit $e^{R(T,S)(S-T)}$, un montant
qu'on ne connaîtra qu'en T, quand le taux $R(T,S)$ sera fixé. Ce second flux vaut
pourtant 1 en T quel que soit ce taux, puisque c'est exactement ce que devient 1 placé de
T à S au taux du moment ; il revient donc en t comme $P(t,T)$. Le premier revient en t
comme $P(t,S)e^{K(S-T)}$. Le contrat ne coûtant rien à la signature, les deux sont égaux,
et K est le taux forward.

Usage : python courses/fpp/figures/fra.py > fra.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

t, T, S = 2.9, 6.0, 9.1
g = Figure(xmin=0, xmax=11.4, ymin=-3.9, ymax=4.0, w=700, h=380, marges=(8, 8, 8, 8),
           titre="FRA : la jambe flottante a un montant inconnu, mais elle vaut 1 en T, donc P(t,T) aujourd'hui")
g.axe_temps(0, 0.4, 11.1, [(t, "t"), (T, "T"), (S, "S")])

# jambe flottante : reçue en S, montant inconnu aujourd'hui
g.fleche(S, 0.35, S, 2.1, couleur=AJOUT, epaisseur=2.2, pointilles="5 4")
g.texte(S, 1.45, "e^{R(T,S)(S−T)}", couleur=AJOUT, gras=True, taille=13.5, dx=10)
g.texte(S, 0.85, "inconnu aujourd'hui", couleur=DOUX, taille=11.5, dx=10)
# elle revient en T, où elle vaut 1 quel que soit le taux…
g.fleche(S - 0.1, 2.5, T + 0.1, 2.5, couleur=AJOUT, epaisseur=1.5, courbure=14,
         pointilles="5 4")
g.point(T, 2.5, couleur=AJOUT, r=3.6)
g.texte(T, 2.5, "vaut 1 en T,", couleur=AJOUT, gras=True, taille=12.5, ancre="end", dx=-9, dy=-4)
g.texte(T, 2.5, "quel que soit R(T,S)", couleur=AJOUT, taille=11.5, ancre="end", dx=-9, dy=12)
# …puis en t, par le zéro-coupon d'échéance T
g.fleche(T - 0.1, 3.3, t + 0.1, 3.3, couleur=AJOUT, epaisseur=1.5, courbure=12)
g.texte(t, 3.3, "P(t,T)", couleur=AJOUT, gras=True, taille=13.5, ancre="end", dx=-6, dy=4)

# jambe fixe : payée en S, montant fixé aujourd'hui
g.fleche(S, -0.75, S, -2.3, couleur=ACCENT, epaisseur=2.2)
g.texte(S, -1.45, "e^{K(S−T)}", couleur=ACCENT, gras=True, taille=13.5, dx=10)
g.texte(S, -2.05, "fixé aujourd'hui", couleur=DOUX, taille=11.5, dx=10)
g.fleche(S - 0.1, -2.85, t + 0.1, -2.85, couleur=ACCENT, epaisseur=1.5, courbure=-18)
g.texte(t, -2.85, "P(t,S)·e^{K(S−T)}", couleur=ACCENT, gras=True, taille=13.5, ancre="end",
        dx=-6, dy=4)

# en t : les deux valeurs sont égales, le contrat ne coûtant rien
g.texte(t - 0.25, 1.35, "égales :", couleur=ENCRE, gras=True, taille=12.5, ancre="end")
g.texte(t - 0.25, 0.85, "le contrat", couleur=DOUX, taille=11.5, ancre="end")
g.texte(t - 0.25, -1.0, "K = F(t,T,S)", couleur=ENCRE, gras=True, taille=13, ancre="end")
g.courbe([(t - 1.0, 2.9), (t - 1.0, 1.75)], couleur=DOUX, epaisseur=1.2)
g.courbe([(t - 1.0, -1.45), (t - 1.0, -2.45)], couleur=DOUX, epaisseur=1.2)
g.texte(t - 0.25, 0.35, "ne coûte rien", couleur=DOUX, taille=11.5, ancre="end")

sys.stdout.write(g.svg())
