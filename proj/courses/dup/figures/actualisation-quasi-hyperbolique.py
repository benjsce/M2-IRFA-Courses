#!/usr/bin/env python3
r"""
actualisation-quasi-hyperbolique.svg — l'exponentielle, abaissée de β partout sauf en 0.

La Forme, $D(0)=1$ et $D(t)=\beta\delta^t$ pour $t>0$, lue barre par barre : le contour en
pointillé est $\delta^t$, la barre pleine $\beta\delta^t$ ; en 0, les deux coïncident. La
mesure à la semaine 1 est le facteur $\beta$ lui-même.

Les valeurs sont choisies pour que les deux modèles se distinguent à l'œil : $\delta=0{,}9$
par semaine et $\beta=\tfrac12$ [ajout]. Avec le $\delta=1$ de l'exemple du cours, le
contour exponentiel serait plat.

Usage : python courses/dup/figures/actualisation-quasi-hyperbolique.py > actualisation-quasi-hyperbolique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

BETA, DELTA = 0.5, 0.9
T = range(0, 9)

f = Figure(xmin=-0.7, xmax=8.7, ymin=0, ymax=1.22, w=560, h=330,
           titre="Le modèle quasi-hyperbolique garde δᵗ et abaisse du même facteur β toutes les dates futures")
f.axes(xlab="semaine t", ylab="D(t)", xticks=tuple(T), yticks=(0.5, 1),
       fmt=lambda t: str(int(t)), fmt_y=lambda t: {0.5: "0,5", 1: "1"}[t])

for t in T:
    qh = 1.0 if t == 0 else BETA * DELTA ** t
    f.barre(t, qh, 0.5, couleur=ACCENT, opacite=0.85)
    ex = DELTA ** t
    x0, x1 = t - 0.25, t + 0.25
    f.courbe([(x0, 0), (x0, ex), (x1, ex), (x1, 0)], couleur=ENCRE, epaisseur=1.3, pointilles="4 3")

f.mesure(1.42, BETA * DELTA, DELTA, couleur=AJOUT, etiquette="× β")
f.texte(3.2, 1.08, "δᵗ, en pointillé", couleur=ENCRE, taille=12)
f.texte(3.2, 0.96, "βδᵗ pour t > 0, en plein ; 1 en 0", couleur=ACCENT, taille=12, gras=True)

sys.stdout.write(f.svg())
