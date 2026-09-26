#!/usr/bin/env python3
r"""
formule-d-ito.svg — le prix du call (strike 100, un an, r = 4 %, σ = 20 %) et sa tangente
en 100. Pour un mouvement de ±10 de l'action, la moyenne des deux prix obtenus dépasse le
prix de départ : la tangente seule prévoit une moyenne inchangée, la courbure ajoute
environ ½ γ ΔS², le terme propre à la formule d'Itô.

Usage : python courses/fpp/figures/formule-d-ito.py > formule-d-ito.svg
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

D = N(d1(100))
m = (bs(90) + bs(110)) / 2
f = Figure(xmin=80, xmax=120, ymin=2, ymax=20, w=560, h=320,
           titre="Un mouvement de ±10 fait gagner en moyenne ce que la tangente ne voit pas : la courbure")
f.axes(xlab="prix de l'action", ylab="prix du call", xticks=(80, 90, 100, 110, 120),
       yticks=(5, 10, 15), fmt=lambda t: "%d" % t)
f.fonction(bs, 80, 120, couleur=ACCENT, epaisseur=2.6)
f.courbe([(85, bs(100) - 15 * D), (117, bs(100) + 17 * D)], couleur=DOUX, epaisseur=1.5)
f.courbe([(90, bs(90)), (110, bs(110))], couleur=AJOUT, epaisseur=1.8)
for s in (90, 110):
    f.point(s, bs(s), couleur=ACCENT)
f.point(100, bs(100), couleur=ENCRE)
f.point(100, m, couleur=AJOUT, r=4.5)
f.mesure(101.2, bs(100), m, couleur=AJOUT, etiquette="courbure : ½ γ ΔS²")
f.texte(100, bs(100), "9,93", dx=8, dy=16, gras=True)
sys.stdout.write(f.svg())
