#!/usr/bin/env python3
r"""
feynman-kac.svg — le prix du call C(t, S) en fonction du prix de l'action pour trois
durées restantes τ₁ > τ₂ > τ₃, puis à l'échéance, où il devient le payoff (S − K)^+. En
remontant le temps, la solution lisse le coude, comme l'équation de la chaleur lisse une
température.

Usage : python courses/fpp/figures/feynman-kac.py > feynman-kac.svg
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
f = Figure(xmin=70, xmax=130, ymin=0, ymax=34, w=560, h=320,
           titre="En remontant le temps, la solution lisse le payoff (S − K)^+")
f.axes(xlab="S", ylab="C(t, S)", xticks=(100,), fmt=lambda t: "K")
f.courbe([(70, 0), (100, 0), (130, 30)], couleur=ENCRE, epaisseur=2.2)
for T, c, lab in ((0.25, AJOUT, "τ_{3}"), (0.5, DOUX, "τ_{2}"), (1.0, ACCENT, "τ_{1}")):
    f.fonction(lambda s, T=T: bs(s, T=T), 70, 130, couleur=c, epaisseur=2.2)
    f.texte(100, bs(100, T=T), lab, couleur=c, ancre="end", dx=-8, dy=4, taille=12, gras=True)
f.texte(112, 12, "en T : (S − K)^{+}", couleur=ENCRE, dx=10, dy=16, taille=12)
f.texte(73, 30, "durées restantes τ_{1} > τ_{2} > τ_{3}", couleur=DOUX, taille=12)
sys.stdout.write(f.svg())
