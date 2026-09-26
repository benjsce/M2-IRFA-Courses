#!/usr/bin/env python3
r"""
valeur-intrinseque.svg — le payoff lu au forward, contre la moyenne des payoffs.

Ce que la figure doit faire voir : la valeur intrinsèque ne demande que le prix forward —
on lit le payoff en ce seul point —, alors que le prix demande toute la loi de $S_T$ —
on fait la moyenne des payoffs. Pour un payoff coudé comme le call, la corde passe
au-dessus du coude : la moyenne des payoffs dépasse le payoff de la moyenne.

Pour que la corde se voie, la loi de $S_T$ est réduite à deux états équiprobables,
choisis pour le dessin : ils ont pour moyenne le prix forward de l'exemple, 104,08, et
sont écartés juste assez pour que le call y vaille ce que donne la formule de Black et
Scholes, 9,925. Le payoff lu au forward vaut 4,08, soit 3,92 une fois actualisé : c'est
la valeur intrinsèque, qui ne dépend pas de cet écart.

Usage : python courses/fpp/figures/valeur-intrinseque.py > valeur-intrinseque.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

S0, K, R, SIG, T = 100.0, 100.0, 0.04, 0.20, 1.0
P = math.exp(-R * T)                                     # 0,9608
F = S0 / P                                               # 104,08
d1 = (math.log(S0 / K) + (R + SIG ** 2 / 2) * T) / (SIG * math.sqrt(T))
C = S0 * NormalDist().cdf(d1) - K * P * NormalDist().cdf(d1 - SIG * math.sqrt(T))   # 9,925
MOYG = C / P                                             # moyenne des payoffs, 10,33
A = 2 * MOYG - (F - K)                                   # demi-écart des deux états
BAS, HAUT = F - A, F + A                                 # 87,50 et 120,66
g = lambda s: max(s - K, 0.0)
v = lambda x: ("%.2f" % x).replace(".", ",").replace(",00", "")
v4 = lambda x: ("%.4f" % x).replace(".", ",")

f = Figure(xmin=78, xmax=132, ymin=-2.5, ymax=26, w=640, h=360, marges=(46, 34, 40, 14),
           titre="La valeur intrinsèque lit le payoff au forward ; le prix fait la moyenne des payoffs")
f.axes(xlab="sous-jacent en T", xticks=(BAS, K, F, HAUT), yticks=(g(F), MOYG, g(HAUT)), fmt=v, fmt_y=v,
       croix=(78, 0))

# le payoff du call
f.courbe([(78, 0), (K, 0), (K + 25, 25)], couleur=ENCRE, epaisseur=2)
f.texte(K + 22, 22, "payoff (S_{T}\u00a0− 100)^{+}", couleur=ENCRE, taille=12, ancre="end", dx=-10)

# la loi réduite à deux états, et la corde
f.courbe([(BAS, g(BAS)), (HAUT, g(HAUT))], couleur=AJOUT, epaisseur=1.6, pointilles="6 4")
for s in (BAS, HAUT):
    f.point(s, g(s), couleur=AJOUT)
    f.segment(s, 0, s, g(s), couleur=DOUX)
f.texte(BAS, 0, "½", couleur=AJOUT, taille=12, ancre="middle", dy=-8)
f.texte(HAUT, g(HAUT), "½", couleur=AJOUT, taille=12, ancre="start", dx=10, dy=16)

# au forward : le payoff de la moyenne, et la moyenne des payoffs
f.segment(F, 0, F, MOYG, couleur=DOUX)
f.point(F, g(F), couleur=ACCENT)
f.point(F, MOYG, couleur=AJOUT)
f.texte(F, g(F), "payoff au forward : %s" % v(g(F)), couleur=ACCENT, gras=True, taille=12.5,
        dx=10, dy=4, fond=True)
f.texte(F, g(F), "× %s = %s : la valeur intrinsèque" % (v4(P), v(P * g(F))), couleur=ACCENT,
        taille=11.5, dx=10, dy=20, fond=True)
f.texte(F, MOYG, "moyenne des payoffs : %s" % v(MOYG), couleur=AJOUT, gras=True, taille=12.5,
        ancre="end", dx=-10, dy=-2, fond=True)
f.texte(F, MOYG, "× %s = %s : le prix" % (v4(P), v(P * MOYG)), couleur=AJOUT, taille=11.5,
        ancre="end", dx=-10, dy=14, fond=True)
f.texte(F, -1.1, "forward", couleur=ACCENT, taille=11, ancre="middle", dy=30)

sys.stdout.write(f.svg())
