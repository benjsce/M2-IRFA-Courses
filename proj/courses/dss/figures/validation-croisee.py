#!/usr/bin/env python3
r"""
validation-croisee.svg — les 20 clients coupés en 5 blocs de 4, chacun évalué une fois.

L'exemple de la fiche. Chaque ligne est un tour : le modèle est ajusté sur les 16 clients
gris et évalué sur les 4 clients du bloc coloré. Au bout des cinq tours, chaque client a
servi exactement une fois à l'évaluation, et l'erreur retenue est la moyenne des cinq.

Usage : python courses/dss/figures/validation-croisee.py > validation-croisee.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

f = Figure(xmin=-3.2, xmax=24.5, ymin=0, ymax=6.4, w=580, h=260, marges=(10, 10, 10, 10),
           titre="Cinq tours : ajuster sur 16 clients, évaluer sur les 4 autres, puis moyenner")
for tour in range(5):
    y = 5 - tour
    for c in range(20):
        test = c // 4 == tour
        x = c + (c // 4) * 0.3
        f.barre(x + 0.5, y + 0.36, 0.82, couleur=ACCENT if test else DOUX,
                opacite=0.85 if test else 0.3, y0=y - 0.36)
    f.texte(-0.3, y, "tour %d" % (tour + 1), couleur=ENCRE, ancre="end", dy=4, taille=11.5)
    f.texte(21.9, y, "erreur %d" % (tour + 1), couleur=ACCENT, dy=4, taille=11.5)
f.texte(10.6, 6.0, "20 clients, en 5 blocs de 4", couleur=ENCRE, ancre="middle", gras=True)
f.texte(22.7, 0.2, "moyenne des 5", couleur=ACCENT, ancre="middle", gras=True)

sys.stdout.write(f.svg())
