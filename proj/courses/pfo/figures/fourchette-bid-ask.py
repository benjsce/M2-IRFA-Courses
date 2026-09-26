#!/usr/bin/env python3
r"""
fourchette-bid-ask.svg — qui paie quoi : on achète à l'ask, on vend au bid.

Ce que la figure doit faire voir : le carnet affiche deux prix, l'un au-dessus de
l'autre ; celui qui veut acheter tout de suite paie le prix du haut, affiché par les
vendeurs, celui qui veut vendre tout de suite touche le prix du bas, affiché par les
acheteurs, et la fourchette est l'écart entre les deux. Les chiffres sont ceux de la
fiche : bid 99,90, ask 100,10, fourchette 0,20.

Usage : python courses/pfo/figures/fourchette-bid-ask.py > fourchette-bid-ask.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

BID, ASK = 99.90, 100.10
S = ASK - BID
fr = lambda v: ("%.2f" % v).replace(".", ",")

x0, x1 = 3.6, 5.6                         # le carnet : deux niveaux de prix
g = Figure(xmin=0, xmax=10, ymin=99.85, ymax=100.15, w=640, h=210, marges=(8, 10, 8, 8),
           titre="Qui paie quoi : on achète à l'ask, on vend au bid")

# les deux prix affichés
g.courbe([(x0, ASK), (x1, ASK)], couleur=ACCENT, epaisseur=3.2)
g.courbe([(x0, BID), (x1, BID)], couleur=AJOUT, epaisseur=3.2)
g.texte(x0, ASK, "ask " + fr(ASK), couleur=ACCENT, gras=True, ancre="end", dx=-10, dy=-3)
g.texte(x0, ASK, "prix affiché par les vendeurs", couleur=DOUX, taille=11.5, ancre="end",
        dx=-10, dy=14)
g.texte(x0, BID, "bid " + fr(BID), couleur=AJOUT, gras=True, ancre="end", dx=-10, dy=-3)
g.texte(x0, BID, "prix affiché par les acheteurs", couleur=DOUX, taille=11.5, ancre="end",
        dx=-10, dy=14)

# l'écart entre les deux
g.mesure((x0 + x1) / 2, BID, ASK, couleur=ENCRE, etiquette="fourchette S_{t} = " + fr(S))

# ce que fait celui qui traite tout de suite
g.texte(x1, ASK, "← acheter tout de suite : on paie " + fr(ASK), couleur=ACCENT,
        ancre="start", dx=10, dy=4)
g.texte(x1, BID, "← vendre tout de suite : on touche " + fr(BID), couleur=AJOUT,
        ancre="start", dx=10, dy=4)

sys.stdout.write(g.svg())
