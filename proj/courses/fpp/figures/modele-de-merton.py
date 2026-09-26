#!/usr/bin/env python3
r"""
modele-de-merton.svg — la valeur des actifs à l'échéance, partagée entre créanciers et
actionnaires pour une dette de nominal 80 : les créanciers reçoivent min(S_T, 80), les
actionnaires (S_T − 80)^+, le payoff d'un call de strike 80. Empilées, les deux parts
redonnent les actifs.

Usage : python courses/fpp/figures/modele-de-merton.py > modele-de-merton.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

D = 80
f = Figure(xmin=0, xmax=160, ymin=0, ymax=165, w=560, h=330,
           titre="Les créanciers reçoivent min(S_{T}, 80), les actionnaires le reste : un call de strike 80")
f.axes(xlab="valeur des actifs à l'échéance", ylab="ce que chacun reçoit",
       xticks=(0, 40, 80, 120, 160), yticks=(40, 80, 120, 160), fmt=lambda t: "%d" % t)
f._add('<path d="M%s %s L%s %s L%s %s L%s %s Z" fill="%s" fill-opacity="0.2"/>'
       % (f.px(0), f.py(0), f.px(D), f.py(D), f.px(160), f.py(D), f.px(160), f.py(0), AJOUT))
f._add('<path d="M%s %s L%s %s L%s %s Z" fill="%s" fill-opacity="0.2"/>'
       % (f.px(D), f.py(D), f.px(160), f.py(160), f.px(160), f.py(D), ACCENT))
f.courbe([(0, 0), (D, D), (160, D)], couleur=AJOUT, epaisseur=2.4)
f.courbe([(0, 0), (160, 160)], couleur=ENCRE, epaisseur=1.6)
f.segment(D, 0, D, D)
f.texte(125, 40, "créanciers : min(S_{T}, 80)", couleur=AJOUT, ancre="middle", gras=True)
f.texte(140, 110, "actionnaires :", couleur=ACCENT, ancre="middle", gras=True)
f.texte(140, 110, "(S_{T} − 80)^{+}", couleur=ACCENT, ancre="middle", dy=16, gras=True)
f.texte(60, 60, "total : S_{T}", couleur=ENCRE, ancre="end", dx=-8, dy=-4, taille=12)
sys.stdout.write(f.svg())
