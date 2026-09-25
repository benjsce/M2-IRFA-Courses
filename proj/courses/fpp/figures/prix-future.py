#!/usr/bin/env python3
r"""
prix-future.svg — un seul flux pour le forward, un flux par jour pour le future.

La fiche : le future se distingue du forward par les appels de marge quotidiens ;
chaque variation est encaissée le jour même et doit être replacée à un taux inconnu.
En haut, le forward : tout se règle en T. En bas, le future : chaque jour, la variation
du prix future est payée ou reçue. Les hauteurs ne viennent d'aucune donnée : seuls le
nombre de flux et leurs dates comptent.

Usage : python courses/fpp/figures/prix-future.py > prix-future.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T = 1.8, 8.8
g = Figure(xmin=0, xmax=10, ymin=-4.6, ymax=4.3, w=640, h=330, marges=(8, 8, 8, 8),
           titre="Forward contre future : un règlement en T, ou un règlement par jour")

for y0, nom in ((2.0, "forward"), (-2.2, "future")):
    g.axe_temps(y0, 1.2, 9.7, [(t, "t"), (T, "T")])
    g.texte(0.05, y0 + 0.15, nom, taille=12, gras=True, couleur=ENCRE)

# forward : un seul flux, en T
g.fleche(T, 2.35, T, 3.7, couleur=ACCENT, epaisseur=2, pointilles="5 4")
g.texte(T, 3.0, "S_{T} − K", couleur=ACCENT, gras=True, taille=13.5, dx=-9, ancre="end")

# future : un flux par jour, de signe quelconque
hauteurs = (0.8, -0.6, 1.1, 0.5, -0.9, 0.7, -0.4, 0.9, -0.6, 0.7)
pas = (T - t) / len(hauteurs)
for k, h in enumerate(hauteurs):
    xk = t + (k + 1) * pas
    y0 = -2.2 + (0.3 if h > 0 else -0.3)
    g.fleche(xk, y0, xk, y0 + h, couleur=AJOUT, epaisseur=1.7)
g.texte(t + 0.2, -0.55, "chaque jour, la variation de Hₜ, encaissée ou payée",
        couleur=AJOUT, gras=True, taille=12.5)
g.texte(t + 0.2, -3.95, "puis replacée jusqu'en T au taux du moment, inconnu en t",
        couleur=DOUX, taille=11.5)

sys.stdout.write(g.svg())
