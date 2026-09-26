#!/usr/bin/env python3
r"""
formule-black-scholes.svg — le payoff du call décomposé : recevoir l'action si elle finit
au-dessus de 100 (prix S_0 N(d_1) = 61,79), moins recevoir 100 dans le même cas
(prix K e^{−rT} N(d_2) = 51,87), égale le call (9,93). S_0 = K = 100, T = 1, r = 4 %, σ = 20 %.

Usage : python courses/fpp/figures/formule-black-scholes.py > formule-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def cadre(titre, prix, pts, couleur):
    f = Figure(xmin=50, xmax=160, ymin=-10, ymax=170, w=220, h=290, marges=(34, 44, 30, 8))
    f.axes(xticks=(50, 100, 150), yticks=(0, 100), fmt=lambda t: "%d" % t)
    for morceau in pts:
        f.courbe(morceau, couleur=couleur, epaisseur=2.8)
    f.texte(105, 170, titre, ancre="middle", dy=-26, couleur=couleur, gras=True, taille=12)
    f.texte(105, 170, prix, ancre="middle", dy=-10, couleur=ENCRE, taille=12)
    return f


a = cadre("l'action si S_{T} > 100", "vaut 61,79", [[(50, 0), (100, 0)], [(100, 100), (160, 160)]], ACCENT)
b = cadre("100 si S_{T} > 100", "vaut 51,87", [[(50, 0), (100, 0)], [(100, 100), (160, 100)]], AJOUT)
c = cadre("le call", "vaut 9,93", [[(50, 0), (100, 0), (160, 60)]], ENCRE)
sys.stdout.write(Planche([a, b, c], signes=["−", "="], ecart=34,
                 titre="C = S_{0} N(d_{1}) − K e^{−rT} N(d_{2}) : 61,79 − 51,87 = 9,93").svg())
