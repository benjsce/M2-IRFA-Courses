#!/usr/bin/env python3
r"""
responsabilite-limitee.svg — les deux moitiés de la Forme sur un même dessin. Les capitaux
propres à l'échéance en fonction des actifs : E = max(A − D, 0), et en pointillé A − D, ce
qu'ils vaudraient sans la règle. Sous l'axe, l'écart entre les actifs d'aujourd'hui A_t et
la dette D est E_t : une baisse relative de E_t / A_t = 1 / l_t suffit à la faillite.

Usage : python courses/fpp/figures/responsabilite-limitee.py > responsabilite-limitee.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

D, A = 80, 100          # la dette, et les actifs d'aujourd'hui ; aucun nombre n'est écrit
f = Figure(xmin=40, xmax=140, ymin=-46, ymax=62, w=560, h=360,
           titre="E = max(A − D, 0), et la faillite dès que les actifs perdent plus que E_t / A_t = 1 / l_t")
f.axes(xlab="actifs à l'échéance", ylab="capitaux propres E", xticks=(D, A), yticks=(0,),
       fmt=lambda t: {D: "D", A: "Aₜ"}[t], fmt_y=lambda t: "0", croix=(40, 0))
f.courbe([(40, -40), (D, 0)], couleur=PALE, epaisseur=1.6, pointilles="5 4")
f.courbe([(40, 0), (D, 0), (140, 60)], couleur=ACCENT, epaisseur=2.8)
f.texte(55, -20, "sans la règle : A − D", couleur=DOUX, taille=12, ancre="middle", dy=-10, fond=True)
f.texte(118, 38, "E = max(A − D, 0)", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.texte(60, 0, "plancher : E = 0", couleur=ACCENT, ancre="middle", dy=-9, gras=True)
# Le seuil de faillite : des actifs A_t aujourd'hui à D, l'écart est E_t.
f.segment(A, 0, A, A - D, couleur=PALE)
f.point(A, A - D, couleur=ENCRE)
f.texte(A, A - D, "E_{t} = A_{t} − D", couleur=ENCRE, dx=8, dy=4, taille=12)
f.mesure_h(-30, D, A, couleur=AJOUT)
f.texte((D + A) / 2, -30, "une baisse de E_{t}, soit E_{t} / A_{t} = 1 / l_{t} en relatif", couleur=AJOUT, ancre="middle", dy=16, gras=True, taille=12)
f.texte(90, -46, "faillite dès que π̃_{A} ≤ −1 / l_{t}", couleur=ENCRE, ancre="middle", dy=-4, gras=True, taille=13)
sys.stdout.write(f.svg())
