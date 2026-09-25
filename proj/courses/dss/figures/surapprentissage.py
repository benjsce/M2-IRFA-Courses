#!/usr/bin/env python3
r"""
surapprentissage.svg — l'erreur d'apprentissage baisse toujours, l'erreur de test non.

C'est aussi le générateur du monde numérique de dss (SPEC-INGESTION, étape 3) : 20
anciens clients en défaut, pour chacun l'endettement x1 (en %, entre 10 et 60), le revenu
x2 (en k€, entre 20 et 80), trois variables sans lien avec la perte x3, x4, x5, et la
perte subie y (en k€). La vraie règle, que la banque ignore :
    y = 2 + 0,10 x1 − 0,05 x2 + ε,   ε de loi normale, d'écart type 1.
Graine 78 ; 20 000 clients nouveaux, tirés de la même loi, mesurent l'erreur de test.
Les nombres cités par les fiches du parcours « Choisir les variables » sortent d'ici.

La figure ajuste par moindres carrés les modèles emboîtés — aucun prédicteur, x1, x1 et
x2, puis x3, x4, x5 ajoutés un à un — et trace, pour chacun, l'erreur quadratique moyenne
sur les 20 clients (RSS/20) et sur les 20 000 nouveaux.

Usage : python courses/dss/figures/surapprentissage.py > surapprentissage.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

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
app, test = clients(rng, N_APP), clients(rng, N_TEST)
app_err, test_err = [], []
for d in range(6):
    cols = list(range(d))
    beta = ajuster(app, cols)
    app_err.append(erreur(app, beta, cols))
    test_err.append(erreur(test, beta, cols))

f = Figure(xmin=-0.3, xmax=5.6, ymin=0, ymax=4.6, w=560, h=320,
           titre="Ajouter des prédicteurs fait toujours baisser l'erreur d'apprentissage")
f.axes(xlab="nombre de prédicteurs", ylab="erreur quadratique moyenne",
       xticks=(0, 1, 2, 3, 4, 5), yticks=(0, 1, 2, 3, 4), fmt=lambda t: str(int(t)))
f.segment(2, 0, 2, 4.3, couleur=PALE)
f.courbe(list(zip(range(6), app_err)), couleur=DOUX, epaisseur=2.0)
f.courbe(list(zip(range(6), test_err)), couleur=ACCENT, epaisseur=2.4)
for d in range(6):
    f.point(d, app_err[d], couleur=DOUX)
    f.point(d, test_err[d], couleur=ACCENT)
f.texte(5, test_err[5], "sur 20 000 clients nouveaux", couleur=ACCENT, dx=-6, dy=-12,
        ancre="end", taille=11.5, gras=True, fond=True)
f.texte(5, app_err[5], "sur les 20 clients d'apprentissage", couleur=DOUX, dx=-6, dy=20,
        ancre="end", taille=11.5, fond=True)
f.texte(2, 4.3, "endettement et revenu", couleur=ENCRE, dx=6, dy=4, taille=11.5)

sys.stdout.write(f.svg())
