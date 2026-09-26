#!/usr/bin/env python3
r"""
gamma.svg — le delta du call de strike 100 à un an, N(d_1), en fonction du prix de
l'action : une courbe en S. Sa tangente en 100 a pour pente le gamma,
n(d_1)/(S σ √τ) = 0,3814/20 ≈ 0,019.

Usage : python courses/fpp/figures/gamma.py > gamma.svg
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

G = math.exp(-0.3 ** 2 / 2) / math.sqrt(2 * math.pi) / (100 * 0.2)
dl = lambda s: N(d1(s))
f = Figure(xmin=50, xmax=160, ymin=0, ymax=1.05, w=560, h=320,
           titre="Le gamma est la pente du delta : 0,019 par euro de mouvement en 100")
f.axes(xlab="prix de l'action", ylab="delta du call", xticks=(60, 80, 100, 120, 140, 160),
       yticks=(0.25, 0.5, 0.75, 1.0), fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%g" % t).replace(".", ","))
f.fonction(dl, 50, 160, couleur=ACCENT, epaisseur=2.6)
f.courbe([(80, dl(100) - 20 * G), (120, dl(100) + 20 * G)], couleur=AJOUT, epaisseur=1.8)
f.point(100, dl(100), couleur=ENCRE)
f.texte(100, dl(100), "δ = 0,618", dx=-10, dy=-4, ancre="end", gras=True)
f.texte(122, 0.55, "tangente : pente γ = 0,019", couleur=AJOUT, gras=True)
sys.stdout.write(f.svg())
