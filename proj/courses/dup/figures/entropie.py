#!/usr/bin/env python3
r"""
entropie.svg — l'entropie d'une loterie à deux résultats, en fonction de la seule probabilité.

La fiche dit que $H$ ne regarde que les probabilités, jamais les montants, et qu'elle est
maximale quand les résultats sont également probables. Pour deux résultats de
probabilités $p$ et $1-p$, $H$ est une fonction de $p$ seul : l'axe horizontal n'a pas de
place pour les montants. Les deux loteries de l'exemple, $(49,\tfrac12;51,\tfrac12)$ et
$(0,\tfrac12;100,\tfrac12)$, tombent donc sur le même point, au sommet.

Le logarithme est naturel ; la fiche ne fixe pas la base, et l'axe vertical n'est pas
gradué pour cette raison.

Usage : python courses/dup/figures/entropie.py > entropie.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE      # noqa: E402


def H(p):
    return -sum(q * math.log(q) for q in (p, 1 - p) if q > 0)


f = Figure(xmin=0, xmax=1.04, ymin=0, ymax=0.86, w=560, h=330,
           titre="Les deux loteries ont la même entropie : l'axe ne connaît que la probabilité")
f.axes(xlab="probabilité p du premier résultat", ylab="H", xticks=(0, 0.5, 1),
       fmt=lambda t: {0: "0", 0.5: "½", 1: "1"}[t])

f.fonction(H, 0, 1, n=200, couleur=ACCENT, epaisseur=2.6)
f.segment(0.5, 0, 0.5, H(0.5))
f.point(0.5, H(0.5), couleur=ENCRE)
f.texte(0.5, H(0.5), "(49, ½ ; 51, ½) et (0, ½ ; 100, ½)", couleur=ENCRE, ancre="middle",
        dy=-12, gras=True, fond=True)
f.texte(0.5, 0.3, "le maximum : résultats également probables", couleur=ENCRE,
        ancre="middle", taille=11.5, fond=True)

sys.stdout.write(f.svg())
