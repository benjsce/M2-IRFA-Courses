#!/usr/bin/env python3
r"""
prime-de-risque.svg — l'équivalent certain, et ce qui le sépare de la moyenne.

Même courbe et même pari que la figure de dup/aversion-au-risque, volontairement : c'est
le même exemple, et le lecteur qui arrive ici doit reconnaître le dessin. Ce qui s'ajoute
est la construction que cette fiche-ci nomme — l'équivalent certain, lu en redescendant
de $\mathbb{E}u$ sur la courbe, et la prime, qui est ce qui reste jusqu'à la moyenne.

Les trois nombres sont ceux de l'exemple minimal : $c=25$, $\mathbb{E}[\tilde x]=50$,
$\pi=25$ [ajout dans la fiche]. Ils sont recalculés ici à partir de $u$ et du pari.

Usage : python courses/dup/figures/prime-de-risque.py > prime-de-risque.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

u = math.sqrt
X0, X1 = 0.0, 100.0
MOYENNE = (X0 + X1) / 2                  # E[x] = 50
EU = (u(X0) + u(X1)) / 2                 # E[u(x)] = 5
CERTAIN = EU ** 2                        # u(c) = E[u]  =>  c = 25
PRIME = MOYENNE - CERTAIN                # pi = 25

f = Figure(xmin=0, xmax=112, ymin=0, ymax=11.6, w=560, h=330,
           titre="L'équivalent certain vaut 25, la moyenne 50 : la prime est ce qui les sépare")

f.axes(xlab="richesse x", ylab="u", xticks=(0, 25, 50, 100), yticks=(5, 10),
       fmt=lambda t: str(int(t)))

f.segment(0, EU, MOYENNE, EU)
f.segment(CERTAIN, 0, CERTAIN, EU)
f.segment(MOYENNE, 0, MOYENNE, EU)

f.courbe([(X0, u(X0)), (X1, u(X1))], couleur=DOUX, epaisseur=1.8)
f.fonction(u, 0, 108, couleur=ACCENT, epaisseur=2.4)

f.point(MOYENNE, EU, couleur=DOUX, r=3.2)
f.point(CERTAIN, EU, couleur=ACCENT)

f.mesure_h(EU, CERTAIN, MOYENNE, couleur=AJOUT)
f.texte((CERTAIN + MOYENNE) / 2, EU, "la prime, 25", couleur=AJOUT, ancre="middle",
        dy=-10, taille=12, gras=True, fond=True)

f.texte(0, EU, "5", couleur=ENCRE, ancre="end", dx=-8, dy=4, taille=11.5, gras=True)
f.texte(104, u(104), "u(x) = √x", couleur=ACCENT, ancre="end", dx=-4, dy=-10, gras=True)
f.texte(CERTAIN, 0, "c", couleur=ACCENT, ancre="middle", dy=-8, taille=12, gras=True)
f.texte(MOYENNE, 0, "E[x]", couleur=DOUX, ancre="middle", dy=-8, taille=12, gras=True)
f.texte(72, EU, "la même utilité, 5, des deux côtés", couleur=DOUX, dx=6, dy=16,
        taille=11.5, fond=True)

sys.stdout.write(f.svg())
