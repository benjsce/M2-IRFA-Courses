#!/usr/bin/env python3
r"""
perceptron.svg — le calcul du neurone en trois temps.

La fiche : multiplier chaque entrée par son poids, sommer, transformer par la fonction
d'activation. Le seuil y est un poids $w_0$ parmi les autres, sur une entrée constante
$x_0=1$. Le schéma suit ce chemin de gauche à droite : les entrées, les poids portés par
les connexions, la somme, puis la marche de la fonction seuil, qui rend 0 ou 1.

Usage : python courses/dss/figures/perceptron.py > perceptron.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

f = Figure(xmin=0, xmax=12, ymin=0, ymax=6, w=580, h=290, marges=(8, 8, 8, 8),
           titre="Multiplier par les poids, sommer, passer le seuil")

ENTREES = [(1.2, 5.0, "x0 = 1"), (1.2, 3.0, "x1"), (1.2, 1.0, "x2")]
POIDS = ["w0", "w1", "w2"]
SOMME = (6.0, 3.0)
for (x, y, nom), w in zip(ENTREES, POIDS):
    f.point(x, y, couleur=DOUX, r=6)
    f.texte(x, y, nom, couleur=ENCRE, ancre="end", dx=-12, dy=4, gras=True)
    f.fleche(x + 0.25, y, SOMME[0] - 0.62, SOMME[1] + (y - 3) * 0.18, couleur=DOUX, epaisseur=1.6)
    f.texte((x + SOMME[0]) / 2, (y + SOMME[1]) / 2, w, couleur=AJOUT, dy=-6, gras=True, fond=True)
f.point(*SOMME, couleur=ACCENT, r=22)
f.texte(*SOMME, "Σ", couleur="var(--card)", ancre="middle", dy=7, taille=20, gras=True)
f.texte(SOMME[0], SOMME[1] - 0.9, "Σ wi xi", couleur=ACCENT, ancre="middle", dy=10, taille=11.5)

# la fonction seuil, dessinée en petit
bx, by = 8.2, 2.2
f.courbe([(bx, by + 1.6), (bx, by), (bx + 1.7, by)], couleur=DOUX, epaisseur=1.0)
f.courbe([(bx, by + 0.05), (bx + 0.85, by + 0.05), (bx + 0.85, by + 1.25), (bx + 1.6, by + 1.25)],
         couleur=ACCENT, epaisseur=2.2)
f.texte(bx + 0.85, by, "0", couleur=DOUX, ancre="middle", dy=14, taille=10.5)
f.texte(bx + 0.85, by + 1.6, "f : 0 ou 1", couleur=ENCRE, ancre="middle", dy=-4, taille=11.5)
f.fleche(SOMME[0] + 0.62, SOMME[1], bx - 0.2, SOMME[1], couleur=DOUX, epaisseur=1.6)
f.fleche(bx + 1.8, SOMME[1], 11.2, SOMME[1], couleur=DOUX, epaisseur=1.6)
f.texte(11.3, SOMME[1], "y", couleur=ENCRE, dy=5, gras=True, taille=14)

sys.stdout.write(f.svg())
