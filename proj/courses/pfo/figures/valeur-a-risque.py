#!/usr/bin/env python3
r"""
valeur-a-risque.svg — du quantile des rendements au montant de la VaR.

Ce que la figure doit faire voir : la VaR est le bord des 5 % pires jours, lu une première
fois comme un rendement négatif, puis une seconde fois, sur un axe retourné, comme une
perte positive en euros. C'est le pas où l'on bute : le changement de signe et la
multiplication par le capital.

Les mille rendements sont ceux de l'exemple de la fiche, une loi normale de moyenne
0,05 % et d'écart type 2 %, placés à leurs positions attendues : le i-ème plus petit au
quantile d'ordre (i − 0,5)/1000. Un trait par jour ; les cinquante premiers, 5 % des
jours, sont en couleur, et leur bord est le quantile à 5 %, −3,24 %. L'axe du bas porte
la perte $L=-\text{rendement}\times1\,000\,000$ : il croît vers la gauche, et le même bord y vaut la
VaR, 32 397.

Les étiquettes s'ancrent au trait du quantile : celle des pires jours finit à sa gauche,
celle de la VaR est centrée sous lui.

Usage : python courses/pfo/figures/valeur-a-risque.py > valeur-a-risque.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n, _echap      # noqa: E402

LOI = NormalDist(0.05, 2.0)                  # rendements journaliers, en %
N, ALPHA, CAPITAL = 1000, 0.05, 1_000_000
R = [LOI.inv_cdf((i - 0.5) / N) for i in range(1, N + 1)]
Q = LOI.inv_cdf(ALPHA)                       # -3,24 %
VAR = -Q / 100 * CAPITAL                     # 32 397
PIRES = int(ALPHA * N)                       # 50
milliers = lambda v: ("{:,.0f}".format(v)).replace(",", " ").replace("-", "−")
pc = lambda t, d: ("%.*f" % (d, t)).replace(".", ",").replace("-", "−")

f = Figure(xmin=-7.6, xmax=7.6, ymin=0, ymax=4.1, w=560, h=270, marges=(14, 20, 12, 14),
           titre="La VaR est le bord des 5 % pires jours, lu en perte")
Y_R, Y_L = 1.95, 0.75                        # l'axe des rendements, celui des pertes
T0, T1 = 2.35, 3.15                          # la bande des mille jours


def traits(xs, couleur, opacite):
    d = "".join("M%s %s L%s %s" % (_n(f.px(x)), _n(f.py(T0)), _n(f.px(x)), _n(f.py(T1)))
                for x in xs)
    f._add('<path d="%s" stroke="%s" stroke-width="0.7" stroke-opacity="%s" fill="none"/>'
           % (d, couleur, _n(opacite)))


traits(R[PIRES:], DOUX, 0.35)
traits(R[:PIRES], AJOUT, 0.9)


def axe(y, valeurs, fmt, titre, vers_gauche=False):
    f.courbe([(-7.4, y), (7.4, y)], couleur=DOUX, epaisseur=1.2)
    if vers_gauche:
        f.fleche(-7.39, y, -7.4, y, couleur=DOUX, epaisseur=1.2)
    else:
        f.fleche(7.39, y, 7.4, y, couleur=DOUX, epaisseur=1.2)
    for x in valeurs:
        f.courbe([(x, y), (x, y - 0.07)], couleur=DOUX, epaisseur=1.2)
        f.texte(x, y, fmt(x), couleur=DOUX, ancre="middle", dy=17, taille=11.5)
    # Le titre de l'axe des rendements est au-dessus, à droite ; celui des pertes en dessous
    # de ses graduations, à gauche, pour ne pas croiser le trait du quantile.
    f.texte(-7.4 if vers_gauche else 7.4, y, titre, couleur=DOUX, ancre="start" if vers_gauche else "end",
            dy=35 if vers_gauche else -7, taille=11.5)


axe(Y_R, (-6, 0, 3, 6), lambda x: pc(x, 0), "rendement, en %")
axe(Y_L, (-6, 0, 3, 6), lambda x: milliers(-x / 100 * CAPITAL), "perte L = −rendement × 1 000 000",
    vers_gauche=True)

# Le bord des pires jours, prolongé d'un axe à l'autre.
f.segment(Q, Y_L, Q, T1 + 0.12, couleur=AJOUT, epaisseur=1.6, pointilles="4 3")
f.texte(Q, T1 + 0.12, "les %d pires jours" % PIRES, couleur=AJOUT, ancre="end", dx=-6,
        dy=-22, taille=11.5, gras=True)
f.texte(Q, T1 + 0.12, "sur %s : 5 %%" % milliers(N), couleur=AJOUT, ancre="end", dx=-6, dy=-7,
        taille=11.5, gras=True)
f.texte(Q, Y_R, "quantile à 5 % : " + pc(Q, 2) + " %", couleur=AJOUT, ancre="middle", dy=17, taille=11.5,
        gras=True, fond=True)
f.texte(Q, Y_L, "VaR = " + milliers(VAR), couleur=AJOUT, ancre="middle", dy=17, taille=12,
        gras=True, fond=True)

sys.stdout.write(f.svg())
