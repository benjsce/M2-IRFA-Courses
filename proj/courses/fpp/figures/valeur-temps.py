#!/usr/bin/env python3
r"""
valeur-temps.svg — le prix du call et sa valeur intrinsèque, selon le sous-jacent.

L'exemple courant : strike 100, taux 4 %, volatilité 20 %, un an. La valeur intrinsèque
évalue le payoff en la moyenne, $e^{-rT}(F-K)^+=(S_0-Ke^{-rT})^+$ : un payoff brisé, nul
jusqu'à 96,08. Le prix, par la formule de Black et Scholes, est la courbe lisse au-dessus.
L'écart est la valeur temps ; à la monnaie, 9,93 contre 3,92, soit 6,00. Il est positif
partout parce que le payoff est convexe.

Usage : python courses/fpp/figures/valeur-temps.py > valeur-temps.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

N = NormalDist()
K, R, SIG, T = 100.0, 0.04, 0.20, 1.0


def call(s):
    d1 = (math.log(s / K) + (R + SIG ** 2 / 2) * T) / (SIG * math.sqrt(T))
    return s * N.cdf(d1) - K * math.exp(-R * T) * N.cdf(d1 - SIG * math.sqrt(T))


iv = lambda s: max(s - K * math.exp(-R * T), 0.0)
fr = lambda v: ("%.2f" % v).replace(".", ",")

f = Figure(xmin=60, xmax=140, ymin=0, ymax=46, w=560, h=330,
           titre="Au-dessus du payoff évalué en la moyenne, la valeur temps")
f.axes(xlab="sous-jacent S0", ylab="valeur", xticks=(60, 80, 96.08, 120, 140),
       yticks=(3.92, 9.93, 20, 40), fmt=lambda t: fr(t) if t % 1 else "%d" % t,
       fmt_y=lambda t: fr(t) if t % 1 else "%d" % t)

f.courbe([(60, 0), (K * math.exp(-R * T), 0), (140, iv(140))], couleur=DOUX, epaisseur=2.2)
f.fonction(call, 60, 140, n=200, couleur=ACCENT, epaisseur=2.6)
f.mesure(100, iv(100), call(100), couleur=AJOUT, etiquette="valeur temps 6,00")
f.point(100, call(100), couleur=ACCENT)
f.point(100, iv(100), couleur=DOUX)
f.texte(128, call(128), "prix du call", couleur=ACCENT, ancre="end", dx=-8, dy=-6, gras=True,
        fond=True)
f.texte(116, iv(116), "valeur intrinsèque", couleur=DOUX, dx=4, dy=18, gras=True, fond=True)

sys.stdout.write(f.svg())
