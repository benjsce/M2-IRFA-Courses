#!/usr/bin/env python3
r"""
regression-ridge.svg — les coefficients standardisés des 20 clients, quand λ grandit.

Les cinq prédicteurs sont standardisés, comme le demande la fiche, et la perte centrée. Pour
chaque $\lambda$, $(\mathbf X^T\mathbf X+\lambda\mathbf I)^{-1}\mathbf X^T\mathbf y$. À gauche,
$\lambda$ presque nul : les coefficients des moindres carrés. À droite, $\lambda$ très grand :
tous tendent vers zéro, sans qu'aucun ne l'atteigne. Les coefficients ne rétrécissent pas
tous au même rythme : celui de x3, la variable sans lien que le hasard a liée à la perte,
commence par grandir (0,245 à λ=0,01, 0,338 à λ=5), rejoint celui de l'endettement vers
λ=20 et le dépasse à λ=100 (0,111 contre 0,102). L'axe des λ est posé en bas du cadre, et
un trait pâle marque zéro, le modèle nul.

Usage : python courses/dss/figures/regression-ridge.py > regression-ridge.svg
Dépendance : aucune.
"""
import itertools
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT, PALE, _n      # noqa: E402

# Le monde des 20 clients, recopié de surapprentissage.py, qui en est le générateur de
# référence : même graine, même tirage, mêmes nombres.
GRAINE, N_APP, N_TEST = 78, 20, 20000


def clients(rng, n):
    lignes = []
    for _ in range(n):
        x1, x2 = rng.uniform(10, 60), rng.uniform(20, 80)
        bruit = [rng.gauss(0, 1) for _ in range(3)]
        y = 2 + 0.10 * x1 - 0.05 * x2 + rng.gauss(0, 1)
        lignes.append(([x1, x2] + bruit, y))
    return lignes


def resoudre(A, b):
    """Élimination de Gauss avec pivot partiel : les équations normales, sans numpy."""
    n = len(A)
    M = [ligne[:] + [v] for ligne, v in zip(A, b)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]
                for c in range(i, n + 1):
                    M[r][c] -= f * M[i][c]
    return [M[i][n] / M[i][i] for i in range(n)]


def ajuster(lignes, cols):
    X = [[1.0] + [x[j] for j in cols] for x, _ in lignes]
    y = [v for _, v in lignes]
    k = len(cols) + 1
    A = [[sum(r[a] * r[b] for r in X) for b in range(k)] for a in range(k)]
    b = [sum(r[a] * v for r, v in zip(X, y)) for a in range(k)]
    return resoudre(A, b)


def rss(lignes, beta, cols):
    return sum((y - beta[0] - sum(beta[1 + i] * x[j] for i, j in enumerate(cols))) ** 2
               for x, y in lignes)


rng = random.Random(GRAINE)
app = clients(rng, N_APP)

X = [x for x, _ in app]
Y = [y for _, y in app]
moy = [sum(r[j] for r in X) / N_APP for j in range(5)]
et = [math.sqrt(sum((r[j] - moy[j]) ** 2 for r in X) / N_APP) for j in range(5)]
Z = [[(r[j] - moy[j]) / et[j] for j in range(5)] for r in X]
ym = sum(Y) / N_APP
Yc = [y - ym for y in Y]


def ridge(lam):
    A = [[sum(z[a] * z[b] for z in Z) + (lam if a == b else 0) for b in range(5)] for a in range(5)]
    b = [sum(z[a] * y for z, y in zip(Z, Yc)) for a in range(5)]
    return resoudre(A, b)


LMIN, LMAX = -2.0, 4.0                      # log10 de lambda
grille = [LMIN + (LMAX - LMIN) * k / 120 for k in range(121)]
chemins = [ridge(10 ** g) for g in grille]
NOMS = ("x1 endettement", "x2 revenu")
COUL = (ACCENT, AJOUT, DOUX, DOUX, DOUX)

f = Figure(xmin=LMIN, xmax=LMAX + 1.3, ymin=-1.0, ymax=1.0, w=560, h=330,
           titre="Quand λ devient très grand, tous les coefficients tendent vers zéro, sans l'atteindre")
f.axes(xlab="λ, échelle logarithmique", ylab="coefficient standardisé",
       xticks=(-2, 0, 2, 4), yticks=(-0.8, -0.4, 0, 0.4, 0.8),
       fmt=lambda t: {-2: "0,01", 0: "1", 2: "100", 4: "10 000"}[t],
       fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(LMIN, -1.0))
f.segment(LMIN, 0, LMAX, 0, couleur=PALE, epaisseur=1.0, pointilles=None)
for j in range(5):
    f.courbe([(g, c[j]) for g, c in zip(grille, chemins)], couleur=COUL[j],
             epaisseur=2.4 if j < 2 else 1.4)
for j in range(2):
    f.texte(LMIN, chemins[0][j], NOMS[j], couleur=COUL[j], dx=6,
            dy=18 if chemins[0][j] > 0 else 16, taille=11.5, gras=True, fond=True)
f.texte(LMIN, chemins[0][2], "x3, x4, x5 : sans lien", couleur=DOUX, dx=6, dy=-8, taille=11,
        fond=True)
f.texte(LMAX, 0, "le modèle nul", couleur=ENCRE, dx=6, dy=-8, taille=11.5)

sys.stdout.write(f.svg())
