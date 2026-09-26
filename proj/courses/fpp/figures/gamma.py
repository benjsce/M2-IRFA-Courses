#!/usr/bin/env python3
r"""
gamma.svg — le delta selon le sous-jacent, à un an et près de l'échéance.

Le gamma est la pente de cette courbe. Pour le call de l'exemple courant, à un an, le
delta passe de 0,618 à 0,637 entre 100 et 101 : pente 0,019. À un mois de l'échéance, la
même courbe se redresse autour du strike, et le gamma y devient grand : c'est ce que dit
la fiche, une couverture qui se dégrade vite près de la monnaie et près de l'échéance.
L'horizon d'un mois est choisi pour le dessin.

Usage : python courses/fpp/figures/gamma.py > gamma.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

N = NormalDist()
K, R, SIG = 100.0, 0.04, 0.20


def delta(s, tau):
    d1 = (math.log(s / K) + (R + SIG ** 2 / 2) * tau) / (SIG * math.sqrt(tau))
    return N.cdf(d1)


f = Figure(xmin=70, xmax=130, ymin=0, ymax=1.08, w=560, h=330,
           titre="Près du strike et de l'échéance, le delta bascule vite : le gamma est grand")
f.axes(xlab="sous-jacent S", ylab="delta", xticks=(70, 85, 100, 115, 130), yticks=(0.5, 0.618, 1),
       fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.fonction(lambda s: delta(s, 1 / 12), 70, 130, n=300, couleur=AJOUT, epaisseur=2.2)
f.fonction(lambda s: delta(s, 1.0), 70, 130, n=300, couleur=ACCENT, epaisseur=2.6)
f.point(100, delta(100, 1.0), couleur=ENCRE)
f.texte(100, delta(100, 1.0), "δ = 0,618, γ ≈ 0,019", couleur=ENCRE, ancre="end", dx=-8, dy=-8,
        taille=11.5, fond=True)
f.texte(120, delta(120, 1.0), "un an", couleur=ACCENT, dx=4, dy=18, gras=True, fond=True)
f.texte(106, delta(106, 1 / 12), "un mois", couleur=AJOUT, dx=8, dy=4, gras=True, fond=True)

sys.stdout.write(f.svg())
