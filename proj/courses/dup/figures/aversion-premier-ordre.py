#!/usr/bin/env python3
r"""
aversion-premier-ordre.svg — une prime qui ne s'évanouit pas quand le pari rétrécit.

La fiche définit le premier ordre **par contraste** : la prime est proportionnelle à
l'écart type, et non à son carré. La figure met les deux courbes sur le même repère et
laisse voir ce qui se passe près de zéro — la droite part avec une pente, la parabole
part à plat.

Les deux courbes viennent des seuls nombres de l'exemple minimal. Le coefficient du
premier ordre est calculé par la formule de la fiche avec $\lambda=2$ et $\gamma=0$,
d'où $k=1/3$. La courbe du second ordre est la parabole qui passe par le seul point que
la fiche en donne, $0{,}5$ pour $\sigma=10$ : la fiche ne fournit pas le coefficient
d'aversion absolue, et le prendre ailleurs ferait dire à la figure plus que sa page.

Usage : python courses/dup/figures/aversion-premier-ordre.py > aversion-premier-ordre.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

LAMBDA, GAMMA = 2.0, 0.0
K = (LAMBDA ** (1.0 / (1.0 - GAMMA)) - 1.0) / (LAMBDA ** (1.0 / (1.0 - GAMMA)) + 1.0)

SIGMA = 10.0                       # le pari de l'exemple : plus ou moins 10
SECOND_EN_SIGMA = 0.5              # la prime du second ordre pour ce pari

premier = lambda s: K * s
second = lambda s: SECOND_EN_SIGMA * (s / SIGMA) ** 2

S_MAX = 13.5

f = Figure(xmin=0, xmax=14.6, ymin=0, ymax=5.0, w=560, h=330,
           titre="Au premier ordre la prime part avec une pente ; au second elle part à plat")

f.axes(xlab="taille du pari, σ", ylab="prime",
       xticks=(0, 5, 10), yticks=(second(SIGMA), premier(SIGMA)),
       fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%.2f" % t).rstrip("0").rstrip(".").replace(".", ","))

f.segment(SIGMA, 0, SIGMA, premier(SIGMA))
f.segment(0, premier(SIGMA), SIGMA, premier(SIGMA))
f.segment(0, second(SIGMA), SIGMA, second(SIGMA))

f.fonction(second, 0, S_MAX, couleur=DOUX, epaisseur=2.2)
f.fonction(premier, 0, S_MAX, couleur=ACCENT, epaisseur=2.6)

f.point(SIGMA, premier(SIGMA), couleur=ACCENT)
f.point(SIGMA, second(SIGMA), couleur=DOUX, r=3.2)

f.texte(S_MAX, premier(S_MAX), "premier ordre : kσ, avec k = 1/3", couleur=ACCENT,
        ancre="end", dx=-2, dy=-10, gras=True)
f.texte(6.0, 1.0, "second ordre : proportionnelle à σ²",
        couleur=DOUX, dy=0, gras=True, fond=True)
f.texte(SIGMA, 2.2, "le pari de ±10", couleur=ENCRE, dx=8, dy=0, taille=11.5, fond=True)

sys.stdout.write(f.svg())
