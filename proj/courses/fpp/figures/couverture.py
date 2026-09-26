#!/usr/bin/env python3
r"""
couverture.svg — le vendeur d'un call de strike 100 à un an (r = 4 %, σ = 20 %) tient
δ = 0,618 action. Sa perte sur le call, −(C(S) − 9,93), et son gain sur les actions,
0,618 (S − 100), se compensent autour de 100 : la somme reste presque plate tant que
l'action bouge peu.

Usage : python courses/fpp/figures/couverture.py > couverture.svg
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

D = N(d1(100))
C0 = bs(100)
f = Figure(xmin=80, xmax=120, ymin=-14, ymax=14, w=560, h=320,
           titre="Call vendu et actions tenues se compensent autour de 100 : l'ensemble reste presque plat")
f.axes(xlab="prix de l'action", ylab="gain ou perte", xticks=(80, 90, 100, 110, 120),
       yticks=(-10, -5, 0, 5, 10), fmt=lambda t: "%d" % t, croix=(80, 0))
f.fonction(lambda s: -(bs(s) - C0), 80, 120, couleur=AJOUT, epaisseur=2.2)
f.fonction(lambda s: D * (s - 100), 80, 120, couleur=DOUX, epaisseur=2.2)
f.fonction(lambda s: -(bs(s) - C0) + D * (s - 100), 80, 120, couleur=ACCENT, epaisseur=3)
f.texte(118, -(bs(118) - C0), "call vendu", couleur=AJOUT, ancre="end", dy=18, gras=True)
f.texte(118, D * 18, "0,618 action", couleur=DOUX, ancre="end", dy=-8, gras=True)
f.texte(100, 0, "ensemble", couleur=ACCENT, ancre="middle", dy=-10, gras=True, fond=True)
sys.stdout.write(f.svg())
