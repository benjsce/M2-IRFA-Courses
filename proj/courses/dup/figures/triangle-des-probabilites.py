#!/usr/bin/env python3
r"""
triangle-des-probabilites.svg — les deux segments d’Allais, parallèles.

Trois résultats, deux degrés de liberté : une loterie est un point du triangle
$p_1+p_3\le1$, où $p_1$ est la probabilité du pire résultat et $p_3$ celle du meilleur
[L1 slide 44]. Sous utilité espérée les courbes d'indifférence y sont des droites
parallèles, et c'est ce parallélisme qui est l'indépendance.

Les quatre loteries d'Allais sont calculées ici à partir des paramètres que donne la
fiche — $x=2400$, $\alpha=0{,}34$, $P=\tfrac{33}{34}\delta_{2500}+\tfrac1{34}\delta_0$
[L2 slide 16] — plutôt que recopiées, pour que le lecteur du script voie d'où viennent
les quatre points.

La pente des droites d'indifférence vaut $u(2400)/(1-u(2400))$ avec $u(0)=0$ et
$u(2500)=1$ : le cours ne la fixe pas, et la figure n'en montre qu'une valeur possible.
Ce qui compte n'est pas la pente, c'est qu'elle soit la même partout. La légende le dit.

Usage : python courses/dup/figures/triangle-des-probabilites.py > triangle-des-probabilites.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

ALPHA = 0.34
P_HAUT, P_BAS = 33.0 / 34.0, 1.0 / 34.0      # la loterie P : 2500 ou 0

# (p du pire résultat 0, p du meilleur 2500) ; le reste de la masse est sur 2400.
A = (0.0, 0.0)                                                   # x avec certitude
B = (ALPHA * P_BAS, ALPHA * P_HAUT)                              # alpha P + (1-alpha) x
C = (1.0 - ALPHA, 0.0)                                           # alpha x + (1-alpha) 0
D = (ALPHA * P_BAS + 1.0 - ALPHA, ALPHA * P_HAUT)                # alpha P + (1-alpha) 0

PENTE = 1.0                      # une pente d'indifférence parmi d'autres

f = Figure(xmin=-0.06, xmax=1.10, ymin=-0.06, ymax=1.10, w=430, h=400,
           marges=(46, 18, 44, 92),
           titre="Les deux segments d’Allais sont parallèles, "
                 "et les droites d’indifférence aussi")

f.axes(xlab="p(0)", ylab="p(2500)", xticks=(0, 0.5, 1), yticks=(0.5, 1),
       fmt=lambda t: ("0" if t == 0 else "1" if t == 1 else "½"))

# le triangle : l'hypoténuse est p(0) + p(2500) = 1, où la masse sur 2400 s'annule
f.courbe([(0, 1), (0, 0), (1, 0)], couleur=DOUX, epaisseur=1.4)
f.courbe([(0, 1), (1, 0)], couleur=DOUX, epaisseur=1.4)

# quelques droites d'indifférence, toutes de même pente
for c in (-0.55, -0.25, 0.05, 0.35, 0.65):
    xs = [x / 100.0 for x in range(0, 101)]
    pts = [(x, PENTE * x + c) for x in xs if 0 <= PENTE * x + c <= 1 - x]
    if len(pts) > 1:
        f.courbe(pts, couleur=PALE, epaisseur=1.1, pointilles="4 4")

for (p, q), nom, cote in ((A, "A", "end"), (B, "B", "start"),
                          (C, "C", "end"), (D, "D", "start")):
    f.point(p, q, couleur=ENCRE, r=3.8)
    f.texte(p, q, nom, couleur=ENCRE, ancre=cote,
            dx=-9 if cote == "end" else 9, dy=5, gras=True)

f.courbe([A, B], couleur=ACCENT, epaisseur=2.6)
f.courbe([C, D], couleur=ACCENT, epaisseur=2.6)

f.texte(B[0], B[1], "A → B", couleur=ACCENT, dx=8, dy=-8, taille=11.5, gras=True)
f.texte(D[0], D[1], "C → D", couleur=ACCENT, dx=8, dy=-8, taille=11.5, gras=True)
f.texte(1.08, 0.80, "les droites d’indifférence", couleur=DOUX, ancre="end",
        dy=0, taille=11.5, fond=True)

sys.stdout.write(f.svg())
