#!/usr/bin/env python3
r"""
biais-pour-le-present.svg — deux attentes de quatre semaines sur la même fonction D.

L'exemple de la fiche, le modèle du cours à $\beta=\tfrac12$, $\delta=1$ [L5 slide 14] :
$D(0)=1$, puis $D(t)=\tfrac12$ à toute date future. L'attente qui part d'aujourd'hui fait
tomber le poids de 1 à ½, $D(0)/D(4)=2$ ; celle qui part de la semaine 26 ne le fait pas
bouger, $D(26)/D(30)=1$. C'est l'inégalité de la Forme, lue sur les deux fenêtres.

Usage : python courses/dup/figures/biais-pour-le-present.py > biais-pour-le-present.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

BETA, DELTA = 0.5, 1.0
def D(t):
    return 1.0 if t == 0 else BETA * DELTA ** t

f = Figure(xmin=-1, xmax=33, ymin=-0.42, ymax=1.18, w=560, h=330, marges=(54, 16, 20, 18),
           titre="La même attente de quatre semaines divise le poids par 2 si elle part d'aujourd'hui, par 1 si elle part de la semaine 26")
f.axes(xlab="semaine t", ylab="D(t)", xticks=(0, 4, 26, 30), yticks=(0.5, 1),
       fmt=lambda t: str(int(t)), fmt_y=lambda t: {0.5: "½", 1: "1"}[t])

for t in range(0, 33):
    f.point(t, D(t), couleur=ACCENT if t in (0, 4, 26, 30) else DOUX,
            r=4 if t in (0, 4, 26, 30) else 2.2)

# les deux fenêtres, sous l'axe
for a, b, lib, c in ((0, 4, "D(0)/D(4) = 1 / ½ = 2", AJOUT), (26, 30, "D(26)/D(30) = ½ / ½ = 1", ACCENT)):
    f.courbe([(a, -0.12), (b, -0.12)], couleur=c, epaisseur=5)
    f.texte((a + b) / 2, -0.12, lib, couleur=c, ancre="middle" if a else "start", dy=22,
            dx=0 if a else -6, taille=12, gras=True)
f.mesure(4.8, D(4), D(0), couleur=AJOUT)
f.segment(0, 1, 4.8, 1)

f.texte(16, 0.86, "D(0)/D(τ)  >  D(t)/D(t+τ)", couleur=ENCRE, ancre="middle", taille=13.5, gras=True)

sys.stdout.write(f.svg())
