#!/usr/bin/env python3
r"""
regression-du-medaf.svg — la régression du MEDAF est une droite tirée dans un nuage de mois.

Ce que la figure doit faire voir : chaque mois est un point, le rendement du marché
au-delà du taux sans risque en abscisse, celui de l'actif en ordonnée. La droite des
moindres carrés a pour pente β et coupe l'axe vertical en α ; ce qui reste, l'écart
vertical d'un point à la droite, est ε. Les trois termes de la Forme se lisent sur le
dessin, et la Forme est écrite dessous.

Ce script est le **générateur de référence** des 60 mois de pfo (chapitre 4), comme
`surapprentissage.py` l'est pour dss : les autres figures du chapitre recopient `monde()`
et `mco()` à l'identique. Le monde est celui du chapitre 3 : deux actifs non corrélés,
6 % et 10 % de rendement espéré par an, 10 % et 20 % de volatilité, un taux sans risque
de 2 %. Le marché les détient à deux tiers et un tiers, ses poids de capitalisation.
Rendements mensuels arithmétiques, gaussiens : moyenne μ/12, écart type σ/√12. La graine
est 42, celle de l'exercice 1 du cours. Le hasard est tiré par random.Random().random(),
reproductible d'une version de Python à l'autre, et transformé en gaussienne par
Box-Muller ici même, pour ne dépendre d'aucune autre fonction du module.

Résultats vérifiés par assertion : β̂ = 1,556 (erreur type 0,209, t = 7,4) ; α̂ = 0,59 %
par mois (erreur type 0,61 %, t = 0,97) ; R² = 0,489. Sans constante, la pente monte à
1,571. Les vrais paramètres sont β = 1,5 et α = 0.

Usage : python courses/pfo/figures/regression-du-medaf.py > regression-du-medaf.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def monde(graine=42, n=60):
    """60 mois de rendements des deux actifs, du marché, et le taux sans risque mensuel."""
    rng = random.Random(graine)

    def z():
        u1, u2 = rng.random(), rng.random()
        return math.sqrt(-2 * math.log(1 - u1)) * math.cos(2 * math.pi * u2)

    r1, r2 = [], []
    for _ in range(n):
        r1.append(0.06 / 12 + 0.10 / math.sqrt(12) * z())
        r2.append(0.10 / 12 + 0.20 / math.sqrt(12) * z())
    rm = [2 / 3 * a + 1 / 3 * b for a, b in zip(r1, r2)]
    return r1, r2, rm, 0.02 / 12


def mco(y, x):
    """Moindres carrés de y sur une constante et x : α̂, β̂, leurs erreurs types, R²."""
    n = len(y)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sxx
    a = my - b * mx
    ssr = sum((c - a - b * u) ** 2 for u, c in zip(x, y))
    sst = sum((c - my) ** 2 for c in y)
    s2 = ssr / (n - 2)
    return a, b, math.sqrt(s2 * (1 / n + mx * mx / sxx)), math.sqrt(s2 / sxx), 1 - ssr / sst


r1, r2, rm, rf = monde()
X = [100 * (m - rf) for m in rm]          # en %
Y = [100 * (v - rf) for v in r2]
a, b, sea, seb, r2_ = mco(Y, X)
b0 = sum(u * v for u, v in zip(X, Y)) / sum(u * u for u in X)
assert abs(b - 1.5556) < 5e-4 and abs(seb - 0.2089) < 5e-4
assert abs(a - 0.5895) < 5e-4 and abs(sea - 0.6051) < 5e-4
assert abs(r2_ - 0.4887) < 5e-4 and abs(b0 - 1.5714) < 5e-4

fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")

f = Figure(xmin=-7.5, xmax=8, ymin=-21, ymax=17, w=560, h=440, marges=(54, 16, 64, 18),
           titre="Soixante mois, une droite : sa pente est β, sa hauteur en zéro est α, "
                 "l'écart d'un mois à la droite est ε")
f.axes(xlab="marché, au-delà du taux sans risque, % par mois",
       ylab="actif 2, au-delà du taux sans risque, %",
       xticks=(-6, -3, 0, 3, 6), yticks=(-15, -10, -5, 0, 5, 10, 15),
       fmt=lambda t: fr(t, 0), croix=(0, 0))

# le mois dont l'écart à la droite est montré : le plus grand écart positif à droite de zéro
k = max((i for i in range(60) if X[i] > 1), key=lambda i: Y[i] - a - b * X[i])
for i in range(60):
    if i != k:
        f.point(X[i], Y[i], couleur=DOUX, r=2.8)
f.fonction(lambda u: a + b * u, -6.6, 7.4, couleur=ACCENT, epaisseur=2.4)
f.point(X[k], Y[k], couleur=ENCRE, r=3.6)
f.mesure(X[k], a + b * X[k], Y[k], couleur=AJOUT, etiquette="ε_{2,t}", cote="right")

# α : la hauteur de la droite en zéro
f.point(0, a, couleur=ACCENT, r=4)
f.texte(0, a, "α̂ = " + fr(a) + " %", couleur=ACCENT, ancre="end", dx=-8, dy=-8,
        gras=True, fond=True)
# β : la pente, lue sur un pas d'un point
x0 = 5.0
f.segment(x0, a + b * x0, x0 + 1, a + b * x0, couleur=ENCRE, epaisseur=1.2, pointilles=None)
f.segment(x0 + 1, a + b * x0, x0 + 1, a + b * (x0 + 1), couleur=ENCRE, epaisseur=1.2,
          pointilles=None)
f.texte(x0 + 0.5, a + b * x0, "1", couleur=ENCRE, ancre="middle", dy=15, taille=11.5)
f.texte(x0 + 1, a + b * (x0 + 0.5), "β̂ = " + fr(b), couleur=ENCRE, dx=8, dy=4,
        gras=True, fond=True)

f.texte(0.25, -21, "R_{2,t} − R_{f,t}  =  α_{2}  +  β_{2} (R_{m,t} − R_{f,t})  +  ε_{2,t}",
        couleur=ENCRE, ancre="middle", taille=14, gras=True, dy=52)

sys.stdout.write(f.svg())
