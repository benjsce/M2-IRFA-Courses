#!/usr/bin/env python3
r"""
gamma.svg — le delta du call, N(d₁), en fonction du prix de l'action : une courbe en S.
Sa tangente en S₀ a pour pente le gamma, γ = ∂²C/∂S² = n(d₁) / (S σ √τ).

Usage : python courses/fpp/figures/gamma.py > gamma.svg
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
G = math.exp(-0.3 ** 2 / 2) / math.sqrt(2 * math.pi) / (100 * 0.2)
dl = lambda s: N(d1(s))
f = Figure(xmin=50, xmax=160, ymin=0, ymax=1.05, w=560, h=320,
           titre="Le gamma est la pente du delta : γ = n(d₁) / (S σ √τ)")
f.axes(xlab="S", ylab="δ(S)", xticks=(100,), yticks=(1.0,), fmt=lambda t: "S₀", fmt_y=lambda t: "1")
f.fonction(dl, 50, 160, couleur=ACCENT, epaisseur=2.6)
f.courbe([(80, dl(100) - 20 * G), (120, dl(100) + 20 * G)], couleur=AJOUT, epaisseur=1.8)
f.point(100, dl(100), couleur=ENCRE)
f.texte(100, dl(100), "δ = N(d_{1})", dx=-10, dy=-4, ancre="end", gras=True)
f.texte(122, 0.55, "tangente : pente γ", couleur=AJOUT, gras=True)
sys.stdout.write(f.svg())
