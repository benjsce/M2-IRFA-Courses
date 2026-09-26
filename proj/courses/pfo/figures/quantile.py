#!/usr/bin/env python3
r"""
quantile.svg — lire un quantile sur la fonction de répartition.

L'exemple de la fiche : des rendements normaux de moyenne 0,05 % et d'écart type 2 %. Le
quantile d'ordre 5 % se lit en partant de 0,05 sur l'axe vertical, jusqu'à la courbe, puis
en descendant sur l'axe des rendements : $-3{,}24\,\%$, soit
$0{,}05\,\%-1{,}6449\times2\,\%$.

Usage : python courses/pfo/figures/quantile.py > quantile.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

LOI = NormalDist(0.05, 2.0)
ALPHA = 0.05
Q = LOI.inv_cdf(ALPHA)                       # -3,24

f = Figure(xmin=-7, xmax=7, ymin=0, ymax=1.06, w=560, h=320,
           titre="Le quantile d'ordre 5 % laisse 5 % des rendements à sa gauche")
f.axes(xlab="rendement, en %", ylab="F", xticks=(-6, Q, 0, 2, 4, 6), yticks=(ALPHA, 0.5, 1),
       fmt=lambda t: ("%.2f" % t if abs(t - Q) < 1e-9 else "%d" % t).replace(".", ",").replace("-", "−"),
       fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(-7, 0))

f.fonction(LOI.cdf, -7, 7, n=300, couleur=ACCENT, epaisseur=2.6)
f.courbe([(-7, ALPHA), (Q, ALPHA)], couleur=AJOUT, epaisseur=1.6)
f.fleche(Q, ALPHA, Q, 0.004, couleur=AJOUT, epaisseur=1.6)
f.point(Q, ALPHA, couleur=AJOUT)
f.texte(Q, ALPHA, "F(q) = 0,05", couleur=AJOUT, dx=10, dy=4, gras=True, fond=True)

sys.stdout.write(f.svg())
