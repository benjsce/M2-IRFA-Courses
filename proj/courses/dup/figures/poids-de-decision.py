#!/usr/bin/env python3
r"""
poids-de-decision.svg — le même quart de probabilité, pesé à deux endroits de la courbe.

L'exemple de la fiche : $\varphi(t)=\sqrt t$ et un état bas de probabilité $\tfrac14$. En
position longue il est le pire état, son cumul va de 0 à $\tfrac14$, et son poids est le
saut de $\varphi$ sur cet intervalle : $0{,}5$. En position courte il devient le meilleur,
son cumul va de $\tfrac34$ à 1, et le saut n'est plus que $1-\varphi(0{,}75)=0{,}134$.
Les deux intervalles ont la même largeur sur l'axe horizontal ; seule la hauteur change.

Usage : python courses/dup/figures/poids-de-decision.py > poids-de-decision.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

phi = math.sqrt
P = 0.25

f = Figure(xmin=0, xmax=1.3, ymin=0, ymax=1.1, w=520, h=400, marges=(54, 16, 44, 18),
           titre="Même largeur de probabilité, deux sauts de φ très différents")
f.axes(xlab="probabilité cumulée", ylab="φ", xticks=(0, 0.25, 0.75, 1), yticks=(0.5, 0.866, 1),
       fmt=lambda t: {0: "0", 0.25: "¼", 0.75: "¾", 1: "1"}[t],
       fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.fonction(phi, 0, 1, n=300, couleur=DOUX, epaisseur=2.2)

# position longue : l'état bas est le pire, cumul de 0 à 1/4
f.courbe([(0, 0), (P, 0)], couleur=ACCENT, epaisseur=5)
f.segment(P, 0, P, phi(P))
f.segment(P, phi(P), 1.08, phi(P))
f.mesure(1.08, 0, phi(P), couleur=ACCENT, etiquette="longue : 0,5")

# position courte : l'état bas est le meilleur, cumul de 3/4 à 1
f.courbe([(1 - P, 0), (1, 0)], couleur=AJOUT, epaisseur=5)
f.segment(1 - P, 0, 1 - P, phi(1 - P))
f.segment(1 - P, phi(1 - P), 1.08, phi(1 - P))
f.segment(1, phi(1), 1.08, phi(1))
f.mesure(1.08, phi(1 - P), 1, couleur=AJOUT, etiquette="courte : 0,134")

f.point(P, phi(P), couleur=ENCRE)
f.point(1 - P, phi(1 - P), couleur=ENCRE)
f.texte(0.38, phi(0.38), "φ(t) = √t", couleur=DOUX, dx=-6, dy=-10, ancre="end", gras=True,
        fond=True)

sys.stdout.write(f.svg())
