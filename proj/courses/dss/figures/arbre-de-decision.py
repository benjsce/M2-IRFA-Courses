#!/usr/bin/env python3
r"""
arbre-de-decision.svg — une question, deux groupes, deux moyennes.

Ce que la figure doit faire voir : un arbre coupe les clients en deux groupes par une
question à seuil, et prédit dans chaque groupe la moyenne des pertes ; le seuil retenu est
celui qui rend la somme des carrés des écarts à ces moyennes la plus petite.

Les 20 clients du monde de dss, tirés comme dans surapprentissage.py (graine 78). La
meilleure première question, sur les cinq prédicteurs et tous les seuils, porte sur x3,
une variable sans lien avec la perte : x3 ≤ 0,22. Elle sépare 8 clients de perte moyenne
2,43 et 12 de perte moyenne 4,39, et fait passer la somme des carrés des écarts de 44,03
(une seule moyenne, 3,60) à 25,60. Chaque client est un point (x3, perte) ; les deux
paliers sont les prédictions ; les traits fins, les écarts dont on somme les carrés.

Le script vérifie aussi deux nombres que citent la fiche et le parcours « Des arbres à la
forêt » :
- l'instabilité : sur les 190 façons de retirer deux clients, la première question change
  de variable 42 fois (elle porte alors 28 fois sur l'endettement, au seuil 42,0) ;
- sur 500 tirages avec remise (graine 1), la première question porte 226 fois sur x3 et
  125 fois sur l'endettement.

Usage : python courses/dss/figures/arbre-de-decision.py > arbre-de-decision.svg
Dépendance : aucune.
"""
import itertools
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

GRAINE, N = 78, 20


def clients(rng, n):
    lignes = []
    for _ in range(n):
        x1, x2 = rng.uniform(10, 60), rng.uniform(20, 80)
        bruit = [rng.gauss(0, 1) for _ in range(3)]
        y = 2 + 0.10 * x1 - 0.05 * x2 + rng.gauss(0, 1)
        lignes.append(([x1, x2] + bruit, y))
    return lignes


D = clients(random.Random(GRAINE), N)


def sce(ix):
    if not ix:
        return 0.0
    m = sum(D[i][1] for i in ix) / len(ix)
    return sum((D[i][1] - m) ** 2 for i in ix)


def meilleure(ix):
    """La meilleure première question : le prédicteur j et le seuil s qui minimisent la
    somme des carrés des écarts dans les deux groupes."""
    best = None
    for j in range(5):
        vals = sorted(set(D[i][0][j] for i in ix))
        for a, b in zip(vals, vals[1:]):
            s = (a + b) / 2
            g = [i for i in ix if D[i][0][j] <= s]
            d = [i for i in ix if D[i][0][j] > s]
            v = sce(g) + sce(d)
            if best is None or v < best[0]:
                best = (v, j, s, g, d)
    return best


TOUS = list(range(N))
V, J, S, G, DR = meilleure(TOUS)
moy = lambda ix: sum(D[i][1] for i in ix) / len(ix)
assert J == 2 and round(S, 2) == 0.22 and (len(G), len(DR)) == (8, 12)
assert (round(moy(G), 2), round(moy(DR), 2)) == (2.43, 4.39)
assert (round(sce(TOUS), 2), round(V, 2), round(moy(TOUS), 2)) == (44.03, 25.6, 3.6)

# instabilité : retirer deux clients
change, sur_x1 = 0, 0
for a, b in itertools.combinations(TOUS, 2):
    _, j2, s2, _, _ = meilleure([i for i in TOUS if i not in (a, b)])
    if j2 != J:
        change += 1
        sur_x1 += (j2 == 0 and round(s2, 1) == 42.0)
assert (change, sur_x1) == (42, 28)

# tirages avec remise
rng = random.Random(1)
racines = [0] * 5
for _ in range(500):
    racines[meilleure([rng.randrange(N) for _ in range(N)])[1]] += 1
assert (racines[2], racines[0]) == (226, 125)

fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")
XMIN, XMAX = -1.2, 1.7
f = Figure(XMIN, XMAX, 0, 7.6, w=600, h=360, marges=(46, 34, 44, 16),
           titre="x₃ ≤ 0,22 ? Deux groupes, deux moyennes : l'arbre prédit la moyenne de son groupe")
f.axes(xlab="x₃, une variable sans lien avec la perte", ylab="perte",
       xticks=(-1, -0.5, 0, 0.5, 1, 1.5), yticks=(2, 4, 6),
       fmt=lambda t: fr(t, 1) if t % 1 else fr(t, 0), fmt_y=lambda t: fr(t, 0), croix=(XMIN, 0))

mg, md = moy(G), moy(DR)
for ix, m in ((G, mg), (DR, md)):
    for i in ix:
        x, y = D[i][0][2], D[i][1]
        f.segment(x, y, x, m, couleur=PALE, epaisseur=1.0, pointilles=None)
for i in TOUS:
    f.point(D[i][0][2], D[i][1], couleur=ENCRE, r=3.6)
f.segment(S, 0, S, 7.2, couleur=AJOUT, epaisseur=1.6, pointilles="5 4")
f.courbe([(XMIN, mg), (S, mg)], couleur=ACCENT, epaisseur=3.2)
f.courbe([(S, md), (XMAX, md)], couleur=ACCENT, epaisseur=3.2)
f.texte(S, 7.2, "question : x₃ ≤ 0,22 ?", couleur=AJOUT, ancre="middle", dy=-6, gras=True)
f.texte(XMIN, mg, "oui : 8 clients, moyenne " + fr(mg), couleur=ACCENT, dx=6, dy=-8, gras=True)
f.texte(XMAX, md, "non : 12 clients, moyenne " + fr(md), couleur=ACCENT, ancre="end", dy=20, gras=True)
f.texte(0.5, 1.0, "traits gris : les écarts à la moyenne du groupe", couleur=DOUX, taille=12)
f.texte(0.5, 1.0, "somme de leurs carrés : 44,03 → 25,60", couleur=ENCRE, dy=17, taille=12)

sys.stdout.write(f.svg())
