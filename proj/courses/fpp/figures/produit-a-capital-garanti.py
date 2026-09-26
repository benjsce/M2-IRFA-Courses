#!/usr/bin/env python3
r"""
produit-a-capital-garanti.svg — un zéro-coupon qui rend V₀ en T coûte V₀ e^{−rT} ; le
coussin C₀ = V₀(1 − e^{−rT}) achète des calls, soit une participation k = C₀ / (V₀ Call).
Ensemble : jamais moins que V₀, et k fois la hausse relative de l'action.

Usage : python courses/fpp/figures/produit-a-capital-garanti.py > produit-a-capital-garanti.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
K = 0.395


def cadre(titre, g, couleur, prix):
    f = Figure(xmin=60, xmax=150, ymin=-4, ymax=128, w=240, h=340, marges=(24, 30, 106, 8))
    f.axes(xlab="S(T)", xticks=(100,), yticks=(100,), fmt=lambda t: "S₀", fmt_y=lambda t: "V₀")
    f.courbe([(60, g(60)), (100, g(100)), (150, g(150))], couleur=couleur, epaisseur=2.8)
    f.texte(105, 128, titre, ancre="middle", dy=-12, couleur=couleur, gras=True, taille=12)
    f.texte(105, -4, prix, ancre="middle", dy=56, couleur=couleur, taille=12)
    return f


a = cadre("zéro-coupon : V_{0}", lambda s: 100, AJOUT, "coûte V_{0} e^{−rT}")
b = cadre("k V_{0} (S_{T}/S_{0} − 1)^{+}", lambda s: K * max(s - 100, 0), ACCENT, "coûte le coussin C_{0}")
c = cadre("capital garanti", lambda s: 100 + K * max(s - 100, 0), ENCRE, "coûte V_{0}")
b.texte(105, -4, "C_{0} = V_{0}(1 − e^{−rT}),  k = C_{0} / (V_{0} Call(S_{0} = 1, K = 1))", ancre="middle", dy=86,
        couleur=ENCRE, gras=True, taille=12.5)
sys.stdout.write(Planche([a, b, c], signes=["+", "="], ecart=30,
                 titre="Zéro-coupon + calls : jamais moins que V_0, et une part k de la hausse").svg())
