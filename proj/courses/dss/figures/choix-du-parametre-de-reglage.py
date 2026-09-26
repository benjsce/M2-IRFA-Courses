#!/usr/bin/env python3
r"""
choix-du-parametre-de-reglage.svg — l'erreur estimée par validation croisée, et le λ qu'elle retient.

Ce que la figure doit faire voir : ce qui est connu, pour chaque λ, c'est une erreur estimée
par validation croisée ; ce qu'on cherche, c'est λ ; on prend celui où la courbe est la plus
basse. Et, sur les 20 clients, ce que la banque ne voit pas : l'erreur sur des clients
nouveaux, que la validation croisée cherche à estimer.

Les 20 clients, régression ridge sur les cinq prédicteurs standardisés. En trait plein,
l'erreur estimée par validation croisée sur les cinq blocs de 4 clients (consécutifs, comme
dans la figure de la validation croisée) : 2,22 à λ presque nul, 2,13 au plus bas, vers
λ=5, 2,46 à λ=100. La courbe est presque plate. En pointillés, l'erreur mesurée sur 20 000
clients nouveaux : 1,83 à λ presque nul, 2,43 au λ retenu. Sur ces 20 clients, la validation
croisée réclame une pénalité que l'erreur de test ne justifie pas.

Usage : python courses/dss/figures/choix-du-parametre-de-reglage.py > choix-du-parametre-de-reglage.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

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


def ridge(lignes, lam):
    """Ridge sur les prédicteurs standardisés du jeu d'ajustement ; rend la prédiction."""
    n = len(lignes)
    X = [x for x, _ in lignes]
    Y = [y for _, y in lignes]
    mo = [sum(r[j] for r in X) / n for j in range(5)]
    et = [math.sqrt(sum((r[j] - mo[j]) ** 2 for r in X) / n) for j in range(5)]
    Z = [[(r[j] - mo[j]) / et[j] for j in range(5)] for r in X]
    ym = sum(Y) / n
    A = [[sum(z[a] * z[b] for z in Z) + (lam if a == b else 0) for b in range(5)] for a in range(5)]
    b = [sum(z[a] * (y - ym) for z, y in zip(Z, Y)) for a in range(5)]
    be = resoudre(A, b)
    return lambda x: ym + sum(be[j] * (x[j] - mo[j]) / et[j] for j in range(5))


def erreur(f, lignes):
    return sum((y - f(x)) ** 2 for x, y in lignes) / len(lignes)


def validation_croisee(lam):
    total = 0.0
    for k in range(5):
        ajuste = [app[i] for i in range(N_APP) if i // 4 != k]
        f = ridge(ajuste, lam)
        total += sum((app[i][1] - f(app[i][0])) ** 2 for i in range(N_APP) if i // 4 == k)
    return total / N_APP


rng = random.Random(GRAINE)
app, test = clients(rng, N_APP), clients(rng, N_TEST)

LMIN, LMAX = -2.0, 3.0                      # log10 de lambda
grille = [LMIN + (LMAX - LMIN) * k / 60 for k in range(61)]
cv = [validation_croisee(10 ** g) for g in grille]
LRET = 5.0                                   # le λ retenu sur la grille 0, 1, …, 10
cv_ret = validation_croisee(LRET)
test_zero, test_ret = erreur(ridge(app, 0.0), test), erreur(ridge(app, LRET), test)
# les erreurs de test ne sont calculées qu'aux deux points que la fiche cite, et sur une
# grille plus lâche pour la courbe : 20 000 clients par point
grille_t = [LMIN + (LMAX - LMIN) * k / 25 for k in range(26)]
tst = [erreur(ridge(app, 10 ** g), test) for g in grille_t]

f = Figure(xmin=LMIN, xmax=LMAX + 0.25, ymin=1.5, ymax=4.3, w=560, h=330,
           titre="La validation croisée retient le λ où l'erreur estimée est la plus basse")
f.axes(xlab="λ, échelle logarithmique", ylab="erreur quadratique moyenne",
       xticks=(-2, -1, 0, 1, 2, 3), yticks=(2, 3, 4),
       fmt=lambda t: {-2: "0,01", -1: "0,1", 0: "1", 1: "10", 2: "100", 3: "1 000"}[t],
       fmt_y=lambda t: "%d" % t)
f.courbe(list(zip(grille_t, tst)), couleur=DOUX, epaisseur=1.6, pointilles="6 4")
f.courbe(list(zip(grille, cv)), couleur=ACCENT, epaisseur=2.6)
lr = math.log10(LRET)
f.segment(lr, 1.5, lr, test_ret, couleur=PALE)
f.point(lr, cv_ret, couleur=ACCENT, r=5)
f.point(lr, test_ret, couleur=DOUX, r=4)
f.texte(lr, 1.5, "λ retenu, voisin de 5", couleur=ACCENT, dx=6, dy=-8, taille=11.5, gras=True)
f.texte(LMIN, cv[0], "estimée par validation croisée", couleur=ACCENT, dx=6, dy=-10,
        taille=11.5, gras=True, fond=True)
f.texte(LMIN, tst[0], "mesurée sur 20 000 clients nouveaux", couleur=DOUX, dx=6, dy=18,
        taille=11.5, fond=True)

sys.stdout.write(f.svg())
