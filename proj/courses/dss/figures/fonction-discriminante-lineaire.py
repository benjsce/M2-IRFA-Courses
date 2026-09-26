#!/usr/bin/env python3
r"""
fonction-discriminante-lineaire.svg — la droite de l'exemple et les deux demi-plans.

L'exemple de la fiche : $w_0=-1$, $w_1=1$, $w_2=1$. La frontière est la droite
$x_1+x_2=1$, qui coupe l'axe vertical en $-w_0/w_2=1$. D'un côté $f>0$, et le point est
rangé dans la classe A ; de l'autre $f<0$, classe B.

Usage : python courses/dss/figures/fonction-discriminante-lineaire.py > fonction-discriminante-lineaire.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, _n      # noqa: E402

W0, W1, W2 = -1.0, 1.0, 1.0
X0, X1 = -0.3, 1.8


def poly(g, pts, coul, op):
    g._add('<path d="M%s Z" fill="%s" fill-opacity="%s" stroke="none"/>'
           % (" L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in pts), coul, op))


f = Figure(xmin=X0, xmax=X1, ymin=X0, ymax=X1, w=420, h=400, marges=(40, 16, 36, 16),
           titre="Le signe de f dit de quel côté de la droite tombe le point")
poly(f, [(X0, 1 - X0), (X0, X1), (X1, X1), (X1, X0), (1 - X0, X0)], ACCENT, 0.18)
poly(f, [(X0, X0), (1 - X0, X0), (X0, 1 - X0)], AJOUT, 0.18)
f.axes(xlab="x1", ylab="x2", xticks=(0, 1), yticks=(1,), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: "%d" % t, croix=(0, 0))
f.courbe([(X0, 1 - X0), (1 - X0, X0)], couleur=ENCRE, epaisseur=2.4)
f.point(0, 1, couleur=ENCRE)
f.texte(0, 1, "−w0 / w2 = 1", couleur=ENCRE, dx=8, dy=-6, taille=11.5, fond=True)
f.texte(1.2, 1.3, "f > 0 : classe A", couleur=ACCENT, ancre="middle", gras=True, fond=True)
f.texte(0.15, 0.2, "f < 0 : classe B", couleur=AJOUT, ancre="middle", gras=True, fond=True)
f.texte(1.45, -0.2, "x1 + x2 = 1", couleur=ENCRE, ancre="middle", taille=11.5, fond=True)

sys.stdout.write(f.svg())
