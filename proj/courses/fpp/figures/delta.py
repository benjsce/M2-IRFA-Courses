#!/usr/bin/env python3
r"""
delta.svg — le prix du call en fonction du prix de l'action, et sa tangente en S₀ : la
pente est le delta, δ = ∂C/∂S = N(d₁).

Usage : python courses/fpp/figures/delta.py > delta.svg
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
D = N(d1(100))
f = Figure(xmin=60, xmax=140, ymin=0, ymax=46, w=560, h=320,
           titre="Le delta est la pente du prix du call : δ = ∂C/∂S = N(d₁)")
f.axes(xlab="S", ylab="C(S)", xticks=(100,), fmt=lambda t: "S₀")
f.fonction(bs, 60, 140, couleur=ACCENT, epaisseur=2.6)
f.courbe([(80, bs(100) - 20 * D), (130, bs(100) + 30 * D)], couleur=AJOUT, epaisseur=1.8)
f.segment(100, 0, 100, bs(100))
f.point(100, bs(100), couleur=ENCRE)
f.texte(100, bs(100), "C(S_{0})", dx=-8, dy=-8, ancre="end", gras=True)
f.texte(126, bs(100) + 26 * D, "pente δ = N(d_{1})", couleur=AJOUT, dx=6, dy=18, gras=True)
sys.stdout.write(f.svg())
