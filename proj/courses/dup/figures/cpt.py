#!/usr/bin/env python3
r"""
cpt.svg — la fonction de pondération du cours, concave puis convexe.

$\varphi(p)=p^\beta/\big(p^\beta+(1-p)^\beta\big)^{1/\beta}$ avec $\beta=0{,}7$, la valeur
de l'exemple de la fiche, qui donne $\varphi(0{,}2)=0{,}2560$ : la mesure verticale est
cette surpondération. Près de 0 la courbe passe au-dessus de la diagonale, ce qui
surpondère les mauvais résultats peu probables ; près de 1 elle passe au-dessous, de
sorte que $1-\varphi$ dépasse $1-p$ et que les bons résultats peu probables sont
surpondérés à leur tour. Ce sont les deux effets que nomme la fiche.

Usage : python courses/dup/figures/cpt.py > cpt.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

BETA = 0.7


def phi(p):
    if p <= 0 or p >= 1:
        return float(p)
    a, b = p ** BETA, (1 - p) ** BETA
    return a / (a + b) ** (1 / BETA)


f = Figure(xmin=0, xmax=1.04, ymin=0, ymax=1.06, w=440, h=400, marges=(54, 16, 44, 18),
           titre="Au-dessus de la diagonale près de 0, au-dessous près de 1")
f.axes(xlab="probabilité cumulée p", ylab="φ(p)", xticks=(0, 0.2, 0.5, 1),
       yticks=(0.256, 0.5, 1), fmt=lambda t: ("%g" % t).replace(".", ","),
       fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.courbe([(0, 0), (1, 1)], couleur=DOUX, epaisseur=1.4, pointilles="5 4")
f.fonction(phi, 0, 1, n=300, couleur=ACCENT, epaisseur=2.6)

f.segment(0.2, 0, 0.2, phi(0.2))
f.segment(0, phi(0.2), 0.2, phi(0.2))
f.mesure(0.2, 0.2, phi(0.2), couleur=AJOUT, etiquette="+0,056")
f.point(0.2, phi(0.2), couleur=ENCRE)

f.texte(0.03, 0.62, "mauvais résultats rares :", couleur=ACCENT, taille=11.5, fond=True)
f.texte(0.03, 0.62, "φ > p, surpondérés", couleur=ACCENT, dy=15, taille=11.5, fond=True)
f.texte(0.98, 0.40, "bons résultats rares :", couleur=ACCENT, ancre="end", taille=11.5,
        fond=True)
f.texte(0.98, 0.40, "1 − φ > 1 − p", couleur=ACCENT, ancre="end", dy=15, taille=11.5,
        fond=True)
f.texte(0.9, 0.9, "φ(p) = p", couleur=DOUX, ancre="end", dx=-4, dy=-6, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
