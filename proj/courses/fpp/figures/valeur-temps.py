#!/usr/bin/env python3
r"""
valeur-temps.svg — le prix de Black et Scholes du call de strike 100 à un an (r = 4 %,
σ = 20 %) en fonction du prix de l'action, au-dessus de sa valeur intrinsèque
(S_0 − 96,08)^+ : l'écart est la valeur temps, 9,93 − 3,92 = 6,00 quand l'action est à 100.

Usage : python courses/fpp/figures/valeur-temps.py > valeur-temps.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs(S, K=100.0, T=1.0, r=0.04, sig=0.2, q=0.0):
    """Prix du call de Black et Scholes, avec un dividende continu q."""
    if T <= 0:
        return max(S - K, 0.0)
    d1 = (math.log(S / K) + (r - q + sig * sig / 2) * T) / (sig * math.sqrt(T))
    return S * math.exp(-q * T) * N(d1) - K * math.exp(-r * T) * N(d1 - sig * math.sqrt(T))

KA = 100 * math.exp(-0.04)
f = Figure(xmin=60, xmax=140, ymin=0, ymax=46, w=560, h=320,
           titre="Prix = valeur intrinsèque + valeur temps : 9,93 = 3,92 + 6,00 à 100")
f.axes(xlab="prix de l'action aujourd'hui", ylab="valeur du call", xticks=(60, 80, 96.08, 120, 140),
       yticks=(10, 20, 30, 40), fmt=lambda t: ("%g" % t).replace(".", ","))
f.courbe([(60, 0), (KA, 0), (140, 140 - KA)], couleur=AJOUT, epaisseur=2.2)
f.fonction(bs, 60, 140, couleur=ACCENT, epaisseur=2.6)
f.mesure(100, 100 - KA, bs(100), couleur=ENCRE, etiquette="valeur temps 6,00")
f.point(100, bs(100), couleur=ACCENT)
f.point(100, 100 - KA, couleur=AJOUT)
f.texte(128, bs(128), "prix", couleur=ACCENT, dx=-6, dy=-10, ancre="end", gras=True)
f.texte(114, 114 - KA, "valeur intrinsèque", couleur=AJOUT, dx=8, dy=16, gras=True)
sys.stdout.write(f.svg())
