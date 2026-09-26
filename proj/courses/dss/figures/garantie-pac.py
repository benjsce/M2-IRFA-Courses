#!/usr/bin/env python3
r"""
garantie-pac.svg — dix exemples par poids : le nombre d'exemples qu'exige la borne.

Ce que la figure doit faire voir : ce qui est connu, le réseau (ses W poids) et la
tolérance ε, fixe la taille d'un rectangle ; ce qu'on cherche, le nombre d'exemples m, en
est l'aire. Une colonne par poids, 1/ε cases par colonne : pour le réseau 5-20-1 de la
banque, 141 colonnes de 10, soit 1 410 exemples. Les 20 clients dont la banque dispose
n'en remplissent que deux colonnes.

141 poids : chacun des 20 neurones cachés reçoit les 5 entrées et un seuil (120), la
sortie reçoit les 20 neurones cachés et un seuil (21).

Usage : python courses/dss/figures/garantie-pac.py > garantie-pac.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX, FOND      # noqa: E402

ENTREES, CACHES, EPS, CLIENTS = 5, 20, 0.1, 20
W = CACHES * (ENTREES + 1) + (CACHES + 1)          # 141
PAR_POIDS = round(1 / EPS)                          # 10
M = W * PAR_POIDS                                   # 1 410
pleines = CLIENTS // PAR_POIDS                      # 2 colonnes

f = Figure(xmin=-36, xmax=W + 3, ymin=-5.2, ymax=14.6, w=660, h=220, marges=(8, 8, 8, 8),
           titre="La borne demande 1/ε exemples par poids : 1 410 pour le réseau de la banque, qui a 20 clients")

for c in range(W):
    f.barre(c + 0.5, PAR_POIDS, 0.78, couleur=ACCENT if c < pleines else DOUX,
            opacite=0.9 if c < pleines else 0.28, y0=0)
for r in range(1, PAR_POIDS):
    f.courbe([(0, r), (W, r)], couleur=FOND, epaisseur=0.9)

# le connu : W colonnes en largeur, 1/ε cases en hauteur
f.courbe([(0, 11.4), (W, 11.4)], couleur=ENCRE, epaisseur=1.2)
f.courbe([(0, 10.8), (0, 12.0)], couleur=ENCRE, epaisseur=1.2)
f.courbe([(W, 10.8), (W, 12.0)], couleur=ENCRE, epaisseur=1.2)
f.texte(W / 2, 11.4, "connu : W = %d poids, une colonne par poids" % W, ancre="middle",
        dy=-7, gras=True, taille=12.5)
f.courbe([(-1.6, 0), (-1.6, PAR_POIDS)], couleur=ENCRE, epaisseur=1.2)
f.courbe([(-2.4, 0), (-0.8, 0)], couleur=ENCRE, epaisseur=1.2)
f.courbe([(-2.4, PAR_POIDS), (-0.8, PAR_POIDS)], couleur=ENCRE, epaisseur=1.2)
f.texte(-3.2, PAR_POIDS / 2, "connu : ε = 0,1", ancre="end", dy=-4, gras=True, taille=11.5)
f.texte(-3.2, PAR_POIDS / 2, "1/ε = %d par poids" % PAR_POIDS, ancre="end", dy=11, taille=11.5,
        couleur=DOUX)

# le trou : l'aire, et ce que la banque a
f.texte(W / 2, 0, "cherché : m > W/ε = %d × %d = %s exemples" % (W, PAR_POIDS,
        "{:,}".format(M).replace(",", " ")), ancre="middle", dy=20, gras=True, taille=13)
f.texte(0, 0, "↑ les %d clients de la banque : deux colonnes" % CLIENTS, couleur=ACCENT,
        dy=38, gras=True, taille=12)

sys.stdout.write(f.svg())
