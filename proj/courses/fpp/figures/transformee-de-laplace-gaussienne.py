#!/usr/bin/env python3
r"""
transformee-de-laplace-gaussienne.svg — la courbe exponentielle et deux valeurs d'une
variable, μ − σ et μ + σ : la moyenne des deux exponentielles, sur la corde, dépasse e^{μ}.
Pour X gaussienne, E(e^{X}) = e^{μ + σ²/2}.

Usage : python courses/fpp/figures/transformee-de-laplace-gaussienne.py > transformee-de-laplace-gaussienne.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
a = 0.2
m = (math.exp(-a) + math.exp(a)) / 2
f = Figure(xmin=-0.3, xmax=0.3, ymin=0.76, ymax=1.28, w=560, h=320,
           titre="E(e^{X}) = e^{μ + σ²/2} > e^{μ} : l'exponentielle est convexe")
f.axes(xlab="x", ylab="exp(x)", xticks=(-a, 0, a), fmt=lambda t: {-a: "μ − σ", 0: "μ", a: "μ + σ"}[t],
       croix=(-0.3, 0.76))
f.fonction(math.exp, -0.29, 0.29, couleur=ACCENT, epaisseur=2.6)
f.courbe([(-a, math.exp(-a)), (a, math.exp(a))], couleur=AJOUT, epaisseur=1.8)
f.segment(-a, 0.76, -a, math.exp(-a))
f.segment(a, 0.76, a, math.exp(a))
f.segment(0, 0.76, 0, 1)
for x in (-a, a):
    f.point(x, math.exp(x), couleur=ACCENT)
f.point(0, 1, couleur=ENCRE)
f.point(0, m, couleur=AJOUT, r=4.5)
f.texte(0, m, "moyenne des exponentielles", couleur=AJOUT, dx=-8, dy=-10, ancre="end", gras=True)
f.texte(0, 1, "e^{μ}", couleur=ENCRE, dx=8, dy=16)
f.mesure(0.035, 1, m, couleur=AJOUT, etiquette="l'écart que corrige σ²/2")
sys.stdout.write(f.svg())
