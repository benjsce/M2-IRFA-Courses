#!/usr/bin/env python3
r"""
produit-a-capital-garanti.svg — 100 investis pour un an à 4 % : un zéro-coupon de 96,08
rend 100 à coup sûr ; le coussin de 3,92 achète 3,92 / 9,93 = 0,395 call à la monnaie.
Ensemble, le paiement ne descend jamais sous 100 et reverse 39,5 % de la hausse.

Usage : python courses/fpp/figures/produit-a-capital-garanti.py > produit-a-capital-garanti.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

K = 0.395


def cadre(titre, g, couleur):
    f = Figure(xmin=60, xmax=150, ymin=-4, ymax=128, w=230, h=270, marges=(34, 30, 36, 8))
    f.axes(xlab="action à T", xticks=(60, 100, 140), yticks=(0, 50, 100), fmt=lambda t: "%d" % t)
    f.courbe([(60, g(60)), (100, g(100)), (150, g(150))], couleur=couleur, epaisseur=2.8)
    f.texte(105, 128, titre, ancre="middle", dy=-12, couleur=couleur, gras=True, taille=12)
    return f


a = cadre("zéro-coupon : 100", lambda s: 100, AJOUT)
b = cadre("0,395 call", lambda s: K * max(s - 100, 0), ACCENT)
c = cadre("capital garanti", lambda s: 100 + K * max(s - 100, 0), ENCRE)
c.texte(150, 100 + K * 50, "+39,5 % de la hausse", couleur=ENCRE, ancre="end", dy=-10, taille=11.5)
sys.stdout.write(Planche([a, b, c], signes=["+", "="], ecart=30,
                 titre="Zéro-coupon + calls : jamais moins de 100, et 39,5 % de la hausse").svg())
