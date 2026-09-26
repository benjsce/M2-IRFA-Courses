#!/usr/bin/env python3
r"""
parite-call-put.svg — payoff du call, moins payoff du put de même strike 100, égale la
droite S_T − 100, le payoff d'un achat à terme au prix 100.

Usage : python courses/fpp/figures/parite-call-put.py > parite-call-put.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def cadre(titre, g, couleur):
    f = Figure(xmin=50, xmax=150, ymin=-52, ymax=52, w=220, h=280, marges=(30, 30, 30, 8))
    f.axes(xticks=(50, 100, 150), yticks=(-50, 0, 50), fmt=lambda t: "%d" % t, croix=(50, 0))
    f.courbe([(x, g(x)) for x in (50, 100, 150)], couleur=couleur, epaisseur=2.8)
    f.texte(100, 52, titre, ancre="middle", dy=-12, couleur=couleur, gras=True, taille=12)
    return f


a = cadre("call (S_{T} − 100)^{+}", lambda s: max(s - 100, 0), ACCENT)
b = cadre("put (100 − S_{T})^{+}", lambda s: max(100 - s, 0), AJOUT)
c = cadre("achat à terme S_{T} − 100", lambda s: s - 100, ENCRE)
sys.stdout.write(Planche([a, b, c], signes=["−", "="], ecart=34,
                 titre="Call moins put de même strike : un achat à terme au prix du strike").svg())
