#!/usr/bin/env python3
r"""
taux-de-change.svg — le taux de change convertit des montants de la même date.

La fiche : $X_t$ est le nombre d'unités étrangères pour une unité locale, aujourd'hui.
Deux lignes de temps, dollars en haut, euros en bas. En t, la conversion est connue :
diviser par $X_t$. En T, elle se fera au taux $X_T$, qu'on ne connaît pas en t : d'où le
pointillé. Un montant futur se ramène donc d'abord à t dans sa devise, puis se convertit.

Usage : python courses/fpp/figures/taux-de-change.py > taux-de-change.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402

t, T = 3.0, 7.6
g = Figure(xmin=0, xmax=10, ymin=-3.2, ymax=3.0, w=600, h=270, marges=(8, 8, 8, 8),
           titre="Le taux de change convertit des montants de la même date")
g.axe_temps(1.6, 1.4, 9.7, [(t, "t"), (T, "T")])
g.axe_temps(-1.9, 1.4, 9.7, [(t, "t"), (T, "T")])
g.texte(0.1, 1.5, "dollars", couleur=AJOUT, gras=True, taille=12.5)
g.texte(0.1, -2.0, "euros", couleur=ACCENT, gras=True, taille=12.5)

# en t : conversion connue
g.fleche(t, 0.95, t, -1.35, couleur=DOUX, epaisseur=2)
g.texte(t, -0.2, "÷ Xₜ", couleur=DOUX, gras=True, taille=14, dx=10)
g.texte(t, -0.75, "connu aujourd'hui", couleur=DOUX, taille=11.5, dx=10)

# en T : conversion au taux de ce jour-là, inconnu en t
g.fleche(T, 0.95, T, -1.35, couleur=DOUX, epaisseur=1.5, pointilles="4 4")
g.texte(T, -0.2, "÷ X_{T}", couleur=DOUX, gras=True, taille=14, dx=10)
g.texte(T, -0.75, "inconnu en t", couleur=DOUX, taille=11.5, dx=10)

sys.stdout.write(g.svg())
