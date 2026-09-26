#!/usr/bin/env python3
r"""
descente-avec-inertie.svg — sur un gradient stable, les pas s'allongent jusqu'à un palier.

Ce que la figure doit faire voir : chaque déplacement est fait de deux morceaux, la
correction que donne le gradient maintenant (connue, la même à chaque mise à jour tant que
le gradient est stable) et la part reconduite du déplacement précédent, α fois lui. Les
barres s'empilent donc, et grandissent : 0,01 ; 0,018 ; 0,0244 ; … jusqu'au palier
0,01 / (1 − 0,8) = 0,05, cinq fois le pas sans inertie.

Chiffres de la fiche : α = 0,8, la valeur typique de la slide 184 ; une correction de
0,01 par mise à jour, choisie pour le dessin.

Usage : python courses/dss/figures/descente-avec-inertie.py > descente-avec-inertie.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

ALPHA, G, N = 0.8, 0.01, 12
PALIER = G / (1 - ALPHA)
k = 100                                   # les pas en centièmes : 0,01 vaut 1

pas, d = [], 0.0
for t in range(N):
    herite = ALPHA * d
    d = G + herite
    pas.append((herite, d))

f = Figure(xmin=0.2, xmax=N + 0.8, ymin=0, ymax=6.3, w=560, h=320,
           marges=(58, 22, 40, 14),
           titre="Sur un gradient stable, chaque pas reprend 0,8 fois le précédent : ils s'allongent jusqu'à 0,05")
virg = lambda v: ("%g" % v).replace(".", ",")
f.axes(xlab="mise à jour", ylab="déplacement du poids", xticks=range(1, N + 1), yticks=(0, 1, 2, 3, 4, 5),
       fmt=lambda v: "%d" % v, fmt_y=lambda v: virg(v / k))

for t, (herite, total) in enumerate(pas, start=1):
    f.barre(t, k * G, 0.62, couleur=ACCENT, opacite=0.85)
    if herite > 0:
        f.barre(t, k * total, 0.62, couleur=AJOUT, opacite=0.45, y0=k * G)
for t in (1, 2, 3):
    f.texte(t, k * pas[t - 1][1], virg(round(pas[t - 1][1], 4)), ancre="middle", dy=-6,
            taille=11.5)

f.segment(0.4, k * PALIER, N + 0.6, k * PALIER, couleur=ENCRE, epaisseur=1.3)
f.texte(N + 0.6, k * PALIER, "palier : 0,01 / (1 − 0,8) = 0,05, cinq fois le pas sans inertie",
        ancre="end", dy=-7, taille=11.5, gras=True)

f.texte(0.5, 5.95, "correction du gradient, 0,01 à chaque mise à jour", couleur=ACCENT,
        taille=12, gras=True)
f.texte(0.5, 5.95, "part reconduite : 0,8 fois le pas précédent", couleur=AJOUT,
        taille=12, gras=True, dy=17)

sys.stdout.write(f.svg())
