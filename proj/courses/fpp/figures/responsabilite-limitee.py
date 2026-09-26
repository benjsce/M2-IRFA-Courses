#!/usr/bin/env python3
r"""
responsabilite-limitee.svg — le rendement des capitaux propres selon celui de l'actif.

Avec le levier de l'exemple, $l=3{,}33$, les capitaux propres rendent $l$ fois l'actif :
une droite de pente 3,33. Elle atteint $-100\,\%$ quand l'actif perd $1/l=30\,\%$, le
seuil de faillite de la fiche. En dessous, la responsabilité limitée coupe la droite :
l'actionnaire ne perd pas plus que sa mise, et c'est la dette qui encaisse le reste. Le
prolongement pointillé est la perte que l'actionnaire aurait subie sans elle.

Usage : python courses/fpp/figures/responsabilite-limitee.py > responsabilite-limitee.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

L = 100 / 30
SEUIL = -100 / L                                  # -30 %

f = Figure(xmin=-52, xmax=22, ymin=-170, ymax=80, w=560, h=340,
           titre="Au-delà de −30 % sur l'actif, l'actionnaire a tout perdu, et pas davantage")
f.axes(xlab="actif, en %", ylab="capitaux propres, en %",
       xticks=(-50, -30, -10, 10), yticks=(-150, -100, -33, 33),
       fmt=lambda t: "%+d" % t, fmt_y=lambda t: "%+d" % t, croix=(0, 0))

f.courbe([(-50, L * -50), (SEUIL, -100)], couleur=DOUX, epaisseur=1.6, pointilles="6 4")
f.courbe([(-50, -100), (SEUIL, -100), (20, L * 20)], couleur=ACCENT, epaisseur=2.8)
f.point(SEUIL, -100, couleur=AJOUT, r=4.5)
f.texte(SEUIL, -100, "faillite : −1/l = −30 %", couleur=AJOUT, dx=8, dy=18, gras=True,
        fond=True)
f.texte(-50, -100, "plancher : la mise", couleur=ACCENT, dy=-8, taille=11.5, fond=True)
f.texte(-44, L * -44, "sans responsabilité limitée", couleur=DOUX, dx=8, dy=4, taille=11,
        fond=True)
f.point(-10, L * -10, couleur=ENCRE)
f.texte(-10, L * -10, "−10 % → −33 %", couleur=ENCRE, ancre="end", dx=-8, dy=-6, taille=11.5, fond=True)
f.texte(12, L * 12, "pente l = 3,33", couleur=ACCENT, ancre="end", dx=-8, dy=-4, gras=True,
        fond=True)

sys.stdout.write(f.svg())
