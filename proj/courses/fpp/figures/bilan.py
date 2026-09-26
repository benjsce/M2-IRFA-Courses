#!/usr/bin/env python3
r"""
bilan.svg — les deux côtés d'un bilan, de même hauteur.

Ce que la figure doit faire voir : d'un côté ce que l'entité possède, l'actif ; de
l'autre qui l'a financé, les actionnaires et les créanciers ; et les deux colonnes ont
toujours la même hauteur, $A_t=E_t+D_t$. L'exemple de la fiche : 100 = 30 + 70.

Usage : python courses/fpp/figures/bilan.py > bilan.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, ENCRE      # noqa: E402

A, E, D = 100, 30, 70
g = Figure(xmin=0, xmax=4.2, ymin=-26, ymax=122, w=500, h=320, marges=(8, 8, 8, 8),
           titre="Un bilan : ce qu'elle possède d'un côté, qui l'a financée de l'autre")

xa, xp, lg = 1.0, 3.1, 1.5                   # centres des deux colonnes, largeur
g.barre(xa, A, lg, couleur=DOUX, opacite=0.45, y0=0)
g.texte(xa, A / 2, "actif %d" % A, ancre="middle", gras=True, taille=13.5)

g.barre(xp, D, lg, couleur=DOUX, opacite=0.25, y0=0)
g.barre(xp, D + E, lg, couleur=ACCENT, opacite=0.75, y0=D)
g.texte(xp, D / 2, "dette %d" % D, ancre="middle", taille=13.5, dy=-6)
g.texte(xp, D / 2, "aux créanciers", ancre="middle", taille=11.5, couleur=DOUX, dy=12)
g.texte(xp, D + E / 2, "capitaux propres %d" % E, ancre="middle", taille=12.5, gras=True,
        dy=-3)
g.texte(xp, D + E / 2, "aux actionnaires", ancre="middle", taille=11.5, dy=13)

g.texte((xa + xp) / 2, A / 2, "=", ancre="middle", taille=26, couleur=DOUX, dy=8)
g.courbe([(0.1, 0), (3.95, 0)], couleur=DOUX, epaisseur=1.2)

g.texte(xa, A, "actif", ancre="middle", gras=True, dy=-10)
g.texte(xp, A, "passif", ancre="middle", gras=True, dy=-10)
g.texte(xa, 0, "ce qu'elle possède", ancre="middle", couleur=DOUX, taille=12, dy=20)
g.texte(xp, 0, "qui l'a financée", ancre="middle", couleur=DOUX, taille=12, dy=20)

sys.stdout.write(g.svg())
