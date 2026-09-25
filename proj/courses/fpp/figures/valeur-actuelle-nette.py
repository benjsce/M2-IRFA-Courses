#!/usr/bin/env python3
r"""
valeur-actuelle-nette.svg — un échéancier ramené flux par flux à une même date.

La fiche : $\mathrm{NPV}(t)=\sum_i P(t,t_i)X_i$. Chaque flux revient en t par son propre
facteur, puis les valeurs ramenées s'additionnent. Trois flux, comme dans l'exemple
minimal, mais sans ses nombres : la figure montre la construction.

Usage : python courses/fpp/figures/valeur-actuelle-nette.py > valeur-actuelle-nette.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t = 2.3
dates = [(4.7, "t_{1}", "X_{1}"), (6.7, "t_{2}", "X_{2}"), (8.7, "t_{3}", "X_{3}")]
g = Figure(xmin=0, xmax=10, ymin=-2.6, ymax=4.9, w=620, h=300, marges=(8, 8, 8, 8),
           titre="Valeur actuelle nette : chaque flux revient en t, puis on somme")
g.axe_temps(0, 0.9, 9.7, [(t, "t")] + [(x, "") for x, _, _ in dates])
for x, lab, _ in dates:                      # étiquettes à indice, hors de axe_temps
    g.texte(x, 0, lab, couleur=DOUX, taille=12.5, ancre="middle", dy=21)

for k, (x, ti, Xi) in enumerate(dates):
    y = 1.35 + 1.1 * k                       # une ligne par flux ramené
    g.fleche(x, 0.4, x, 1.5, couleur=AJOUT, epaisseur=2)
    g.texte(x, 1.0, Xi, couleur=AJOUT, gras=True, taille=13.5, dx=8)
    g.fleche(x - 0.15, 1.8, t + 0.95, y + 0.12, couleur=ACCENT, courbure=10 + 7 * k,
             epaisseur=1.3)
    g.texte(t + 0.85, y, "P(t,%s)·%s" % (ti, Xi), couleur=ACCENT, taille=12.5, ancre="end")

g.texte(t, -1.6, "NPV(t) : leur somme", couleur=ENCRE, gras=True, taille=13,
        ancre="middle")

sys.stdout.write(g.svg())
