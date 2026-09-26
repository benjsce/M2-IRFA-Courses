#!/usr/bin/env python3
r"""
marche-financier.svg — l'argent va des épargnants vers ceux qui en ont besoin, les titres
en sens inverse.

Les ordres de grandeur du poly (§1.1.1, §1.1.2), en milliers de milliards de dollars :
à gauche ceux qui épargnent, à droite ceux qui ont besoin d'argent.

Usage : python courses/fpp/figures/marche-financier.py > marche-financier.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, _n      # noqa: E402

EPARGNE = [("gérants d'actifs", 120), ("assureurs", 40), ("fonds souverains", 10),
           ("fondations", 2)]
BESOIN = [("actions", 100), ("dette d'entreprise", 90), ("dette souveraine", 90)]
ECH = 3.3 / 120          # unités de dessin par millier de milliards

f = Figure(xmin=0, xmax=10, ymin=0, ymax=6.2, w=600, h=300, marges=(10, 10, 10, 10),
           titre="Les épargnants financent ceux qui ont besoin d'argent ; les titres font le chemin inverse")


def rect(x0, x1, y, h, couleur):
    X0, X1 = sorted((f.px(x0), f.px(x1)))
    Y = f.py(y + h / 2)
    f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" rx="2"/>'
           % (_n(X0), _n(Y), _n(X1 - X0), _n(f.py(y - h / 2) - Y), couleur))


f.texte(3.9, 5.75, "épargnent", ancre="end", gras=True)
for k, (nom, v) in enumerate(EPARGNE):
    y = 4.85 - 1.25 * k
    rect(3.9 - v * ECH, 3.9, y, 0.42, AJOUT)
    f.texte(3.9, y + 0.21, "%s  %d" % (nom, v), ancre="end", taille=12, couleur=DOUX, dy=-5)

f.texte(6.1, 5.75, "ont besoin d'argent", gras=True)
for k, (nom, v) in enumerate(BESOIN):
    y = 4.85 - 1.25 * k
    rect(6.1, 6.1 + v * ECH, y, 0.42, ACCENT)
    f.texte(6.1, y + 0.21, "%s  %d" % (nom, v), taille=12, couleur=DOUX, dy=-5)

f.fleche(4.15, 3.3, 5.85, 3.3, couleur=ENCRE, epaisseur=1.8)
f.texte(5.0, 3.5, "argent", ancre="middle", taille=12.5)
f.fleche(5.85, 2.4, 4.15, 2.4, couleur=ENCRE, epaisseur=1.8)
f.texte(5.0, 1.95, "titres", ancre="middle", taille=12.5)
f.texte(5.0, 0.25, "en milliers de milliards de dollars", ancre="middle", taille=11.5, couleur=DOUX)

sys.stdout.write(f.svg())
