#!/usr/bin/env python3
r"""
tendance-risque-neutre.svg — trois trajectoires moyennes de l'action à 100 sur un an :
sous P, à la tendance réelle de 8 % (108,33) ; sous Q sans dividende, à r = 4 % (104,08) ;
sous Q avec un dividende continu de 2 %, à r − d = 2 % (102,02).

Usage : python courses/fpp/figures/tendance-risque-neutre.py > tendance-risque-neutre.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=0, xmax=1.62, ymin=99, ymax=109.5, w=560, h=320,
           titre="Sous Q, la tendance ne dépend que de r − d : 4 % sans dividende, 2 % avec")
f.axes(xlab="années", ylab="espérance du prix", xticks=(0, 0.5, 1), yticks=(100, 102, 104, 106, 108),
       fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: "%d" % t)
for mu, c, lab, ep in ((0.08, DOUX, "sous P, μ = 8 % : 108,33", 2),
                       (0.04, ACCENT, "sous Q, r = 4 % : 104,08", 2.6),
                       (0.02, AJOUT, "sous Q, r − d = 2 % : 102,02", 2.6)):
    f.fonction(lambda t, mu=mu: 100 * math.exp(mu * t), 0, 1, couleur=c, epaisseur=ep,
               pointilles="6 4" if c == DOUX else None)
    f.texte(1, 100 * math.exp(mu), lab, couleur=c, dx=8, dy=4, taille=12, gras=c != DOUX)
sys.stdout.write(f.svg())
