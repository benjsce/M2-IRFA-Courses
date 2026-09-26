#!/usr/bin/env python3
r"""
meilleur-sous-ensemble.svg — les 32 modèles des 20 clients, rangés par taille.

Chaque point est l'un des $2^5=32$ modèles possibles avec les cinq prédicteurs, placé à sa
taille et à sa RSS d'apprentissage. À taille fixée, le plus bas est retenu : c'est
$\mathcal{M}_k$, et la ligne les relie. Le meilleur à un prédicteur est, par hasard, une
variable sans lien avec la perte, x3 ; le meilleur à deux est l'endettement x1 et le
revenu x2. Les étiquettes disent ce que sont ces variables, que la fiche nomme.
La ligne descend toujours : la RSS ne peut pas départager des tailles différentes.

Usage : python courses/dss/figures/meilleur-sous-ensemble.py > meilleur-sous-ensemble.svg
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

NOMS = ("x1", "x2", "x3", "x4", "x5")
tous = []
for k in range(6):
    for c in itertools.combinations(range(5), k):
        tous.append((k, rss(app, ajuster(app, list(c)), list(c)), c))
meilleurs = {}
for k, r, c in tous:
    if k not in meilleurs or r < meilleurs[k][0]:
        meilleurs[k] = (r, c)

f = Figure(xmin=-0.5, xmax=5.8, ymin=15, ymax=47, w=560, h=330,
           titre="À chaque taille, le plus bas des modèles est retenu ; entre tailles, la RSS ne tranche pas")
f.axes(xlab="nombre de prédicteurs k", ylab="RSS d'apprentissage", xticks=(0, 1, 2, 3, 4, 5),
       yticks=(20, 30, 40), fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d" % t, croix=(-0.5, 15))
for k, r, c in tous:
    f.point(k, r, couleur=DOUX, r=3.2)
f.courbe([(k, meilleurs[k][0]) for k in range(6)], couleur=ACCENT, epaisseur=2.2)
for k in range(6):
    f.point(k, meilleurs[k][0], couleur=ACCENT, r=4.5)
nom = lambda c: "{" + ", ".join(NOMS[j] for j in c) + "}" if c else "aucun"
# Les étiquettes se posent à gauche et sous leur point, là où la colonne précédente n'a
# aucun modèle : rien ne passe dessous.
f.texte(1, meilleurs[1][0], nom(meilleurs[1][1]) + " : sans lien", couleur=AJOUT, ancre="end",
        dx=-8, dy=16, taille=11.5, gras=True, fond=True)
f.texte(2, meilleurs[2][0], nom(meilleurs[2][1]) + " :", couleur=ACCENT,
        ancre="end", dx=-8, dy=18, taille=11.5, gras=True, fond=True)
f.texte(2, meilleurs[2][0], "endettement et revenu", couleur=ACCENT,
        ancre="end", dx=-8, dy=33, taille=11.5, gras=True, fond=True)

sys.stdout.write(f.svg())
