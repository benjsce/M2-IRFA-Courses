#!/usr/bin/env python3
r"""
amelioration-de-rendement.svg — l'action seule, et l'action avec le call vendu.

Ce que la figure doit faire voir : l'échange. On reçoit un montant connu aujourd'hui, la
prime du call à la monnaie, 9,93 ; on cède un montant inconnu, toute la hausse au-delà de
100. Deux gains à l'échéance, pour une action achetée 100 : l'action seule, S_T − 100 ;
l'action avec le call vendu, prime comprise, min(S_T, 100) − 100 + 9,93. En dessous de
100, la seconde fait mieux de 9,93, la prime ; au-dessus, elle plafonne à 9,93, et
l'action seule la dépasse à partir de 109,93. Elle ne perd qu'en dessous de 90,07.

La prime est ajoutée sans ses intérêts, comme dans la fiche.

Usage : python courses/fpp/figures/amelioration-de-rendement.py > amelioration-de-rendement.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

S, K, R, SIG = 100.0, 100.0, 0.04, 0.20
N = NormalDist()
d1 = (math.log(S / K) + R + SIG ** 2 / 2) / SIG
PRIME = S * N.cdf(d1) - K * math.exp(-R) * N.cdf(d1 - SIG)      # 9,93
v = lambda x: ("%.2f" % x).replace(".", ",").replace("-", "−")

seule = lambda s: s - S
couverte = lambda s: min(s, K) - S + PRIME
X0, X1 = 70.0, 132.0

f = Figure(xmin=X0, xmax=X1 + 2, ymin=-31, ymax=34, w=600, h=360, marges=(46, 20, 44, 14),
           titre="Vendre le call : 9,93 de plus aujourd'hui, contre la hausse au-delà de 100")
f.axes(xlab="cours de l'action à l'échéance", ylab="gain",
       xticks=(80, 90.07, 100, 109.93, 120), yticks=(-20, -10, 0, 9.93, 20),
       croix=(X0, 0), fmt=lambda t: v(t) if t % 1 else "%d" % t,
       fmt_y=lambda t: v(t) if t % 1 else ("%d" % t).replace("-", "−"))

f.courbe([(X0, seule(X0)), (X1, seule(X1))], couleur=AJOUT, epaisseur=2.2)
f.courbe([(X0, couverte(X0)), (K, couverte(K)), (X1, couverte(X1))], couleur=ACCENT,
         epaisseur=2.8)
f.texte(128, seule(128), "l'action seule", couleur=AJOUT, gras=True, ancre="end", dx=-8, dy=-6)
f.texte(128, couverte(128), "l'action, call vendu", couleur=ACCENT, gras=True, ancre="end",
        dy=18)

# en dessous de 100 : la prime, connue aujourd'hui
f.mesure(80, seule(80), couverte(80), couleur=ENCRE)
f.texte(81, -27, "+%s : la prime, connue aujourd'hui" % v(PRIME), couleur=ENCRE, dx=4)
# au-dessus : la hausse cédée, inconnue
f.mesure(124, couverte(124), seule(124), couleur=ENCRE, etiquette="la hausse cédée", cote="left")

f.point(K - PRIME, 0, couleur=ACCENT, r=3.6)
f.point(K + PRIME, PRIME, couleur=ENCRE, r=3.6)
f.segment(K + PRIME, 0, K + PRIME, PRIME, couleur=DOUX, epaisseur=1, pointilles="3 3")
f.segment(X0, PRIME, K, PRIME, couleur=DOUX, epaisseur=1, pointilles="3 3")

sys.stdout.write(f.svg())
