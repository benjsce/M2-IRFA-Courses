#!/usr/bin/env python3
r"""
payoff.svg — deux payoffs élémentaires qui s'additionnent en un troisième.

La fiche dit que les payoffs élémentaires se combinent, et cite le straddle : un call et
un put de même strike, achetés ensemble. Posés côte à côte, le call, le put et leur somme
montrent le geste de la fiche — le point de rupture unique, au strike, dit qu'il faut une
option de chaque côté. Strike 100, comme dans l'exemple.

Usage : python courses/fpp/figures/payoff.py > payoff.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

K = 100.0
S0, S1 = 58.0, 142.0


def cadre(titre, g_, couleur, epaisseur=2.4):
    g = Figure(xmin=S0 - 3, xmax=S1 + 3, ymin=-8, ymax=50, w=232, h=260, marges=(34, 26, 40, 12))
    g.axes(xticks=(K,), yticks=(0, 40), fmt=lambda t: "K" if t == K else str(int(t)))
    g.courbe([(S0, g_(S0)), (K, g_(K)), (S1, g_(S1))], couleur=couleur, epaisseur=epaisseur)
    g.point(K, g_(K), couleur=ENCRE, r=3)
    g.texte((S0 + S1) / 2, 50, titre, couleur=couleur, ancre="middle", dy=-2, taille=12.5,
            gras=True)
    return g


p = Planche([cadre("le call", lambda s: max(s - K, 0.0), DOUX),
             cadre("le put", lambda s: max(K - s, 0.0), AJOUT),
             cadre("le straddle", lambda s: abs(s - K), ACCENT, 2.8)],
            signes=("+", "="), ecart=34,
            titre="Un call plus un put de même strike : le straddle, qui paie dans les deux sens")
sys.stdout.write(p.svg())
