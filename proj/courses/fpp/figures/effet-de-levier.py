#!/usr/bin/env python3
r"""
effet-de-levier.svg — actifs et capitaux propres dans le plan volatilité–prime :
(σ_E, π_E) = (l_t σ_A, l_t π_A), le même point multiplié par l_t, sur la même demi-droite.

Usage : python courses/fpp/figures/effet-de-levier.py > effet-de-levier.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

L, SA, PA = 5, 4.0, 2.0
f = Figure(xmin=0, xmax=25, ymin=0, ymax=12.5, w=560, h=320,
           titre="σ_E = l_t σ_A et π_E = l_t π_A : même demi-droite, l_t fois plus loin")
f.axes(xlab="volatilité", ylab="prime espérée", xticks=(SA, L * SA), yticks=(PA, L * PA),
       fmt=lambda t: "", fmt_y=lambda t: "")
f.texte(SA, 0, "σ_{A}", couleur=DOUX, ancre="middle", dy=19, taille=12)
f.texte(L * SA, 0, "σ_{E} = l_{t} σ_{A}", couleur=DOUX, ancre="middle", dy=19, taille=12)
f.texte(0, PA, "π_{A}", couleur=DOUX, ancre="end", dx=-8, dy=4, taille=12)
f.texte(0, L * PA, "π_{E} = l_{t} π_{A}", couleur=DOUX, ancre="start", dx=6, dy=-6, taille=12)
f.courbe([(0, 0), (24, 12)], couleur=PALE, epaisseur=1.4, pointilles="5 4")
f.segment(SA, 0, SA, PA)
f.segment(0, PA, SA, PA)
f.segment(L * SA, 0, L * SA, L * PA)
f.segment(0, L * PA, L * SA, L * PA)
f.fleche(SA + 0.8, PA + 0.4, L * SA - 0.8, L * PA - 0.4, couleur=DOUX, epaisseur=1.3)
f.point(SA, PA, couleur=AJOUT, r=5)
f.point(L * SA, L * PA, couleur=ACCENT, r=5)
f.texte(SA, PA, "actifs", couleur=AJOUT, dx=10, dy=18, gras=True)
f.texte(L * SA, L * PA, "capitaux propres", couleur=ACCENT, ancre="end", dx=-10, dy=-10, gras=True)
f.texte(12, 6, "× l_{t}", couleur=DOUX, ancre="middle", dx=-16, dy=-6, fond=True)
sys.stdout.write(f.svg())
