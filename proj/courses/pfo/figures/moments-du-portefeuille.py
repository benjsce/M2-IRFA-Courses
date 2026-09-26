#!/usr/bin/env python3
r"""
moments-du-portefeuille.svg — la variance d'un portefeuille est une grille qu'on somme.

Ce que la figure doit faire voir : σp² est la somme des cases w_i w_j σ_ij d'une grille
N × N ; la diagonale porte les variances, le reste les covariances. La moyenne pondérée
des volatilités n'est la volatilité du portefeuille que si les cases hors diagonale sont
pleines, c'est-à-dire si les actifs sont parfaitement corrélés.

Deux cadres, mêmes actifs que l'exemple de la fiche (poids ½ et ½, volatilités 10 % et
20 %). À gauche, sans corrélation, l'exemple : 0,0025 + 0,01 = 0,0125, σp = 11,18 %. À
droite, corrélation parfaite : σ12 = 0,10 × 0,20 = 0,02, chaque case hors diagonale vaut
0,005, la somme 0,0225, σp = 15 %, la moyenne des volatilités. Chaque case porte un carré
d'aire proportionnelle à sa valeur ; la case la plus grande, 0,01, est pleine.

Usage : python courses/pfo/figures/moments-du-portefeuille.py > moments-du-portefeuille.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, ENCRE, DOUX, PALE      # noqa: E402

W = (0.5, 0.5)
SIG = (0.10, 0.20)
fr = lambda v, d: ("%.*f" % (d, v)).replace(".", ",")


def cadre(rho, titre, note):
    cases = [[W[i] * W[j] * (SIG[i] ** 2 if i == j else rho * SIG[i] * SIG[j])
              for j in range(2)] for i in range(2)]
    total = sum(sum(r) for r in cases)
    f = Figure(xmin=0, xmax=2.8, ymin=-1.35, ymax=2.8, w=280, h=390, marges=(10, 10, 10, 10))
    f.texte(1.7, 2.5, titre, couleur=ENCRE, ancre="middle", taille=12.5, gras=True)
    for j in range(2):
        f.texte(0.7 + j + 0.5, 2.1, "actif %d" % (j + 1), couleur=DOUX, ancre="middle",
                taille=11.5)
    for i in range(2):
        yc = 1.5 - i                      # l'actif 1 en haut
        f.texte(0.62, yc, "actif %d" % (i + 1), couleur=DOUX, ancre="end", dy=4, taille=11.5)
        for j in range(2):
            xc = 0.7 + j + 0.5
            f.courbe([(xc - .5, yc - .5), (xc + .5, yc - .5), (xc + .5, yc + .5),
                      (xc - .5, yc + .5), (xc - .5, yc - .5)], couleur=PALE, epaisseur=1.2)
            v = cases[i][j]
            if v > 0:
                c = math.sqrt(v / 0.01) * 0.92          # côté ∝ racine : aire ∝ valeur
                f.barre(xc, yc + c / 2, c, couleur=ACCENT if i == j else AJOUT,
                        opacite=0.28, y0=yc - c / 2)
            f.texte(xc, yc, fr(v, 4) if v else "0", couleur=ENCRE if v else DOUX,
                    ancre="middle", dy=4, taille=12)
    f.texte(1.7, -0.3, "somme " + fr(total, 4), couleur=ENCRE, ancre="middle", taille=12.5)
    f.texte(1.7, -0.75, "σ_{p}\u00a0= " + fr(100 * math.sqrt(total), 2).rstrip("0").rstrip(",")
            + " %", couleur=ACCENT, ancre="middle", taille=13.5, gras=True)
    f.texte(1.7, -1.15, note, couleur=DOUX, ancre="middle", taille=11.5)
    return f


gauche = cadre(0.0, "sans corrélation", "sous la moyenne des volatilités")
droite = cadre(1.0, "corrélation parfaite", "la moyenne des volatilités")
sys.stdout.write(Planche([gauche, droite], ecart=30,
                         titre="La variance est la somme des cases ; sans corrélation, "
                               "les cases hors diagonale sont vides").svg())
