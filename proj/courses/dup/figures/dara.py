#!/usr/bin/env python3
r"""
dara.svg — une aversion qui décroît avec la richesse, et une qui croît.

La fiche oppose deux utilités : la logarithmique, DARA, dont $A(z)=1/z$ décroît, et la
quadratique, qui viole DARA parce que $A(z)=(c-z)^{-1}$ croît. Pour la quadratique on
prend $c=100$, le point de satiété de l'exemple de dup/utilite-quadratique
($\alpha=1$, $\beta=-0{,}005$, donc $-\alpha/2\beta=100$) : le dessin s'arrête avant, là
où $A$ explose. Les deux courbes se croisent à 50, où elles valent 0,02.

Usage : python courses/dup/figures/dara.py > dara.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402

C = 100.0
YMAX = 0.1

f = Figure(xmin=0, xmax=104, ymin=0, ymax=YMAX, w=560, h=330,
           titre="Le logarithme devient moins averse en s'enrichissant, la quadratique plus")
f.axes(xlab="richesse z", ylab="A(z)", xticks=(0, 25, 50, 75, 100),
       yticks=(0.02, 0.05, 0.1), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))

f.segment(C, 0, C, YMAX, couleur=DOUX)
f.fonction(lambda z: 1.0 / z, 1.0 / YMAX, 96, couleur=ACCENT, epaisseur=2.4)
f.fonction(lambda z: 1.0 / (C - z), 4, C - 1.0 / YMAX, couleur=AJOUT, epaisseur=2.2)

f.point(50, 0.02, couleur=DOUX)
f.texte(20, 1.0 / 20, "ln z : DARA", couleur=ACCENT, dx=8, dy=-2, gras=True, fond=True)
f.texte(80, 1.0 / 20, "quadratique : A croît", couleur=AJOUT, ancre="end", dx=-8, dy=-2,
        gras=True, fond=True)
f.texte(C, YMAX, "satiété", couleur=DOUX, ancre="end", dx=-5, dy=12, taille=11.5)

sys.stdout.write(f.svg())
