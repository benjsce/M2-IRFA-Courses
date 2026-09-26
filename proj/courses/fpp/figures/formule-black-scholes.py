#!/usr/bin/env python3
r"""
formule-black-scholes.svg — le payoff du call décomposé : recevoir l'action si S_T > K
(prix S₀ N(d₁)), moins recevoir K dans le même cas (prix K e^{−rT} N(d₂)), égale le call.

Usage : python courses/fpp/figures/formule-black-scholes.py > formule-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402


def cadre(titre, prix, pts, couleur):
    f = Figure(xmin=50, xmax=160, ymin=-10, ymax=170, w=230, h=300, marges=(20, 44, 42, 8))
    f.axes(xlab="S(T)", xticks=(100,), yticks=(100,), fmt=lambda t: "K", fmt_y=lambda t: "K")
    for morceau in pts:
        f.courbe(morceau, couleur=couleur, epaisseur=2.8)
    f.texte(105, 170, titre, ancre="middle", dy=-26, couleur=couleur, gras=True, taille=12)
    f.texte(105, 170, prix, ancre="middle", dy=-10, couleur=ENCRE, taille=12)
    return f


a = cadre("S_{T} si S_{T} > K", "vaut S_{0} N(d_{1})", [[(50, 0), (100, 0)], [(100, 100), (160, 160)]], ACCENT)
b = cadre("K si S_{T} > K", "vaut K e^{−rT} N(d_{2})", [[(50, 0), (100, 0)], [(100, 100), (160, 100)]], AJOUT)
c = cadre("le call (S_{T} − K)^{+}", "vaut C", [[(50, 0), (100, 0), (160, 60)]], ENCRE)
sys.stdout.write(Planche([a, b, c], signes=["−", "="], ecart=34,
                 titre="C = S_0 N(d_1) − K e^{−rT} N(d_2)").svg())
