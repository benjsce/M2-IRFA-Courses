#!/usr/bin/env python3
r"""
bilan.svg — le bilan : les actifs A_t à gauche, financés à droite par les capitaux propres
E_t et la dette D_t ; A_t = E_t + D_t. Forme de la figure 1 du poly (§1.2).

Usage : python courses/fpp/figures/bilan.py > bilan.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

A, E, D = 100, 20, 80
f = Figure(xmin=0, xmax=10, ymin=-12, ymax=112, w=440, h=320, marges=(10, 10, 10, 10),
           titre="A_t = E_t + D_t : les capitaux propres sont ce qui reste une fois la dette déduite")


def boite(x0, x1, y0, y1, couleur, etiquette, symbole):
    X0, X1, Y0, Y1 = f.px(x0), f.px(x1), f.py(y1), f.py(y0)
    f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.18" '
           'stroke="%s" stroke-width="1.6"/>' % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), couleur, couleur))
    f.texte((x0 + x1) / 2, (y0 + y1) / 2, etiquette, ancre="middle", dy=-2)
    f.texte((x0 + x1) / 2, (y0 + y1) / 2, symbole, ancre="middle", dy=15, gras=True)


boite(1.0, 4.4, 0, A, AJOUT, "actifs", "A_{t}")
boite(5.6, 9.0, D, A, ACCENT, "capitaux propres", "E_{t}")
boite(5.6, 9.0, 0, D, DOUX, "dette", "D_{t}")
f.texte(2.7, 104, "actif", ancre="middle", couleur=DOUX, taille=12)
f.texte(7.3, 104, "passif", ancre="middle", couleur=DOUX, taille=12)
f.texte(5.0, 50, "=", ancre="middle", taille=20, couleur=DOUX, dy=7)
f.texte(5.0, -8, "A_{t} = E_{t} + D_{t}", ancre="middle", gras=True)
sys.stdout.write(f.svg())
