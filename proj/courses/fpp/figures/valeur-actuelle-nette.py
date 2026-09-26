#!/usr/bin/env python3
r"""
valeur-actuelle-nette.svg — un échéancier ramené flux par flux à une même date.

Ce que la figure doit faire voir : connus, deux flux de 100, dans un an et dans deux
ans, et le prix du zéro-coupon de chaque date, 0,9608 et 0,9048 ; cherché, ce que vaut
l'échéancier en t. Chaque flux revient en t par le facteur de sa propre date, puis les
valeurs ramenées s'additionnent : 96,08 + 90,48 = 186,56.

Usage : python courses/fpp/figures/valeur-actuelle-nette.py > valeur-actuelle-nette.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

X = 100
flux = [(5.2, "t+1", 0.9608), (8.4, "t+2", 0.9048)]
v = lambda x, d=2: ("%.*f" % (d, x)).replace(".", ",")

t = 2.2
g = Figure(xmin=0, xmax=10, ymin=-2.4, ymax=4.2, w=620, h=290, marges=(8, 8, 8, 8),
           titre="Valeur actuelle nette : chaque flux revient en t par son propre prix, puis on somme")
g.axe_temps(0, 0.9, 9.7, [(t, "t")] + [(x, s) for x, s, _ in flux])

total = 0.0
for k, (x, s, P) in enumerate(flux):
    y = 1.5 + 1.25 * k                      # une ligne par flux ramené
    g.fleche(x, 0.4, x, 1.6, couleur=AJOUT, epaisseur=2)
    g.texte(x, 0.95, "%d" % X, couleur=AJOUT, gras=True, taille=13.5, dx=8)
    g.fleche(x - 0.15, 1.9, t + 0.95, y + 0.12, couleur=ACCENT, courbure=10 + 8 * k,
             epaisseur=1.3)
    g.texte(t + 0.85, y, "%s × %d = %s" % (v(P, 4), X, v(P * X)), couleur=ACCENT,
            taille=13, ancre="end")
    total += P * X

g.texte(t, -1.5, "NPV(t) = %s + %s = %s" % (v(flux[0][2] * X), v(flux[1][2] * X), v(total)),
        couleur=ENCRE, gras=True, taille=13.5, dx=-60)

sys.stdout.write(g.svg())
