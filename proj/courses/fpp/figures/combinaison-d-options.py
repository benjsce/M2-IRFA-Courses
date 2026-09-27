#!/usr/bin/env python3
r"""
combinaison-d-options.svg — les deux identités de la Forme, une par ligne, lues de gauche
à droite comme des sommes de payoffs.

Straddle : le call (S_T − K)⁺ plus le put (K − S_T)⁺ de même strike font |S_T − K|.
Call spread : le call de strike K₁ moins le call de strike K₂ > K₁ fait un payoff qui
monte de K₁ à K₂ puis plafonne. Aucune valeur numérique : les axes ne portent que les
strikes.

Usage : python courses/fpp/figures/combinaison-d-options.py > combinaison-d-options.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, Colonne, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

p = lambda x: max(x, 0.0)
K, K1, K2 = 100, 90, 110


def cadre(g, couleur, ticks, formule, nom):
    f = Figure(xmin=70, xmax=130, ymin=-5, ymax=42, w=190, h=190, marges=(8, 26, 44, 6))
    f.axes(xticks=tuple(ticks), fmt=lambda t: ticks[t], croix=(70, 0))
    f.courbe([(s / 2, g(s / 2)) for s in range(140, 261)], couleur=couleur, epaisseur=2.6)
    f.texte(100, 42, nom, ancre="middle", dy=-10, couleur=couleur, gras=True, taille=12.5)
    f.texte(100, -5, formule, ancre="middle", dy=30, couleur=couleur, taille=12.5)
    return f


straddle = Planche([
    cadre(lambda s: p(s - K), ACCENT, {K: "K"}, "(S_{T} − K)^{+}", "call"),
    cadre(lambda s: p(K - s), AJOUT, {K: "K"}, "(K − S_{T})^{+}", "put"),
    cadre(lambda s: abs(s - K), ENCRE, {K: "K"}, "|S_{T} − K|", "straddle"),
], signes=("+", "="), ecart=30)
spread = Planche([
    cadre(lambda s: p(s - K1), ACCENT, {K1: "K₁"}, "(S_{T} − K_{1})^{+}", "call de strike K₁"),
    cadre(lambda s: p(s - K2), AJOUT, {K2: "K₂"}, "(S_{T} − K_{2})^{+}", "call de strike K₂"),
    cadre(lambda s: p(s - K1) - p(s - K2), ENCRE, {K1: "K₁", K2: "K₂"},
          "(S_{T} − K_{1})^{+} − (S_{T} − K_{2})^{+}", "call spread"),
], signes=("−", "="), ecart=30)
sys.stdout.write(Colonne([straddle, spread],
                         intitules=["Straddle : call + put de même strike",
                                    "Call spread : call de strike K₁ − call de strike K₂"],
                         titre="Les deux combinaisons de la Forme, lues comme des sommes de payoffs").svg())
