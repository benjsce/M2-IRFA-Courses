#!/usr/bin/env python3
r"""
echelonnement-de-la-variance.svg — l'enveloppe d'un écart type autour du log-prix, ±σ√T.
Au quart de la durée, elle vaut σ√(T/4) = σ√T / 2 : la moitié, et non le quart ; en
pointillé, ce qu'on aurait si les écarts types s'additionnaient.

Usage : python courses/fpp/figures/echelonnement-de-la-variance.py > echelonnement-de-la-variance.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
SIG = 20.0
f = Figure(xmin=0, xmax=1.05, ymin=-24, ymax=24, w=560, h=320,
           titre="σ(T) = σ√T : au quart de la durée, la moitié de l'écart type")
f.axes(xlab="durée", ylab="log-rendement", xticks=(0.25, 1), fmt=lambda t: "T/4" if t < 1 else "T",
       croix=(0, 0))
f.courbe([(0, 0), (1, SIG)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.courbe([(0, 0), (1, -SIG)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.fonction(lambda t: SIG * math.sqrt(t), 0, 1, couleur=ACCENT, epaisseur=2.6, n=200)
f.fonction(lambda t: -SIG * math.sqrt(t), 0, 1, couleur=ACCENT, epaisseur=2.6, n=200)
f.segment(0.25, -10, 0.25, 10)
f.point(0.25, 10, couleur=ACCENT)
f.point(0.25, -10, couleur=ACCENT)
f.texte(0.25, 10, "σ√T / 2", couleur=ACCENT, dx=-6, dy=-8, ancre="end", gras=True)
f.texte(1, 20, "σ√T", couleur=ACCENT, dx=-6, dy=-8, ancre="end", gras=True)
f.point(0.25, 5, couleur=DOUX, r=3)
f.texte(0.25, 5, "et non σ√T / 4", couleur=DOUX, dx=8, dy=4, taille=12)
f.texte(0.42, -6.2, "pointillé : si les écarts types s'additionnaient", couleur=DOUX, taille=11.5)
sys.stdout.write(f.svg())
