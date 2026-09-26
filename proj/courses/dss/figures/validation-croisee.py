#!/usr/bin/env python3
r"""
validation-croisee.svg — les 20 clients coupés en 5 blocs de 4, chacun évalué une fois.

Ce que la figure doit faire voir : on n'a pas de clients nouveaux, on en fabrique en en
cachant 4 au modèle ; l'erreur sur chaque bloc caché est une mesure, et leur moyenne est
l'estimation de l'erreur de test.

L'exemple de la fiche, pour le modèle à deux prédicteurs (l'endettement et le revenu).
Chaque ligne est un tour : le modèle est ajusté sur les 16 clients gris et évalué sur les
4 clients du bloc coloré, pris dans l'ordre du tirage (blocs consécutifs). À droite de
chaque tour, l'erreur quadratique moyenne sur le bloc caché ; en bas, leur moyenne, 1,66.

Usage : python courses/dss/figures/validation-croisee.py > validation-croisee.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX      # noqa: E402

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


def erreur(lignes, beta, cols):
    return sum((y - beta[0] - sum(beta[1 + i] * x[j] for i, j in enumerate(cols))) ** 2
               for x, y in lignes) / len(lignes)


rng = random.Random(GRAINE)
app = clients(rng, N_APP)
COLS = [0, 1]                                  # l'endettement et le revenu
err = []
for tour in range(5):
    appr = [r for i, r in enumerate(app) if i // 4 != tour]
    cache = [r for i, r in enumerate(app) if i // 4 == tour]
    err.append(erreur(cache, ajuster(appr, COLS), COLS))
moy = sum(err) / len(err)
fr = lambda v: ("%.2f" % v).replace(".", ",")

f = Figure(xmin=-3.2, xmax=29.8, ymin=-0.5, ymax=6.4, w=640, h=280, marges=(10, 10, 10, 10),
           titre="Cinq tours : ajuster sur 16 clients, mesurer l'erreur sur les 4 autres, puis moyenner")
XE = 21.9                                      # colonne des erreurs, juste après les blocs
for tour in range(5):
    y = 5 - tour
    for c in range(20):
        test = c // 4 == tour
        x = c + (c // 4) * 0.3
        f.barre(x + 0.5, y + 0.36, 0.82, couleur=ACCENT if test else DOUX,
                opacite=0.85 if test else 0.3, y0=y - 0.36)
    f.texte(-0.3, y, "tour %d" % (tour + 1), couleur=ENCRE, ancre="end", dy=4, taille=11.5)
    f.texte(XE, y, fr(err[tour]), couleur=ACCENT, dy=4, taille=12)
f.texte(10.6, 6.0, "20 clients, en 5 blocs de 4", couleur=ENCRE, ancre="middle", gras=True)
f.texte(XE, 6.0, "erreur sur le bloc", couleur=ACCENT, ancre="start", taille=11.5)
f.segment(XE, 0.45, XE + 2.4, 0.45, couleur=DOUX, pointilles=None)
f.texte(XE, -0.1, "moyenne : " + fr(moy), couleur=ACCENT, ancre="start", gras=True, taille=12.5)

sys.stdout.write(f.svg())
