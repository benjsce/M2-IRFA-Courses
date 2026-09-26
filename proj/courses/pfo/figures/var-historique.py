#!/usr/bin/env python3
r"""
var-historique.svg — trier, lire le 50e, moyenner les 50 premiers.

Ce que la figure doit faire voir : la méthode historique n'est qu'un tri. On range les
1 000 rendements du pire au meilleur ; le 5e centile tombe entre le 50e et le 51e, et
c'est la VaR ; les 50 premiers, moyennés, donnent la CVaR. Rien d'autre n'est supposé
de la loi.

L'échantillon est fictif : 1 000 tirages d'une loi de Student à 4 degrés de liberté,
graine 7, pour que la queue soit épaisse comme celle d'un vrai marché, puis déplacés et
dilatés pour que le 5e centile (interpolé comme `np.percentile`) vaille −3,2 % et la
moyenne des rendements qui lui sont inférieurs ou égaux −4,5 %, les chiffres de la
fiche. Seuls les 150 plus petits sont tracés.

Usage : python courses/pfo/figures/var-historique.py > var-historique.svg
Dépendance : aucune.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, PALE      # noqa: E402

rng = random.Random(7)
brut = []
for _ in range(1000):
    z = rng.gauss(0, 1)
    chi2 = sum(rng.gauss(0, 1) ** 2 for _ in range(4))
    brut.append(z / math.sqrt(chi2 / 4))
brut.sort()


def centile(x, p):
    """Le centile interpolé linéairement, comme np.percentile par défaut."""
    pos = p / 100 * (len(x) - 1)
    i = int(pos)
    return x[i] + (pos - i) * (x[i + 1] - x[i])


q0 = centile(brut, 5)
m0 = sum(v for v in brut if v <= q0) / sum(1 for v in brut if v <= q0)
b = (-3.2 + 4.5) / (q0 - m0)                  # dilatation, pour tomber sur les chiffres
a = -3.2 - b * q0
R = [a + b * v for v in brut]                 # en %, triés du pire au meilleur
Q = centile(R, 5)                             # −3,2
QUEUE = [v for v in R if v <= Q]
M = sum(QUEUE) / len(QUEUE)                   # −4,5
assert len(QUEUE) == 50 and abs(Q + 3.2) < 1e-9 and abs(M + 4.5) < 1e-9

NB = 150
bas = math.floor(R[0]) - 0.5
fr = lambda v: ("%.1f" % v).replace(".", ",").replace("-", "−")
f = Figure(xmin=0, xmax=NB + 1, ymin=bas, ymax=0.2, w=560, h=330, marges=(54, 16, 40, 18),
           titre="Trier les rendements : le 50e donne la VaR, la moyenne des 50 premiers la CVaR")
f.axes(xlab="rang, du pire rendement au meilleur", ylab="rendement, en %",
       xticks=(1, 50, 100, 150), yticks=[k for k in range(-2, int(bas) - 1, -2)],
       fmt=lambda t: "%d" % t, fmt_y=lambda t: ("%d" % t).replace("-", "−"),
       croix=(0, bas))
for k in range(NB):
    f.barre(k + 1, R[k], 0.62, couleur=ACCENT if k < 50 else PALE,
            opacite=0.85 if k < 50 else 1.0, y0=0)

f.segment(0, Q, NB + 1, Q, couleur=ENCRE, epaisseur=1.4, pointilles="5 4")
f.segment(0.5, M, 50.5, M, couleur=ACCENT, epaisseur=2.2, pointilles=None)
f.texte(NB + 1, Q, "5e centile " + fr(Q) + " % : VaR 32 000", couleur=ENCRE, ancre="end",
        dy=16, taille=11.5, gras=True, fond=True)
f.texte(50.5, M, "moyenne des 50 : " + fr(M) + " % : CVaR 45 000", couleur=ACCENT,
        ancre="start", dx=8, dy=4, taille=11.5, gras=True, fond=True)

sys.stdout.write(f.svg())
