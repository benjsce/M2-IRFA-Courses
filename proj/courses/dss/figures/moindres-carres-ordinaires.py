#!/usr/bin/env python3
r"""
moindres-carres-ordinaires.svg — la droite qui rend la somme des carrés des écarts minimale.

Ce que la figure doit faire voir : ce qui est connu, les 20 clients, chacun un point
(endettement, perte) ; ce qu'on cherche, la droite, c'est-à-dire ses deux coefficients ;
et ce qui la choisit, les écarts verticaux entre chaque point et la droite, dont la somme
des carrés, la RSS, doit être la plus petite possible.

Les clients sont ceux de courses/dss/figures/surapprentissage.py, graine 78 ; un seul
prédicteur, l'endettement, pour tenir dans un plan. La droite plate à la perte moyenne
laisse une RSS de 44,0 ; inclinée autour du client moyen jusqu'à la pente des moindres
carrés, elle tombe à 34,8, et aucune autre droite ne fait moins.

Usage : python courses/dss/figures/moindres-carres-ordinaires.py > moindres-carres-ordinaires.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

# le monde de dss, tiré comme dans surapprentissage.py : seuls les 20 clients servent ici
rng = random.Random(78)
clients = []
for _ in range(20):
    x1, x2 = rng.uniform(10, 60), rng.uniform(20, 80)
    [rng.gauss(0, 1) for _ in range(3)]
    y = 2 + 0.10 * x1 - 0.05 * x2 + rng.gauss(0, 1)
    clients.append((x1, y))

# moindres carrés à un prédicteur : les deux pentes nulles, résolues à la main
n = len(clients)
xm = sum(x for x, _ in clients) / n
ym = sum(y for _, y in clients) / n
b1 = (sum((x - xm) * (y - ym) for x, y in clients)
      / sum((x - xm) ** 2 for x, _ in clients))
b0 = ym - b1 * xm
rss = sum((y - b0 - b1 * x) ** 2 for x, y in clients)
rss_plate = sum((y - ym) ** 2 for _, y in clients)
virg = lambda v, d=1: ("%.*f" % (d, v)).replace(".", ",")

f = Figure(xmin=5, xmax=65, ymin=0, ymax=7.6, w=600, h=360, marges=(54, 20, 44, 18),
           titre="Les moindres carrés : la droite dont les écarts verticaux ont la plus petite somme des carrés")
f.axes(xlab="endettement (%)", ylab="perte (k€)", xticks=(10, 20, 30, 40, 50, 60),
       yticks=(0, 2, 4, 6), fmt=lambda t: str(int(t)))

# la droite plate, à la perte moyenne : le point de comparaison
f.segment(8, ym, 62, ym, couleur=DOUX, epaisseur=1.3, pointilles="5 4")
# les écarts verticaux à la droite des moindres carrés : ce dont on somme les carrés
for x, y in clients:
    f.segment(x, y, x, b0 + b1 * x, couleur=ACCENT, epaisseur=1.6, pointilles=None)
f.courbe([(8, b0 + b1 * 8), (62, b0 + b1 * 62)], couleur=ACCENT, epaisseur=2.6)
for x, y in clients:
    f.point(x, y, couleur=ENCRE, r=3.8)
f.point(xm, ym, couleur=PALE, r=6.5)
f.point(xm, ym, couleur=ACCENT, r=3.2)

f.texte(62, 0.9, "moindres carrés : RSS = " + virg(rss), couleur=ACCENT, ancre="end",
        gras=True)
f.texte(8, ym, "perte moyenne : RSS = " + virg(rss_plate), couleur=DOUX, dx=2, dy=-8,
        taille=11.5)

sys.stdout.write(f.svg())
