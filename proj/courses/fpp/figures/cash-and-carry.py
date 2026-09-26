#!/usr/bin/env python3
r"""
cash-and-carry.svg — le portage vu du vendeur à terme. En t, il emprunte 100 et achète
l'action : rien ne sort de sa poche. En T, un an plus tard, il livre l'action, reçoit K et
rembourse 100 / 0,9608 = 104,08. Son résultat, K − 104,08, est connu dès aujourd'hui.

Usage : python courses/fpp/figures/cash-and-carry.py > cash-and-carry.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.9, xmax=2.3, ymin=-2.0, ymax=1.9, w=560, h=360, marges=(10, 10, 10, 10),
           titre="Porter l'action coûte 104,08 dans un an : le vendeur à terme connaît son résultat, K − 104,08")
f.axe_temps(0, -0.5, 2.2, [(0, "t"), (1.6, "T")])
f.fleche(-0.12, 0.1, -0.12, 1.1, couleur=ACCENT, epaisseur=2)
f.texte(-0.12, 0.8, "+100 emprunté", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.fleche(0.12, -0.42, 0.12, -1.4, couleur=AJOUT, epaisseur=2)
f.texte(0.12, -0.85, "−100 : achat de l'action", couleur=AJOUT, dx=8, gras=True)
f.fleche(1.48, 0.1, 1.48, 1.2, couleur=ACCENT, epaisseur=2)
f.texte(1.48, 0.85, "+K reçu", couleur=ACCENT, ancre="end", dx=-8, gras=True)
f.texte(1.48, 0.55, "l'action est livrée", couleur=DOUX, ancre="end", dx=-8, taille=12)
f.fleche(1.72, -0.42, 1.72, -1.55, couleur=AJOUT, epaisseur=2.4)
f.texte(1.72, -1.35, "−104,08 remboursé", couleur=AJOUT, ancre="end", dx=-8, gras=True)
f.fleche(0.0, 1.35, 1.6, 1.35, couleur=DOUX, courbure=16, epaisseur=1.3)
f.texte(0.8, 1.35, "100 / P(t,T) = 100 / 0,9608", couleur=DOUX, ancre="middle", dy=-24, taille=12)
f.texte(0.8, -1.85, "résultat en T : K − 104,08, connu en t", couleur=ENCRE, ancre="middle", gras=True)
sys.stdout.write(f.svg())
