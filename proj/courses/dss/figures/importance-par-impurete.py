#!/usr/bin/env python3
r"""
importance-par-impurete.svg — la part de chaque prédicteur dans la baisse d'impureté.

Ce que la figure doit faire voir : des arbres poussés jusqu'au bout coupent aussi sur le
bruit, et chaque coupure compte ; une variable sans lien, liée à la perte par hasard,
passe devant l'endettement, et les trois variables sans lien prennent ensemble plus de la
moitié du total.

Les 20 clients (générateur de surapprentissage.py, graine 78). Une forêt de 500 arbres
poussés jusqu'au bout, 2 prédicteurs candidats sur 5 à chaque coupure, graine de la forêt
1. L'impureté d'un nœud est la somme des carrés des écarts à sa moyenne ; on additionne,
pour chaque prédicteur, la baisse obtenue à chaque coupure faite sur lui, sur les 500
arbres, et l'on donne sa part du total. La même forêt sert à la figure de
importance-par-permutation.

Usage : python courses/dss/figures/importance-par-impurete.py > importance-par-impurete.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE, AJOUT, _n      # noqa: E402

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


D = clients(random.Random(GRAINE), N_APP)
X = [x for x, _ in D]
Y = [y for _, y in D]


def sce(ix):
    """Somme des carrés des écarts à la moyenne : l'impureté d'un nœud en régression."""
    if not ix:
        return 0.0
    m = sum(Y[i] for i in ix) / len(ix)
    return sum((Y[i] - m) ** 2 for i in ix)


def arbre(ix, r, imp, m=2):
    """Un arbre poussé jusqu'au bout ; imp[j] cumule la baisse d'impureté des coupures sur j."""
    if len(ix) < 2 or len(set(Y[i] for i in ix)) == 1:
        return
    meilleur, base = None, sce(ix)
    for j in r.sample(range(5), m):
        vals = sorted(set(X[i][j] for i in ix))
        for a, b in zip(vals, vals[1:]):
            s = (a + b) / 2
            g = [i for i in ix if X[i][j] <= s]
            d = [i for i in ix if X[i][j] > s]
            gain = base - sce(g) - sce(d)
            if meilleur is None or gain > meilleur[0]:
                meilleur = (gain, j, g, d)
    if meilleur is None:
        return
    gain, j, g, d = meilleur
    imp[j] += gain
    arbre(g, r, imp, m)
    arbre(d, r, imp, m)


r, imp = random.Random(1), [0.0] * 5
for _ in range(500):
    arbre([r.randrange(N_APP) for _ in range(N_APP)], r, imp)
parts = [v / sum(imp) for v in imp]

NOMS = ("x1  endettement", "x2  revenu", "x3  sans lien", "x4  sans lien", "x5  sans lien")
ordre = sorted(range(5), key=lambda j: -parts[j])

f = Figure(xmin=-0.3, xmax=0.36, ymin=-0.6, ymax=4.7, w=520, h=250, marges=(8, 10, 34, 12),
           titre="Des arbres poussés au bout coupent aussi sur le bruit, et chaque coupure compte")
f.courbe([(0, -0.5), (0, 4.6)], couleur=DOUX, epaisseur=1.2)
for rang, j in enumerate(ordre):
    y = 4 - rang
    couleur = ACCENT if j == 2 else (AJOUT if j < 2 else PALE)
    f._add('<rect x="%s" y="%s" width="%s" height="20" fill="%s" rx="1.5"/>'
           % (_n(f.px(0)), _n(f.py(y) - 10), _n(f.px(parts[j]) - f.px(0)), couleur))
    f.texte(0, y, NOMS[j], couleur=ENCRE, ancre="end", dx=-10, dy=4, taille=12,
            gras=(j == 2))
    f.texte(parts[j], y, "%d %%" % round(100 * parts[j]), couleur=ENCRE if j > 2 else couleur,
            dx=6, dy=4, taille=12, gras=(j == 2))
f.texte(0, -0.5, "part de la baisse d'impureté totale, sur 500 arbres", couleur=DOUX,
        dx=4, dy=14, taille=11)

sys.stdout.write(f.svg())
