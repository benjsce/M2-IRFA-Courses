#!/usr/bin/env python3
r"""
produit-a-capital-protege.svg — la mise coupée en deux : un zéro-coupon, des calls.

Ce que la figure doit faire voir : ce qui est connu (la mise, 100 ; le prix du
zéro-coupon, 0,9608 ; le prix du call, 9,93) et le trou, le nombre de calls qu'on peut
s'offrir. Deux lignes, une par brique, sur le même axe du temps. En haut, 96,08 placés en
zéro-coupon rendent la mise, 100, en T. En bas, le solde, 3,92, achète des calls à 9,93
l'unité : k = 3,92 / 9,93 = 0,395 call, soit 39,5 % de la hausse au-delà de 100. La
hausse est en pointillé : elle est aléatoire, et peut être nulle.

Usage : python courses/fpp/figures/produit-a-capital-protege.py > produit-a-capital-protege.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

MISE, P1 = 100.0, 0.9608                   # la mise, et le zéro-coupon à un an
S, K, R, SIG = 100.0, 100.0, 0.04, 0.20
N = NormalDist()
d1 = (math.log(S / K) + R + SIG ** 2 / 2) / SIG
CALL = S * N.cdf(d1) - K * math.exp(-R) * N.cdf(d1 - SIG)      # 9,93
ZC = MISE * P1                             # 96,08
SOLDE = MISE - ZC                          # 3,92
k = SOLDE / CALL                           # 0,395
v = lambda x, d=2: ("%.*f" % (d, x)).replace(".", ",")

t, T = 3.0, 7.6
g = Figure(xmin=0, xmax=10.6, ymin=-4.6, ymax=4.6, w=680, h=350, marges=(8, 8, 8, 8),
           titre="Capital protégé : le zéro-coupon rend la mise, le solde achète 0,395 call")

for y0, nom, coul in ((1.9, "zéro-coupon", ACCENT), (-2.4, "calls", AJOUT)):
    g.axe_temps(y0, 1.3, 9.9, [(t, "t"), (T, "T")])
    g.texte(0.05, y0 + 0.15, nom, taille=12, gras=True, couleur=coul)

# zéro-coupon : 96,08 payés, 100 reçus — tout est connu
g.fleche(t, 1.1, t, -0.1, couleur=ACCENT, epaisseur=2)
g.texte(t, 0.6, "%s = 100 × %s" % (v(ZC), v(P1, 4)), couleur=ACCENT, gras=True,
        taille=13.5, dx=9)
g.texte(t, 0.0, "connu aujourd'hui", couleur=DOUX, taille=11.5, dx=9)
g.fleche(T, 2.35, T, 3.85, couleur=ACCENT, epaisseur=2)
g.texte(T, 3.0, "100 : la mise rendue", couleur=ACCENT, gras=True, taille=13.5, dx=9)

# calls : le solde payé, la hausse reçue — le trou est le nombre de calls
g.fleche(t, -3.2, t, -4.45, couleur=AJOUT, epaisseur=2)
g.texte(t, -3.6, "%s = 100 − %s : le solde" % (v(SOLDE), v(ZC)), couleur=AJOUT, gras=True,
        taille=13.5, dx=9)
g.texte(t, -4.25, "le trou : combien de calls à %s ?  k = %s / %s = %s"
        % (v(CALL), v(SOLDE), v(CALL), v(k, 3)), couleur=ENCRE, gras=True, taille=12.5, dx=9)
g.fleche(T, -1.95, T, -0.55, couleur=AJOUT, epaisseur=2, pointilles="5 4")
g.texte(T, -1.05, "%s × (S_{T} − 100)^{+}" % v(k, 3), couleur=AJOUT, gras=True,
        taille=13.5, dx=9)
g.texte(T, -1.65, "%s %% de la hausse, ou rien" % v(100 * k, 1), couleur=AJOUT,
        taille=12, dx=9)

sys.stdout.write(g.svg())
