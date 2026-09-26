#!/usr/bin/env python3
r"""
smote.svg — des observations rares fabriquées entre deux observations rares voisines.

Un nuage construit pour le dessin, avec une graine fixée : beaucoup d'observations de la
classe majoritaire, cinq de la minoritaire. SMOTE ne recopie pas les cinq, il en construit
de nouvelles : chaque point synthétique est pris au hasard sur le segment qui joint une
observation rare à l'une de ses voisines rares, assez loin des deux bouts pour ne
recouvrir aucune d'elles. La fiche retient exactement cette
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


def tirage():
    """Un point majoritaire, retiré tant qu'il sortirait du cadre."""
    while True:
        x, y = rng.gauss(3.5, 1.3), rng.gauss(3.5, 1.3)
        if 0.4 < x < 9.6 and 0.4 < y < 8.8:
            return x, y


majo = [tirage() for _ in range(60)]
mino = [(7.0, 6.6), (7.9, 7.4), (6.4, 7.8), (8.3, 6.2), (7.3, 8.6)]


def voisins(p, k=2):
    return sorted((q for q in mino if q != p), key=lambda q: math.dist(p, q))[:k]


synth, segments = [], []
for p in mino:
    for q in voisins(p):
        if (q, p) not in segments:
            segments.append((p, q))
for p, q in segments:
    t = 0.15 + 0.7 * rng.random()      # loin des extrémités : un point pris sur un bout
    #                                    recouvrirait l'observation rare, et se lirait copie
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
f.texte(0.3, 9.4, "classe majoritaire", couleur=DOUX, gras=True)
f.texte(9.8, 9.4, "connues, rares : pleins", couleur=ACCENT, ancre="end", taille=11.5, gras=True)
f.texte(9.8, 9.4, "fabriquées, synthétiques : creux", couleur=AJOUT, ancre="end", dy=17,
        taille=11.5, gras=True)

sys.stdout.write(f.svg())
