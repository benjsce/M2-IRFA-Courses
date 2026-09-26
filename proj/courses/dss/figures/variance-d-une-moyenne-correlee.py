#!/usr/bin/env python3
r"""
variance-d-une-moyenne-correlee.svg — la variance de la moyenne de B arbres, et son plancher.

La forme de la fiche, $\rho\sigma^2+(1-\rho)\sigma^2/B$, rapportée à $\sigma^2$. Pour des
arbres indépendants, $\rho=0$, elle tombe vers zéro quand $B$ grandit. Pour $\rho=0{,}5$,
l'exemple, elle ne descend jamais sous 0,5 : le second terme disparaît, le premier reste.

Usage : python courses/dss/figures/variance-d-une-moyenne-correlee.py > variance-d-une-moyenne-correlee.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

v = lambda B, rho: rho + (1 - rho) / B

f = Figure(xmin=0, xmax=104, ymin=0, ymax=1.08, w=560, h=300,
           titre="Ajouter des arbres n'efface que le second terme : ρσ² reste")
f.axes(xlab="nombre d'arbres B", ylab="variance / σ²", xticks=(1, 25, 50, 75, 100),
       yticks=(0.5, 1), fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%g" % t).replace(".", ","))
f.courbe([(0, 0.5), (104, 0.5)], couleur=AJOUT, epaisseur=1.4, pointilles="6 4")
f.fonction(lambda B: v(B, 0.0), 1, 100, n=300, couleur=DOUX, epaisseur=2.2)
f.fonction(lambda B: v(B, 0.5), 1, 100, n=300, couleur=ACCENT, epaisseur=2.6)
f.texte(100, v(100, 0.5), "ρ = 0,5 : plancher 0,5", couleur=ACCENT, ancre="end", dy=-10, gras=True,
        fond=True)
f.texte(100, v(100, 0.0), "ρ = 0 : vers zéro", couleur=DOUX, ancre="end", dy=-10, gras=True,
        fond=True)

sys.stdout.write(f.svg())
