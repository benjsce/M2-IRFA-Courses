#!/usr/bin/env python3
r"""
processus-stochastique.svg — deux lectures d'un même tableau (t, ω) ↦ X_t(ω).

Ce que la figure doit faire voir : à ω fixé, X est une fonction du temps, une trajectoire ;
à t fixé, X_t est une variable aléatoire, une fonction de ω.

L'exemple des slides (§0.5 slide 4) : ω est tiré uniformément dans [0, 1] et
X_t(ω) = ω + a t, ici avec a = 1, pour t dans [0, 1]. Trois tirages, ω = 0,2, 0,5 et 0,9,
donnent trois trajectoires. La coupe verticale en t = 0,5 rencontre chacune en ω + 0,5 :
0,7, 1 et 1,4 ; quand ω parcourt [0, 1], X_{0,5} parcourt [0,5 ; 1,5], qu'on marque sur la
coupe : c'est la loi de cette variable, uniforme.

Usage : python courses/cs/figures/processus-stochastique.py > processus-stochastique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

A = 1.0
OMEGAS = (0.2, 0.5, 0.9)
T0 = 0.5
X = lambda t, w: w + A * t
fr = lambda v: ("%g" % v).replace(".", ",")

f = Figure(0, 1.35, 0, 2.2, w=580, h=340, marges=(40, 18, 40, 16),
           titre="À ω fixé, une trajectoire ; à t fixé, une variable aléatoire")
f.axes(xlab="t", xticks=(0, 0.5, 1), yticks=(0.5, 1, 1.5, 2), fmt=fr, croix=(0, 0))
f.texte(0, 2.2, "X_{t}(ω)", couleur=DOUX, dx=8, dy=4)
for w in OMEGAS:
    f.courbe([(0, X(0, w)), (1, X(1, w))], couleur=ACCENT, epaisseur=2.4)
    f.texte(1, X(1, w), "ω = " + fr(w), couleur=ACCENT, dx=8, dy=4, gras=True)

# la coupe en t = 0,5
f.segment(T0, 0, T0, 2.05, couleur=PALE, epaisseur=1.2)
f.courbe([(T0, X(T0, 0)), (T0, X(T0, 1))], couleur=AJOUT, epaisseur=5.0)
for w in OMEGAS:
    f.point(T0, X(T0, w), couleur=AJOUT, r=4.2)
f.texte(T0, X(T0, 1), "X_{0,5} : une variable aléatoire,", couleur=AJOUT, dx=-8, dy=-26, ancre="end", gras=True)
f.texte(T0, X(T0, 1), "uniforme sur [0,5 ; 1,5]", couleur=AJOUT, dx=-8, dy=-10, ancre="end")
f.texte(1, X(1, 0.2), "une trajectoire par ω", couleur=ACCENT, dx=8, dy=24)

sys.stdout.write(f.svg())
