#!/usr/bin/env python3
r"""
decomposition-en-valeurs-singulieres.svg — ce que ridge garde de chaque direction.

Ce que la figure doit faire voir : dans la base de la décomposition, les moindres carrés
gardent entière la coordonnée de y sur chaque direction, ridge n'en garde que la part
$d_j^2/(d_j^2+\lambda)$, d'autant plus petite que la direction est peu étirée.

Les 20 clients, cinq prédicteurs standardisés. Les valeurs singulières $d_j$ sont les racines
des valeurs propres de $\mathbf X^T\mathbf X$, calculées par la méthode de Jacobi : 6,70 ;
4,34 ; 4,14 ; 3,83 ; 2,12. Avec $\lambda=5$, le λ que la validation croisée retient sur ces
clients, ridge garde 0,90 de la première coordonnée et 0,47 de la dernière. Chaque cadre vaut
1, ce que gardent les moindres carrés ; la barre pleine, ce que garde ridge.

Usage : python courses/dss/figures/decomposition-en-valeurs-singulieres.py > decomposition-en-valeurs-singulieres.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, _n      # noqa: E402

# Le monde des 20 clients, recopié de surapprentissage.py, qui en est le générateur de
# référence : même graine, même tirage, mêmes nombres.
GRAINE, N_APP = 78, 20


def clients(rng, n):
    lignes = []
    for _ in range(n):
        x1, x2 = rng.uniform(10, 60), rng.uniform(20, 80)
        bruit = [rng.gauss(0, 1) for _ in range(3)]
        y = 2 + 0.10 * x1 - 0.05 * x2 + rng.gauss(0, 1)
        lignes.append(([x1, x2] + bruit, y))
    return lignes


def jacobi(A):
    """Valeurs propres d'une matrice symétrique, par rotations de Jacobi."""
    A = [r[:] for r in A]
    k = len(A)
    for _ in range(100):
        for p in range(k):
            for q in range(p + 1, k):
                if abs(A[p][q]) < 1e-15:
                    continue
                th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
                c, s = math.cos(th), math.sin(th)
                for r in range(k):
                    arp, arq = A[r][p], A[r][q]
                    A[r][p], A[r][q] = c * arp - s * arq, s * arp + c * arq
                for r in range(k):
                    apr, aqr = A[p][r], A[q][r]
                    A[p][r], A[q][r] = c * apr - s * aqr, s * apr + c * aqr
    return [A[i][i] for i in range(k)]


rng = random.Random(GRAINE)
app = clients(rng, N_APP)
X = [x for x, _ in app]
moy = [sum(r[j] for r in X) / N_APP for j in range(5)]
et = [math.sqrt(sum((r[j] - moy[j]) ** 2 for r in X) / N_APP) for j in range(5)]
Z = [[(r[j] - moy[j]) / et[j] for j in range(5)] for r in X]
XtX = [[sum(z[a] * z[b] for z in Z) for b in range(5)] for a in range(5)]
d = sorted((math.sqrt(v) for v in jacobi(XtX)), reverse=True)
LAM = 5.0
garde = [dj ** 2 / (dj ** 2 + LAM) for dj in d]
virg = lambda v: ("%.2f" % v).replace(".", ",")

f = Figure(xmin=0.3, xmax=5.7, ymin=0, ymax=1.14, w=560, h=280, marges=(20, 16, 54, 16),
           titre="Ridge garde presque toute la direction la plus étirée, la moitié de la moins étirée")
f.courbe([(0.3, 0), (5.7, 0)], couleur=DOUX, epaisseur=1.2)
for j, (dj, g) in enumerate(zip(d, garde), start=1):
    f.barre(j, g, 0.56, couleur=ACCENT, opacite=0.85)
    f.courbe([(j - 0.28, 0), (j - 0.28, 1), (j + 0.28, 1), (j + 0.28, 0)], couleur=ENCRE,
             epaisseur=1.3)
    f.texte(j, g, virg(g), couleur=ACCENT, ancre="middle", dy=-7, taille=12, gras=True)
    f.texte(j, 0, "direction %d" % j, couleur=ENCRE, ancre="middle", dy=18, taille=11.5)
    f.texte(j, 0, "d = " + virg(dj), couleur=DOUX, ancre="middle", dy=34, taille=11.5)
f.texte(0.72, 1, "moindres carrés : 1", couleur=ENCRE, dy=-8, taille=11.5)
f.texte(5.28, 1, "ridge, λ = 5", couleur=ACCENT, ancre="end", dy=-8, taille=11.5, gras=True)

sys.stdout.write(f.svg())
