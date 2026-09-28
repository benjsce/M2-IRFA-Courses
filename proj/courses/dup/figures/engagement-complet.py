#!/usr/bin/env python3
r"""
engagement-complet.svg — les deux équations d'Euler du plan engagé, lues sur trois barres.

L'exemple de la fiche [ajout] : $u=\ln$, $\beta=\tfrac12$, $\delta=R=1$, $w_1=100$, d'où le
plan $(50,25,25)$ et les utilités marginales $u'(c_t)=1/c_t$ : 0,02, 0,04, 0,04. La flèche
courbe ramène $u'(c_2)$ en période 1 en portant $\beta\delta R$, et arrive à la hauteur de
$u'(c_1)$ ; celle qui ramène $u'(c_3)$ en période 2 porte $\delta R$ et arrive à la hauteur de
$u'(c_2)$. Ce sont les deux équations de la Forme, un facteur par flèche.

Usage : python courses/dup/figures/engagement-complet.py > engagement-complet.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

BETA, DELTA, R, W1 = 0.5, 1.0, 1.0, 100.0
c1 = W1 / (1 + BETA * DELTA * R + BETA * DELTA ** 2 * R)   # u = ln : c2 = βδR c1, c3 = δR c2
c2 = BETA * DELTA * R * c1
c3 = DELTA * R * c2
assert abs(c1 + c2 / R + c3 / R ** 2 - W1) < 1e-9
um = [1 / c1, 1 / c2, 1 / c3]                               # 0,02 0,04 0,04

f = Figure(xmin=0.3, xmax=3.9, ymin=-0.013, ymax=0.066, w=560, h=340, marges=(58, 16, 20, 18),
           titre="Chaque flèche ramène une utilité marginale d'une période en arrière, multipliée par son facteur")
f.axes(ylab="u′(cₜ)", yticks=(0.02, 0.04), fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(0.3, 0))

for t, (m, c) in enumerate(zip(um, (c1, c2, c3)), start=1):
    f.barre(t, m, 0.36, couleur=ACCENT if t == 1 else DOUX, opacite=0.85 if t == 1 else 0.55, y0=0)
    f.texte(t, 0, "période %d" % t, couleur=DOUX, ancre="middle", dy=17, taille=12)
    f.texte(t, 0, "c%s = %s" % ("₁₂₃"[t - 1], ("%.0f" % c)), couleur=DOUX, ancre="middle", dy=32, taille=11.5)
    f.texte(t, m, "u′(c%s)" % "₁₂₃"[t - 1], couleur=ENCRE, ancre="middle", dy=-6, gras=True)

f.fleche(2 - 0.1, um[1] + 0.004, 1 + 0.2, BETA * DELTA * R * um[1], couleur=AJOUT, courbure=26, epaisseur=1.8)
f.texte(1.55, um[1] + 0.011, "× βδR = ½", couleur=AJOUT, ancre="middle", gras=True, fond=True)
f.fleche(3 - 0.1, um[2] + 0.004, 2 + 0.2, DELTA * R * um[2], couleur=AJOUT, courbure=26, epaisseur=1.8)
f.texte(2.55, um[2] + 0.011, "× δR = 1", couleur=AJOUT, ancre="middle", gras=True, fond=True)

f.texte(2.1, 0.06, "u′(c₁) = βδR u′(c₂)   ;   u′(c₂) = δR u′(c₃)", couleur=ENCRE, ancre="middle",
        taille=13.5, gras=True)

sys.stdout.write(f.svg())
