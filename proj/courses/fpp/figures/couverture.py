#!/usr/bin/env python3
r"""
couverture.svg — le vendeur d'un call tient δ actions. Sa perte sur le call,
−(C(S) − C(S₀)), et son gain sur les actions, δ (S − S₀), se compensent autour de S₀ :
la somme reste presque plate tant que l'action bouge peu.

Usage : python courses/fpp/figures/couverture.py > couverture.svg
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
C0 = bs(100)
f = Figure(xmin=80, xmax=120, ymin=-14, ymax=14, w=560, h=320,
           titre="Call vendu et δ actions tenues se compensent autour de S₀ : l'ensemble reste presque plat")
f.axes(xlab="prix de l'action S", ylab="gain ou perte", xticks=(100,), yticks=(0,),
       fmt=lambda t: "S₀", fmt_y=lambda t: "0", croix=(80, 0))
f.fonction(lambda s: -(bs(s) - C0), 80, 120, couleur=AJOUT, epaisseur=2.2)
f.fonction(lambda s: D * (s - 100), 80, 120, couleur=DOUX, epaisseur=2.2)
f.fonction(lambda s: -(bs(s) - C0) + D * (s - 100), 80, 120, couleur=ACCENT, epaisseur=3)
f.texte(118, -(bs(118) - C0), "call vendu : − (C(S) − C(S_{0}))", couleur=AJOUT, ancre="end", dy=18, gras=True)
f.texte(118, D * 18, "δ actions : δ (S − S_{0})", couleur=DOUX, ancre="end", dy=-8, gras=True)
f.texte(100, 0, "ensemble", couleur=ACCENT, ancre="middle", dy=-10, gras=True, fond=True)
sys.stdout.write(f.svg())
