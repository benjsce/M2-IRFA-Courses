#!/usr/bin/env python3
r"""
prix-forward.svg — le prix forward de l'action pour la livraison dans un an, recalculé à
mesure que l'échéance approche, si l'action restait à 100 et le taux à 4 % :
F = 100·e^{0,04 (T − t)}, de 104,08 à 100. La base F − S se referme.

Usage : python courses/fpp/figures/prix-forward.py > prix-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

S, R = 100, 0.04
f = Figure(xmin=0, xmax=1.12, ymin=99, ymax=105.5, w=560, h=300,
           titre="La base F − S, 4,08 au départ, se referme à l'échéance")
f.axes(xlab="date, en années depuis aujourd'hui", ylab="prix", xticks=(0, 0.25, 0.5, 0.75, 1.0),
       yticks=(100, 102, 104), fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: "%d" % t)
f.courbe([(0, S), (1, S)], couleur=DOUX, epaisseur=2)
f.fonction(lambda t: S * math.exp(R * (1 - t)), 0, 1, couleur=ACCENT, epaisseur=2.6)
f.mesure(0.03, S, S * math.exp(R), etiquette="base 4,08")
f.point(1, S, couleur=ENCRE)
f.texte(0.45, S * math.exp(R * 0.55), "prix forward F(t,T)", couleur=ACCENT, dy=-10, gras=True)
f.texte(0.45, S, "prix comptant S = 100", couleur=DOUX, dy=16)
f.texte(1, S, "T : F = S", couleur=ENCRE, dx=6, dy=-8, taille=12)
sys.stdout.write(f.svg())
