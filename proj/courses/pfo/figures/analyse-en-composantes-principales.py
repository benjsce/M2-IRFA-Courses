#!/usr/bin/env python3
r"""
analyse-en-composantes-principales.svg — les vecteurs propres de Σ sont les axes du nuage.

Ce que la figure doit faire voir : le nuage des rendements de deux actifs corrélés est une
ellipse penchée. La matrice de covariance n'étire certaines directions que sans les
tourner : ce sont ses vecteurs propres V_k, les axes de l'ellipse, et l'étirement est la
valeur propre λ_k. Une direction quelconque u, elle, ressort tournée : Σu ne lui est plus
parallèle. Le long axe porte λ_1/(λ_1 + λ_2) de la variance totale.

Le monde du chapitre 2 (fiche pfo/matrice-de-covariance) : volatilités journalières 1 %
et 2 %, corrélation 0,5, annualisées par 252 :
Σ = [[0,0252 ; 0,0252], [0,0252 ; 0,1008]]. Valeurs propres 0,1084 et 0,0176 ;
V_1 = (0,29 ; 0,96), V_2 = (0,96 ; −0,29) ; part de V_1 : 86 %. L'ellipse dessinée est
celle d'un écart type : demi-axes √λ_1 = 32,9 % et √λ_2 = 13,3 %. Pour la direction
u = (−1 ; 0), Σu = (−0,0252 ; −0,0252), à 45° : la matrice l'a tournée.

Usage : python courses/pfo/figures/analyse-en-composantes-principales.py > analyse-en-composantes-principales.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

s1, s2, rho = 0.01, 0.02, 0.5
S = [[252 * s1 * s1, 252 * rho * s1 * s2], [252 * rho * s1 * s2, 252 * s2 * s2]]
a, c, d = S[0][0], S[0][1], S[1][1]
disc = math.sqrt((a - d) ** 2 + 4 * c * c)
l1, l2 = (a + d + disc) / 2, (a + d - disc) / 2
v1 = (c, l1 - a)
n1 = math.hypot(*v1)
v1 = (v1[0] / n1, v1[1] / n1)
v2 = (v1[1], -v1[0])
for lam, v in ((l1, v1), (l2, v2)):                       # Σ V = λ V
    Sv = (a * v[0] + c * v[1], c * v[0] + d * v[1])
    assert abs(Sv[0] - lam * v[0]) < 1e-12 and abs(Sv[1] - lam * v[1]) < 1e-12
assert abs(l1 - 0.10843) < 1e-5 and abs(l2 - 0.01757) < 1e-5
assert abs(v1[0] - 0.2898) < 1e-4 and abs(v1[1] - 0.9571) < 1e-4
part = l1 / (l1 + l2)
assert abs(part - 0.8606) < 1e-4

fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")
P = 100                                                    # en % de rendement annuel
f = Figure(xmin=-42, xmax=42, ymin=-38, ymax=38, w=520, h=530, marges=(44, 30, 70, 14),
           titre="Σ étire ses vecteurs propres sans les tourner : ce sont les axes du nuage")
f.axes(xlab="rendement de l'actif 1, %", ylab="rendement de l'actif 2, %",
       xticks=(-30, 0, 30), yticks=(-30, 0, 30), fmt=lambda t: fr(t, 0), croix=(0, 0))

r1, r2 = math.sqrt(l1) * P, math.sqrt(l2) * P
pts = []
for k in range(181):
    th = 2 * math.pi * k / 180
    pts.append((r1 * math.cos(th) * v1[0] + r2 * math.sin(th) * v2[0],
                r1 * math.cos(th) * v1[1] + r2 * math.sin(th) * v2[1]))
f.courbe(pts, couleur=DOUX, epaisseur=1.4)

f.fleche(0, 0, r1 * v1[0], r1 * v1[1], couleur=ACCENT, epaisseur=2.4)
f.texte(r1 * v1[0], r1 * v1[1], "V_{1} = (" + fr(v1[0]) + " ; " + fr(v1[1]) + ")",
        couleur=ACCENT, dx=8, dy=4, gras=True, fond=True)
f.texte(r1 * v1[0], r1 * v1[1], "λ_{1} = " + fr(l1, 4) + " : " + fr(100 * part, 0)
        + " % de la variance", couleur=ACCENT, dx=8, dy=20, taille=11.5, fond=True)
f.fleche(0, 0, r2 * v2[0], r2 * v2[1], couleur=AJOUT, epaisseur=2.2)
f.texte(r2 * v2[0], r2 * v2[1], "V_{2},  λ_{2} = " + fr(l2, 4), couleur=AJOUT, dx=-4, dy=-10,
        gras=True, fond=True)

# une direction quelconque, u = (−1 ; 0), et son image Σu, tournée de 45°
L = 22
Su = (a, c)
nu = math.hypot(*Su)
f.fleche(0, 0, -L, 0, couleur=DOUX, epaisseur=1.6, pointilles="4 3")
f.texte(-L, 0, "u", couleur=DOUX, ancre="end", dx=-4, dy=16, gras=True)
f.fleche(0, 0, -L * Su[0] / nu, -L * Su[1] / nu, couleur=DOUX, epaisseur=1.6)
f.texte(-L * Su[0] / nu, -L * Su[1] / nu, "Σu : tournée", couleur=DOUX, ancre="end",
        dx=-6, dy=4, taille=11.5)

f.texte(0, -38, "Σ V_{k} = λ_{k} V_{k}  ·  part de V_{k} : λ_{k} / Σ_{j} λ_{j}",
        couleur=ENCRE, ancre="middle", taille=14, gras=True, dy=56)

sys.stdout.write(f.svg())
