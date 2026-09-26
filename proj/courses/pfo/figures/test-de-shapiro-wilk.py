#!/usr/bin/env python3
r"""
test-de-shapiro-wilk.svg — l'échantillon rangé, face aux positions attendues d'une loi normale.

L'échantillon de la fiche, $\{3, -1, 2, 5, -2\}$ en %, rangé : $-2, -1, 2, 3, 5$. En
abscisse, les positions $m_i$ qu'occuperaient en moyenne les cinq observations rangées
d'un échantillon normal centré réduit de taille 5 : $-1{,}163$, $-0{,}495$, 0, $0{,}495$,
$1{,}163$ (valeurs tabulées). Le test compare ces deux colonnes : pour un échantillon
normal, les points s'aligneraient sur une droite ; ici ils le sont presque, et $W=0{,}951$
(calculé par `scipy.stats.shapiro`, écrit dans la fiche et non sur la figure). La droite
tracée est celle des moindres carrés, pour guider l'œil.

Les étiquettes s'ancrent aux points : à gauche et au-dessus, sauf celle de $X_{(1)}$,
posée à droite et en dessous pour s'écarter de la graduation de l'axe. Les titres d'axe
sont écrits avec leurs indices, $m_i$ et $X_{(i)}$.

Usage : python courses/pfo/figures/test-de-shapiro-wilk.py > test-de-shapiro-wilk.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

X = sorted([3, -1, 2, 5, -2])
M = [-1.16296, -0.49502, 0.0, 0.49502, 1.16296]
xm = sum(X) / len(X)
pente = sum(m * x for m, x in zip(M, X)) / sum(m * m for m in M)
droite = lambda m: xm + pente * m

f = Figure(xmin=-1.5, xmax=1.5, ymin=-4, ymax=7, w=480, h=360, marges=(54, 16, 40, 18),
           titre="Chaque observation rangée, face à la position qu'elle aurait sous une loi normale")
moins = lambda t: t.replace("-", "−")
f.axes(xlab="", ylab="", xticks=(-1.163, -0.495, 0, 0.495, 1.163),
       yticks=(-2, 0, 2, 4, 6), fmt=lambda t: moins(("%g" % round(t, 3)).replace(".", ",")),
       fmt_y=lambda t: moins("%d" % t), croix=(-1.5, -4))
# Les titres d'axe, aux places que leur donnerait axes(), mais avec leurs indices.
f.texte(1.5, -4, "position attendue m_{i}", couleur=DOUX, ancre="end", dy=33, taille=12)
f.texte(-1.5, 7, "X_{(i)}, en %", couleur=DOUX, dx=-44, dy=-6, taille=12)

f.fonction(droite, -1.4, 1.4, couleur=DOUX, epaisseur=1.4, pointilles="5 4")
for i, (m, x) in enumerate(zip(M, X), start=1):
    f.point(m, x, couleur=ACCENT, r=4.5)
    s_ = moins("X_{(%d)} = %d %%" % (i, x))     # insécable : l'espace après l'indice tombait
    if i == 1:
        f.texte(m, x, s_, couleur=ACCENT, dx=8, dy=18, ancre="start", taille=11, fond=True)
    else:
        f.texte(m, x, s_, couleur=ACCENT, dx=-8, dy=-8, ancre="end", taille=11, fond=True)

sys.stdout.write(f.svg())
