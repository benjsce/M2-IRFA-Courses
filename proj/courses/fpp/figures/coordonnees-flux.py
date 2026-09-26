#!/usr/bin/env python3
r"""
coordonnees-flux.svg — un flux est un point : une date, une devise.

Ce que la figure doit faire voir : un montant ne suffit pas à situer un flux ; il lui
faut une date (en abscisse) et une devise (une ligne par devise). Les trois flux de
l'exemple de la fiche — 100 euros en t, 104 euros en t+1, 100 dollars en t+½ — sont
trois points différents : aucun ne se compare directement à un autre. Pour les comparer,
il faut les amener au même point, en changeant de date le long d'une ligne, ou de devise
en passant d'une ligne à l'autre.

Usage : python courses/fpp/figures/coordonnees-flux.py > coordonnees-flux.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

t, tm, t1 = 2.4, 5.2, 8.0                  # t, t+½, t+1
yU, yE = 1.8, -1.6                         # ligne des dollars, ligne des euros
g = Figure(xmin=0, xmax=10, ymin=-4.1, ymax=3.1, w=620, h=300, marges=(8, 8, 8, 8),
           titre="Un flux est un point : une date, une devise")
g.axe_temps(yU, 1.5, 9.7, [(t, "t"), (tm, "t+½"), (t1, "t+1")])
g.axe_temps(yE, 1.5, 9.7, [(t, "t"), (tm, "t+½"), (t1, "t+1")])
g.texte(0.05, yU - 0.1, "dollars", couleur=AJOUT, gras=True, taille=12.5)
g.texte(0.05, yE - 0.1, "euros", couleur=ACCENT, gras=True, taille=12.5)

for x, y, s, c in [(t, yE, "100 €", ACCENT), (t1, yE, "104 €", ACCENT),
                   (tm, yU, "100 $", AJOUT)]:
    g.point(x, y, couleur=c, r=5.5)
    g.texte(x, y, s, couleur=c, gras=True, taille=13.5, ancre="middle", dy=-12)

# changer de date : le long d'une ligne ; changer de devise : d'une ligne à l'autre
g.fleche(t1 - 0.2, yE - 1.05, t + 0.2, yE - 1.05, couleur=DOUX, epaisseur=1.3, courbure=-10)
g.texte((t + t1) / 2, yE - 1.05, "changer de date : le long d'une ligne", couleur=DOUX,
        taille=12, ancre="middle", dy=30)
g.fleche(tm, yU - 0.62, tm, yE + 0.7, couleur=DOUX, epaisseur=1.3, pointilles="4 3")
g.texte(tm + 0.2, (yU + yE) / 2 + 0.05, "changer de devise :", couleur=DOUX, taille=12)
g.texte(tm + 0.2, (yU + yE) / 2 - 0.45, "d'une ligne à l'autre", couleur=DOUX, taille=12)

sys.stdout.write(g.svg())
