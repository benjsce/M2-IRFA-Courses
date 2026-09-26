#!/usr/bin/env python3
r"""
amelioration-de-rendement.svg — l'action moins le call vendu : un gain plafonné au strike.

L'exemple de la fiche : vendre le call à la monnaie, de strike 100. Posés côte à côte,
l'action détenue, le call vendu et leur différence montrent le geste de la fiche : le
payoff est plafonné là où se situe le strike. La prime encaissée, 9,93, est reçue en $t$
et n'apparaît pas sur ces payoffs à l'échéance.

Usage : python courses/fpp/figures/amelioration-de-rendement.py > amelioration-de-rendement.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

K = 100.0
S0, S1 = 58.0, 142.0


def cadre(titre, g_, couleur, epaisseur=2.4):
    g = Figure(xmin=S0 - 3, xmax=S1 + 3, ymin=-4, ymax=150, w=232, h=260, marges=(34, 26, 40, 12))
    g.axes(xticks=(K,), yticks=(K,), fmt=lambda t: "K", fmt_y=lambda t: "100")
    pts = [(S0, g_(S0)), (K, g_(K)), (S1, g_(S1))]
    g.courbe(pts, couleur=couleur, epaisseur=epaisseur)
    g.point(K, g_(K), couleur=ENCRE, r=3)
    g.texte((S0 + S1) / 2, 150, titre, couleur=couleur, ancre="middle", dy=-2, taille=12.5,
            gras=True)
    return g


p = Planche([cadre("l'action", lambda s: s, DOUX),
             cadre("le call vendu", lambda s: max(s - K, 0.0), AJOUT),
             cadre("le profil détenu", lambda s: min(s, K), ACCENT, 2.8)],
            signes=("−", "="), ecart=34,
            titre="Vendre le call plafonne le payoff au strike ; en échange, la prime est encaissée")
sys.stdout.write(p.svg())
