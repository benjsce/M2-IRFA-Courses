#!/usr/bin/env python3
r"""
valeur-temps.svg — le prix du call en fonction du prix de l'action, au-dessus de sa valeur
intrinsèque (S₀ − K e^{−rT})^+ : l'écart est la valeur temps, TV = prix − IV, la plus grande
près du coude.

Usage : python courses/fpp/figures/valeur-temps.py > valeur-temps.svg
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
KA = 100 * math.exp(-0.04)
f = Figure(xmin=60, xmax=140, ymin=0, ymax=46, w=560, h=320,
           titre="Prix = IV + TV : la valeur temps est l'écart entre le prix et la valeur intrinsèque")
f.axes(xlab="S₀", ylab="valeur du call", xticks=(KA,), fmt=lambda t: "K e⁻ʳᵀ")
f.courbe([(60, 0), (KA, 0), (140, 140 - KA)], couleur=AJOUT, epaisseur=2.2)
f.fonction(bs, 60, 140, couleur=ACCENT, epaisseur=2.6)
f.mesure(104, 104 - KA, bs(104), couleur=ENCRE, etiquette="TV")
f.texte(128, bs(128), "prix", couleur=ACCENT, dx=-6, dy=-10, ancre="end", gras=True)
f.texte(112, 112 - KA, "IV = (S_{0} − K e^{−rT})^{+}", couleur=AJOUT, dx=8, dy=16, gras=True)
sys.stdout.write(f.svg())
