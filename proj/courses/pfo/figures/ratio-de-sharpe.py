#!/usr/bin/env python3
r"""
ratio-de-sharpe.svg — le ratio de Sharpe est une pente, lue depuis l'actif sans risque.

L'exemple de la fiche : $R_f=2\,\%$, deux actifs de rendements 6 % et 10 % et de
volatilités 10 % et 20 %, non corrélés. Les deux actifs sont sur la même droite issue de
$(0 ; 2\,\%)$ : même pente, même ratio, 0,40. Leur mélange à parts égales, à 11,18 % de
volatilité pour 8 %, est sur une droite plus raide : 0,54.

Usage : python courses/pfo/figures/ratio-de-sharpe.py > ratio-de-sharpe.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

RF = 2.0
A1, A2 = (10.0, 6.0), (20.0, 10.0)
MIX = (math.sqrt(0.25 * 100 + 0.25 * 400), 8.0)          # (11,18 ; 8)
fr = lambda v: ("%.2f" % v).replace(".", ",")

f = Figure(xmin=0, xmax=23, ymin=0, ymax=12, w=560, h=330,
           titre="Les deux actifs ont la même pente, 0,40 ; leur mélange, une pente plus raide")
f.axes(xlab="volatilité σp, en %", ylab="rendement, en %", xticks=(0, 10, 11.18, 20),
       yticks=(2, 6, 8, 10), fmt=lambda t: ("%g" % t).replace(".", ","),
       fmt_y=lambda t: "%d" % t)

pente = lambda p: (p[1] - RF) / p[0]
f.fonction(lambda s: RF + pente(A1) * s, 0, 22, couleur=DOUX, epaisseur=1.8)
f.fonction(lambda s: RF + pente(MIX) * s, 0, 17.5, couleur=ACCENT, epaisseur=2.2)
f.point(0, RF, couleur=ENCRE)
f.texte(0, RF, "sans risque", couleur=ENCRE, dx=8, dy=16, taille=11.5)
for p, nom in ((A1, "actif 1"), (A2, "actif 2")):
    f.point(p[0], p[1], couleur=DOUX, r=4.2)
    f.texte(p[0], p[1], nom, couleur=DOUX, dx=8, dy=16, taille=11.5, gras=True)
f.point(MIX[0], MIX[1], couleur=ACCENT, r=4.5)
f.texte(MIX[0], MIX[1], "parts égales", couleur=ACCENT, ancre="end", dx=-8, dy=-6, gras=True,
        fond=True)
f.texte(15, RF + pente(A1) * 15, "pente " + fr(pente(A1)), couleur=DOUX, ancre="middle",
        dy=20, gras=True, fond=True)
f.texte(17.5, RF + pente(MIX) * 17.5, "pente " + fr(pente(MIX)), couleur=ACCENT,
        ancre="end", dx=-6, dy=-6, gras=True, fond=True)

sys.stdout.write(f.svg())
