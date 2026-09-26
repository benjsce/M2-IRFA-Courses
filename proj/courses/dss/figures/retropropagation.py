#!/usr/bin/env python3
r"""
retropropagation.svg — les sorties vont vers l'avant, les erreurs reviennent vers l'arrière.

Un petit réseau, deux entrées, deux nœuds cachés, une sortie, choisi pour le dessin. Les
flèches pleines portent les sorties $o$ vers l'avant. Les flèches courbes portent les $d$
vers l'arrière : d'abord celui de la sortie, $d_j=o_j(1-o_j)(t_j-o_j)$, calculé sur l'écart
à la cible ; puis ceux des nœuds cachés, $d_i=o_i(1-o_i)\sum_j d_jw_{ij}$, qui ont besoin du
$d$ du dessus. C'est l'ordre du geste de la fiche.

Usage : python courses/dss/figures/retropropagation.py > retropropagation.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

f = Figure(xmin=0, xmax=12, ymin=0, ymax=7, w=580, h=320, marges=(8, 8, 8, 8),
           titre="Vers l'avant les sorties, vers l'arrière les erreurs, couche par couche")
ENT = [(1.5, 5.0), (1.5, 2.0)]
CACH = [(5.5, 5.0), (5.5, 2.0)]
SORT = (9.5, 3.5)
for e in ENT:
    for c in CACH:
        f.fleche(e[0] + 0.35, e[1], c[0] - 0.4, c[1], couleur=DOUX, epaisseur=1.4)
for c in CACH:
    f.fleche(c[0] + 0.4, c[1], SORT[0] - 0.4, SORT[1], couleur=DOUX, epaisseur=1.4)
    f.fleche(SORT[0] - 0.3, SORT[1] + 0.35, c[0] + 0.35, c[1] + 0.4 * (1 if c[1] > 3.5 else -1),
             couleur=AJOUT, epaisseur=2.0, courbure=26 if c[1] > 3.5 else -26)
for x, y in ENT + CACH + [SORT]:
    f.point(x, y, couleur=ACCENT if (x, y) == SORT else ENCRE, r=13)
f.texte(1.5, 6.2, "entrées", couleur=ENCRE, ancre="middle", gras=True)
f.texte(5.5, 6.4, "couche cachée", couleur=ENCRE, ancre="middle", gras=True)
f.texte(9.5, 6.4, "sortie", couleur=ENCRE, ancre="middle", gras=True)
f.fleche(SORT[0] + 0.35, SORT[1], 11.0, SORT[1], couleur=DOUX, epaisseur=1.4)
f.texte(11.1, SORT[1], "o", couleur=ENCRE, dy=5, gras=True)
f.texte(9.5, 1.6, "1. dj = oj(1 − oj)(tj − oj)", couleur=AJOUT, ancre="middle", taille=11.5,
        gras=True)
f.texte(5.5, 0.6, "2. di = oi(1 − oi) Σ dj wij", couleur=AJOUT, ancre="middle", taille=11.5,
        gras=True)

sys.stdout.write(f.svg())
