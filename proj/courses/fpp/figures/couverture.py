#!/usr/bin/env python3
r"""
couverture.svg — le call acheté, moins 0,618 action : une position presque plate.

Ce que la figure doit faire voir : la sensibilité connue (le call gagne quand l'action
monte) et la position qui l'annule (0,618 action vendue, qui perd autant), posées côte à
côte, puis leur somme, qui ne bouge presque plus autour de 100. Ce qui reste, loin de
100, est le second ordre que la couverture n'annule pas.

Les trois cadres ont la même échelle, pour que la platitude de la somme se voie. Le call
est celui de l'exemple courant : strike 100, taux 4 %, volatilité 20 %, un an, prix 9,93
quand l'action vaut 100 ; on trace son gain quand le cours de l'action change aussitôt.

Usage : python courses/fpp/figures/couverture.py > couverture.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

N = NormalDist()
K, R, SIG, T = 100.0, 0.04, 0.20, 1.0


def call(s):
    d1 = (math.log(s / K) + (R + SIG ** 2 / 2) * T) / (SIG * math.sqrt(T))
    return s * N.cdf(d1) - K * math.exp(-R * T) * N.cdf(d1 - SIG * math.sqrt(T))


C0 = call(100.0)
DELTA = N.cdf((R + SIG ** 2 / 2) * T / (SIG * math.sqrt(T)))       # 0,618
gain_call = lambda s: call(s) - C0
gain_actions = lambda s: -DELTA * (s - 100.0)
gain_total = lambda s: gain_call(s) + gain_actions(s)
virg = lambda v: ("%+.2f" % v).replace(".", ",").replace("-", "−")


def cadre(titre, f, couleur, note, xn, yn):
    g = Figure(xmin=78, xmax=122, ymin=-14, ymax=17, w=232, h=270, marges=(40, 28, 40, 10))
    g.axes(xlab="action", xticks=(80, 100, 120), yticks=(-10, 0, 10), croix=(78, 0),
           fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%d" % t).replace("-", "−"))
    g.fonction(f, 80, 120, couleur=couleur, epaisseur=2.6)
    g.point(100, 0, couleur=ENCRE, r=3)
    g.point(110, f(110), couleur=couleur, r=2.8)
    g.texte(100, 17, titre, couleur=couleur, ancre="middle", dy=-4, taille=12.5, gras=True)
    g.texte(xn, yn, note, couleur=couleur, ancre="middle", taille=11.5, fond=True)
    return g


p = Planche([cadre("le call acheté", gain_call, AJOUT,
                   "à 110 : " + virg(gain_call(110)), 104, 11.5),
             cadre("0,618 action vendue", gain_actions, DOUX,
                   "à 110 : " + virg(gain_actions(110)), 104, -11.5),
             cadre("la position couverte", gain_total, ACCENT,
                   "à 110 : " + virg(gain_total(110)), 104, 6.5)],
            signes=("+", "="), ecart=34,
            titre="Se couvrir : 0,618 action vendue par call acheté, et la position ne bouge "
                  "presque plus autour de 100")
sys.stdout.write(p.svg())
