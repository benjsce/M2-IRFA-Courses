#!/usr/bin/env python3
r"""
ensemble-de-priors.svg — le triangle des probabilités sur trois états, et la bande de l'exemple.

Pour trois états, une probabilité est un point du triangle ; ses sommets sont les
certitudes. On place $p_R$ en abscisse et la probabilité d'un deuxième état en ordonnée,
la troisième étant ce qui reste. L'exemple de la fiche, $K=\{p:0{,}2\le p_R\le0{,}6\}$,
est la bande comprise entre les deux verticales $p_R=0{,}2$ et $p_R=0{,}6$, coupée par le
triangle.

Usage : python courses/dup/figures/ensemble-de-priors.py > ensemble-de-priors.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, ENCRE, _n      # noqa: E402

A, B = 0.2, 0.6

f = Figure(xmin=-0.06, xmax=1.12, ymin=-0.06, ymax=1.10, w=440, h=400,
           marges=(46, 18, 44, 70),
           titre="K est la bande 0,2 ≤ pR ≤ 0,6 : toutes ces compositions sont plausibles, aucune n'est préférée")
f.axes(xlab="pR", ylab="p du 2e état", xticks=(0, A, B, 1), yticks=(1,),
       fmt=lambda t: ("%g" % t).replace(".", ","))

bande = [(A, 0), (B, 0), (B, 1 - B), (A, 1 - A)]
f._add('<path d="M%s Z" fill="%s" fill-opacity="0.22" stroke="none"/>'
       % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in bande), ACCENT))
f.courbe(bande + [bande[0]], couleur=ACCENT, epaisseur=2.2)

f.courbe([(0, 1), (0, 0), (1, 0)], couleur=DOUX, epaisseur=1.4)
f.courbe([(0, 1), (1, 0)], couleur=DOUX, epaisseur=1.4)

for (x, y), nom, ancre, dx, dy in (((1, 0), "R sûr", "start", 6, -8),
                                   ((0, 1), "2e sûr", "start", 8, 4),
                                   ((0, 0), "3e sûr", "start", 8, -8)):
    f.point(x, y, couleur=ENCRE)
    f.texte(x, y, nom, couleur=ENCRE, ancre=ancre, dx=dx, dy=dy, taille=11.5, fond=True)

f.texte((A + B) / 2, 0.22, "K", couleur=ACCENT, ancre="middle", taille=16, gras=True)

sys.stdout.write(f.svg())
