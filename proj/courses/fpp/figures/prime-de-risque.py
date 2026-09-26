#!/usr/bin/env python3
r"""
prime-de-risque.svg — le levier déplace le point le long d'une droite issue de l'origine.

Les exemples des fiches : un actif de volatilité 6 % et de prime 3 % ; avec un levier de
3,33, les capitaux propres ont une volatilité de 20 % et une prime de 10 %. Le levier
multiplie les deux coordonnées par le même nombre, donc le point glisse sur la droite qui
le relie à l'origine : le rapport de la prime à la volatilité, 0,5, ne change pas. C'est
le geste de la fiche.

Usage : python courses/fpp/figures/prime-de-risque.py > prime-de-risque.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

A = (6.0, 3.0)
L = 100 / 30
E = (A[0] * L, A[1] * L)

f = Figure(xmin=0, xmax=24, ymin=0, ymax=12.5, w=560, h=320,
           titre="Le levier multiplie la prime et la volatilité par le même nombre")
f.axes(xlab="volatilité, en %", ylab="prime de risque, en %", xticks=(0, 6, 20),
       yticks=(3, 10), fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d" % t)

f.courbe([(0, 0), (23, 23 * 0.5)], couleur=DOUX, epaisseur=1.4, pointilles="5 4")
f.fleche(A[0] + 0.5, A[1] + 0.25, E[0] - 0.5, E[1] - 0.25, couleur=ACCENT, epaisseur=2.2)
f.point(*A, couleur=ENCRE, r=4.5)
f.point(*E, couleur=ACCENT, r=4.5)
f.texte(*A, "actif (6 ; 3)", couleur=ENCRE, dx=10, dy=16, gras=True, fond=True)
f.texte(*E, "capitaux propres (20 ; 10)", couleur=ACCENT, ancre="end", dx=-14, dy=-14,
        gras=True, fond=True)
f.texte(13, 6.5, "× l = 3,33", couleur=ACCENT, ancre="end", dx=-6, dy=-10, gras=True, fond=True)
f.texte(23, 4.5, "même rapport prime / volatilité : 0,5", couleur=DOUX, ancre="end", taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
