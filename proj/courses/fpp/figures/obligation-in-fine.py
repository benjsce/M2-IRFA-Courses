#!/usr/bin/env python3
r"""
obligation-in-fine.svg — le prix d'une obligation de coupon 5 % sur deux ans en fonction
du taux du marché (actuariel) : 1 exactement à 5 %, 1,0189 à 4 %, 0,9817 à 6 %.

Usage : python courses/fpp/figures/obligation-in-fine.py > obligation-in-fine.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

RS, N = 0.05, 2


def B(r):
    return RS * sum((1 + r) ** -i for i in range(1, N + 1)) + (1 + r) ** -N


f = Figure(xmin=0, xmax=0.10, ymin=0.9, ymax=1.11, w=560, h=320,
           titre="Coupon 5 % : au-dessus du pair si le marché est sous 5 %, en dessous sinon")
f.axes(xlab="taux du marché r", ylab="prix B(5 %, r)", xticks=(0, 0.02, 0.04, 0.05, 0.06, 0.08, 0.10),
       yticks=(0.95, 1.0, 1.05, 1.1), fmt=lambda t: ("%g %%" % (100 * t)).replace(".", ","),
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))
f.segment(0, 1, 0.10, 1)
f.segment(0.05, 0.9, 0.05, 1)
f.fonction(B, 0, 0.10, couleur=ACCENT, epaisseur=2.6)
for r in (0.04, 0.06):
    f.point(r, B(r), couleur=ACCENT)
f.point(0.05, 1, couleur=ENCRE)
f.texte(0.04, B(0.04), "1,0189", couleur=ACCENT, dx=8, dy=-8, gras=True)
f.texte(0.06, B(0.06), "0,9817", couleur=ACCENT, dx=-8, dy=16, ancre="end", gras=True)
f.texte(0.003, 1.0, "au-dessus du pair", couleur=DOUX, dy=-8, taille=12)
f.texte(0.097, 1.0, "en dessous du pair", couleur=DOUX, ancre="end", dy=17, taille=12)
f.texte(0.05, 1, "au pair", couleur=ENCRE, dx=8, dy=-8, taille=12)
sys.stdout.write(f.svg())
