#!/usr/bin/env python3
r"""
intervalle-de-non-echange.svg — la valeur d'acheter et celle de vendre, selon le prix.

Les nombres de la fiche : $V(X)=1{,}8$ et $V(-X)=-2{,}4$. Au prix $p$, une unité achetée
vaut $1{,}8-p$ et une unité vendue $p-2{,}4$. Les deux droites sont négatives entre 1,8 et
2,4 : sur cette plage, ne rien faire bat les deux. Au prix 2, l'exemple de la fiche,
acheter vaut $-0{,}2$ et vendre $-0{,}4$.

Usage : python courses/dup/figures/intervalle-de-non-echange.py > intervalle-de-non-echange.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

VL, VC = 1.8, 2.4
P0, P1 = 1.3, 2.9

f = Figure(xmin=P0, xmax=P1, ymin=-0.8, ymax=0.8, w=560, h=330,
           titre="Entre 1,8 et 2,4, acheter et vendre valent tous deux moins que rien")

f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.10"/>'
       % (_n(f.px(VL)), _n(f.py(0.8)), _n(f.px(VC) - f.px(VL)), _n(f.py(-0.8) - f.py(0.8)), DOUX))
f.axes(xlab="prix p", ylab="valeur", xticks=(1.5, 1.8, 2, 2.4, 2.7), yticks=(-0.4, -0.2, 0.4),
       fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: ("%g" % t).replace(".", ","),
       croix=(P0, 0))

f.fonction(lambda p: VL - p, P0, P1, couleur=ACCENT, epaisseur=2.4)
f.fonction(lambda p: p - VC, P0, P1, couleur=AJOUT, epaisseur=2.4)

f.segment(2, -0.4, 2, -0.2)
f.point(2, VL - 2, couleur=ACCENT)
f.point(2, 2 - VC, couleur=AJOUT)

f.texte(1.45, VL - 1.45, "acheter : 1,8 − p", couleur=ACCENT, dx=6, dy=-6, gras=True, fond=True)
f.texte(2.75, 2.75 - VC, "vendre : p − 2,4", couleur=AJOUT, ancre="end", dx=-6, dy=-6,
        gras=True, fond=True)
f.texte((VL + VC) / 2, 0.62, "ni l'un ni l'autre", couleur=ENCRE, ancre="middle", gras=True,
        fond=True)

sys.stdout.write(f.svg())
