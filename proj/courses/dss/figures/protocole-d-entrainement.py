#!/usr/bin/env python3
r"""
protocole-d-entrainement.svg — trois jeux, trois rôles : apprendre, régler, juger.

Ce que la figure doit faire voir : les exemples disponibles se coupent en trois jeux qui
ne se mélangent pas. Sur grand échantillon (slide 181), un seul découpage au hasard :
70 % pour l'apprentissage et le réglage, 30 % pour le jeu de production, qui donne
l'erreur de généralisation. Sur petit échantillon (slide 182), dix blocs : neuf pour
l'apprentissage et le réglage, un pour la production, et l'on recommence dix fois, chaque
bloc servant à son tour ; l'erreur est la moyenne des dix, avec son écart type.

La slide ne chiffre pas le partage entre apprentissage et réglage : le trait qui les
sépare est posé pour le dessin, sans graduation.

Usage : python courses/dss/figures/protocole-d-entrainement.py > protocole-d-entrainement.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX, FOND      # noqa: E402

H = 0.8                                   # hauteur d'une bande
f = Figure(xmin=-2, xmax=102, ymin=-0.9, ymax=5.0, w=620, h=220, marges=(8, 8, 8, 8),
           titre="Trois jeux séparés : un pour apprendre, un pour régler, un pour juger")


def bande(y, x0, x1, couleur, opacite):
    f.barre((x0 + x1) / 2, y + H, x1 - x0, couleur=couleur, opacite=opacite, y0=y)


def trois(y, fin_app, fin_reg):
    bande(y, 0, fin_app, DOUX, 0.35)
    bande(y, fin_app, fin_reg, AJOUT, 0.55)
    bande(y, fin_reg, 100, ACCENT, 0.85)


# grand échantillon : un découpage
y1 = 3.2
f.texte(0, y1 + H, "grand échantillon : un seul découpage, au hasard", dy=-7, gras=True,
        taille=12.5)
trois(y1, 48, 70)
f.texte(24, y1 + H / 2, "apprendre", ancre="middle", dy=4, taille=12)
f.texte(59, y1 + H / 2, "régler", ancre="middle", dy=4, taille=12, couleur=FOND, gras=True)
f.texte(85, y1 + H / 2, "juger : production", ancre="middle", dy=4, taille=12,
        couleur=FOND, gras=True)
f.texte(70, y1, "70 %", ancre="end", dx=-3, dy=15, taille=11.5, couleur=DOUX)
f.texte(100, y1, "30 %", ancre="end", dy=15, taille=11.5, couleur=DOUX)

# petit échantillon : dix blocs, dix fois ; les rôles se lisent aux couleurs de la bande du haut
y2 = 0.4
f.texte(0, y2 + H, "petit échantillon : dix blocs, et l'on recommence dix fois",
        dy=-7, gras=True, taille=12.5)
for k in range(10):
    couleur, opacite = (DOUX, 0.35) if k < 7 else (AJOUT, 0.55) if k < 9 else (ACCENT, 0.85)
    f.barre(10 * k + 5, y2 + H, 9.3, couleur=couleur, opacite=opacite, y0=y2)
f.texte(90, y2, "90 %", ancre="end", dx=-3, dy=15, taille=11.5, couleur=DOUX)
f.texte(100, y2, "10 %", ancre="end", dy=15, taille=11.5, couleur=DOUX)
f.texte(0, y2, "chaque bloc juge à son tour ; l'erreur est la moyenne des dix",
        dy=15, taille=11.5, couleur=ACCENT)

sys.stdout.write(f.svg())
