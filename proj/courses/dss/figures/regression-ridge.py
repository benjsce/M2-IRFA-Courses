#!/usr/bin/env python3
r"""
regression-ridge.svg — le critère de ridge, dessiné comme la somme que la Forme écrit.

Pour qu'un seul coefficient se voie, l'endettement seul, standardisé, face à la perte
centrée des 20 clients : RSS(β) = Σ (yᵢ − β zᵢ)² est une parabole de sommet β̂ls, la
pénalité λβ² une parabole de sommet 0, et leur somme, le critère de ridge, une parabole de
sommet β̂ridge = Σ zᵢyᵢ / (Σ zᵢ² + λ), entre les deux : c'est, à une dimension,
(XᵀX + λI)⁻¹Xᵀy. Σ zᵢ² vaut 20 puisque z est standardisé ; le dessin prend λ = 20, pour que
le glissement se voie : le coefficient est divisé par deux, 20 / (20 + 20). Chaque cadre a
sa propre échelle verticale, sans graduation ; les abscisses sont communes.

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


LAM = 20.0
z = [r[0] for r in Z]                       # l'endettement, standardisé
Szz = sum(v * v for v in z)                 # vaut 20 : z est standardisé sur les 20 clients
Szy = sum(v * y for v, y in zip(z, Yc))
Syy = sum(y * y for y in Yc)
b_ls, b_r = Szy / Szz, Szy / (Szz + LAM)
RSS = lambda b: Syy - 2 * b * Szy + b * b * Szz
PEN = lambda b: LAM * b * b
CRI = lambda b: RSS(b) + PEN(b)
B0, B1 = -0.25, 1.1


def cadre(g, couleur, nom, formule, sommet, lab):
    bas = min(g(B0 + (B1 - B0) * k / 100) for k in range(101))
    haut = max(g(B0), g(B1))
    y0 = bas - 0.25 * (haut - bas)
    f = Figure(xmin=B0, xmax=B1, ymin=y0, ymax=haut + 0.35 * (haut - bas), w=210, h=262,
               marges=(10, 30, 70, 8))
    f.axes(xticks=(0,), fmt=lambda t: "0", croix=(B0, y0))
    YMAX = f.ymax
    f.fonction(g, B0, B1, couleur=couleur, epaisseur=2.4)
    f.segment(b_ls, y0, b_ls, g(b_ls), couleur=PALE)
    f.point(sommet, g(sommet), couleur=couleur)
    f.texte(sommet, g(sommet), lab, couleur=couleur, ancre="middle", dy=-10, gras=True, taille=12)
    f.texte((B0 + B1) / 2, YMAX, nom, ancre="middle", dy=-12, couleur=couleur, gras=True, taille=12.5)
    f.texte((B0 + B1) / 2, y0, formule, ancre="middle", dy=36, couleur=couleur, taille=12)
    if sommet == b_r:
        f.texte((B0 + B1) / 2, y0, "β̂ridge = Σ zᵢyᵢ / (Σ zᵢ² + λ)", ancre="middle", dy=56,
                couleur=ENCRE, taille=12)
    return f


pl = Planche([
    cadre(RSS, AJOUT, "l'erreur", "RSS(β) = Σ (yᵢ − β zᵢ)²", b_ls, "β̂ls"),
    cadre(PEN, DOUX, "la pénalité", "λ β²", 0.0, "0"),
    cadre(CRI, ACCENT, "le critère de ridge", "RSS(β) + λ β²", b_r, "β̂ridge"),
], signes=("+", "="), ecart=28,
    titre="Le critère de ridge est l'erreur plus la pénalité ; son minimum glisse de β̂ls vers 0")
sys.stdout.write(pl.svg())
