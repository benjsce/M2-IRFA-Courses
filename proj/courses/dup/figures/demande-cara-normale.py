#!/usr/bin/env python3
r"""
demande-cara-normale.svg — l'équivalent certain comme parabole en la position.

Le geste de la fiche : écrire l'équivalent certain comme une parabole en $x$, puis
chercher son sommet. Sur l'exemple, $\hat v=110$, $p=100$, $\hat\sigma=20$ :
$\mathrm{CE}-w=10\,x-200\,x^2$, dont le sommet est en $x=10/400=0{,}025$. Le terme en $x$
est le gain espéré, le terme en $x^2$ la pénalité de variance ; au-delà du sommet la
seconde l'emporte.

Usage : python courses/dup/figures/demande-cara-normale.py > demande-cara-normale.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

V, P, S = 110.0, 100.0, 20.0
gain = lambda x: (V - P) * x - 0.5 * S * S * x * x
XS = (V - P) / (S * S)                     # 0,025

f = Figure(xmin=-0.012, xmax=0.058, ymin=-0.2, ymax=0.2, w=560, h=330, marges=(54, 30, 40, 18),
           titre="Le sommet de la parabole est la demande : 0,025")
f.axes(xlab="position x", ylab="CE − w", xticks=(0, 0.025), yticks=(-0.1, 0.125),
       fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: ("%g" % t).replace(".", ","),
       croix=(0, 0))

f.fonction(lambda x: (V - P) * x, -0.004, 0.015, couleur=DOUX, epaisseur=1.4, pointilles="5 4")
f.fonction(gain, -0.01, 0.055, couleur=ACCENT, epaisseur=2.6)

f.segment(XS, 0, XS, gain(XS), couleur=AJOUT)
f.point(XS, gain(XS), couleur=AJOUT)
f.texte(XS, gain(XS), "sommet : x = 10/400", couleur=AJOUT, ancre="middle", dy=-10,
        gras=True, fond=True)
f.texte(0.015, (V - P) * 0.015, "le gain espéré seul", couleur=DOUX, ancre="end", dx=-8,
        dy=-2, taille=11.5, fond=True)
f.texte(0.054, -0.1, "la pénalité de variance l'emporte", couleur=ACCENT, ancre="end",
        taille=11.5, fond=True)

sys.stdout.write(f.svg())
