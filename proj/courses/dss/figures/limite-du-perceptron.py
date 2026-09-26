#!/usr/bin/env python3
r"""
limite-du-perceptron.svg — le OU se sépare par une droite, le OU exclusif non.

Les quatre points des deux tables de vérité, sorties 1 pleines et sorties 0 creuses. À
gauche, le OU : une droite sépare $(0,0)$ des trois autres, et un seul neurone suffit. À
droite, le OU exclusif : les deux classes sont en diagonale, aucune droite ne les sépare ;
deux droites y parviennent, celles de deux neurones, et la bande entre elles contient les
sorties 1. C'est la couche cachée qui apparaît.

Usage : python courses/dss/figures/limite-du-perceptron.py > limite-du-perceptron.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT, _n      # noqa: E402

OU = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
XOU = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}


def cadre(titre, table, droites, couleur):
    # marges gauche et basse assez larges pour les étiquettes d'axe « x2 » et « x1 »
    g = Figure(xmin=-0.5, xmax=1.6, ymin=-0.5, ymax=1.6, w=290, h=290, marges=(50, 30, 40, 10))
    g.axes(xlab="x1", ylab="x2", xticks=(0, 1), yticks=(0, 1), fmt=lambda t: "%d" % t,
           fmt_y=lambda t: "%d" % t, croix=(-0.5, -0.5))
    for c in droites:
        xa, xb = max(-0.5, c - 1.6), min(1.6, c + 0.5)      # la droite x1 + x2 = c, coupée au cadre
        g.courbe([(xa, c - xa), (xb, c - xb)], couleur=couleur, epaisseur=2.2)
    for (a, b), v in table.items():
        if v:
            g.point(a, b, couleur=ACCENT, r=7)
        else:
            g.point(a, b, couleur=ENCRE, r=7)
            g.point(a, b, couleur="var(--card)", r=4.5)
    g.texte(0.55, 1.6, titre, couleur=ENCRE, ancre="middle", dy=-10, gras=True)
    return g


p = Planche([cadre("OU : une droite suffit", OU, (0.5,), DOUX),
             cadre("OU exclusif : il en faut deux", XOU, (0.5, 1.5), AJOUT)],
            ecart=30, titre="Un neurone trace une droite : le OU exclusif en demande deux")
sys.stdout.write(p.svg())
