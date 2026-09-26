#!/usr/bin/env python3
r"""
vega.svg — le prix du call de strike 100 à un an, l'action à 100, en fonction de la
volatilité, et sa tangente à 20 % : la pente, S n(d_1) √τ = 38,1, est le véga
(0,38 par point de volatilité).

Usage : python courses/fpp/figures/vega.py > vega.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def d1(S, K=100.0, T=1.0, r=0.04, sig=0.2):
    return (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))


def bs(S, K=100.0, T=1.0, r=0.04, sig=0.2):
    """Prix du call de Black et Scholes, sans dividende."""
    if T <= 0:
        return max(S - K, 0.0)
    d = d1(S, K, T, r, sig)
    return S * N(d) - K * math.exp(-r * T) * N(d - sig * math.sqrt(T))

V = 100 * math.exp(-0.3 ** 2 / 2) / math.sqrt(2 * math.pi)
c = lambda s: bs(100, sig=s)
f = Figure(xmin=0, xmax=0.5, ymin=0, ymax=23, w=560, h=320,
           titre="Le véga est la pente du prix le long de la volatilité : 38,1, soit 0,38 par point")
f.axes(xlab="volatilité σ", ylab="prix du call", xticks=(0, 0.1, 0.2, 0.3, 0.4, 0.5),
       yticks=(5, 10, 15, 20), fmt=lambda t: "%d %%" % round(100 * t), fmt_y=lambda t: "%d" % t)
f.fonction(c, 0.005, 0.5, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0.05, c(0.2) - 0.15 * V), (0.4, c(0.2) + 0.2 * V)], couleur=AJOUT, epaisseur=1.8)
f.point(0.2, c(0.2), couleur=ENCRE)
f.texte(0.2, c(0.2), "9,93", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(0.38, c(0.2) + 0.18 * V, "pente 𝒱 = 38,1", couleur=AJOUT, dx=6, dy=18, gras=True)
sys.stdout.write(f.svg())
