#!/usr/bin/env python3
r"""
statistique-t.svg — la statistique t compte combien d'erreurs types séparent l'estimation de zéro.

Ce que la figure doit faire voir : chaque coefficient estimé est posé sur une règle
graduée dans sa propre erreur type. α̂ tient en moins d'une graduation : on ne le
distingue pas de zéro. β̂ en demande plus de sept. La bande grise marque |t| < 2, à peu
près le seuil d'un test à 5 % sur 60 mois. La Forme se lit sur chaque règle : le nombre de
graduations jusqu'au point est θ̂ / SE(θ̂).

Le monde des 60 mois est recopié de regression-du-medaf.py, qui en est le générateur de
référence (graine 42) : β̂ = 1,556 (erreur type 0,209), α̂ = 0,59 % par mois (erreur type
0,61 %), R² = 0,489, pour l'actif 2 régressé sur le marché.

Usage : python courses/pfo/figures/statistique-t.py > statistique-t.svg
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
ta, tb = a / sea, b / seb
assert abs(ta - 0.974) < 1e-3 and abs(tb - 7.445) < 1e-3


def regle(nom, est, se, t, couleur):
    f = Figure(xmin=-2.6, xmax=8.6, ymin=-1.1, ymax=1.3, w=600, h=130, marges=(12, 6, 6, 12))
    f.barre(0, 0.55, 4, couleur=PALE, opacite=0.45, y0=-0.55)
    f.segment(-2.4, 0, 8.4, 0, couleur=DOUX, epaisseur=1.2, pointilles=None)
    for k in range(-2, 9):
        f.segment(k, -0.12, k, 0.12, couleur=DOUX, epaisseur=1.2, pointilles=None)
        f.texte(k, 0, str(k).replace("-", "−"), couleur=DOUX, ancre="middle", dy=26,
                taille=10.5)
    f.point(t, 0, couleur=couleur, r=5)
    f.texte(t, 0, "%s = %s" % (nom, fr(est, 2 if nom.startswith("β") else 2))
            + (" %" if nom.startswith("α") else ""), couleur=couleur, ancre="middle",
            dy=-14, gras=True, fond=True)
    f.texte(-2.5, 0.9, "%s ; une graduation = SE = %s%s ; t = %s" % (
        "constante α̂" if nom.startswith("α") else "pente β̂", fr(se, 2),
        " %" if nom.startswith("α") else "", fr(t, 2)), couleur=ENCRE, taille=12)
    return f


haut = regle("α̂", a, sea, ta, AJOUT)
bas = regle("β̂", b, seb, tb, ACCENT)
pied = Figure(xmin=0, xmax=1, ymin=0, ymax=1, w=600, h=40, marges=(0, 0, 0, 0))
pied.texte(0.5, 0.35, "t = θ̂ / SE(θ̂)  ·  bande grise : |t| < 2", couleur=ENCRE,
           ancre="middle", taille=14, gras=True)
from figure import Colonne      # noqa: E402
sys.stdout.write(Colonne([Planche([haut]), Planche([bas]), Planche([pied])], ecart=6,
                         titre="Combien d'erreurs types entre l'estimation et zéro").svg())
