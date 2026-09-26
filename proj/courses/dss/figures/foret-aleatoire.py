#!/usr/bin/env python3
r"""
foret-aleatoire.svg — tirer les candidats à chaque coupure : les arbres ne commencent plus
tous par la même variable.

Ce que la figure doit faire voir : en bagging, beaucoup d'arbres commencent par la même
coupure, et se ressemblent ; en forêt, où seuls $m=2$ des 5 prédicteurs sont candidats à
chaque coupure, la variable la plus forte n'est candidate que deux fois sur cinq, et les
racines se répartissent.

Les 20 clients (générateur de surapprentissage.py, graine 78). Deux ensembles de 500
arbres poussés jusqu'au bout sur des tirages avec remise, graine de la forêt 1 : le
bagging ($m=5$, tous les prédicteurs candidats) et la forêt ($m=2$). Pour chacun, la part
des arbres dont la première coupure porte sur chaque prédicteur.

Usage : python courses/dss/figures/foret-aleatoire.py > foret-aleatoire.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

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


def arbre(ix, r, m, racines, profondeur=0):
    """Un arbre poussé jusqu'au bout ; seule la variable de la première coupure est gardée."""
    if len(ix) < 2 or len(set(Y[i] for i in ix)) == 1:
        return
    meilleur, base = None, sce(ix)
    for j in r.sample(range(5), m):            # les m candidats, tirés à chaque coupure
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
    _, j, g, d = meilleur
    if profondeur == 0:
        racines.append(j)
    arbre(g, r, m, racines, profondeur + 1)
    arbre(d, r, m, racines, profondeur + 1)


def parts_racine(m):
    r, racines = random.Random(1), []
    for _ in range(500):
        arbre([r.randrange(N_APP) for _ in range(N_APP)], r, m, racines)
    return [racines.count(j) / len(racines) for j in range(5)]


NOMS = ("x1", "x2", "x3", "x4", "x5")
SOUS = ("endett.", "revenu", "sans lien", "sans lien", "sans lien")


def cadre(titre, parts):
    g = Figure(xmin=-0.7, xmax=4.7, ymin=0, ymax=0.56, w=300, h=270, marges=(12, 34, 44, 8))
    g.courbe([(-0.6, 0), (4.6, 0)], couleur=DOUX, epaisseur=1.2)
    for j, p in enumerate(parts):
        g.barre(j, p, 0.62, couleur=ACCENT if j == 2 else PALE)
        g.texte(j, p, "%d %%" % round(100 * p), couleur=ACCENT if j == 2 else ENCRE,
                ancre="middle", dy=-6, taille=12, gras=(j == 2))
        g.texte(j, 0, NOMS[j], couleur=ENCRE, ancre="middle", dy=16, taille=12)
        g.texte(j, 0, SOUS[j], couleur=DOUX, ancre="middle", dy=30, taille=10)
    g.texte(2, 0.56, titre, couleur=ENCRE, ancre="middle", dy=-14, gras=True)
    return g


p = Planche([cadre("bagging : 5 candidats sur 5", parts_racine(5)),
             cadre("forêt : 2 candidats sur 5", parts_racine(2))],
            signes=("→",), ecart=34,
            titre="Part des 500 arbres dont la première coupure porte sur chaque prédicteur")
sys.stdout.write(p.svg())
