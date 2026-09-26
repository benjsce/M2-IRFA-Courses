#!/usr/bin/env python3
r"""
effet-epps.svg — une nouvelle, deux places, deux dates de rendement.

Le mécanisme que décrit la fiche, en schéma : sur deux jours, la séance de Tokyo puis
celle de New York, qui ne se recouvrent pas. Une nouvelle tombe après la clôture de
Tokyo ; New York la cote le jour même, Tokyo le lendemain. Les deux rendements qu'elle
fait bouger portent deux dates différentes, et la corrélation calculée date à date ne
les rapproche pas.

Le schéma n'est pas à l'échelle des horaires réels : il ne montre que l'ordre des
séances.

Usage : python courses/pfo/figures/effet-epps.py > effet-epps.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

f = Figure(xmin=0, xmax=2.0, ymin=0, ymax=3.2, w=560, h=260, marges=(80, 16, 36, 16),
           titre="New York cote la nouvelle le jour même, Tokyo le lendemain")

f.axe_temps(0.35, 0, 1.97, [(0.5, "jour 1"), (1.5, "jour 2")])
f.segment(1.0, 0.25, 1.0, 3.0, couleur=DOUX, epaisseur=1.0)

TOKYO, NY = 2.4, 1.3
for j in (0.0, 1.0):
    f.barre(j + 0.20, TOKYO + 0.22, 0.26, couleur=DOUX, opacite=0.5, y0=TOKYO - 0.22)
    f.barre(j + 0.72, NY + 0.22, 0.26, couleur=DOUX, opacite=0.5, y0=NY - 0.22)
f.texte(0, TOKYO, "Tokyo", couleur=ENCRE, ancre="end", dx=-8, dy=4, gras=True)
f.texte(0, NY, "New York", couleur=ENCRE, ancre="end", dx=-8, dy=4, gras=True)

NOUV = 0.45
f.point(NOUV, 3.0, couleur=AJOUT, r=5)
f.texte(NOUV, 3.0, "la nouvelle", couleur=AJOUT, dx=8, dy=4, gras=True)
f.fleche(NOUV, 2.95, 0.72, NY + 0.26, couleur=ACCENT, epaisseur=1.8)
f.fleche(NOUV + 0.02, 3.0, 1.20, TOKYO + 0.26, couleur=ACCENT, epaisseur=1.8, courbure=18)
f.texte(0.72, NY - 0.22, "rendement du jour 1", couleur=ACCENT, ancre="middle", dy=16,
        taille=11.5)
f.texte(1.20, TOKYO - 0.22, "rendement du jour 2", couleur=ACCENT, ancre="middle", dy=16,
        taille=11.5)

sys.stdout.write(f.svg())
