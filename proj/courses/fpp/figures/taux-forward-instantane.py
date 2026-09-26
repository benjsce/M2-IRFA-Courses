#!/usr/bin/env python3
r"""
taux-forward-instantane.svg — le taux forward instantané f(t,u) en fonction de la date u :
l'aire sous la courbe de t à T vaut −ln P(t,T), donc P(t,T) = exp(−∫ f(t,u) du). Courbe
illustrative ; aucun nombre écrit.

Usage : python courses/fpp/figures/taux-forward-instantane.py > taux-forward-instantane.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

T = 1.6
g = lambda u: 0.03 + 0.035 * (1 - math.exp(-1.4 * u))
f = Figure(xmin=0, xmax=2.3, ymin=0, ymax=0.08, w=560, h=320,
           titre="L'aire sous f(t,u) de t à T vaut −ln P(t,T) : P(t,T) = exp(− ∫ f(t,u) du)")
f.axes(xlab="date u", ylab="f(t,u)", xticks=(0, T), fmt=lambda t: "t" if t == 0 else "T")
n = 80
pts = [(T * k / n, g(T * k / n)) for k in range(n + 1)]
from figure import _n
d = "M%s %s " % (_n(f.px(0)), _n(f.py(0))) + " ".join("L%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in pts)     + " L%s %s Z" % (_n(f.px(T)), _n(f.py(0)))
f._add('<path d="%s" fill="%s" fill-opacity="0.22"/>' % (d, ACCENT))
f.fonction(g, 0, 2.2, couleur=ENCRE, epaisseur=2.4)
f.segment(T, 0, T, g(T))
f.texte(T / 2, 0.022, "aire = − ln P(t,T)", couleur=ACCENT, ancre="middle", gras=True)
f.texte(T / 2, 0.022, "= ∫ f(t,u) du, de t à T", couleur=ACCENT, ancre="middle", dy=18, taille=12)
f.texte(2.2, g(2.2), "f(t,u)", couleur=ENCRE, ancre="end", dy=-10, gras=True)
sys.stdout.write(f.svg())
