#!/usr/bin/env python3
r"""
courbe-roc.svg — une courbe ROC d'AUC 0,75, entre le hasard et le parfait.

La fiche place deux repères : le classifieur aléatoire est la diagonale, le classifieur
parfait le coin supérieur gauche. La courbe dessinée a l'AUC de l'exemple, 0,75, soit un
GINI de 0,50 ; sa forme est celle de deux scores gaussiens de même écart type, choisie
pour le dessin, et l'aire grisée sous elle est l'AUC.

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
f.texte(0.7, 0.7, "hasard : AUC ½, GINI 0", couleur=DOUX, dx=8, dy=14, taille=11.5, fond=True)
f.texte(0.55, 0.35, "AUC 0,75", couleur=ACCENT, ancre="middle", gras=True)
f.texte(0.55, 0.35, "GINI 2 × 0,75 − 1 = 0,50", couleur=ACCENT, ancre="middle", dy=16, taille=11.5)

sys.stdout.write(f.svg())
