#!/usr/bin/env python3
r"""
alpha-de-jensen.svg — l'alpha est la hauteur dont l'actif dépasse ce que son bêta lui vaut.

Ce que la figure doit faire voir : dans le plan bêta – rendement moyen au-delà du taux
sans risque, la droite issue de zéro qui passe par le marché (bêta 1) donne, pour chaque
bêta, le rendement que le marché seul explique. L'actif 2, au bêta estimé 1,56, a fait
mieux en moyenne sur les 60 mois ; l'écart vertical entre son point et la droite est α̂.
La Forme se lit en descendant : moyenne de l'actif, moins β̂ fois moyenne du marché.

Le monde des 60 mois est recopié de regression-du-medaf.py, qui en est le générateur de
référence (graine 42) : β̂ = 1,556 (erreur type 0,209), α̂ = 0,59 % par mois (erreur type
0,61 %), R² = 0,489, pour l'actif 2 régressé sur le marché.

Usage : python courses/pfo/figures/alpha-de-jensen.py > alpha-de-jensen.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


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
assert abs(b - 1.5556) < 5e-4 and abs(a - 0.5895) < 5e-4 and abs(r2_ - 0.4887) < 5e-4
fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")
n = len(X)
mx, my = sum(X) / n, sum(Y) / n
assert abs(my - b * mx - a) < 1e-12          # l'identité des moindres carrés
assert abs(mx - 0.2241) < 5e-4 and abs(my - 0.9382) < 5e-4

f = Figure(xmin=0, xmax=2.1, ymin=-0.32, ymax=1.2, w=560, h=380, marges=(54, 16, 20, 18),
           titre="Au-dessus de ce que son bêta lui vaut, de α̂")
f.axes(xlab="bêta", ylab="rendement moyen au-delà du taux sans risque, % par mois",
       xticks=(0, 1, round(b, 2)), yticks=(0, round(mx, 2), round(b * mx, 2), round(my, 2)),
       fmt=lambda t: fr(t, 2).rstrip("0").rstrip(","), croix=(0, 0))
f.fonction(lambda u: u * mx, 0, 2.0, couleur=ACCENT, epaisseur=2.2)
f.texte(1.9, 1.9 * mx, "β × moyenne du marché", couleur=ACCENT, ancre="end", dy=-8,
        taille=11.5, fond=True)
f.point(1, mx, couleur=ACCENT, r=4)
f.texte(1, mx, "marché", couleur=ACCENT, dx=6, dy=16, taille=11.5)
f.segment(b, 0, b, my, couleur=PALE, epaisseur=1.0)
f.point(b, b * mx, couleur=ACCENT, r=3.4)
f.point(b, my, couleur=ENCRE, r=4.4)
f.texte(b, my, "actif 2 : " + fr(my) + " %", couleur=ENCRE, dx=8, dy=4, gras=True)
f.mesure(b, b * mx, my, couleur=AJOUT, etiquette="α̂ = " + fr(a) + " %", cote="left")
f.texte(1.05, -0.32, "α̂_{2} = moy(R_{2,t} − R_{f,t}) − β̂_{2} × moy(R_{m,t} − R_{f,t})",
        couleur=ENCRE, ancre="middle", taille=13.5, gras=True, dy=-10)

sys.stdout.write(f.svg())
