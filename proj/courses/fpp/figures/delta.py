#!/usr/bin/env python3
r"""
delta.svg — le delta est la pente du prix, et la tangente est la couverture.

L'exemple courant : call de strike 100, taux 4 %, volatilité 20 %, un an. La courbe est le
prix de Black et Scholes selon le sous-jacent ; la droite est sa tangente en 100, de pente
$N(d_1)=0{,}618$. Détenir 0,618 action reproduit le call au voisinage de 100 : c'est la
couverture au premier ordre de la fiche. Loin de 100, la courbe s'écarte de la tangente,
et il faut rééquilibrer.

Usage : python courses/fpp/figures/delta.py > delta.svg
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


def d1(s):
    return (math.log(s / K) + (R + SIG ** 2 / 2) * T) / (SIG * math.sqrt(T))


def call(s):
    return s * N.cdf(d1(s)) - K * math.exp(-R * T) * N.cdf(d1(s) - SIG * math.sqrt(T))


D = N.cdf(d1(100))                     # 0,618
C0 = call(100)

f = Figure(xmin=60, xmax=140, ymin=0, ymax=44, w=560, h=330,
           titre="Au voisinage de 100, le call se comporte comme 0,618 action")
f.axes(xlab="sous-jacent S", ylab="prix du call", xticks=(60, 80, 100, 120, 140),
       yticks=(9.93, 20, 40), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: ("%.2f" % t).replace(".", ",") if t % 1 else "%d" % t)

f.fonction(call, 60, 140, n=200, couleur=ACCENT, epaisseur=2.6)
f.fonction(lambda s: C0 + D * (s - 100), 86, 140, couleur=AJOUT, epaisseur=1.8)
f.point(100, C0, couleur=ENCRE)
f.courbe([(100, C0), (110, C0)], couleur=DOUX, epaisseur=1.2)
f.courbe([(110, C0), (110, C0 + 10 * D)], couleur=DOUX, epaisseur=1.2)
f.texte(110, C0 + 5 * D, "+6,18", couleur=DOUX, dx=6, dy=4, taille=11.5)
f.texte(105, C0, "+10", couleur=DOUX, ancre="middle", dy=14, taille=11.5)
f.texte(132, C0 + D * 32, "tangente : pente δ = 0,618", couleur=AJOUT, ancre="end", dx=-4,
        dy=18, gras=True, fond=True)
f.texte(64, 11, "prix du call", couleur=ACCENT, gras=True, fond=True)

sys.stdout.write(f.svg())
