#!/usr/bin/env python3
r"""
courbe-roc.svg — une courbe ROC d'AUC 0,75 : chaque seuil est un point, l'aire les résume tous.

Ce que la figure doit faire voir : le seuil, qu'on ne connaît pas, balaie la courbe. Trois
seuils y sont marqués ; chacun donne une matrice de confusion, donc un point (taux de faux
positifs, taux de vrais positifs), et baisser le seuil fait monter le long de la courbe.
La diagonale est le hasard, le coin supérieur gauche le classifieur parfait, et l'aire
grisée sous la courbe est l'AUC de l'exemple, 0,75, soit un GINI de 0,50. La forme de la
courbe, celle de deux scores gaussiens de même écart type, est choisie pour le dessin.

Usage : python courses/dss/figures/courbe-roc.py > courbe-roc.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, _n      # noqa: E402

N = NormalDist()
AUC = 0.75
D = math.sqrt(2) * N.inv_cdf(AUC)                  # écart des deux moyennes


def tpr(fpr):
    if fpr <= 0:
        return 0.0
    if fpr >= 1:
        return 1.0
    return 1 - N.cdf(N.inv_cdf(1 - fpr) - D)


pts = [(k / 400, tpr(k / 400)) for k in range(401)]
f = Figure(xmin=0, xmax=1.04, ymin=0, ymax=1.06, w=440, h=400, marges=(54, 16, 44, 18),
           titre="Entre la diagonale du hasard et le coin du parfait, l'aire sous la courbe")
f.axes(xlab="taux de faux positifs", ylab="taux de vrais positifs", xticks=(0, 0.5, 1),
       yticks=(0.5, 1), fmt=lambda t: {0: "0", 0.5: "½", 1: "1"}[t],
       fmt_y=lambda t: {0.5: "½", 1: "1"}[t])
f._add('<path d="M%s L%s %s Z" fill="%s" fill-opacity="0.22" stroke="none"/>'
       % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in pts),
          _n(f.px(1)), _n(f.py(0)), ACCENT))
f.courbe([(0, 0), (1, 1)], couleur=DOUX, epaisseur=1.4, pointilles="5 4")
f.courbe([(0, 0), (0, 1), (1, 1)], couleur=AJOUT, epaisseur=1.6, pointilles="2 4")
f.courbe(pts, couleur=ACCENT, epaisseur=2.6)
f.point(0, 1, couleur=AJOUT, r=5)
f.texte(0, 1, "parfait : AUC 1, GINI 1", couleur=AJOUT, dx=10, dy=16, taille=11.5, gras=True)
f.texte(0.99, 0.5, "hasard : AUC ½, GINI 0", couleur=DOUX, ancre="end", taille=11.5, fond=True)

# trois seuils sur l'échelle du score : négatifs centrés en 0, positifs en D
for seuil, nom, dx, dy in ((1.5, "seuil haut", 8, 5), (0.5, "seuil moyen", 8, 8),
                           (-0.5, "seuil bas", 4, 20)):
    x, y = 1 - N.cdf(seuil), 1 - N.cdf(seuil - D)
    f.point(x, y, couleur=ENCRE, r=4.2)
    f.texte(x, y, nom, dx=dx, dy=dy, taille=11.5, fond=True)

f.texte(0.45, 0.2, "AUC 0,75", couleur=ACCENT, ancre="middle", gras=True)
f.texte(0.45, 0.2, "GINI 2 × 0,75 − 1 = 0,50", couleur=ACCENT, ancre="middle", dy=16, taille=11.5)

sys.stdout.write(f.svg())
