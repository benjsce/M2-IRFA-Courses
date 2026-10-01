#!/usr/bin/env python3
r"""
processus-indistinguables.svg — une version qui n'est pas indistinguable.

Ce que la figure doit faire voir : à chaque instant fixé, X et Y ne diffèrent que pour un
seul ω, donc avec probabilité nulle ; mais chaque trajectoire de Y a son propre trou,
et aucune ne coïncide avec celle de X sur tout le temps.

L'exemple des slides (§0.5 slide 4), avec a = 1 : sur [0, 1] muni de la mesure de
Lebesgue, X_t(ω) = ω + t, et Y_t(ω) = X_t(ω) sauf à l'instant t = ω, où Y vaut 0. Deux
tirages, ω = 0,3 et 0,7 : la trajectoire de Y suit celle de X, avec un point manquant en
t = ω (rond vide) et un point posé à 0 (rond plein). La coupe t = 0,5 ne rencontre
aucun des deux trous : en un instant fixé, seul ω = 0,5 aurait le sien.

Usage : python courses/cs/figures/processus-indistinguables.py > processus-indistinguables.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE, FOND   # noqa: E402

OMEGAS = (0.3, 0.7)
T0 = 0.5
X = lambda t, w: w + t
fr = lambda v: ("%g" % v).replace(".", ",")

f = Figure(0, 1.3, -0.15, 2.0, w=580, h=370, marges=(40, 18, 76, 16),
           titre="Y est une version de X ; elle n'en est pas indistinguable")
f.axes(xlab="t", xticks=(0, 0.3, 0.5, 0.7, 1), yticks=(0.5, 1, 1.5), fmt=fr, croix=(0, 0))
f.segment(T0, -0.1, T0, 1.9, couleur=PALE, epaisseur=1.2)
f.texte(T0, 1.9, "t = 0,5 fixé : X_{t} = Y_{t} sauf si ω = 0,5,", couleur=ENCRE, ancre="middle", dy=-4)
f.texte(T0, 1.9, "probabilité 0 : Y est une version de X", couleur=ENCRE, ancre="middle", dy=12, gras=True)

for w in OMEGAS:
    f.courbe([(0, X(0, w)), (1, X(1, w))], couleur=ACCENT, epaisseur=2.4)
    f.texte(1, X(1, w), "ω = " + fr(w), couleur=ACCENT, dx=8, dy=4, gras=True)
    # le trou de Y en t = ω, et la valeur 0 posée à la place
    f.point(w, X(w, w), couleur=AJOUT, r=5.2)
    f.point(w, X(w, w), couleur=FOND, r=3.2)
    f.segment(w, X(w, w), w, 0, couleur=AJOUT, epaisseur=1.2)
    f.point(w, 0, couleur=AJOUT, r=4.4)

f.texte(0, -0.15, "Chaque trajectoire de Y a son trou en t = ω, où Y_{ω}(ω) = 0 :", couleur=AJOUT, dy=44)
f.texte(0, -0.15, "P(X_{t} = Y_{t} pour tout t) = 0, X et Y ne sont pas indistinguables", couleur=AJOUT, dy=62, gras=True)

sys.stdout.write(f.svg())
