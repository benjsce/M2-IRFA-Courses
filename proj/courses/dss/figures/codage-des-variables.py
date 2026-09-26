#!/usr/bin/env python3
r"""
codage-des-variables.svg — la valeur 4 sous les trois codages de la fiche.

Les trois écritures de l'exemple, une case par entrée du réseau, remplie quand l'entrée
vaut 1 : un parmi $N$, (0 1 0 0 0), une seule case allumée ; thermomètre, (1 1 1 1 0),
les cases s'allument jusqu'à la valeur ; valeur réelle, 0,4, une seule entrée, remplie aux
quatre dixièmes. Le premier ne dit rien de l'ordre des valeurs, le deuxième le porte, le
troisième aussi, en une entrée.

Usage : python courses/dss/figures/codage-des-variables.py > codage-des-variables.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

LIGNES = [("un parmi N", (0, 1, 0, 0, 0)), ("thermomètre", (1, 1, 1, 1, 0))]

f = Figure(xmin=-4.6, xmax=9.0, ymin=0, ymax=4.2, w=560, h=240, marges=(8, 8, 8, 8),
           titre="La même valeur, 4, écrite de trois façons pour les entrées d'un réseau")
for r, (nom, bits) in enumerate(LIGNES):
    y = 3.3 - 1.25 * r
    f.texte(-0.4, y, nom, couleur=ENCRE, ancre="end", dy=4, gras=True)
    for i, b in enumerate(bits):
        f.barre(i + 0.5, y + 0.4, 0.86, couleur=ACCENT if b else DOUX, opacite=0.85 if b else 0.18,
                y0=y - 0.4)
        f.texte(i + 0.5, y, "%d" % b, couleur="var(--card)" if b else ENCRE, ancre="middle", dy=4,
                gras=True)
    f.texte(5.4, y, "(%s)" % " ".join(str(b) for b in bits), couleur=DOUX, dy=4, taille=11.5)
y = 0.8
f.texte(-0.4, y, "valeur réelle", couleur=ENCRE, ancre="end", dy=4, gras=True)
f.barre(2.5, y + 0.4, 4.86, couleur=DOUX, opacite=0.18, y0=y - 0.4)
f.barre(0.07 + 0.4 * 4.86 / 2, y + 0.4, 0.4 * 4.86, couleur=AJOUT, opacite=0.85, y0=y - 0.4)
f.texte(5.4, y, "0,4 : une seule entrée", couleur=AJOUT, dy=4, taille=11.5, gras=True)

sys.stdout.write(f.svg())
