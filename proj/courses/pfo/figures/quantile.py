#!/usr/bin/env python3
r"""
quantile.svg — lire un quantile sur la fonction de répartition : le connu, puis le trou.

L'exemple de la fiche : des rendements normaux de moyenne 0,05 % et d'écart type 2 %. On
connaît la probabilité, 5 % ; on cherche le niveau. Le quantile d'ordre 5 % se lit en
partant de 0,05 sur l'axe vertical, jusqu'à la courbe, puis en descendant sur l'axe des
rendements : $-3{,}24\,\%$, soit $0{,}05\,\%-1{,}6449\times2\,\%$.

À l'échelle de la courbe entière, 0,05 est au ras de l'axe et la descente fait quelques
pixels : le cadre ne montre donc que le bas de la fonction de répartition, de 0 à 0,25,
où le trajet se voit. La courbe s'arrête là où elle sort du cadre.

Les étiquettes s'ancrent aux axes et au point : « connu » part de l'axe vertical à la
hauteur 0,05, « cherché » part du pied de la flèche, sous la courbe, où le cadre est vide.

Usage : python courses/pfo/figures/quantile.py > quantile.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

LOI = NormalDist(0.05, 2.0)
ALPHA = 0.05
Q = LOI.inv_cdf(ALPHA)                       # -3,24
YMAX = 0.25
XMIN, XFIN = -8.0, LOI.inv_cdf(YMAX)         # la courbe sort du cadre en haut, vers -1,30
fr = lambda t, d: ("%.*f" % (d, t)).replace(".", ",").replace("-", "−")

f = Figure(xmin=XMIN, xmax=-0.6, ymin=0, ymax=YMAX, w=560, h=320, marges=(54, 22, 40, 18),
           titre="Le quantile d'ordre 5 % laisse 5 % des rendements à sa gauche")
f.axes(xlab="rendement, en %", ylab="F", xticks=(-8, -6, Q, -2),
       yticks=(ALPHA, 0.1, 0.15, 0.2, 0.25),
       fmt=lambda t: fr(t, 2) if abs(t - Q) < 1e-9 else fr(t, 0),
       fmt_y=lambda t: fr(t, 2), croix=(XMIN, 0))

f.fonction(LOI.cdf, XMIN, XFIN, n=300, couleur=ACCENT, epaisseur=2.6)
f.fleche(XMIN, ALPHA, Q - 0.06, ALPHA, couleur=AJOUT, epaisseur=1.8)
f.fleche(Q, ALPHA - 0.002, Q, 0.0015, couleur=AJOUT, epaisseur=1.8)
f.point(Q, ALPHA, couleur=AJOUT)
f.texte(XMIN, ALPHA, "connu : 5 %", couleur=AJOUT, dx=8, dy=-8, gras=True)
# Les deux étiquettes du point sont à droite de la flèche qui descend, sous la courbe, où
# le cadre est vide. Après un indice, l'espace est insécable : le rendu mangeait l'autre.
f.texte(Q, ALPHA, "F(q_{α}) = 0,05", couleur=ENCRE, dx=10, dy=18)
f.texte(Q, 0, "cherché : q_{α}\u00a0= " + fr(Q, 2) + " %", couleur=AJOUT, dx=10, dy=-8, gras=True)

sys.stdout.write(f.svg())
