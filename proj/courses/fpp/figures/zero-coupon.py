#!/usr/bin/env python3
r"""
zero-coupon.svg — deux zéro-coupons sur l'échéancier : 1 payé en T₁ vaut P(t,T₁) en t,
1 payé en T₂ vaut P(t,T₂), plus petit parce que plus lointain.

Usage : python courses/fpp/figures/zero-coupon.py > zero-coupon.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.75, xmax=2.35, ymin=-0.35, ymax=2.0, w=560, h=300, marges=(10, 10, 10, 10),
           titre="1 payé en T vaut P(t,T) aujourd'hui : moins, et d'autant moins que T est loin")
f.axe_temps(0, -0.1, 2.3, [(0, "t"), (1, "T₁"), (2, "T₂")])
for x in (1, 2):
    f.fleche(x, 0.08, x, 0.8, couleur=AJOUT, epaisseur=2)
    f.texte(x, 0.45, "1", couleur=AJOUT, dx=8, gras=True)
f.fleche(1, 0.95, 0.12, 0.95, couleur=ACCENT, courbure=14)
f.fleche(2, 0.95, 0.12, 1.55, couleur=ACCENT, courbure=34)
f.texte(0, 0.95, "P(t,T_{1})", couleur=ACCENT, ancre="end", dx=-4, dy=4, gras=True)
f.texte(0, 1.55, "P(t,T_{2})", couleur=ACCENT, ancre="end", dx=-4, dy=4, gras=True)
f.segment(0, 0.08, 0, 1.5)
sys.stdout.write(f.svg())
