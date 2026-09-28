#!/usr/bin/env python3
r"""
conditions-d-equilibre-de-laibson.svg — le revenu alterne, la consommation beaucoup moins.

L'exemple du revenu variable de la source [L5 slide 50, L5 slide 51], chiffré [ajout] :
$\delta R=1$, $R=1{,}1$, $\bar y=10$ les périodes impaires, $\underline y=5$ les paires,
$x_0=0$, $w_0=z_0=20$, qui satisfait $\underline y+z_0(R^2-1)=9{,}2\le\bar y$. La solution
de la source : $c_t=\bar y$ aux périodes impaires, $\underline y+w_0(R^2-1)$ aux paires.
Le script vérifie les deux contraintes de l'actif illiquide à chaque période.

Usage : python courses/dup/figures/conditions-d-equilibre-de-laibson.py > conditions-d-equilibre-de-laibson.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

R, YH, YB, W0 = 1.1, 10.0, 5.0, 20.0
assert YB + W0 * (R ** 2 - 1) <= YH
T = range(1, 7)
y = {t: YH if t % 2 else YB for t in T}
c = {t: YH if t % 2 else YB + W0 * (R ** 2 - 1) for t in T}
x = {0: 0.0}; z = {0: W0}
for t in T:
    x[t] = W0 / R * (R ** 2 - 1) if t % 2 else 0.0
    z[t] = W0 / R if t % 2 else W0
    assert c[t] <= y[t] + R * x[t - 1] + 1e-9                                  # liquide
    assert abs(c[t] + x[t] + z[t] - (y[t] + R * (z[t - 1] + x[t - 1]))) < 1e-9   # budget

f = Figure(xmin=0.4, xmax=6.6, ymin=3.2, ymax=11.4, w=560, h=320, marges=(58, 16, 40, 18),
           titre="Le revenu tombe à 5 une période sur deux ; la consommation ne tombe qu'à 9,2")
f.axes(xlab="période t", xticks=tuple(T), yticks=(5, 9.2, 10), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%g" % t).replace(".", ","))
for v in (5, 9.2, 10):
    f.segment(0.4, v, 6.6, v)
f.courbe([(t, y[t]) for t in T], couleur=DOUX, epaisseur=1.8, pointilles="6 4")
f.courbe([(t, c[t]) for t in T], couleur=ACCENT, epaisseur=2.6)
for t in T:
    f.point(t, c[t], couleur=ACCENT, r=3.6)
f.texte(4.5, y[4], "revenu yₜ", couleur=DOUX, dx=10, dy=16, taille=12)
f.texte(4.5, 10.75, "consommation cₜ", couleur=ACCENT, ancre="middle", dy=0, taille=12, gras=True)
f.texte(2, c[2], "cₜ = yₜ + R xₜ₋₁", couleur=ENCRE, ancre="middle", dy=18, taille=12, fond=True)

sys.stdout.write(f.svg())
