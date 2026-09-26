#!/usr/bin/env python3
r"""
option-americaine.svg — à gauche, le call européen sur une action sans dividende reste
partout au-dessus du gain d'un exercice immédiat, S − K. À droite, un call sur une devise
dont le taux dépasse le taux local : très dans la monnaie, son prix passe sous X − K, et
exercer tout de suite vaut mieux.

Usage : python courses/fpp/figures/option-americaine.py > option-americaine.svg
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


def cadre(titre, prix, xlab, lab_ex):
    f = Figure(xmin=70, xmax=140, ymin=-2, ymax=44, w=300, h=290, marges=(20, 30, 40, 10))
    f.axes(xlab=xlab, xticks=(100,), fmt=lambda t: "K")
    f.courbe([(70, 0), (100, 0), (140, 40)], couleur=AJOUT, epaisseur=2)
    f.fonction(prix, 70, 140, couleur=ACCENT, epaisseur=2.6)
    f.texte(105, 44, titre, ancre="middle", dy=-12, gras=True, taille=12)
    f.texte(118, 18, lab_ex, couleur=AJOUT, dx=4, dy=16, taille=11.5)
    return f


g = cadre("action sans dividende", lambda s: bs(s), "S", "exercice : S − K")
g.texte(92, bs(92), "call européen", couleur=ACCENT, ancre="end", dx=-4, dy=-8, taille=11.5)
dev = lambda x: bs(x, sig=0.1, q=0.06)
d = cadre("devise, taux étranger > taux local", dev, "X", "exercice : X − K")
x0 = next(x / 10 for x in range(1000, 1400) if dev(x / 10) < x / 10 - 100)
d.point(x0, x0 - 100, couleur=ENCRE)
d.texte(x0, x0 - 100, "au-delà, exercer vaut mieux", dx=-6, dy=-10, ancre="end", taille=11.5)
sys.stdout.write(Planche([g, d], ecart=30,
                 titre="Exercer avant l'échéance ne sert à rien sur l'action sans dividende ; sur une devise, parfois").svg())
