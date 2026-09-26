#!/usr/bin/env python3
r"""
piege-d-agregation.svg — le logarithme est courbe, et la moyenne passe sous la courbe.

La courbe est $r=\ln(1+R)$, qui convertit un rendement arithmétique en rendement
logarithmique. L'exemple de la fiche : deux actifs à $+10\,\%$ et $-10\,\%$, à parts
égales. Le portefeuille fait $R_p=0$, donc $r_p=\ln 1=0$, un point de la courbe. La moyenne
pondérée des deux logarithmes, $(9{,}53-10{,}54)/2=-0{,}50\,\%$, est le milieu de la corde :
elle tombe sous la courbe, parce que le logarithme est concave.

À gauche, la vue d'ensemble, où l'écart ne se voit presque pas : c'est ce que dit « Cesse
d'être valide quand », un écart du second ordre. À droite, le voisinage de zéro agrandi.

Usage : python courses/pfo/figures/piege-d-agregation.py > piege-d-agregation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

lg = lambda R: 100 * math.log(1 + R / 100)          # en %
A, B = 10.0, -10.0
MOY = 0.5 * lg(A) + 0.5 * lg(B)                      # -0,50
corde = lambda R: lg(B) + (lg(A) - lg(B)) * (R - B) / (A - B)
fr = lambda v: ("%+.2f" % v).replace(".", ",").replace("-", "−")

g = Figure(xmin=-14, xmax=14, ymin=-14, ymax=12, w=290, h=300, marges=(44, 30, 40, 10))
g.axes(xlab="R, en %", xticks=(-10, 10), yticks=(-10.54, 9.53),
       fmt=lambda t: "%+d" % t, fmt_y=fr, croix=(0, 0))
g.fonction(lg, -13, 13, couleur=ACCENT, epaisseur=2.4)
g.courbe([(B, lg(B)), (A, lg(A))], couleur=AJOUT, epaisseur=1.6)
g.point(A, lg(A), couleur=ENCRE)
g.point(B, lg(B), couleur=ENCRE)
g.texte(0, 12, "r = ln(1 + R) et la corde", couleur=ENCRE, ancre="middle", dy=-8, gras=True)

d = Figure(xmin=-1.5, xmax=1.5, ymin=-1.7, ymax=1.1, w=290, h=300, marges=(44, 30, 40, 10))
d.axes(xlab="R, en %", xticks=(-1, 1), yticks=(-0.5,), fmt=lambda t: "%+d" % t,
       fmt_y=fr, croix=(0, 0))
d.fonction(lg, -1.45, 1.45, couleur=ACCENT, epaisseur=2.4)
d.fonction(corde, -1.2, 1.45, couleur=AJOUT, epaisseur=1.8)
d.point(0, 0, couleur=ACCENT)
d.point(0, MOY, couleur=AJOUT)
d.mesure(0.12, MOY, 0, couleur=ENCRE)
d.texte(0, 0, "rp = 0", couleur=ACCENT, ancre="end", dx=-8, dy=-8, gras=True, fond=True)
d.texte(0, MOY, "moyenne des r", couleur=AJOUT, dx=8, dy=18, gras=True, fond=True)
d.texte(0, 1.1, "autour de 0, agrandi", couleur=ENCRE, ancre="middle", dy=-8, gras=True)

sys.stdout.write(Planche([g, d], signes=("→",), ecart=30,
                         titre="La moyenne des logarithmes passe sous le logarithme de la moyenne").svg())
