#!/usr/bin/env python3
r"""
option-americaine.svg — à gauche, le call européen sur l'action sans dividende (strike 100,
un an, r = 4 %, σ = 20 %) reste partout au-dessus du gain d'un exercice immédiat S − 100.
À droite, un call sur une devise dont le taux (6 %) dépasse le taux local (4 %), σ = 10 % :
très dans la monnaie, son prix passe sous X − 100, et exercer tout de suite vaut mieux.

Usage : python courses/fpp/figures/option-americaine.py > option-americaine.svg
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


def cadre(titre, prix, xlab):
    f = Figure(xmin=70, xmax=140, ymin=-2, ymax=44, w=300, h=290, marges=(34, 30, 40, 10))
    f.axes(xlab=xlab, xticks=(80, 100, 120, 140), yticks=(0, 20, 40), fmt=lambda t: "%d" % t)
    f.courbe([(70, 0), (100, 0), (140, 40)], couleur=AJOUT, epaisseur=2)
    f.fonction(prix, 70, 140, couleur=ACCENT, epaisseur=2.6)
    f.texte(105, 44, titre, ancre="middle", dy=-12, gras=True, taille=12)
    return f


g = cadre("action sans dividende", lambda s: bs(s), "action")
g.texte(118, 18, "exercice : S − 100", couleur=AJOUT, dx=4, dy=16, taille=11.5)
g.texte(92, bs(92), "call européen", couleur=ACCENT, ancre="end", dx=-4, dy=-8, taille=11.5)
dev = lambda x: bs(x, sig=0.1, q=0.06)
d = cadre("devise à 6 % contre 4 %", dev, "change")
x0 = next(x / 10 for x in range(1000, 1400) if dev(x / 10) < x / 10 - 100)
d.point(x0, x0 - 100, couleur=ENCRE)
d.texte(x0, x0 - 100, "au-delà, exercer vaut mieux", dx=-6, dy=-10, ancre="end", taille=11.5)
sys.stdout.write(Planche([g, d], ecart=30,
                 titre="Exercer avant l'échéance ne sert à rien sur l'action sans dividende ; sur une devise, parfois").svg())
