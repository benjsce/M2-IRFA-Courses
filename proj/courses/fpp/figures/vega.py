#!/usr/bin/env python3
r"""
vega.svg — le prix du call en fonction de la volatilité, et sa tangente en σ₀ : la pente
est le véga, 𝒱 = ∂C/∂σ = S n(d₁) √τ.

Usage : python courses/fpp/figures/vega.py > vega.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def d1(S, K=100.0, T=1.0, r=0.04, sig=0.2, q=0.0):
    return (math.log(S / K) + (r - q + sig * sig / 2) * T) / (sig * math.sqrt(T))


def bs(S, K=100.0, T=1.0, r=0.04, sig=0.2, q=0.0):
    """Prix du call de Black et Scholes, pour le tracé seulement."""
    if T <= 0:
        return max(S - K, 0.0)
    d = d1(S, K, T, r, sig, q)
    return S * math.exp(-q * T) * N(d) - K * math.exp(-r * T) * N(d - sig * math.sqrt(T))
V = 100 * math.exp(-0.3 ** 2 / 2) / math.sqrt(2 * math.pi)
c = lambda s: bs(100, sig=s)
f = Figure(xmin=0, xmax=0.5, ymin=0, ymax=23, w=560, h=320,
           titre="Le véga est la pente du prix le long de la volatilité : 𝒱 = S n(d₁) √τ")
f.axes(xlab="σ", ylab="C(σ)", xticks=(0.2,), fmt=lambda t: "σ₀")
f.fonction(c, 0.005, 0.5, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0.05, c(0.2) - 0.15 * V), (0.4, c(0.2) + 0.2 * V)], couleur=AJOUT, epaisseur=1.8)
f.segment(0.2, 0, 0.2, c(0.2))
f.point(0.2, c(0.2), couleur=ENCRE)
f.texte(0.2, c(0.2), "C(σ_{0})", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(0.38, c(0.2) + 0.18 * V, "pente 𝒱 = S n(d_{1}) √τ", couleur=AJOUT, dx=6, dy=20, gras=True)
sys.stdout.write(f.svg())
