#!/usr/bin/env python3
r"""
modele-de-merton.svg — la valeur des actifs à l'échéance, partagée entre créanciers et
actionnaires pour une dette de nominal D : les créanciers reçoivent min(S_T, D), les
actionnaires (S_T − D)^+, le payoff d'un call de strike D.

Usage : python courses/fpp/figures/modele-de-merton.py > modele-de-merton.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
D = 80
f = Figure(xmin=0, xmax=160, ymin=0, ymax=165, w=560, h=330,
           titre="Les créanciers reçoivent min(S_T, D), les actionnaires le reste : un call de strike D")
f.axes(xlab="valeur des actifs à l'échéance S(T)", ylab="ce que chacun reçoit", xticks=(D,), yticks=(D,),
       fmt=lambda t: "D", fmt_y=lambda t: "D")
f._add('<path d="M%s %s L%s %s L%s %s L%s %s Z" fill="%s" fill-opacity="0.2"/>'
       % (f.px(0), f.py(0), f.px(D), f.py(D), f.px(160), f.py(D), f.px(160), f.py(0), AJOUT))
f._add('<path d="M%s %s L%s %s L%s %s Z" fill="%s" fill-opacity="0.2"/>'
       % (f.px(D), f.py(D), f.px(160), f.py(160), f.px(160), f.py(D), ACCENT))
f.courbe([(0, 0), (D, D), (160, D)], couleur=AJOUT, epaisseur=2.4)
f.courbe([(0, 0), (160, 160)], couleur=ENCRE, epaisseur=1.6)
f.segment(D, 0, D, D)
f.texte(125, 40, "créanciers : min(S_{T}, D)", couleur=AJOUT, ancre="middle", gras=True)
f.texte(140, 110, "actionnaires :", couleur=ACCENT, ancre="middle", gras=True)
f.texte(140, 110, "(S_{T} − D)^{+}", couleur=ACCENT, ancre="middle", dy=16, gras=True)
f.texte(60, 60, "total : S_{T}", couleur=ENCRE, ancre="end", dx=-8, dy=-4, taille=12)
sys.stdout.write(f.svg())
