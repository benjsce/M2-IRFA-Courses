#!/usr/bin/env python3
r"""
tendance-risque-neutre.svg — trois trajectoires moyennes de l'action : S₀ e^{μt} sous P,
S₀ e^{rt} sous Q sans dividende, S₀ e^{(r−d)t} sous Q avec un dividende continu d.

Usage : python courses/fpp/figures/tendance-risque-neutre.py > tendance-risque-neutre.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
f = Figure(xmin=0, xmax=1.62, ymin=99, ymax=109.5, w=560, h=320,
           titre="Sous Q, la tendance ne dépend que de r − d, pas de la tendance réelle μ")
f.axes(xlab="temps", ylab="espérance du prix", xticks=(0,), yticks=(100,), fmt=lambda t: "0",
       fmt_y=lambda t: "S₀")
for mu, c, lab, ep in ((0.08, DOUX, "sous P : S_{0} e^{μt}", 2),
                       (0.04, ACCENT, "sous Q : S_{0} e^{rt}", 2.6),
                       (0.02, AJOUT, "sous Q, dividende d : S_{0} e^{(r − d)t}", 2.6)):
    f.fonction(lambda t, mu=mu: 100 * math.exp(mu * t), 0, 1, couleur=c, epaisseur=ep,
               pointilles="6 4" if c == DOUX else None)
    f.texte(1, 100 * math.exp(mu), lab, couleur=c, dx=8, dy=4, taille=12, gras=c != DOUX)
sys.stdout.write(f.svg())
