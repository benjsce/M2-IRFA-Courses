#!/usr/bin/env python3
r"""
boosting.svg — la prédiction du boosting après 10, 100 et 1 000 arbres.

Les 20 clients, la perte en fonction de l'endettement seul. Chaque arbre n'a qu'une
coupure, et le rétrécissement vaut $\lambda=0{,}01$, les valeurs de l'exemple de la fiche.
On part de $\hat f=0$ et des résidus $r=y$ ; chaque arbre est ajusté sur les résidus
courants, et l'on n'en ajoute qu'un centième. Après 10 arbres la prédiction a à peine
bougé ; après 100 elle a pris la tendance ; après 1 000 elle suit les points en escalier.

Usage : python courses/dss/figures/boosting.py > boosting.svg
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

xs = [x[0] for x, _ in app]
ys = [y for _, y in app]
LAM = 0.01


def souche(res):
    # la coupure qui minimise la RSS des résidus : un seuil sur x, une valeur de chaque côté
    ordre = sorted(set(xs))
    meilleur = None
    for a, b in zip(ordre, ordre[1:]):
        s = (a + b) / 2
        g = [r for x, r in zip(xs, res) if x <= s]
        d = [r for x, r in zip(xs, res) if x > s]
        mg, md = sum(g) / len(g), sum(d) / len(d)
        e = sum((r - mg) ** 2 for r in g) + sum((r - md) ** 2 for r in d)
        if meilleur is None or e < meilleur[0]:
            meilleur = (e, s, mg, md)
    return meilleur[1:]


arbres, res, fits = [], ys[:], {}
for b in range(1, 1001):
    s, mg, md = souche(res)
    arbres.append((s, mg, md))
    res = [r - LAM * (mg if x <= s else md) for x, r in zip(xs, res)]
    if b in (10, 100, 1000):
        fits[b] = list(arbres)


def prediction(x, liste):
    return sum(LAM * (mg if x <= s else md) for s, mg, md in liste)


f = Figure(xmin=8, xmax=66, ymin=-0.5, ymax=7.3, w=560, h=340,
           titre="Chaque arbre corrige un centième de ce qui reste : la prédiction rattrape les points lentement")
f.axes(xlab="endettement x1, en %", ylab="perte, en k€", xticks=(10, 20, 30, 40, 50, 60),
       yticks=(0, 2, 4, 6), fmt=lambda t: "%d" % t, fmt_y=lambda t: "%d" % t, croix=(8, 0))
grille = [8 + 58 * k / 400 for k in range(401)]
for b, coul, ep in ((10, DOUX, 1.8), (100, AJOUT, 2.0), (1000, ACCENT, 2.4)):
    f.courbe([(x, prediction(x, fits[b])) for x in grille], couleur=coul, epaisseur=ep)
for x, y in zip(xs, ys):
    f.point(x, y, couleur=ENCRE, r=3.4)
f.texte(65, prediction(65, fits[10]), "10 arbres", couleur=DOUX, ancre="end", dy=-6,
        taille=11.5, gras=True, fond=True)
f.texte(65, prediction(65, fits[100]), "100", couleur=AJOUT, ancre="end", dy=-6,
        taille=11.5, gras=True, fond=True)
f.texte(65, prediction(65, fits[1000]), "1 000", couleur=ACCENT, ancre="end", dy=-6,
        taille=11.5, gras=True, fond=True)

sys.stdout.write(f.svg())
