#!/usr/bin/env python3
r"""
convention-capitalisation.svg — un même taux affiché, autant de montants que de conventions.

Ce que la figure doit faire voir : le taux et la durée sont connus, 5 % par an pendant
deux ans, et ce que devient un euro ne l'est pas tant qu'on n'a pas dit combien de fois
l'intérêt est versé et réinvesti. En abscisse ce nombre n, en ordonnée le facteur
$(1+rt/n)^n$ avec $rt=0{,}10$ : une fois, le facteur linéaire 1,10 ; une fois par an
(n = 2), l'actuariel 1,1025 ; huit trimestres, 1,1045 ; et la limite continue
$e^{0,10}=1{,}1052$, que les points approchent par en dessous.

Usage : python courses/fpp/figures/convention-capitalisation.py > convention-capitalisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

R, DUREE = 0.05, 2
RT = R * DUREE
fac = lambda n: (1 + RT / n) ** n
LIM = math.exp(RT)
f4 = lambda v: ("%.4f" % v).replace(".", ",")

f = Figure(xmin=0, xmax=25, ymin=1.0975, ymax=1.1072, w=600, h=340,
           marges=(62, 22, 44, 18),
           titre="Un même taux, 5 % par an pendant deux ans : chaque convention donne un autre montant")
f.axes(xlab="n : versements d'intérêt en deux ans",
       ylab="ce que devient 1 € au bout de deux ans",
       xticks=(1, 2, 4, 8, 12, 16, 20, 24), yticks=(fac(1), fac(2), fac(8), LIM),
       fmt=lambda t: "%d" % t, fmt_y=f4)

f.courbe([(0, LIM), (25, LIM)], couleur=AJOUT, epaisseur=1.6, pointilles="6 4")
f.texte(24.6, LIM, "continu : e^{0,10} = " + f4(LIM), couleur=AJOUT, ancre="end", dy=-8,
        gras=True, fond=True)
MARQUES = {1: "linéaire, une fois : " + f4(fac(1)),
           2: "actuariel, une fois par an : " + f4(fac(2)),
           8: "trimestriel, huit fois : " + f4(fac(8))}
for n in range(1, 25):
    f.point(n, fac(n), couleur=ACCENT if n in MARQUES else DOUX, r=4.4 if n in MARQUES else 2.8)
f.texte(1, fac(1), MARQUES[1], couleur=ACCENT, dx=12, dy=5, gras=True, fond=True)
f.texte(2, fac(2), MARQUES[2], couleur=ACCENT, dx=12, dy=5, gras=True, fond=True)
f.texte(8, fac(8), MARQUES[8], couleur=ACCENT, dx=10, dy=19, gras=True, fond=True)

f.texte(24.6, 1.0995, "connu : 5 % par an, pendant 2 ans", couleur=ENCRE, ancre="end",
        taille=12.5, fond=True)

sys.stdout.write(f.svg())
