#!/usr/bin/env python3
r"""
cp-de-mallows.svg — l'erreur d'apprentissage et la pénalité, empilées, pour chaque taille.

Les 20 clients, et les modèles emboîtés du parcours : aucun prédicteur, puis l'endettement,
le revenu, et les trois variables sans lien ajoutées une à une. Pour chaque taille $d$, la
barre grise est $\mathrm{RSS}/n$, qui baisse toujours ; la barre colorée posée dessus est la
pénalité $2d\hat\sigma^2/n$, qui monte toujours, violette à toutes les tailles ; la
hauteur totale est $C_p$, et seule la valeur du minimum est marquée, en gras. Avec
$\hat\sigma^2=1{,}40$ estimé sur le modèle complet, le total est le plus bas à $d=2$, 1,40,
et vaut 1,68 pour le modèle complet — l'exemple de la fiche.

Usage : python courses/dss/figures/cp-de-mallows.py > cp-de-mallows.svg
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

cols_complet = list(range(5))
s2 = rss(app, ajuster(app, cols_complet), cols_complet) / (N_APP - 5 - 1)
err, pen = [], []
for d in range(6):
    c = list(range(d))
    err.append(rss(app, ajuster(app, c), c) / N_APP)
    pen.append(2 * d * s2 / N_APP)
cp = [e + p for e, p in zip(err, pen)]
meilleur = min(range(6), key=lambda d: cp[d])
fr = lambda v: ("%.2f" % v).replace(".", ",")

f = Figure(xmin=-0.6, xmax=5.6, ymin=0, ymax=2.5, w=560, h=330,
           titre="L'erreur baisse, la pénalité monte : leur somme est la plus basse à deux prédicteurs")
f.axes(xlab="nombre de prédicteurs d", ylab="Cp", xticks=(0, 1, 2, 3, 4, 5), yticks=(0.5, 1, 1.5, 2),
       fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%g" % t).replace(".", ","))
for d in range(6):
    f.barre(d, err[d], 0.56, couleur=DOUX, opacite=0.5)
    if pen[d] > 0:
        f.barre(d, cp[d], 0.56, couleur=AJOUT, opacite=0.8, y0=err[d])
    f.texte(d, cp[d], fr(cp[d]), couleur=ACCENT if d == meilleur else ENCRE, ancre="middle",
            dy=-6, taille=11.5, gras=d == meilleur)
f.texte(0, 0.45, "RSS / n", couleur=ENCRE, ancre="middle", taille=11.5)
f.texte(5.0, 2.3, "pénalité 2dσ̂² / n", couleur=AJOUT, ancre="middle", taille=11.5, gras=True)

sys.stdout.write(f.svg())
