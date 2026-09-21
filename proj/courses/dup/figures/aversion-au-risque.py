#!/usr/bin/env python3
r"""
aversion-au-risque.svg — l'écart de Jensen sur l'exemple minimal de la fiche.

La fiche pose $u(x)=\sqrt{x}$ et le pari $(0,\tfrac12;100,\tfrac12)$, et donne les deux
nombres : $u(50)=7{,}07$ contre $5$. La figure ne dit rien de plus — elle montre d'où
vient l'écart : la corde passe sous la courbe parce que la courbe est concave.

L'équivalent certain et la prime de risque n'y figurent pas, bien que le dessin s'y
prête : ils appartiennent à d'autres fiches, et la figure d'une fiche ne montre que ce
que sa fiche dit.

Usage : python courses/dup/figures/aversion-au-risque.py > aversion-au-risque.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX          # noqa: E402

u = math.sqrt
X0, X1, XM = 0.0, 100.0, 50.0            # les deux résultats du pari, et leur moyenne
CORDE = (u(X0) + u(X1)) / 2              # E[u(x)] = 5
HAUT = u(XM)                             # u(E[x]) = 7,07

f = Figure(xmin=0, xmax=112, ymin=0, ymax=11.6, w=560, h=330,
           titre="La corde passe sous la courbe : u(50) = 7,07 contre 5 pour le pari")

f.axes(xlab="richesse x", ylab="u", xticks=(0, 50, 100), yticks=(5, 10),
       fmt=lambda t: str(int(t)))

# les traits de construction d'abord, la courbe par-dessus
f.segment(XM, 0, XM, HAUT)
f.segment(0, CORDE, XM, CORDE)
f.segment(0, HAUT, XM, HAUT)

f.courbe([(X0, u(X0)), (X1, u(X1))], couleur=DOUX, epaisseur=1.8, pointilles=None)
f.fonction(u, 0, 108, couleur=ACCENT, epaisseur=2.4)

f.point(X0, u(X0), couleur=DOUX, r=3.2)
f.point(X1, u(X1), couleur=DOUX, r=3.2)
f.point(XM, HAUT, couleur=ACCENT)
f.point(XM, CORDE, couleur=ENCRE)

f.mesure(XM, CORDE, HAUT, couleur=ENCRE, etiquette="l'écart de Jensen")

f.texte(104, u(104), "u(x) = √x", couleur=ACCENT, dx=-4, dy=-10, ancre="end", gras=True)
f.texte(58, CORDE, "la corde : moyenne des utilités", couleur=DOUX, dx=6, dy=16,
        taille=11.5, fond=True)
f.texte(0, HAUT, "7,07", couleur=ACCENT, ancre="end", dx=-8, dy=4, taille=11.5, gras=True)
f.texte(0, CORDE, "5", couleur=ENCRE, ancre="end", dx=-8, dy=4, taille=11.5, gras=True)
f.texte(XM, 0, "la moyenne certaine", couleur=DOUX, ancre="middle", dy=-8, taille=11)

sys.stdout.write(f.svg())
