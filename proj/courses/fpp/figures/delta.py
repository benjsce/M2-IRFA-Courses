#!/usr/bin/env python3
r"""
delta.svg — le prix du call de strike 100 à un an (r = 4 %, σ = 20 %) en fonction du prix
de l'action, et sa tangente en 100 : la pente, N(d_1) = N(0,30) = 0,618, est le delta.

Usage : python courses/fpp/figures/delta.py > delta.svg
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
f = Figure(xmin=60, xmax=140, ymin=0, ymax=46, w=560, h=320,
           titre="Le delta est la pente du prix : 0,618 action par call en 100")
f.axes(xlab="prix de l'action", ylab="prix du call", xticks=(60, 80, 100, 120, 140),
       yticks=(10, 20, 30, 40), fmt=lambda t: "%d" % t)
f.fonction(bs, 60, 140, couleur=ACCENT, epaisseur=2.6)
f.courbe([(80, bs(100) - 20 * D), (130, bs(100) + 30 * D)], couleur=AJOUT, epaisseur=1.8)
f.point(100, bs(100), couleur=ENCRE)
f.texte(100, bs(100), "9,93", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(126, bs(100) + 26 * D, "pente δ = 0,618", couleur=AJOUT, dx=6, dy=18, gras=True)
sys.stdout.write(f.svg())
