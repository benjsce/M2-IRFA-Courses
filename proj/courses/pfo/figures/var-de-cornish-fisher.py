#!/usr/bin/env python3
r"""
var-de-cornish-fisher.svg — les quantiles de la queue, gaussiens et corrigés.

Les paramètres de l'exemple de la fiche : $\mu=0{,}05\,\%$, $\sigma=2\,\%$, asymétrie
$-0{,}5$, excès de kurtosis 3. Chaque courbe donne le quantile $q_u$ pour $u$ de 0,0001 à
0,05, la grille du listing. La VaR se lit au bout, en $u=0{,}05$ : $-3{,}24\,\%$ contre
$-3{,}39\,\%$, presque rien. La CVaR est la moyenne de toute la courbe sur la grille, et
c'est dans l'extrême queue, à gauche, que la correction écarte les deux courbes : la
moyenne passe de $-4{,}08\,\%$ à $-5{,}35\,\%$. D'où les 40 754 et 53 511 de la fiche, pour
un capital de 1 000 000. Pourquoi l'extrême queue : au-delà de √3 ≈ 1,73 écart type
(u < 4,2 %), le terme de kurtosis change de signe et pousse vers les pertes.

Les étiquettes des deux moyennes sont posées chacune du côté libre de sa ligne : la
gaussienne au-dessus, à gauche, où les courbes sont plus bas ; la corrigée au-dessous, à
droite, où elles sont plus haut.

La moyenne gaussienne est la formule fermée de la fiche ; la moyenne corrigée est
l'intégrale par trapèzes du listing, sur 1 000 points.

Usage : python courses/pfo/figures/var-de-cornish-fisher.py > var-de-cornish-fisher.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

N = NormalDist()
MU, SIG, S, K, ALPHA = 0.05, 2.0, -0.5, 3.0, 0.05


def z_cf(u):
    z = N.inv_cdf(u)
    return (z + S / 6 * (z * z - 1) + K / 24 * (z ** 3 - 3 * z)
            - S * S / 36 * (2 * z ** 3 - 5 * z))


q_g = lambda u: MU + SIG * N.inv_cdf(u)
q_c = lambda u: MU + SIG * z_cf(u)
U = [0.0001 + (ALPHA - 0.0001) * i / 999 for i in range(1000)]
QC = [q_c(u) for u in U]
CVAR_C = sum((QC[i] + QC[i + 1]) / 2 * (U[i + 1] - U[i]) for i in range(999)) / ALPHA
za = N.inv_cdf(ALPHA)
CVAR_G = MU - SIG * N.pdf(za) / ALPHA
fr = lambda v: ("%.2f" % v).replace(".", ",").replace("-", "−")

f = Figure(xmin=0, xmax=0.053, ymin=-20, ymax=0, w=560, h=340,
           titre="La VaR ne bouge presque pas ; la CVaR, moyenne de toute la queue, beaucoup")
f.axes(xlab="probabilité u", ylab="quantile q(u), en %", xticks=(0.0001, 0.01, 0.02, 0.03, 0.04, 0.05),
       yticks=(-15, -10, -5), fmt=lambda t: ("%g" % t).replace(".", ","),
       fmt_y=lambda t: "%d" % t, croix=(0, -20))

f.courbe(list(zip(U, [q_g(u) for u in U])), couleur=DOUX, epaisseur=2.2)
f.courbe(list(zip(U, QC)), couleur=ACCENT, epaisseur=2.6)
f.segment(0, CVAR_G, ALPHA, CVAR_G, couleur=DOUX, epaisseur=1.4)
f.segment(0, CVAR_C, ALPHA, CVAR_C, couleur=ACCENT, epaisseur=1.4)
f.texte(0.0012, CVAR_G, "moyenne gaussienne " + fr(CVAR_G), couleur=DOUX, ancre="start",
        dy=-6, taille=11.5, fond=True)
f.texte(ALPHA, CVAR_C, "moyenne corrigée " + fr(CVAR_C), couleur=ACCENT, ancre="end",
        dy=16, taille=11.5, gras=True, fond=True)
f.point(ALPHA, q_g(ALPHA), couleur=DOUX)
f.point(ALPHA, q_c(ALPHA), couleur=ACCENT)
f.texte(ALPHA, q_g(ALPHA), "VaR : " + fr(q_g(ALPHA)) + " (gaussien), " + fr(q_c(ALPHA)) + " (corrigé)",
        couleur=ENCRE, ancre="end", dx=-8, dy=-8, taille=11.5, fond=True)
f.texte(0.004, q_c(0.004), "Cornish-Fisher", couleur=ACCENT, dx=8, dy=4, gras=True, fond=True)
f.texte(0.0003, q_g(0.0003), "gaussien", couleur=DOUX, dx=8, dy=4, gras=True, fond=True)

sys.stdout.write(f.svg())
