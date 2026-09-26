#!/usr/bin/env python3
r"""
hypothese-de-machina.svg — les courbes d'indifférence en éventail dans le triangle.

La fiche dit que l'hypothèse impose aux courbes d'indifférence de s'ouvrir en éventail. On
reprend le triangle de dup/triangle-des-probabilites — $p$ du pire résultat en abscisse,
$p$ du meilleur en ordonnée — et l'on trace des droites qui toutes passent par un même
point situé hors du triangle, en bas à gauche : plus on monte vers les meilleures
loteries, plus elles sont raides. Sous l'utilité espérée elles seraient parallèles.

Le point de fuite et les pentes sont un choix de dessin ; le cours ne les fixe pas. Seul
compte le sens de l'ouverture.

Usage : python courses/dup/figures/hypothese-de-machina.py > hypothese-de-machina.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

FOYER = (-0.4, -0.3)               # le point commun, hors du triangle
ORDONNEES = (-0.22, -0.12, 0.02, 0.2, 0.42, 0.68)          # où chaque droite coupe p(pire) = 0
PENTES = [(y0 - FOYER[1]) / (0 - FOYER[0]) for y0 in ORDONNEES]

f = Figure(xmin=-0.06, xmax=1.10, ymin=-0.06, ymax=1.10, w=430, h=400,
           marges=(46, 18, 44, 92),
           titre="Plus on monte vers les meilleures loteries, plus les courbes d'indifférence sont raides")
f.axes(xlab="p(pire)", ylab="p(meilleur)", xticks=(0, 0.5, 1), yticks=(0.5, 1),
       fmt=lambda t: ("0" if t == 0 else "1" if t == 1 else "½"))

f.courbe([(0, 1), (0, 0), (1, 0)], couleur=DOUX, epaisseur=1.4)
f.courbe([(0, 1), (1, 0)], couleur=DOUX, epaisseur=1.4)

for s in PENTES:
    pts = []
    for k in range(0, 401):
        x = k / 400.0
        y = FOYER[1] + s * (x - FOYER[0])
        if 0 <= y <= 1 - x:
            pts.append((x, y))
    if len(pts) > 1:
        f.courbe(pts, couleur=ACCENT, epaisseur=2.0)

f.fleche(0.46, 0.30, 0.26, 0.56, couleur=AJOUT, epaisseur=1.6)
f.texte(0.58, 0.44, "préférence croissante", couleur=AJOUT, taille=11.5, gras=True, fond=True)
f.texte(1.08, 0.80, "l'éventail s'ouvre", couleur=ACCENT, ancre="end", taille=11.5,
        gras=True, fond=True)

sys.stdout.write(f.svg())
