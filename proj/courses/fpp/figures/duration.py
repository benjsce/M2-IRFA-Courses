#!/usr/bin/env python3
r"""
duration.svg — le prix d'un zéro-coupon à deux ans, P(2, r) = e^{−2r}, et sa tangente à
5 % : pente −2 × 0,9048 ≈ −1,81, soit une perte relative de 2 fois la hausse du taux.

Usage : python courses/fpp/figures/duration.py > duration.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

T, R0 = 2, 0.05
P0 = math.exp(-T * R0)
f = Figure(xmin=0, xmax=0.30, ymin=0.5, ymax=1.02, w=560, h=320,
           titre="∂P/∂r = −t P : à 5 %, la pente vaut −2 × 0,9048")
f.axes(xlab="taux r", ylab="P(2, r)", xticks=(0, 0.05, 0.10, 0.20, 0.30),
       yticks=(0.6, 0.7, 0.8, 0.9, 1.0), fmt=lambda t: ("%g %%" % (100 * t)).replace(".", ","),
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))
f.fonction(lambda r: math.exp(-T * r), 0, 0.30, couleur=ACCENT, epaisseur=2.6)
f.courbe([(0.0, P0 - T * P0 * (0.0 - R0)), (0.25, P0 - T * P0 * (0.25 - R0))],
         couleur=AJOUT, epaisseur=1.8)
f.segment(R0, 0.5, R0, P0)
f.point(R0, P0, couleur=ENCRE)
f.texte(R0, P0, "0,9048", dx=8, dy=-8, gras=True)
f.texte(0.2, P0 - T * P0 * (0.2 - R0), "tangente, pente −1,81", couleur=AJOUT, dx=-6, dy=18, ancre="end", gras=True)
f.texte(0.2, math.exp(-T * 0.2), "P(2, r) = e^{−2r}", couleur=ACCENT, dx=6, dy=-12)
sys.stdout.write(f.svg())
