#!/usr/bin/env python3
r"""
valeur-de-continuation-non-concave.svg — une valeur non concave fait sauter la richesse transmise.

D'après le schéma de la slide 32 [L5 slide 32], simplifié à son cadre de droite. La courbe
est $\beta\delta R\,V(w_2)$ : croissante, mais avec une bosse où elle cesse d'être concave.
Le moi 1 choisit $w_2$ là où la pente de cette courbe égale $u'(c_1)$. Une droite de cette
pente la touche en deux points à la fois ; quand la richesse du moi 1 franchit le seuil
correspondant, le point retenu passe de l'un à l'autre, et $w_2$ saute.

La courbe est schématique [ajout] : $\ln(1+w)$ plus une marche logistique ; la source ne
donne pas de forme. La droite est calculée : sa pente est celle pour laquelle les deux
maxima locaux de $g(w)-m\,w$ sont égaux, trouvée par dichotomie.

Usage : python courses/dup/figures/valeur-de-continuation-non-concave.py > valeur-de-continuation-non-concave.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

def g(w):
    return 1.6 * math.log(1 + w) + 1.5 / (1 + math.exp(-3.2 * (w - 5.0)))

GRILLE = [i / 400 for i in range(0, 4001)]           # w de 0 à 10
MIL = 5.0

def meilleurs(m):
    a = max((g(w) - m * w, w) for w in GRILLE if w <= MIL)
    b = max((g(w) - m * w, w) for w in GRILLE if w > MIL)
    return a, b

lo, hi = 0.05, 1.5
for _ in range(60):
    m = (lo + hi) / 2
    a, b = meilleurs(m)
    if a[0] > b[0]:
        hi = m
    else:
        lo = m
m = (lo + hi) / 2
(ka, wa), (kb, wb) = meilleurs(m)
k = (ka + kb) / 2

f = Figure(xmin=0, xmax=10.4, ymin=0, ymax=6.4, w=560, h=340, marges=(64, 22, 40, 18),
           titre="Une droite de pente u′(c₁) touche la valeur en deux points : la richesse transmise saute de l'un à l'autre")
f.axes(xlab="w₂", ylab="βδRV(w₂)")
f.fonction(g, 0, 10.2, n=300, couleur=ACCENT, epaisseur=2.4)
XF = min(10.2, (6.1 - k) / m)
f.courbe([(0.3, k + m * 0.3), (XF, k + m * XF)], couleur=AJOUT, epaisseur=1.5, pointilles="6 4")
for w in (wa, wb):
    f.point(w, g(w), couleur=ENCRE, r=4.2)
    f.segment(w, 0, w, g(w))
f.fleche(wa + 0.2, 0.45, wb - 0.2, 0.45, couleur=ENCRE, epaisseur=1.6)
f.texte((wa + wb) / 2, 0.45, "w₂ saute", couleur=ENCRE, ancre="middle", dy=-8, gras=True, fond=True)
f.texte(XF, k + m * XF, "pente u′(c₁)", couleur=AJOUT, ancre="end", dx=-10, dy=4, gras=True)
f.texte(5.0, g(5.0), "non concave", couleur=ACCENT, dx=12, dy=14, taille=12)

sys.stdout.write(f.svg())
