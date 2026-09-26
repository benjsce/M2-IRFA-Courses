#!/usr/bin/env python3
r"""
famille-hara.svg — trois points de la famille, lus sur leur aversion absolue.

La fiche dit que choisir une utilité revient à fixer $\eta$ et $\gamma$ dans
$A(z)=(\eta+z/\gamma)^{-1}$, que $\eta=0$ donne CRRA et que $\gamma\to\infty$ donne CARA.
Le dessin montre ce que ces deux réglages font à la courbe : avec $\eta=0$ l'aversion
décroît comme $\gamma/z$, avec $\gamma\to\infty$ elle devient la constante $1/\eta$.

Trois membres, pris dans les exemples des fiches du cours : $\gamma=4$ (exemple de la
fiche, $A(100)=0{,}04$), $\gamma=1$ (l'utilité logarithmique, $A(100)=0{,}01$) et CARA avec
$A=0{,}01$, soit $\eta=100$. Les deux derniers ont la même aversion à 100 et divergent
partout ailleurs.

Usage : python courses/dup/figures/famille-hara.py > famille-hara.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

YMAX = 0.07

f = Figure(xmin=0, xmax=310, ymin=0, ymax=YMAX, w=560, h=330,
           titre="η = 0 fait décroître l'aversion avec la richesse, γ → ∞ la rend constante")
f.axes(xlab="richesse z", ylab="A(z)", xticks=(0, 100, 200, 300),
       yticks=(0.01, 0.02, 0.04, 0.06), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))

f.fonction(lambda z: 4.0 / z, 4.0 / YMAX, 300, couleur=ACCENT, epaisseur=2.4)
f.fonction(lambda z: 1.0 / z, 1.0 / YMAX, 300, couleur=AJOUT, epaisseur=2.2)
f.courbe([(0, 0.01), (300, 0.01)], couleur=DOUX, epaisseur=2.0, pointilles="6 4")

f.segment(100, 0, 100, 0.04)
f.point(100, 0.04, couleur=ACCENT)
f.point(100, 0.01, couleur=ENCRE)

f.texte(135, 4.0 / 135, "η = 0, γ = 4 : CRRA", couleur=ACCENT, dx=6, dy=-8, gras=True,
        fond=True)
f.texte(58, 1.0 / 58, "η = 0, γ = 1 : logarithme", couleur=AJOUT, dx=8, dy=-2, gras=True,
        fond=True)
f.texte(300, 0.01, "γ → ∞, η = 100 : CARA", couleur=DOUX, ancre="end", dy=17, gras=True,
        fond=True)
f.texte(100, 0.01, "même A à 100", couleur=ENCRE, ancre="end", dx=-8, dy=17, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
