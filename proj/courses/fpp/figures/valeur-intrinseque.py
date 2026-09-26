#!/usr/bin/env python3
r"""
valeur-intrinseque.svg — la valeur intrinsèque d'un call de strike 100 : dans un monde sans
aléa, l'action vaudrait à coup sûr son prix forward, 104,08 ; le call paierait 4,08 dans un
an, soit 4,08 × 0,9608 = 3,92 aujourd'hui.

Usage : python courses/fpp/figures/valeur-intrinseque.py > valeur-intrinseque.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

F = 100 / math.exp(-0.04)
f = Figure(xmin=-0.35, xmax=1.45, ymin=97, ymax=107.5, w=560, h=300,
           titre="Sans aléa, le call paierait F − K = 4,08 dans un an : il vaudrait 3,92 aujourd'hui")
f.axes(xlab="temps", ylab="prix de l'action", xticks=(0, 1), yticks=(100, 104.08),
       fmt=lambda t: "t" if t == 0 else "T", fmt_y=lambda t: ("%g" % t).replace(".", ","),
       croix=(-0.35, 97))
f.segment(-0.35, 100, 1.4, 100)
f.texte(1.4, 100, "strike 100", couleur=DOUX, ancre="end", dy=16, taille=12)
f.courbe([(0, 100), (1, F)], couleur=ACCENT, epaisseur=2.4, pointilles="6 4")
f.texte(0.5, 102, "à coup sûr, le prix forward", couleur=ACCENT, ancre="middle", dy=-12, taille=12)
f.mesure(1.05, 100, F, couleur=AJOUT, etiquette="payoff 4,08")
f.fleche(1.0, 106.2, 0.05, 106.2, couleur=AJOUT, courbure=12)
f.texte(0.0, 106.2, "IV = 4,08 × 0,9608 = 3,92", couleur=AJOUT, dx=-4, dy=-14, gras=True)
sys.stdout.write(f.svg())
