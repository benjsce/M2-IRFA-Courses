#!/usr/bin/env python3
r"""
coefficient-de-determination.svg — R² est la part de la dispersion que la droite emporte.

Ce que la figure doit faire voir : la dispersion totale de l'actif autour de sa moyenne,
la somme des (Y_t − Ȳ)², est une longueur. La droite du marché en explique une partie ;
il reste la somme des carrés des résidus, (Y_t − Ŷ_t)². R² est 1 moins la part qui reste,
lue sur la barre. La Forme est écrite dessous.

Le monde des 60 mois est recopié de regression-du-medaf.py, qui en est le générateur de
référence (graine 42) : β̂ = 1,556 (erreur type 0,209), α̂ = 0,59 % par mois (erreur type
0,61 %), R² = 0,489, pour l'actif 2 régressé sur le marché.

Usage : python courses/pfo/figures/coefficient-de-determination.py > coefficient-de-determination.svg
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
n = len(Y)
my = sum(Y) / n
sst = sum((v - my) ** 2 for v in Y)
ssr = sum((v - a - b * u) ** 2 for u, v in zip(X, Y))
sse = sst - ssr
assert abs(sst - 2476.66) < 0.05 and abs(ssr - 1266.36) < 0.05
fe = lambda v: ("%.0f" % v)

f = Figure(xmin=-0.04, xmax=1.04, ymin=-1.3, ymax=1.5, w=600, h=250, marges=(10, 10, 10, 10),
           titre="R² : la part de la dispersion que la droite emporte")
f.texte(0, 1.25, "dispersion totale  Σ(Y_{t} − Ȳ)² = " + fe(sst), couleur=ENCRE, taille=12.5)
f.barre(0.5, 1.0, 1.0, couleur=DOUX, opacite=0.30, y0=0.7)
f.barre(sse / sst / 2, 0.3, sse / sst, couleur=ACCENT, opacite=0.35, y0=0.0)
f.barre(sse / sst + ssr / sst / 2, 0.3, ssr / sst, couleur=AJOUT, opacite=0.35, y0=0.0)
f.texte(sse / sst / 2, 0.15, "expliqué par le marché : " + fe(sse), couleur=ENCRE,
        ancre="middle", dy=4, taille=12)
f.texte(sse / sst + ssr / sst / 2, 0.15, "résidus  Σ(Y_{t} − Ŷ_{t})² = " + fe(ssr),
        couleur=ENCRE, ancre="middle", dy=4, taille=12)
f.mesure_h(-0.2, 0, sse / sst, couleur=ACCENT)
f.texte(sse / sst / 2, -0.2, "R² = 1 − " + fe(ssr) + " / " + fe(sst) + " = " + fr(r2_, 3),
        couleur=ACCENT, ancre="middle", dy=20, gras=True)
f.texte(0.5, -1.3, "R² = 1 − Σ(Y_{t} − Ŷ_{t})² / Σ(Y_{t} − Ȳ)²", couleur=ENCRE,
        ancre="middle", taille=14, gras=True, dy=-8)

sys.stdout.write(f.svg())
