#!/usr/bin/env python3
r"""
valeur-intrinseque.svg — la valeur intrinsèque d'un call de strike K : dans un monde sans
aléa, l'action vaudrait à coup sûr son prix forward F = E(S_T) ; le call paierait (F − K)^+
en T, soit IV = e^{−rT} g(E(S_T)) = e^{−rT}(F − K)^+ aujourd'hui.

Usage : python courses/fpp/figures/valeur-intrinseque.py > valeur-intrinseque.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
F = 100 / math.exp(-0.04)
f = Figure(xmin=-0.35, xmax=1.6, ymin=97, ymax=107.5, w=560, h=300,
           titre="Sans aléa, le call paierait F − K en T : IV = e^{−rT} (F − K)^+")
f.axes(xlab="temps", ylab="prix de l'action", xticks=(0, 1), yticks=(100, F),
       fmt=lambda t: "t" if t == 0 else "T", fmt_y=lambda t: "K" if t == 100 else "F",
       croix=(-0.35, 97))
f.segment(-0.35, 100, 1.55, 100)
f.courbe([(0, 100), (1, F)], couleur=ACCENT, epaisseur=2.4, pointilles="6 4")
f.texte(0.5, 102, "à coup sûr, le prix forward F = E(S_{T})", couleur=ACCENT, ancre="middle", dy=-12, taille=12)
f.mesure(1.05, 100, F, couleur=AJOUT, etiquette="payoff F − K")
f.fleche(1.0, 106.2, 0.05, 106.2, couleur=AJOUT, courbure=12)
f.texte(0.0, 106.2, "IV = e^{−rT} (F − K)^{+}", couleur=AJOUT, dx=-4, dy=-14, gras=True)
sys.stdout.write(f.svg())
