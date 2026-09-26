#!/usr/bin/env python3
r"""
rho.svg — le prix du call de strike 100 à un an, l'action à 100, en fonction du taux
d'intérêt, et sa tangente à 4 % : la pente, K τ e^{−rτ} N(d_2) = 51,9, est le rhô
(0,52 par point de taux).

Usage : python courses/fpp/figures/rho.py > rho.svg
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

RHO = 100 * math.exp(-0.04) * N(0.1)
c = lambda r: bs(100, r=r)
f = Figure(xmin=0, xmax=0.1, ymin=6, ymax=14, w=560, h=320,
           titre="Le rhô est la pente du prix le long du taux : 51,9, soit 0,52 par point")
f.axes(xlab="taux d'intérêt r", ylab="prix du call", xticks=(0, 0.02, 0.04, 0.06, 0.08, 0.1),
       yticks=(8, 10, 12), fmt=lambda t: "%d %%" % round(100 * t), fmt_y=lambda t: "%d" % t)
f.fonction(c, 0, 0.1, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0.0, c(0.04) - 0.04 * RHO), (0.09, c(0.04) + 0.05 * RHO)], couleur=AJOUT, epaisseur=1.8)
f.point(0.04, c(0.04), couleur=ENCRE)
f.texte(0.04, c(0.04), "9,93", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(0.085, c(0.04) + 0.045 * RHO, "pente ρ = 51,9", couleur=AJOUT, dx=-4, dy=20, ancre="end", gras=True)
sys.stdout.write(f.svg())
