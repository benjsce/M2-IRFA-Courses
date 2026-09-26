#!/usr/bin/env python3
r"""
parite-call-put.svg — payoff du call, moins payoff du put de même strike K, égale la
droite S_T − K, le payoff d'un achat à terme au prix K. Mêmes paiements, mêmes prix :
C − P = S₀ − K P(0,T).

Usage : python courses/fpp/figures/parite-call-put.py > parite-call-put.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402


def cadre(titre, g, couleur, prix):
    f = Figure(xmin=50, xmax=150, ymin=-52, ymax=52, w=220, h=330, marges=(20, 30, 80, 8))
    f.axes(xticks=(100,), fmt=lambda t: "K", croix=(50, 0))
    f.courbe([(x, g(x)) for x in (50, 100, 150)], couleur=couleur, epaisseur=2.8)
    f.texte(100, 52, titre, ancre="middle", dy=-12, couleur=couleur, gras=True, taille=12)
    f.texte(100, -52, prix, ancre="middle", dy=22, couleur=couleur, taille=12)
    return f


a = cadre("call (S_{T} − K)^{+}", lambda s: max(s - 100, 0), ACCENT, "prix aujourd'hui : C")
b = cadre("put (K − S_{T})^{+}", lambda s: max(100 - s, 0), AJOUT, "prix aujourd'hui : P")
c = cadre("achat à terme S_{T} − K", lambda s: s - 100, ENCRE, "prix : S_{0} − K P(0,T)")
b.texte(100, -52, "mêmes paiements, mêmes prix : C − P = S_{0} − K P(0,T)", ancre="middle", dy=52,
        couleur=ENCRE, gras=True, taille=12.5)
sys.stdout.write(Planche([a, b, c], signes=["−", "="], ecart=34,
                 titre="Call moins put de même strike : un achat à terme au prix du strike").svg())
