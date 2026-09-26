#!/usr/bin/env python3
r"""
taux-zero-coupon.svg — moins le logarithme du prix du zéro-coupon en fonction de la
durée : le taux zéro-coupon R(t,T) = −ln P(t,T) / (T − t) est la pente de la corde issue
de l'origine. Tracé avec la courbe du cours ; aucun nombre écrit.

Usage : python courses/fpp/figures/taux-zero-coupon.py > taux-zero-coupon.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=0, xmax=2.4, ymin=0, ymax=0.125, w=560, h=320,
           titre="R(t,T) = −ln P(t,T) / (T − t) : la pente de la corde depuis l'origine")
f.axes(xlab="durée T − t", ylab="− ln P(t,T)", xticks=(1, 2), fmt=lambda t: "")
f.texte(1, 0, "T_{1} − t", couleur=DOUX, ancre="middle", dy=19, taille=12)
f.texte(2, 0, "T_{2} − t", couleur=DOUX, ancre="middle", dy=19, taille=12)
f.courbe([(0, 0), (2, 0.10)], couleur=ACCENT, epaisseur=2.4)
f.courbe([(0, 0), (1, 0.04)], couleur=AJOUT, epaisseur=2.4)
f.segment(1, 0, 1, 0.04)
f.segment(2, 0, 2, 0.10)
f.point(1, 0.04, couleur=AJOUT, r=4.5)
f.point(2, 0.10, couleur=ACCENT, r=4.5)
f.texte(1, 0.04, "pente R(t,T_{1})", couleur=AJOUT, dx=10, dy=14, gras=True)
f.texte(2, 0.10, "pente R(t,T_{2})", couleur=ACCENT, ancre="end", dx=-10, dy=-8, gras=True)
f.texte(2, 0.10, "− ln P(t,T_{2})", couleur=ACCENT, dx=8, dy=20, taille=12)
sys.stdout.write(f.svg())
