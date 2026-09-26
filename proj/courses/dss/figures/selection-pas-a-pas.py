#!/usr/bin/env python3
r"""
selection-pas-a-pas.svg — les deux chemins sur les 20 clients, et le modèle que chacun retient.

Ce que la figure doit faire voir : un chemin ne visite qu'une case par taille ; partis
des deux bouts, les deux sens ne passent pas par les mêmes cases, et ne retiennent pas
le même modèle.

Les 20 clients, les cinq prédicteurs : x1 l'endettement, x2 le revenu, x3, x4, x5 sans
lien avec la perte. En haut, la sélection ascendante, de gauche à droite : à chaque pas,
la variable ajoutée est celle qui fait le plus baisser la RSS. En bas, la sélection
descendante, de droite à gauche : à chaque pas, la variable retirée est celle dont le
retrait fait le moins monter la RSS. Sous les noms, le $C_p$ de chaque modèle du chemin,
avec $\hat\sigma^2$ estimé sur le modèle complet ; la case colorée est le plus petit,
le modèle que chaque sens retient.

Usage : python courses/dss/figures/selection-pas-a-pas.py > selection-pas-a-pas.svg
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


def rss(lignes, beta, cols):
    return sum((y - beta[0] - sum(beta[1 + i] * x[j] for i, j in enumerate(cols))) ** 2
               for x, y in lignes)


rng = random.Random(GRAINE)
app = clients(rng, N_APP)
P = 5
RSS = lambda c: rss(app, ajuster(app, sorted(c)), sorted(c))
s2 = RSS(range(P)) / (N_APP - P - 1)
cp = lambda c: (RSS(c) + 2 * len(c) * s2) / N_APP

# Les deux chemins, un modèle par taille.
monte = [()]
while len(monte[-1]) < P:
    c = monte[-1]
    j = min((j for j in range(P) if j not in c), key=lambda j: RSS(c + (j,)))
    monte.append(c + (j,))
descend = [tuple(range(P))]
while descend[-1]:
    c = descend[-1]
    j = min(c, key=lambda j: RSS(tuple(i for i in c if i != j)))
    descend.append(tuple(i for i in c if i != j))
descend = descend[::-1]                          # rangé par taille, comme l'autre

fr = lambda v: ("%.2f" % v).replace(".", ",")


def nom(c):
    if not c:
        return "aucun"
    if len(c) == P:
        return "les cinq"
    return " ".join("x%d" % (j + 1) for j in sorted(c))


# Un repère en pixels, y vers le haut.
W, H = 680, 300
f = Figure(xmin=0, xmax=W, ymin=0, ymax=H, w=W, h=H, marges=(0, 0, 0, 0),
           titre="Deux chemins d'une case par taille : ils ne passent pas par les mêmes modèles")
X = lambda k: 52 + 114 * k                       # centre de la colonne k
L, HB = 84, 44                                   # largeur et hauteur d'une case


def rangee(chemin, yc, sens):
    retenu = min(range(len(chemin)), key=lambda k: cp(chemin[k]))
    for k, c in enumerate(chemin):
        x0, x1, y0, y1 = X(k) - L / 2, X(k) + L / 2, yc - HB / 2, yc + HB / 2
        if k == retenu:
            f.barre(X(k), y1, L, couleur=ACCENT, opacite=0.18, y0=y0)
        f.courbe([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                 couleur=ACCENT if k == retenu else DOUX, epaisseur=1.8 if k == retenu else 1.2)
        f.texte(X(k), yc, nom(c), couleur=ENCRE, ancre="middle", dy=-2, taille=11.5,
                gras=k == retenu)
        f.texte(X(k), yc, "Cp = " + fr(cp(c)), couleur=ACCENT if k == retenu else DOUX,
                ancre="middle", dy=14, taille=11, gras=k == retenu)
    for k in range(len(chemin) - 1):
        j = (set(chemin[k + 1]) - set(chemin[k])).pop()
        a, b = X(k) + L / 2 + 3, X(k + 1) - L / 2 - 3
        if sens > 0:
            f.fleche(a, yc, b, yc, couleur=DOUX, epaisseur=1.3)
            f.texte((a + b) / 2, yc, "+x%d" % (j + 1), couleur=ENCRE, ancre="middle", dy=-7,
                    taille=11)
        else:
            f.fleche(b, yc, a, yc, couleur=DOUX, epaisseur=1.3)
            f.texte((a + b) / 2, yc, "−x%d" % (j + 1), couleur=ENCRE, ancre="middle", dy=-7,
                    taille=11)


f.texte(X(0) - L / 2, 272, "sélection ascendante : partir de rien, ajouter une variable à chaque pas",
        couleur=ENCRE, gras=True, taille=12.5)
rangee(monte, 222, +1)
for k in range(P + 1):
    f.texte(X(k), 166, "k = %d" % k, couleur=DOUX, ancre="middle", taille=11.5)
rangee(descend, 112, -1)
f.texte(X(0) - L / 2, 62, "sélection descendante : partir des cinq, retirer une variable à chaque pas",
        couleur=ENCRE, gras=True, taille=12.5)
f.texte(X(0) - L / 2, 30, "x1 l'endettement, x2 le revenu, x3 à x5 sans lien avec la perte ; "
        "en couleur, le plus petit Cp du chemin", couleur=DOUX, taille=11)

sys.stdout.write(f.svg())
