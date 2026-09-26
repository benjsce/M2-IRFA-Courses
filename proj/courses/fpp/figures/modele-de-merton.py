#!/usr/bin/env python3
r"""
modele-de-merton.svg — la valeur finale de la firme, partagée entre créanciers et actionnaires.

La fiche : la firme vaut $S_T$ à l'échéance, la dette zéro-coupon a pour notionnel $D$.
Les créanciers reçoivent $D$, ou toute la firme si $S_T<D$ ; les actionnaires reçoivent le
reste, $(S_T-D)^+$. En abscisse $S_T$, en ordonnée ce que reçoit chacun : la bande du bas
est la dette, celle du haut les fonds propres, et leur somme est la diagonale $S_T$ — le
bilan. Au-dessus de $D$ la dette est plate et les fonds propres ont le payoff d'un call de
strike $D$ ; en dessous, la faillite. $D=80$, pour une firme de valeur forward 100 comme
dans l'exemple.

Ce qu'on cherche se voit en haut à gauche : le triangle entre la dette promise $D$ (le
pointillé) et ce que la dette reçoit vraiment sous $D$. C'est ce que les créanciers
perdent en cas de faillite, $(D-S_T)^+$, le payoff d'un put de strike $D$ : la dette
risquée est la dette sans risque moins ce put, et son prix est le spread.

Usage : python courses/fpp/figures/modele-de-merton.py > modele-de-merton.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

D, SMAX = 80.0, 160.0


def poly(pts, coul, op):
    return ('<path d="M%s Z" fill="%s" fill-opacity="%s" stroke="none"/>'
            % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in pts), coul, op))


f = Figure(xmin=0, xmax=SMAX + 4, ymin=0, ymax=SMAX + 8, w=480, h=400, marges=(54, 16, 40, 18),
           titre="Les fonds propres ont le payoff d'un call ; la dette perd sous D le payoff d'un put")
f.axes(xlab="valeur de la firme en T", ylab="ce que reçoit chacun", xticks=(0, D, SMAX),
       yticks=(D, SMAX), fmt=lambda t: "D" if t == D else "%d" % t,
       fmt_y=lambda t: "D" if t == D else "%d" % t)

f._add(poly([(0, 0), (D, D), (SMAX, D), (SMAX, 0)], DOUX, 0.35))
f._add(poly([(D, D), (SMAX, SMAX), (SMAX, D)], ACCENT, 0.45))
f._add(poly([(0, 0), (0, D), (D, D)], AJOUT, 0.22))           # le trou : le put vendu
f.segment(0, D, D, D, couleur=AJOUT, epaisseur=1.6, pointilles="6 4")
f.courbe([(0, 0), (SMAX, SMAX)], couleur=ENCRE, epaisseur=1.6)
f.courbe([(0, 0), (D, D), (SMAX, D)], couleur=DOUX, epaisseur=2.2)
f.segment(D, 0, D, D)
f.texte(125, 40, "dette : min(S_{T}, D)", couleur=ENCRE, ancre="middle", gras=True)
f.texte(138, 106, "fonds propres", couleur=ENCRE, ancre="middle", gras=True)
f.texte(138, 106, "(S_{T} − D)^{+}", couleur=ENCRE, ancre="middle", dy=16)
f.texte(40, 14, "faillite", couleur=ENCRE, ancre="middle", gras=True)
f.texte(40, 14, "la dette prend tout", couleur=ENCRE, ancre="middle", dy=15, taille=11)
f.texte(4, D, "dette promise D, sans risque", couleur=AJOUT, taille=11.5, dy=-7)
f.texte(24, 58, "ce que la dette perd", couleur=AJOUT, ancre="middle", gras=True, taille=12)
f.texte(24, 58, "sous D : le put vendu", couleur=AJOUT, ancre="middle", taille=11.5, dy=15)
f.texte(24, 58, "(D − S_{T})^{+}", couleur=AJOUT, ancre="middle", taille=11.5, dy=30)
f.texte(SMAX, SMAX, "S_{T} : la firme", couleur=ENCRE, ancre="end", dx=-10, dy=0, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
