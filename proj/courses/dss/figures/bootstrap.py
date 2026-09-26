#!/usr/bin/env python3
r"""
bootstrap.svg — la part des observations absentes d'un échantillon bootstrap.

Tirer $n$ fois avec remise parmi $n$ observations laisse chacune de côté avec probabilité
$(1-1/n)^n$. La courbe tend vers $e^{-1}\approx0{,}368$ : environ un tiers, comme le dit la
fiche. À $n=100$, l'exemple, la part vaut 0,366, soit environ 37 observations de côté.

Usage : python courses/dss/figures/bootstrap.py > bootstrap.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

part = lambda n: (1 - 1 / n) ** n

f = Figure(xmin=0, xmax=105, ymin=0, ymax=0.45, w=560, h=300,
           titre="Environ un tiers des observations manque à chaque échantillon bootstrap")
f.axes(xlab="taille n de l'échantillon", ylab="part laissée de côté", xticks=(1, 25, 50, 75, 100),
       yticks=(0.25, 0.368), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: ("%g" % t).replace(".", ","))
f.courbe([(0, math.exp(-1)), (105, math.exp(-1))], couleur=AJOUT, epaisseur=1.4, pointilles="6 4")
f.texte(104, math.exp(-1), "e^{−1}", couleur=AJOUT, ancre="end", dy=-8, gras=True)
for n in range(1, 101):
    f.point(n, part(n), couleur=ACCENT if n == 100 else DOUX, r=4.5 if n == 100 else 2.2)
f.texte(100, part(100), "n = 100 : 37 de côté", couleur=ACCENT, ancre="end", dx=-8, dy=18,
        gras=True, fond=True)
f.texte(1, part(1), "n = 1 : aucune", couleur=DOUX, dx=8, dy=4, taille=11.5)

sys.stdout.write(f.svg())
