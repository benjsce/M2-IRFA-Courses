#!/usr/bin/env python3
r"""
compte-capitalise.svg — un saut connu d'avance, ou une suite de sauts courts.

La fiche : $B(t,T)=\prod_k P(t_k,t_{k+1})$. Au-dessus de l'axe, le zéro-coupon fait le
trajet de T à t en un seul saut, connu en t. Au-dessous, le compte capitalisé enchaîne
des zéro-coupons courts ; seul le premier est connu en t, les suivants ne le seront qu'à
leur date — d'où le pointillé. Trois pas, pour que l'enchaînement se voie.

Usage : python courses/fpp/figures/compte-capitalise.py > compte-capitalise.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

x = [2.0, 4.2, 6.4, 8.6]
g = Figure(xmin=0, xmax=10, ymin=-4.4, ymax=3.9, w=640, h=320, marges=(8, 8, 8, 8),
           titre="Compte capitalisé : des zéro-coupons courts enchaînés, dont un seul est connu en t")
g.axe_temps(0, 0.9, 9.7, [(xk, "") for xk in x])
for xk, s in zip(x, ("t = t_{0}", "t_{1}", "t_{2}", "t_{3} = T")):
    g.texte(xk, 0, s, couleur=DOUX, taille=12.5, ancre="middle", dy=21)

# le zéro-coupon : un seul saut, connu en t
g.fleche(x[3] - 0.1, 0.5, x[0] + 0.1, 0.5, couleur=ACCENT, courbure=44, epaisseur=1.8)
g.texte((x[0] + x[3]) / 2, 2.65, "P(t,T) : connu en t", couleur=ACCENT, gras=True,
        taille=13, ancre="middle", fond=True)

# le compte capitalisé : trois sauts courts
labels = ("P(t_{0},t_{1})", "P(t_{1},t_{2})", "P(t_{2},t_{3})")
for k in range(3):
    connu = k == 0
    g.fleche(x[k + 1] - 0.1, -1.1, x[k] + 0.1, -1.1, couleur=AJOUT, courbure=-24,
             epaisseur=1.8, pointilles=None if connu else "5 4")
    g.texte((x[k] + x[k + 1]) / 2, -2.75, labels[k], couleur=AJOUT, gras=True, taille=12.5,
            ancre="middle", fond=True)
    g.texte((x[k] + x[k + 1]) / 2, -3.35, "connu en t" if connu else "inconnu en t",
            couleur=DOUX, taille=11, ancre="middle")
g.texte(5.3, -4.15, "B(t,T) = P(t_{0},t_{1})·P(t_{1},t_{2})·P(t_{2},t_{3})", couleur=AJOUT,
        taille=12.5, ancre="middle")

sys.stdout.write(g.svg())
