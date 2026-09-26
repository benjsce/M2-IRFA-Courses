#!/usr/bin/env python3
r"""
approximation-arrow-pratt.svg — la prime exacte et son approximation, selon la taille du pari.

La fiche dit deux choses que la prose sépare et que le dessin réunit : l'approximation
vaut pour un petit pari, et elle se dégrade quand le pari grandit devant la richesse. On
trace donc, pour le pari de $\pm h$ à pile ou face à la richesse 100 sous utilité
logarithmique (l'exemple minimal, où $h=10$), la prime exacte — la richesse moins
l'équivalent certain $\sqrt{(100-h)(100+h)}$ — et l'approximation
$\tfrac12\,h^2\,A(100)=h^2/200$.

À $h=10$ les deux valent 0,50 ; à $h=50$ la prime exacte vaut 13,4 et l'approximation
12,5. Ces nombres sont recalculés ici.

Usage : python courses/dup/figures/approximation-arrow-pratt.py > approximation-arrow-pratt.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402

W = 100.0


def exacte(h):
    return W - math.sqrt((W - h) * (W + h))      # u = ln : c = exp(E ln) = √((W-h)(W+h))


def approchee(h):
    return 0.5 * h * h * (1.0 / W)               # ½ Var A(w0), A(z) = 1/z


def fr(v, d=1):
    return ("%.*f" % (d, v)).replace(".", ",")


f = Figure(xmin=0, xmax=64, ymin=0, ymax=22, w=560, h=330,
           titre="Les deux primes se confondent pour un petit pari et s'écartent quand il grandit")
f.axes(xlab="taille h du pari ±h", ylab="prime", xticks=(0, 10, 30, 50),
       yticks=(5, 10, 15, 20), fmt=lambda t: str(int(t)))

f.fonction(approchee, 0, 60, couleur=AJOUT, epaisseur=2.0, pointilles="6 4")
f.fonction(exacte, 0, 60, couleur=ACCENT, epaisseur=2.4)

f.point(10, exacte(10), couleur=ACCENT)
f.texte(4, 3.3, "h = 10 : 0,50 et 0,50", couleur=DOUX, taille=11.5, fond=True)

f.segment(50, 0, 50, exacte(50))
f.point(50, exacte(50), couleur=ACCENT)
f.point(50, approchee(50), couleur=AJOUT, r=3.2)
f.mesure(50, approchee(50), exacte(50), couleur=DOUX)
f.texte(50, exacte(50), "exacte : " + fr(exacte(50)), couleur=ACCENT, ancre="end",
        dx=-8, dy=-4, taille=12, gras=True, fond=True)
f.texte(50, approchee(50), "½ Var A : " + fr(approchee(50)), couleur=AJOUT, dx=8, dy=12,
        taille=12, gras=True, fond=True)

sys.stdout.write(f.svg())
