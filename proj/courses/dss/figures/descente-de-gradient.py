#!/usr/bin/env python3
r"""
descente-de-gradient.svg — les pas d'une descente, avec un petit et un grand taux.

Une erreur quadratique $E(w)=w^2$, choisie pour le dessin, et la règle de la fiche,
$\Delta w=-\eta\,\partial E/\partial w$. À gauche, $\eta=0{,}1$ : chaque pas garde huit
dixièmes de l'écart, et le poids glisse vers le minimum du même côté. À droite,
$\eta=0{,}9$ : chaque pas franchit le minimum, et le poids saute d'un bord à l'autre —
l'oscillation que le geste de la fiche corrige en réduisant le taux.

Au point de départ $w=4$, un bout de tangente, de pente $\partial E/\partial w=8$ : c'est tout ce
que la descente connaît de la surface d'erreur. Le premier pas vaut $-0{,}8$ à gauche,
$-7{,}2$ à droite.

Usage : python courses/dss/figures/descente-de-gradient.py > descente-de-gradient.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

E = lambda w: w * w


def cadre(titre, eta, couleur):
    g = Figure(xmin=-4.6, xmax=4.6, ymin=-1.5, ymax=19, w=270, h=260, marges=(20, 30, 30, 10))
    g.axes(xlab="w", xticks=(), croix=(0, 0))
    # le « 0 » de l'origine, posé à gauche de l'axe vertical pour qu'il ne le traverse pas
    g.texte(0, 0, "0", couleur=DOUX, ancre="end", dx=-5, dy=16, taille=11.5)
    g.fonction(E, -4.4, 4.4, couleur=DOUX, epaisseur=2.0)
    # la seule chose connue au départ : la pente de l'erreur au point où l'on est
    g.courbe([(2.3, E(4) + 8 * (2.3 - 4)), (4.35, E(4) + 8 * (4.35 - 4))], couleur=ENCRE,
             epaisseur=1.4, pointilles="4 3")
    g.texte(4, E(4), "pente 8", couleur=ENCRE, ancre="end", dx=-10, dy=-4, taille=11,
            fond=True)
    w = 4.0
    for _ in range(6):
        w2 = w - eta * 2 * w
        g.fleche(w, E(w), w2, E(w2), couleur=couleur, epaisseur=1.6)
        g.point(w, E(w), couleur=couleur, r=3.4)
        w = w2
    g.point(w, E(w), couleur=couleur, r=3.4)
    g.texte(0, 19, titre, couleur=couleur, ancre="middle", dy=-10, gras=True)
    return g


p = Planche([cadre("η = 0,1 : il glisse", 0.1, ACCENT), cadre("η = 0,9 : il oscille", 0.9, AJOUT)],
            ecart=30, titre="Un pas trop grand franchit le minimum à chaque fois")
sys.stdout.write(p.svg())
