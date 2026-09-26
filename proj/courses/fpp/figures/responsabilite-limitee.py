#!/usr/bin/env python3
r"""
responsabilite-limitee.svg — les capitaux propres à l'échéance en fonction des actifs :
E = max(A − D, 0) ; en pointillé, A − D, ce qu'ils vaudraient sans la règle.

Usage : python courses/fpp/figures/responsabilite-limitee.py > responsabilite-limitee.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

D = 80
f = Figure(xmin=40, xmax=140, ymin=-40, ymax=62, w=560, h=320,
           titre="E = max(A − D, 0) : sous A = D, la perte passe à la dette")
f.axes(xlab="actifs A à l'échéance", ylab="capitaux propres E", xticks=(D,), yticks=(0,),
       fmt=lambda t: "D", fmt_y=lambda t: "0", croix=(40, 0))
f.courbe([(40, -40), (D, 0)], couleur=PALE, epaisseur=1.6, pointilles="5 4")
f.courbe([(40, 0), (D, 0), (140, 60)], couleur=ACCENT, epaisseur=2.8)
f.texte(55, -20, "sans la règle : A − D", couleur=DOUX, taille=12, ancre="middle", dy=-10, fond=True)
f.texte(118, 38, "E = A − D", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.texte(60, 0, "plancher : E = 0", couleur=ACCENT, ancre="middle", dy=-9, gras=True)
sys.stdout.write(f.svg())
