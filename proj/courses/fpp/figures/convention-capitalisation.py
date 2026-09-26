#!/usr/bin/env python3
r"""
convention-capitalisation.svg — le facteur de capitalisation selon le nombre de périodes.

La forme de la fiche : $(1+rt/n)^n$ tend vers $e^{rt}$ quand $n$ grandit. Avec l'exemple,
$r=5\,\%$ sur deux ans, $rt=0{,}10$ : une seule période donne le facteur linéaire 1,10,
huit trimestres donnent 1,1038, et la limite continue vaut 1,1052. Chaque point est une
convention ; toutes décrivent le même placement, écrit autrement.

Usage : python courses/fpp/figures/convention-capitalisation.py > convention-capitalisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

RT = 0.10
fac = lambda n: (1 + RT / n) ** n
LIM = math.exp(RT)

f = Figure(xmin=0, xmax=25, ymin=1.0985, ymax=1.1065, w=560, h=320,
           titre="Plus on découpe la période, plus le facteur approche e^{rt} = 1,1052")
f.axes(xlab="nombre de périodes n sur deux ans", ylab="facteur", xticks=(1, 4, 8, 12, 16, 20, 24),
       yticks=(1.1, 1.1038, LIM), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: ("%.4f" % t).replace(".", ","))

f.courbe([(0, LIM), (25, LIM)], couleur=AJOUT, epaisseur=1.6, pointilles="6 4")
f.texte(24.5, LIM, "continu : e^{0,10}", couleur=AJOUT, ancre="end", dy=-8, gras=True,
        fond=True)
for n in range(1, 25):
    f.point(n, fac(n), couleur=ACCENT if n in (1, 8) else DOUX, r=4.2 if n in (1, 8) else 3)
f.texte(1, fac(1), "linéaire : 1,10", couleur=ACCENT, dx=10, dy=4, gras=True, fond=True)
f.texte(8, fac(8), "trimestriel : 1,1038", couleur=ACCENT, dx=8, dy=18, gras=True, fond=True)

sys.stdout.write(f.svg())
