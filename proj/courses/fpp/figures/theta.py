#!/usr/bin/env python3
r"""
theta.svg — le prix du call à la monnaie à mesure que le temps passe, l'action restant
fixe : il fond jusqu'à 0 à l'échéance, de plus en plus vite. La tangente au départ a pour
pente le thêta, Θ = ∂C/∂t.

Usage : python courses/fpp/figures/theta.py > theta.svg
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
TH = -(100 * math.exp(-0.045) / math.sqrt(2 * math.pi) * 0.2 / 2) - 0.04 * 100 * math.exp(-0.04) * N(0.1)
c = lambda t: bs(100, T=1 - t)
f = Figure(xmin=0, xmax=1.05, ymin=0, ymax=12, w=560, h=320,
           titre="L'option fond quand l'échéance approche : Θ = ∂C/∂t < 0, de plus en plus fort")
f.axes(xlab="temps t", ylab="C", xticks=(0, 1), fmt=lambda t: "t" if t == 0 else "T")
f.fonction(c, 0, 0.9995, n=400, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0, c(0)), (0.6, c(0) + 0.6 * TH)], couleur=AJOUT, epaisseur=1.8)
f.point(0, c(0), couleur=ENCRE)
f.texte(0.6, c(0) + 0.6 * TH, "pente Θ = ∂C/∂t", couleur=AJOUT, dx=-4, dy=18, ancre="end", gras=True)
f.point(1, 0, couleur=ENCRE)
f.texte(1, 0, "en T : (S − K)^{+} = 0 à la monnaie", dx=-6, dy=-8, ancre="end", taille=12)
sys.stdout.write(f.svg())
