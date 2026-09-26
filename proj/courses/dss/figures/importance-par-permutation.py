#!/usr/bin/env python3
r"""
importance-par-permutation.svg — ce que l'erreur hors du sac perd quand on brouille une
colonne.

Ce que la figure doit faire voir : une variable qui a servi à couper sans rien apprendre
ne coûte rien quand on la brouille ; les variables sans lien x4 et x5, qui prennent
chacune 18 % de la baisse d'impureté, ne coûtent presque rien ici.

Les 20 clients (générateur de surapprentissage.py, graine 78), et la même forêt que la
figure de importance-par-impurete : 500 arbres poussés jusqu'au bout, 2 prédicteurs
candidats sur 5, graine de la forêt 1. La procédure est celle de la slide 106, arbre par
arbre : on note l'erreur quadratique moyenne de l'arbre sur ses clients hors du sac, on
mélange au hasard la colonne j de ces clients, on note à nouveau, et l'on moyenne la hausse
sur les 500 arbres (dix mélanges par arbre et par colonne). À droite, en gris, la part de
la même variable dans la baisse d'impureté, pour comparer.

Usage : python courses/dss/figures/importance-par-permutation.py > importance-par-permutation.svg
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
    """Un arbre poussé jusqu'au bout ; imp[j] cumule la baisse d'impureté des coupures sur j.
    Une feuille est ("f", perte moyenne) ; un nœud, ("n", j, seuil, gauche, droite)."""
    if len(ix) < 2 or len(set(Y[i] for i in ix)) == 1:
        return ("f", sum(Y[i] for i in ix) / len(ix))
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
        return ("f", sum(Y[i] for i in ix) / len(ix))
    gain, j, g, d = meilleur
    imp[j] += gain
    seuil = (max(X[i][j] for i in g) + min(X[i][j] for i in d)) / 2
    return ("n", j, seuil, arbre(g, r, imp, m), arbre(d, r, imp, m))


def prevoir(t, x):
    while t[0] == "n":
        t = t[3] if x[t[1]] <= t[2] else t[4]
    return t[1]


def eqm(t, lignes):
    return sum((Y[i] - prevoir(t, x)) ** 2 for i, x in lignes) / len(lignes)



r, imp, foret = random.Random(1), [0.0] * 5, []
for _ in range(500):
    tirage = [r.randrange(N_APP) for _ in range(N_APP)]
    hors = sorted(set(range(N_APP)) - set(tirage))       # les clients hors du sac
    foret.append((arbre(tirage, r, imp), hors))
parts = [v / sum(imp) for v in imp]

hausse = [0.0] * 5
for t, hors in foret:
    avant = eqm(t, [(i, X[i]) for i in hors])
    for j in range(5):
        for _ in range(10):
            col = [X[i][j] for i in hors]
            r.shuffle(col)
            apres = eqm(t, [(i, X[i][:j] + [c] + X[i][j + 1:]) for i, c in zip(hors, col)])
            hausse[j] += (apres - avant) / 10 / len(foret)

NOMS = ("x1  endettement", "x2  revenu", "x3  sans lien", "x4  sans lien", "x5  sans lien")
ordre = sorted(range(5), key=lambda j: -hausse[j])
virg = lambda v: ("%+.2f" % v).replace(".", ",").replace("-", "−")

f = Figure(xmin=-0.3, xmax=0.52, ymin=-0.6, ymax=4.7, w=560, h=250, marges=(8, 10, 34, 12),
           titre="Brouiller une variable qui n'a rien appris ne coûte rien")
f.courbe([(0, -0.5), (0, 4.6)], couleur=DOUX, epaisseur=1.2)
for rang, j in enumerate(ordre):
    y = 4 - rang
    couleur = ACCENT if j == 2 else (AJOUT if j < 2 else PALE)
    x0, x1 = min(0, hausse[j]), max(0, hausse[j])
    f._add('<rect x="%s" y="%s" width="%s" height="20" fill="%s" rx="1.5"/>'
           % (_n(f.px(x0)), _n(f.py(y) - 10), _n(max(f.px(x1) - f.px(x0), 1.5)), couleur))
    f.texte(x0, y, NOMS[j], couleur=ENCRE, ancre="end", dx=-10, dy=4, taille=12,
            gras=(j == 2))
    f.texte(x1, y, virg(hausse[j]), couleur=ENCRE if j > 2 else couleur, dx=6, dy=4,
            taille=12, gras=(j == 2))
    f.texte(0.52, y, "impureté : %d %%" % round(100 * parts[j]), couleur=DOUX, ancre="end",
            dy=4, taille=11)
f.texte(0, -0.5, "hausse de l'erreur hors du sac, moyenne sur 500 arbres", couleur=DOUX, dx=4, dy=14, taille=11)

sys.stdout.write(f.svg())
