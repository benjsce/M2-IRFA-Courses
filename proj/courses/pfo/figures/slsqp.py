#!/usr/bin/env python3
r"""
slsqp.svg — une itération : le modèle quadratique, son minimum, et le pas.

L'exemple de la fiche : minimiser $f(x)=(x-3)^2$ sous $x\ge0$, depuis $x_0=0$, avec
$H_0=1$. Le sous-problème remplace $f$ par le modèle $f(x_0)-6d+\tfrac12d^2$, une parabole
deux fois plus plate que $f$, dont le minimum est en $d_0=6$. Le pas $\alpha_0=\tfrac12$
ramène à $x_1=3$, le vrai minimum.

Usage : python courses/pfo/figures/slsqp.py > slsqp.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

fx = lambda x: (x - 3) ** 2
modele = lambda x: fx(0) - 6 * x + 0.5 * x * x        # d = x - x0, x0 = 0

f = Figure(xmin=-0.6, xmax=8.2, ymin=-10, ymax=12, w=560, h=330,
           titre="Le modèle, trop plat, vise 6 ; le pas de ½ ramène au minimum, 3")
f.axes(xlab="x", xticks=(0, 3, 6), yticks=(-9, 0, 9), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: "%d" % t, croix=(0, 0))

f.fonction(fx, -0.4, 6.4, couleur=ACCENT, epaisseur=2.6)
f.fonction(modele, -0.5, 8.0, couleur=AJOUT, epaisseur=2.0, pointilles="6 4")
f.point(0, fx(0), couleur=ENCRE)
f.texte(0, fx(0), "x0", couleur=ENCRE, dx=8, dy=4, gras=True)
f.point(6, modele(6), couleur=AJOUT)
f.texte(6, modele(6), "minimum du modèle : d0 = 6", couleur=AJOUT, ancre="middle", dy=18,
        gras=True, fond=True)
f.point(3, 0, couleur=ACCENT, r=4.5)
f.texte(3.35, -1.9, "x1 = x0 + ½ d0 = 3", couleur=ACCENT, gras=True,
        fond=True)
f.fleche(0.2, -4.5, 5.8, -4.5, couleur=DOUX, epaisseur=1.3)
f.fleche(0.2, -6.5, 2.8, -6.5, couleur=ACCENT, epaisseur=1.6)
f.texte(0.3, -4.5, "direction d0", couleur=DOUX, dy=-5, taille=11)
f.texte(0.3, -6.5, "pas α0 = ½", couleur=ACCENT, dy=14, taille=11)
f.texte(6.4, fx(6.4), "f(x) = (x − 3)²", couleur=ACCENT, ancre="end", dx=-8, dy=-4, gras=True,
        fond=True)

sys.stdout.write(f.svg())
