#!/usr/bin/env python3
r"""
retropropagation.svg — l'erreur connue en sortie revient vers les nœuds cachés, chacun
en recevant une part proportionnelle à son poids vers la sortie.

Ce que la figure doit faire voir : le connu et le trou. La sortie a une cible, donc une
erreur ; les nœuds cachés n'en ont pas. La rétropropagation leur fabrique un signal
d'erreur : le $d$ de la sortie, renvoyé par le poids qui les relie à elle, puis multiplié
par leur propre pente.

Le mini-réseau de la fiche : le point $(1,0)$ du OU exclusif, dont la sortie désirée est
1, deux nœuds cachés, une sortie, des sigmoïdes, sans seuil pour garder les calculs courts.
Le passage avant a donné $o_1=0{,}5$ et $o_2=0{,}2$ aux nœuds cachés ; les poids vers la
sortie valent $0{,}4$ et $1$, d'où un total $0{,}4$ et une sortie $o_j=1/(1+e^{-0,4})\approx0{,}60$.
Puis, vers l'arrière :
    sortie   d_j = o_j (1 − o_j)(t_j − o_j)     = 0,60 × 0,40 × 0,40  ≈ 0,096
    caché 1  d_1 = o_1 (1 − o_1) · w_1j · d_j   = 0,25 × 0,4 × 0,096  ≈ 0,0096
    caché 2  d_2 = o_2 (1 − o_2) · w_2j · d_j   = 0,16 × 1 × 0,096    ≈ 0,015
Le nœud caché qui a le plus fort poids vers la sortie reçoit la plus grosse part, bien que
sa pente soit plus faible.

Usage : python courses/dss/figures/retropropagation.py > retropropagation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

O1, O2 = 0.5, 0.2                 # sorties des nœuds cachés, données par le passage avant
W1, W2 = 0.4, 1.0                 # poids des nœuds cachés vers la sortie
T = 1.0                           # sortie désirée au point (1, 0)
OJ = 1 / (1 + math.exp(-(W1 * O1 + W2 * O2)))
DJ = OJ * (1 - OJ) * (T - OJ)
D1 = O1 * (1 - O1) * W1 * DJ
D2 = O2 * (1 - O2) * W2 * DJ


def v(x, chiffres=2):
    s = ("%." + str(chiffres) + "f") % x
    return s.replace(".", ",")


def g3(x):
    """Deux chiffres significatifs : 0,096, 0,0096, 0,015."""
    e = math.floor(math.log10(abs(x)))
    return v(round(x, 1 - e), max(0, 1 - e))


f = Figure(xmin=0, xmax=14.6, ymin=-0.4, ymax=7.7, w=680, h=370, marges=(8, 8, 8, 8),
           titre="Connue en sortie, l'erreur revient vers les nœuds cachés en proportion de leur poids")
ENT = [(1.6, 5.5), (1.6, 1.5)]
CACH = [(5.4, 5.5), (5.4, 1.5)]
SORT = (9.3, 3.5)
R = 0.36                          # rayon d'un nœud, en unités de x

# vers l'avant : les sorties
for e in ENT:
    for c in CACH:
        f.fleche(e[0] + R, e[1], c[0] - R - 0.05, c[1], couleur=DOUX, epaisseur=1.3)
for (c, w, dessus) in ((CACH[0], W1, True), (CACH[1], W2, False)):
    f.fleche(c[0] + R, c[1], SORT[0] - R - 0.05, SORT[1], couleur=DOUX, epaisseur=1.3)
    mx, my = (c[0] + SORT[0]) / 2, (c[1] + SORT[1]) / 2
    f.texte(mx, my, "w = " + v(w, 1).replace(",0", ""), couleur=ENCRE, ancre="middle",
            dy=20 if dessus else -10, taille=12, fond=True)

# vers l'arrière : le d de la sortie, renvoyé par chaque poids. L'étiquette est posée
# au-delà du sommet de l'arc, du côté où il se bombe, pour ne pas le croiser.
C = 18                            # courbure des arcs, en pixels
for (c, w, dessus) in ((CACH[0], W1, True), (CACH[1], W2, False)):
    x0, y0 = SORT[0] - R * 0.7, SORT[1] + (0.3 if dessus else -0.3)
    x1, y1 = c[0] + R * 0.8, c[1] + (0.3 if dessus else -0.3)
    f.fleche(x0, y0, x1, y1, couleur=AJOUT, epaisseur=2.0, courbure=C if dessus else -C)
    X0, Y0, X1, Y1 = f.px(x0), f.py(y0), f.px(x1), f.py(y1)
    L = math.hypot(X1 - X0, Y1 - Y0)
    nx, ny = (Y1 - Y0) / L, -(X1 - X0) / L              # normale à la corde
    if (ny > 0) == dessus:                              # vers le haut pour l'arc du haut
        nx, ny = -nx, -ny
    AX, AY = (X0 + X1) / 2 + (C + 12) * nx, (Y0 + Y1) / 2 + (C + 12) * ny
    f.texte(f.xmin, f.ymax, v(w, 1).replace(",0", "") + " × " + g3(DJ), couleur=AJOUT,
            ancre="start", dx=AX - f.px(f.xmin), dy=AY - f.py(f.ymax) + (0 if dessus else 10),
            taille=12, gras=True, fond=True)

# les nœuds
for x, y in ENT:
    f.point(x, y, couleur=DOUX, r=15)
for x, y in CACH:
    f.point(x, y, couleur=ACCENT, r=15)
f.point(*SORT, couleur=ENCRE, r=15)

# entrées
f.texte(ENT[0][0] - R, ENT[0][1], "x1 = 1", couleur=ENCRE, ancre="end", dx=-6, dy=4)
f.texte(ENT[1][0] - R, ENT[1][1], "x2 = 0", couleur=ENCRE, ancre="end", dx=-6, dy=4)

# nœuds cachés : pas de cible, un d fabriqué
f.texte(CACH[0][0], CACH[0][1] + 1.45, "o = " + v(O1, 1) + ", pas de cible",
        couleur=DOUX, ancre="middle", taille=12)
f.texte(CACH[0][0], CACH[0][1] + 0.85, "d = 0,25 × 0,4 × " + g3(DJ) + " = " + g3(D1),
        couleur=ACCENT, ancre="middle", taille=12.5, gras=True)
f.texte(CACH[1][0], CACH[1][1] - 0.95, "o = " + v(O2, 1) + ", pas de cible",
        couleur=DOUX, ancre="middle", taille=12)
f.texte(CACH[1][0], CACH[1][1] - 1.55, "d = 0,16 × 1 × " + g3(DJ) + " = " + g3(D2),
        couleur=ACCENT, ancre="middle", taille=12.5, gras=True)

# sortie : la cible est connue, donc l'erreur
f.texte(SORT[0] + R, SORT[1] + 0.7, "o = " + v(OJ), couleur=ENCRE, dx=8, taille=12.5)
f.texte(SORT[0] + R, SORT[1] + 0.05, "cible t = 1, connue", couleur=ENCRE, dx=8, taille=12.5,
        gras=True)
f.texte(SORT[0] + R, SORT[1] - 0.6, "d = %s × %s × %s = %s" % (v(OJ), v(1 - OJ), v(T - OJ), g3(DJ)),
        couleur=ENCRE, dx=8, taille=12.5)

f.texte(1.6, 7.35, "entrées", couleur=DOUX, ancre="middle", gras=True)
f.texte(5.4, 7.35, "couche cachée", couleur=DOUX, ancre="middle", gras=True)
f.texte(9.3, 7.35, "sortie", couleur=DOUX, ancre="middle", gras=True)

sys.stdout.write(f.svg())
