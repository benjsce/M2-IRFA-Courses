#!/usr/bin/env python3
r"""
taux-de-change.svg — le taux de change convertit des montants de la même date.

La fiche : l'euro est la devise locale, le dollar l'étrangère, et $X_t$ est le nombre de
dollars pour un euro, aujourd'hui : 1,10. Deux lignes de temps, dollars en haut, euros
en bas. En t, la conversion est connue : 110 dollars divisés par 1,10 font 100 euros. En
T, elle se fera au taux $X_T$, qu'on ne connaît pas en t : d'où le pointillé.

Usage : python courses/fpp/figures/taux-de-change.py > taux-de-change.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402

X = 1.10
dollars = 110
v = lambda x: ("%.2f" % x).replace(".", ",")

t, T = 3.4, 7.8
g = Figure(xmin=0, xmax=10, ymin=-3.2, ymax=3.0, w=620, h=270, marges=(8, 8, 8, 8),
           titre="Le taux de change convertit des montants de la même date")
g.axe_temps(1.6, 2.0, 9.7, [(t, "t"), (T, "T")])
g.axe_temps(-1.9, 2.0, 9.7, [(t, "t"), (T, "T")])
g.texte(0.05, 1.75, "dollars", couleur=AJOUT, gras=True, taille=12.5)
g.texte(0.05, 1.2, "devise étrangère", couleur=DOUX, taille=11)
g.texte(0.05, -1.85, "euros", couleur=ACCENT, gras=True, taille=12.5)
g.texte(0.05, -2.4, "devise locale", couleur=DOUX, taille=11)

# en t : conversion connue
g.texte(t, 1.6, "%d $" % dollars, couleur=AJOUT, gras=True, taille=13, ancre="middle", dy=-10)
g.fleche(t, 0.95, t, -1.35, couleur=DOUX, epaisseur=2)
g.texte(t, -0.2, "÷ X_{t}\u00a0= %s" % v(X), couleur=DOUX, gras=True, taille=14, dx=10)
g.texte(t, -0.75, "connu aujourd'hui", couleur=DOUX, taille=11.5, dx=10)
g.texte(t, -1.9, "%.0f €" % (dollars / X), couleur=ACCENT, gras=True, taille=13,
        ancre="middle", dy=38)

# en T : conversion au taux de ce jour-là, inconnu en t
g.fleche(T, 0.95, T, -1.35, couleur=DOUX, epaisseur=1.5, pointilles="4 4")
g.texte(T, -0.2, "÷ X_{T}", couleur=DOUX, gras=True, taille=14, dx=10)
g.texte(T, -0.75, "inconnu en t", couleur=DOUX, taille=11.5, dx=10)

sys.stdout.write(g.svg())
