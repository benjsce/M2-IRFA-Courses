#!/usr/bin/env python3
r"""
effet-de-levier.svg — actifs et capitaux propres dans le plan volatilité–prime : le
levier de 5 pousse le point cinq fois plus loin sur la même demi-droite.

Actifs : σ_A = 4 %, π_A = 2 %. Capitaux propres : σ_E = 20 %, π_E = 10 %.

Usage : python courses/fpp/figures/effet-de-levier.py > effet-de-levier.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

L = 5
SA, PA = 4.0, 2.0
f = Figure(xmin=0, xmax=25, ymin=0, ymax=12.5, w=560, h=320,
           titre="Le levier multiplie par 5 la volatilité et la prime : même demi-droite, cinq fois plus loin")
f.axes(xlab="volatilité, en %", ylab="prime espérée, en %", xticks=(0, 4, 10, 15, 20, 25),
       yticks=(2, 4, 6, 8, 10, 12), fmt=lambda t: "%d" % t)
f.courbe([(0, 0), (24, 12)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.segment(SA, 0, SA, PA)
f.segment(0, PA, SA, PA)
f.segment(L * SA, 0, L * SA, L * PA)
f.segment(0, L * PA, L * SA, L * PA)
f.fleche(SA + 0.8, PA + 0.4, L * SA - 0.8, L * PA - 0.4, couleur=DOUX, epaisseur=1.3)
f.point(SA, PA, couleur=AJOUT, r=5)
f.point(L * SA, L * PA, couleur=ACCENT, r=5)
f.texte(SA, PA, "actifs (4 % ; 2 %)", couleur=AJOUT, dx=10, dy=18, gras=True)
f.texte(L * SA, L * PA, "capitaux propres (20 % ; 10 %)", couleur=ACCENT, ancre="end",
        dx=-10, dy=-10, gras=True)
f.texte(12, 6, "× 5", couleur=DOUX, ancre="middle", dx=-14, dy=-6, fond=True)

sys.stdout.write(f.svg())
