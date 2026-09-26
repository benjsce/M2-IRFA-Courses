#!/usr/bin/env python3
r"""
smote.svg — des observations rares fabriquées entre deux observations rares voisines.

Un nuage construit pour le dessin, avec une graine fixée : beaucoup d'observations de la
classe majoritaire, cinq de la minoritaire. SMOTE ne recopie pas les cinq, il en construit
de nouvelles : chaque point synthétique est pris au hasard sur le segment qui joint une
observation rare à l'une de ses voisines rares. La fiche retient exactement cette
différence avec un simple sur-échantillonnage.

Usage : python courses/dss/figures/smote.py > smote.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

rng = random.Random(5)
majo = [(rng.gauss(3.5, 1.3), rng.gauss(3.5, 1.3)) for _ in range(60)]
mino = [(7.0, 6.6), (7.9, 7.4), (6.4, 7.8), (8.3, 6.2), (7.3, 8.6)]


def voisins(p, k=2):
    return sorted((q for q in mino if q != p), key=lambda q: math.dist(p, q))[:k]


synth, segments = [], []
for p in mino:
    for q in voisins(p):
        if (q, p) not in segments:
            segments.append((p, q))
for p, q in segments:
    t = rng.random()
    synth.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))

f = Figure(xmin=0, xmax=10, ymin=0, ymax=10, w=440, h=400, marges=(20, 16, 20, 16),
           titre="Chaque point synthétique naît sur le segment entre deux observations rares")
for x, y in majo:
    f.point(x, y, couleur=DOUX, r=3)
for p, q in segments:
    f.courbe([p, q], couleur=AJOUT, epaisseur=1.0, pointilles="3 3")
for x, y in mino:
    f.point(x, y, couleur=ACCENT, r=5.5)
for x, y in synth:
    f.point(x, y, couleur=AJOUT, r=4.2)
    f.point(x, y, couleur="var(--card)", r=2.2)
f.texte(2.2, 9.4, "classe majoritaire", couleur=DOUX, ancre="middle", gras=True)
f.texte(7.4, 9.4, "rares : pleins ; synthétiques : creux", couleur=ACCENT, ancre="middle",
        taille=11.5, gras=True)

sys.stdout.write(f.svg())
