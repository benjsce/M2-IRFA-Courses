#!/usr/bin/env python3
r"""
vega.svg — écarter les issues ajoute en haut et ne retire rien en bas.

Ce que la figure doit faire voir : pourquoi plus d'incertitude vaut plus cher pour le
détenteur d'un call. Le payoff du call de strike 100 a un plancher. Deux issues également
probables, 90 ou 110, paient 0 ou 10 : en moyenne 5. Écartées à 80 ou 120, elles paient
0 ou 20 : en moyenne 10. L'issue basse tombe sur le plancher et n'y perd rien, l'issue
haute gagne tout l'écart. C'est la corde et la courbe : le milieu de la corde monte quand
on l'élargit, parce que le payoff est convexe.

Les issues à deux points sont choisies pour le dessin ; la fiche le dit.

Usage : python courses/fpp/figures/vega.py > vega.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE      # noqa: E402

K = 100.0
g_ = lambda s: max(s - K, 0.0)

f = Figure(xmin=66, xmax=134, ymin=-1.5, ymax=27, w=560, h=330, marges=(44, 18, 46, 16),
           titre="Plus d'écart, plus de valeur : le plancher coupe la perte, pas le gain")
f.axes(xlab="cours de l'action à l'échéance", ylab="payoff du call",
       xticks=(80, 90, 100, 110, 120), yticks=(0, 5, 10, 20), croix=(66, 0),
       fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d" % t)
f.courbe([(68, 0), (K, 0), (126, 26)], couleur=ENCRE, epaisseur=2.4)
f.texte(122, 24, "payoff", couleur=ENCRE, gras=True, ancre="end", dx=-6)

for bas, haut, coul, etiq, dy in ((90, 110, AJOUT, "90 ou 110 : en moyenne 5", 0),
                                  (80, 120, ACCENT, "80 ou 120 : en moyenne 10", 0)):
    m = (g_(bas) + g_(haut)) / 2
    f.segment(bas, g_(bas), haut, g_(haut), couleur=coul, epaisseur=1.8, pointilles="6 4")
    f.point(bas, g_(bas), couleur=coul, r=4)
    f.point(haut, g_(haut), couleur=coul, r=4)
    f.point(K, m, couleur=coul, r=4.4)
    f.texte(K, m, etiq, couleur=coul, gras=True, ancre="end", dx=-10, dy=4, fond=True)


sys.stdout.write(f.svg())
