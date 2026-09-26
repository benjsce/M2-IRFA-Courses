#!/usr/bin/env python3
r"""
remplissage-des-valeurs-manquantes.svg — ffill() recopie vers l'avant, bfill() vers l'arrière.

Ce que la figure doit faire voir : la série du poly, [NaN, NaN, 100, 105, NaN], et d'où
vient chaque valeur qui bouche un trou. `ffill()` recopie la dernière valeur connue dans
la case vide qui la suit (flèche vers la droite) ; les deux premières cases, que rien ne
précède, restent vides ; `bfill()` y recopie la première valeur connue après elles
(flèches vers la gauche). Trois rangées : la série brute, après ffill(), puis après bfill().

Usage : python courses/pfo/figures/remplissage-des-valeurs-manquantes.py > remplissage-des-valeurs-manquantes.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

N = None
brute = [N, N, 100, 105, N]
apres_ffill = [N, N, 100, 105, 105]
apres_bfill = [100, 100, 100, 105, 105]

L, H = 0.84, 0.56                          # largeur et hauteur d'une case
g = Figure(xmin=-1.9, xmax=5.6, ymin=0.45, ymax=3.75, w=540, h=250, marges=(8, 8, 8, 8),
           titre="ffill() recopie vers l'avant, bfill() vers l'arrière")


def rangee(y, valeurs, etiquette, remplies=(), couleur=ENCRE):
    g.texte(0.45, y, etiquette, couleur=DOUX, taille=12, ancre="end", dy=4)
    for k, v in enumerate(valeurs, start=1):
        if k in remplies:
            g.barre(k, y + H / 2, L, couleur=couleur, opacite=0.18, y0=y - H / 2)
        g.courbe([(k - L / 2, y - H / 2), (k + L / 2, y - H / 2), (k + L / 2, y + H / 2),
                  (k - L / 2, y + H / 2), (k - L / 2, y - H / 2)], couleur=DOUX, epaisseur=1.1)
        if v is None:
            g.texte(k, y, "NaN", couleur=DOUX, taille=12, ancre="middle", dy=4)
        else:
            c = couleur if k in remplies else ENCRE
            g.texte(k, y, "%d" % v, couleur=c, taille=13, ancre="middle", dy=4.5,
                    gras=k in remplies)


rangee(3.1, brute, "série brute")
rangee(2.0, apres_ffill, "après ffill()", remplies=(5,), couleur=ACCENT)
rangee(0.9, apres_bfill, "puis bfill()", remplies=(1, 2), couleur=AJOUT)

# d'où vient chaque valeur recopiée
g.fleche(4.0, 2.0 + H / 2, 5.0, 2.0 + H / 2, couleur=ACCENT, courbure=11)
g.fleche(3.0, 0.9 + H / 2, 2.0, 0.9 + H / 2, couleur=AJOUT, courbure=9)
g.fleche(3.0, 0.9 + H / 2, 1.0, 0.9 + H / 2, couleur=AJOUT, courbure=16)

sys.stdout.write(g.svg())
