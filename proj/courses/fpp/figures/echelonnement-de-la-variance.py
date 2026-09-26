#!/usr/bin/env python3
r"""
echelonnement-de-la-variance.svg — l'enveloppe d'un écart type autour du log-prix, pour
une volatilité de 20 % par an : ±20 % √t. Au quart de l'année, elle vaut ±10 %, la moitié
et non le quart ; en pointillé, ce qu'on aurait si les écarts types s'additionnaient.

Usage : python courses/fpp/figures/echelonnement-de-la-variance.py > echelonnement-de-la-variance.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

SIG = 20.0
f = Figure(xmin=0, xmax=1.05, ymin=-24, ymax=24, w=560, h=320,
           titre="L'écart type croît comme la racine du temps : 10 % en trois mois, 20 % en un an")
f.axes(xlab="années", ylab="log-rendement, en %", xticks=(0, 0.25, 0.5, 0.75, 1),
       yticks=(-20, -10, 0, 10, 20), fmt=lambda t: ("%g" % t).replace(".", ","),
       fmt_y=lambda t: "%+d" % t if t else "0", croix=(0, 0))
f.courbe([(0, 0), (1, SIG)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.courbe([(0, 0), (1, -SIG)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.fonction(lambda t: SIG * math.sqrt(t), 0, 1, couleur=ACCENT, epaisseur=2.6, n=200)
f.fonction(lambda t: -SIG * math.sqrt(t), 0, 1, couleur=ACCENT, epaisseur=2.6, n=200)
f.segment(0.25, -10, 0.25, 10)
f.point(0.25, 10, couleur=ACCENT)
f.point(0.25, -10, couleur=ACCENT)
f.texte(0.25, 10, "±10 %", couleur=ACCENT, dx=-6, dy=-8, ancre="end", gras=True)
f.texte(1, 20, "±20 %", couleur=ACCENT, dx=-6, dy=-8, ancre="end", gras=True)
f.point(0.25, 5, couleur=DOUX, r=3)
f.texte(0.25, 5, "et non ±5 %", couleur=DOUX, dx=8, dy=4, taille=12)
f.texte(0.42, -6.2, "pointillé : si les écarts types s'additionnaient", couleur=DOUX, taille=11.5)
sys.stdout.write(f.svg())
