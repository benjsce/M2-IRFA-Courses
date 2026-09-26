#!/usr/bin/env python3
r"""
formule-d-ito.svg — le prix du call C(S) et sa tangente en S. Pour un mouvement ±ΔS de
l'action, la moyenne de C(S − ΔS) et C(S + ΔS) dépasse C(S) : la tangente prévoit une
moyenne inchangée, la courbure ajoute ½ ∂²C/∂S² ΔS², le terme propre à la formule d'Itô.

Usage : python courses/fpp/figures/formule-d-ito.py > formule-d-ito.svg
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
m = (bs(90) + bs(110)) / 2
f = Figure(xmin=80, xmax=120, ymin=2, ymax=20, w=560, h=320,
           titre="Un mouvement ±ΔS fait gagner en moyenne ce que la tangente ne voit pas : ½ ∂²C/∂S² ΔS²")
f.axes(xlab="S", ylab="C", xticks=(90, 100, 110), fmt=lambda t: {90: "S − ΔS", 100: "S", 110: "S + ΔS"}[t])
f.fonction(bs, 80, 120, couleur=ACCENT, epaisseur=2.6)
f.courbe([(85, bs(100) - 15 * D), (117, bs(100) + 17 * D)], couleur=DOUX, epaisseur=1.5)
f.courbe([(90, bs(90)), (110, bs(110))], couleur=AJOUT, epaisseur=1.8)
for s in (90, 110):
    f.point(s, bs(s), couleur=ACCENT)
f.point(100, bs(100), couleur=ENCRE)
f.point(100, m, couleur=AJOUT, r=4.5)
f.mesure(101.2, bs(100), m, couleur=AJOUT, etiquette="½ ∂²C/∂S² ΔS²")
f.texte(100, bs(100), "C(S)", dx=8, dy=16, gras=True)
f.texte(100, m, "moyenne de C(S ± ΔS)", couleur=AJOUT, dx=-8, dy=-8, ancre="end", taille=12)
sys.stdout.write(f.svg())
