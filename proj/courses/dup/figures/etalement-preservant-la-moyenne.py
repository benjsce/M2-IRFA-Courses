#!/usr/bin/env python3
r"""
etalement-preservant-la-moyenne.svg — la probabilité part vers les queues, la moyenne ne bouge pas.

La fiche donne l'exemple de la source : « De {40,60} uniforme vers {20,40,60,80}
uniforme : la moyenne reste 50, la probabilité est partie vers les extrêmes »
[L1 slide 24]. La figure pose les deux distributions côte à côte sur le même axe, et
marque la moyenne, qui est la même.

Les deux barres de 40 et de 60 se retrouvent d'une distribution à l'autre, moitié moins
hautes : c'est là que se voit le déplacement, et c'est pourquoi elles ne sont pas
empilées mais décalées.

Usage : python courses/dup/figures/etalement-preservant-la-moyenne.py > etalement-preservant-la-moyenne.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

AVANT = [(40, 0.5), (60, 0.5)]
APRES = [(20, 0.25), (40, 0.25), (60, 0.25), (80, 0.25)]
MOYENNE = 50.0
LARG, DECAL = 5.2, 2.9

f = Figure(xmin=8, xmax=94, ymin=0, ymax=0.60, w=560, h=330,
           titre="La probabilité part du centre vers les queues, la moyenne reste 50")

f.axes(xlab="résultat", ylab="probabilité",
       xticks=(20, 40, 60, 80), yticks=(0.25, 0.5),
       fmt=lambda t: ("½" if abs(t - 0.5) < 1e-9 else
                      "¼" if abs(t - 0.25) < 1e-9 else str(int(t))))

for x, p in AVANT:
    f.barre(x - DECAL, p, LARG, couleur=DOUX)
for x, p in APRES:
    f.barre(x + DECAL, p, LARG, couleur=ACCENT)

f.segment(MOYENNE, 0, MOYENNE, 0.60, couleur=AJOUT, epaisseur=1.6, pointilles="5 4")
f.texte(MOYENNE, 0.60, "la moyenne, 50, dans les deux cas", couleur=AJOUT,
        ancre="middle", dy=-2, taille=11.5, fond=True)

f.texte(40 - DECAL, 0.5, "avant : {40, 60}", couleur=DOUX, ancre="end", dx=-8, dy=-6, gras=True)
f.texte(92, 0.335, "après : {20, 40, 60, 80}", couleur=ACCENT,
        ancre="end", dy=0, gras=True)

sys.stdout.write(f.svg())
