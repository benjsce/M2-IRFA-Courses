#!/usr/bin/env python3
r"""
arret-precoce.svg — deux erreurs au fil de l'entraînement, et le point où l'on s'arrête.

La fiche : l'erreur d'apprentissage continue de baisser alors que celle du jeu de réglage
remonte, et c'est ce retournement qui fixe l'arrêt. Les deux courbes n'ont que leur forme :
la source ne les chiffre pas, et le dessin ne porte donc aucune graduation.

Usage : python courses/dss/figures/arret-precoce.py > arret-precoce.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

app = lambda t: 0.15 + 0.85 * math.exp(-t / 2.2)
reg = lambda t: app(t) + 0.012 * t * t
T = min((k / 100 for k in range(1, 1000)), key=reg)

f = Figure(xmin=0, xmax=10.5, ymin=0, ymax=1.25, w=560, h=300,
           titre="L'erreur d'apprentissage ne dit jamais quand s'arrêter ; celle du réglage, si")
f.axes(xlab="itérations d'entraînement", ylab="erreur", xticks=(), yticks=())
f.segment(T, 0, T, 1.1, couleur=ACCENT, epaisseur=1.6)
f.fonction(app, 0, 10, couleur=DOUX, epaisseur=2.2)
f.fonction(reg, 0, 10, couleur=AJOUT, epaisseur=2.4)
f.point(T, reg(T), couleur=ACCENT, r=4.5)
f.texte(T, 1.1, "arrêt", couleur=ACCENT, ancre="middle", dy=-6, gras=True)
f.texte(9.8, app(9.8), "apprentissage", couleur=DOUX, ancre="end", dy=16, gras=True)
f.texte(8.3, reg(8.3), "jeu de réglage", couleur=AJOUT, ancre="end", dx=-8, dy=-4, gras=True, fond=True)

sys.stdout.write(f.svg())
