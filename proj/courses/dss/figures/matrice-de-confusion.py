#!/usr/bin/env python3
r"""
matrice-de-confusion.svg — les cent dossiers de l'exemple, rangés dans les quatre cases.

Ce que la figure doit faire voir : la matrice elle-même, et que le verdict dépend de la
marge par laquelle on divise. Sur 100 dossiers, 10 défauts (les positifs, colorés) ; le
classifieur annonce toujours « pas de défaut ». Chaque dossier est un carré posé dans sa
case : 0 en TP, 10 en FN, 0 en FP, 90 en TN. Divisé par la seule ligne des réels
positifs, encadrée, le tableau donne la sensibilité, 0 sur 10 ; divisé par le tableau
entier, l'exactitude, 90 sur 100.

Usage : python courses/dss/figures/matrice-de-confusion.py > matrice-de-confusion.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

P, N = 10, 90                    # défauts réels, bons dossiers réels
TP, FP = 0, 0                    # le classifieur n'annonce jamais de défaut
FN, TN = P - TP, N - FP

X0, X1, X2 = 6.2, 9.6, 21.2      # bords des colonnes : prédit +, prédit −
Y0, Y1, Y2 = 0.5, 8.1, 9.7       # bords des lignes : réel −, réel +
YH = 10.5                        # en-têtes des colonnes
PAS, COTE = 0.8, 0.64            # grille des carrés, un par dossier

f = Figure(xmin=0, xmax=28, ymin=0, ymax=11.2, w=680, h=290, marges=(12, 12, 12, 12),
           titre="Le même tableau, deux dénominateurs : sensibilité 0 sur 10, exactitude 90 sur 100")


def cadre(x0, y0, x1, y1, couleur, epaisseur, pointilles=None):
    f.courbe([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], couleur=couleur,
             epaisseur=epaisseur, pointilles=pointilles)


def carres(n, x0, ytop, couleur, opacite):
    for k in range(n):
        i, j = k % 10, k // 10
        x = x0 + PAS * i + PAS / 2
        y = ytop - PAS * j
        f.barre(x, y, COTE, couleur=couleur, opacite=opacite, y0=y - COTE)


# la grille des quatre cases
f.segment(X1, Y0, X1, Y2, couleur=PALE, pointilles=None)
f.segment(X0, Y1 + 0.1, X2, Y1 + 0.1, couleur=PALE, pointilles=None)

# en-têtes
f.texte((X0 + X1) / 2, YH, "prédit +", ancre="middle", gras=True)
f.texte((X1 + X2) / 2, YH, "prédit −", ancre="middle", gras=True)
f.texte(X0, (Y1 + Y2) / 2, "réel +", ancre="end", dx=-8, dy=-2, gras=True, couleur=AJOUT)
f.texte(X0, (Y1 + Y2) / 2, "défaut, P = %d" % P, ancre="end", dx=-8, dy=13, taille=11,
        couleur=AJOUT)
f.texte(X0, (Y0 + Y1) / 2, "réel −", ancre="end", dx=-8, dy=-2, gras=True)
f.texte(X0, (Y0 + Y1) / 2, "sans défaut, N = %d" % N, ancre="end", dx=-8, dy=13, taille=11,
        couleur=DOUX)

# les cases : TP et FP vides, FN et TN remplies d'un carré par dossier
f.texte((X0 + X1) / 2, (Y1 + Y2) / 2, "TP = %d" % TP, ancre="middle", dy=4, taille=11.5)
f.texte((X0 + X1) / 2, (Y0 + Y1) / 2, "FP = %d" % FP, ancre="middle", dy=4, taille=11.5)
xs = X1 + 0.3
carres(FN, xs, Y2 - 0.15, AJOUT, 0.85)
carres(TN, xs, Y1 - 0.25, DOUX, 0.35)
xfin = xs + 10 * PAS
f.texte(xfin, (Y1 + Y2) / 2, "FN = %d" % FN, dx=8, dy=4, taille=11.5, couleur=AJOUT, gras=True)
f.texte(xfin, (Y0 + Y1) / 2, "TN = %d" % TN, dx=8, dy=4, taille=11.5, gras=True)

# les deux dénominateurs : la ligne des réels positifs, puis le tableau entier
cadre(X0, Y1 + 0.2, X2, Y2, AJOUT, 2.2)
cadre(X0 - 0.12, Y0 - 0.12, X2 + 0.12, Y2 + 0.12, ENCRE, 1.3, pointilles="5 4")
f.texte(X2, (Y1 + Y2) / 2, "sensibilité", dx=16, dy=-3, gras=True, couleur=AJOUT)
f.texte(X2, (Y1 + Y2) / 2, "TP / P = %d / %d" % (TP, P), dx=16, dy=13, taille=11.5,
        couleur=AJOUT)
f.texte(X2, (Y0 + Y1) / 2, "exactitude", dx=16, dy=-10, gras=True)
f.texte(X2, (Y0 + Y1) / 2, "(TP + TN) / (P + N)", dx=16, dy=6, taille=11.5)
f.texte(X2, (Y0 + Y1) / 2, "= %d / %d" % (TP + TN, P + N), dx=16, dy=22, taille=11.5)

sys.stdout.write(f.svg())
