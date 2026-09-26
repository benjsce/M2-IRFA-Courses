#!/usr/bin/env python3
r"""
payoff.svg — le payoff du call (S_T − K)^+ et celui du put (K − S_T)^+, côte à côte.

Usage : python courses/fpp/figures/payoff.py > payoff.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402


def cadre(titre, g, couleur):
    f = Figure(xmin=50, xmax=150, ymin=-5, ymax=52, w=290, h=260, marges=(20, 26, 36, 10))
    f.axes(xlab="S(T)", xticks=(100,), yticks=(0,), fmt=lambda t: "K", fmt_y=lambda t: "0")
    f.courbe([(x, g(x)) for x in (50, 100, 150)], couleur=couleur, epaisseur=2.8)
    f.texte(100, 52, titre, ancre="middle", dy=-10, couleur=couleur, gras=True)
    return f


call = cadre("call : (S_{T} − K)^{+}", lambda s: max(s - 100, 0), ACCENT)
put = cadre("put : (K − S_{T})^{+}", lambda s: max(100 - s, 0), AJOUT)
sys.stdout.write(Planche([call, put], ecart=34,
                 titre="Le call paie au-dessus du strike K, le put en dessous, jamais un montant négatif").svg())
