#!/usr/bin/env python3
r"""
capitalisation.svg — le facteur C(t,n) = (1 + rt/n)^n selon le nombre n de versements
d'intérêts : 1 + rt pour n = 1, puis de plus en plus près de e^{rt}, la capitalisation
continue, quand n grandit. Le tracé emploie r = 5 %, t = 2 ; aucun nombre n'est écrit.

Usage : python courses/fpp/figures/capitalisation.py > capitalisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

RT = 0.1
NS = [1, 2, 4, 12, 52, 365]
f = Figure(xmin=0.4, xmax=6.9, ymin=1.0985, ymax=1.1065, w=560, h=320,
           titre="C(t,n) = (1 + rt/n)^n croît avec n et tend vers e^{rt}")
f.axes(xlab="nombre n de versements d'intérêts", ylab="ce que devient 1")
lim = math.exp(RT)
f.segment(0.4, lim, 6.9, lim, couleur=ACCENT, pointilles="6 4", epaisseur=1.6)
f.texte(6.9, lim, "continu : C(t) = e^{rt}", couleur=ACCENT, ancre="end", dy=-8, gras=True)
pts = [(k, (1 + RT / n) ** n) for k, n in enumerate(NS, start=1)]
for (k, v), n in zip(pts, NS):
    lab = {1: "n = 1", 2: "n = 2", 6: "n → ∞"}.get(k, "…")
    f.texte(k, 1.0985, lab, couleur=DOUX, ancre="middle", taille=11.5, dy=17)
f.courbe(pts, couleur=PALE, epaisseur=1.2)
for k, v in pts:
    f.point(k, v, couleur=AJOUT if k > 1 else DOUX, r=4.5)
f.texte(1, pts[0][1], "linéaire : 1 + rt", couleur=DOUX, dx=10, dy=4, taille=12)
f.texte(2, pts[1][1], "(1 + rt/2)^{2}", couleur=AJOUT, dx=10, dy=4, taille=12)
f.texte(3, pts[2][1], "(1 + rt/n)^{n}", couleur=AJOUT, dx=10, dy=12, taille=12)
sys.stdout.write(f.svg())
