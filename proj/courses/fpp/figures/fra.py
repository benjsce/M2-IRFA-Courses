#!/usr/bin/env python3
r"""
fra.svg — les flux d'un FRA sur l'échéancier : le taux variable R(T,S) est fixé en T,
inconnu aujourd'hui ; en S, on reçoit l'intérêt variable et on paie l'intérêt fixe K,
écrit dès la signature en t.

Usage : python courses/fpp/figures/fra.py > fra.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.35, xmax=2.75, ymin=-1.55, ymax=1.6, w=560, h=320, marges=(10, 10, 10, 10),
           titre="FRA : en S, l'intérêt variable, inconnu aujourd'hui, contre l'intérêt fixe K, écrit en t")
f.axe_temps(0, -0.2, 2.6, [(0, "t"), (1, "T"), (2, "S")])
f.courbe([(1, 0.35), (1, 0.45), (2, 0.45), (2, 0.35)], couleur=DOUX, epaisseur=1.3)
f.texte(1.5, 0.45, "période couverte", couleur=DOUX, ancre="middle", dy=-7, taille=12)
f.fleche(2, 0.1, 2, 1.25, couleur=ACCENT, epaisseur=2, pointilles="5 4")
f.texte(2, 1.05, "reçu : e^{R(T,S)(S−T)}", couleur=ACCENT, dx=10, gras=True)
f.texte(2, 0.8, "inconnu aujourd'hui", couleur=ACCENT, dx=10, taille=12)
f.fleche(2, -0.42, 2, -1.35, couleur=AJOUT, epaisseur=2.2)
f.texte(2, -0.95, "payé : e^{K(S−T)}", couleur=AJOUT, dx=10, gras=True)
f.texte(2, -1.2, "fixé aujourd'hui", couleur=AJOUT, dx=10, taille=12)
f.texte(1, -0.1, "R(T,S) observé", couleur=ACCENT, ancre="middle", dy=38, taille=12)
f.texte(0, -0.1, "signature : K écrit", couleur=AJOUT, ancre="middle", dy=38, taille=12)
f.texte(0, -0.1, "au contrat", couleur=AJOUT, ancre="middle", dy=53, taille=12)
sys.stdout.write(f.svg())
