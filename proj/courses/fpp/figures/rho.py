#!/usr/bin/env python3
r"""
rho.svg — le prix du call en fonction du taux d'intérêt, et sa tangente en r₀ : la pente
est le rhô, ρ = ∂C/∂r = K τ e^{−rτ} N(d₂).

Usage : python courses/fpp/figures/rho.py > rho.svg
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
RHO = 100 * math.exp(-0.04) * N(0.1)
c = lambda r: bs(100, r=r)
f = Figure(xmin=0, xmax=0.1, ymin=6, ymax=14, w=560, h=320,
           titre="Le rhô est la pente du prix le long du taux : ρ = K τ e^{−rτ} N(d₂)")
f.axes(xlab="r", ylab="C(r)", xticks=(0.04,), fmt=lambda t: "r₀")
f.fonction(c, 0, 0.1, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0.0, c(0.04) - 0.04 * RHO), (0.09, c(0.04) + 0.05 * RHO)], couleur=AJOUT, epaisseur=1.8)
f.segment(0.04, 6, 0.04, c(0.04))
f.point(0.04, c(0.04), couleur=ENCRE)
f.texte(0.04, c(0.04), "C(r_{0})", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(0.085, c(0.04) + 0.045 * RHO, "pente ρ = K τ e^{−rτ} N(d_{2})", couleur=AJOUT, dx=-4, dy=38, ancre="end", gras=True)
sys.stdout.write(f.svg())
