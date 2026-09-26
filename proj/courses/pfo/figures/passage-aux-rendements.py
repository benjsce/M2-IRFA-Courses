#!/usr/bin/env python3
r"""
passage-aux-rendements.svg — le prix dérive, ses rendements restent dans la même bande.

Ce que la figure doit faire voir : un prix qui passe de 100 à 1 000 n'a ni le même niveau
ni la même amplitude de variation au début et à la fin ; ses rendements du jour, eux,
restent de l'ordre de quelques pour cent du premier au dernier jour. Deux cadres reliés
par « → » : le prix à gauche, ses rendements à droite, sur les mêmes jours.

La série est simulée [ajout] : 750 jours de rendements logarithmiques tirés d'une loi
normale d'écart type 1,5 % par jour (graine 7), recentrés pour que le prix finisse
exactement à 1 000. Une variation de 1 % y vaut 1 au départ et 10 à l'arrivée.

Usage : python courses/pfo/figures/passage-aux-rendements.py > passage-aux-rendements.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX      # noqa: E402

N, VOL, P0, PT = 750, 0.015, 100.0, 1000.0
rng = random.Random(7)
e = [rng.gauss(0.0, VOL) for _ in range(N)]
m = sum(e) / N
r = [x - m + math.log(PT / P0) / N for x in e]          # la somme vaut ln(10)
prix = [P0]
for x in r:
    prix.append(prix[-1] * math.exp(x))

pc = lambda v: ("%+d %%" % v).replace("+0", "0") if v else "0"

# à gauche : le prix
g = Figure(xmin=0, xmax=N, ymin=0, ymax=1250, w=330, h=262, marges=(46, 30, 42, 10))
g.axes(xlab="jours", yticks=(100, 500, 1000), fmt_y=lambda t: "%d" % t)
g.courbe([(k, p) for k, p in enumerate(prix)], couleur=ACCENT, epaisseur=1.2)
g.texte(0, 1250, "le prix", couleur=ACCENT, gras=True, dy=-14)
g.texte(N, 1250, "de 100 à 1 000", couleur=DOUX, taille=11.5, ancre="end", dy=-14)

# à droite : ses rendements du jour
d = Figure(xmin=0, xmax=N, ymin=-6, ymax=6, w=330, h=262, marges=(46, 30, 42, 10))
d.axes(xlab="jours", yticks=(-5, 0, 5), fmt_y=pc)
d.courbe([(k + 1, 100 * x) for k, x in enumerate(r)], couleur=AJOUT, epaisseur=0.6)
d.texte(0, 6, "ses rendements du jour", couleur=AJOUT, gras=True, dy=-14)

sys.stdout.write(Planche([g, d], signes=["→"], ecart=34,
                         titre="Le prix dérive ; ses rendements gardent la même amplitude").svg())
