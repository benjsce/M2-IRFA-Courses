#!/usr/bin/env python3
r"""
portage.svg — des dividendes en montant : ils se retirent du comptant, date par date.

La fiche, rubrique « Cesse d'être valide quand » : avec des dividendes en montant fixe,
$F=\bigl(S_t-\sum_i D_iP(t,T_i)\bigr)/P(t,T)$, et les dates de détachement
réapparaissent. Le détenteur de l'action reçoit chaque $D_i$ à sa date et l'action en
T ; l'acheteur à terme ne reçoit que l'action. Chaque dividende revient en t par son
propre zéro-coupon, et ce qui reste du comptant est la valeur de l'action livrée en T.
Deux dividendes, comme sur forward-action.svg.

Usage : python courses/fpp/figures/portage.py > portage.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T1, T2, T = 3.4, 5.2, 6.9, 8.7
g = Figure(xmin=0, xmax=10, ymin=-4.6, ymax=5.2, w=640, h=360, marges=(8, 8, 8, 8),
           titre="Dividendes en montant : chacun se retire du comptant à sa date")
g.axe_temps(0, 1.6, 9.7, [(t, "t"), (T, "T")])
for x, s in ((T1, "T_{1}"), (T2, "T_{2}")):
    g.texte(x, 0, s, couleur=DOUX, taille=12.5, ancre="middle", dy=21)
    g.courbe([(x, -0.14), (x, 0.14)], couleur=DOUX, epaisseur=1.3)

# ce que reçoit le détenteur de l'action, chaque flux ramené en t
xe = t + 0.95                               # bord droit des étiquettes en t
g.texte(xe, 4.75, "valeur en t de l'action livrée en T", couleur=AJOUT, taille=11,
        ancre="end")
g.texte(xe, 4.05, "Sₜ − D_{1}P(t,T_{1}) − D_{2}P(t,T_{2})", couleur=AJOUT, gras=True,
        taille=12.5, ancre="end")
g.fleche(T, 0.45, T, 2.3, couleur=AJOUT, epaisseur=2)
g.texte(T, 1.4, "1 action", couleur=AJOUT, gras=True, taille=13.5, dx=-9, ancre="end")
g.fleche(T - 0.1, 2.6, xe + 0.1, 4.17, couleur=AJOUT, courbure=14)
for x, D, Pk, y in ((T2, "D_{2}", "P(t,T_{2})", 2.85), (T1, "D_{1}", "P(t,T_{1})", 1.85)):
    g.fleche(x, 0.45, x, 1.4, couleur=DOUX, epaisseur=1.8)
    g.texte(x, 0.9, D, couleur=DOUX, gras=True, taille=13, dx=7)
    g.fleche(x - 0.12, 1.65, xe + 0.1, y + 0.12, couleur=DOUX, courbure=8, epaisseur=1.2)
    g.texte(xe, y, "+ %s·%s" % (D, Pk), couleur=DOUX, taille=12.5, ancre="end")
g.texte(xe, 0.75, "= Sₜ, le comptant", couleur=ENCRE, gras=True, taille=12.5, ancre="end")

# l'acheteur à terme paie F en T
g.fleche(T, -1.25, T, -3.1, couleur=ACCENT, epaisseur=2)
g.texte(T, -2.2, "F", couleur=ACCENT, gras=True, taille=14, dx=9)
g.fleche(T - 0.2, -3.5, xe + 0.1, -3.5, couleur=ACCENT, courbure=-20)
g.texte(xe, -3.4, "F·P(t,T)", couleur=ACCENT, gras=True, taille=13.5, ancre="end")

sys.stdout.write(g.svg())
