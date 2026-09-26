#!/usr/bin/env python3
r"""
equilibre-sous-ambiguite.svg — la demande agrégée rencontre l'offre à 106.

L'exemple de la fiche : $\hat v=110$, $\hat\sigma=20$, une offre de 0,005 par
investisseur, la moitié d'investisseurs ambigus dont la moyenne est connue dans
$[105;115]$. La demande agrégée est la moyenne des deux demandes, et elle garde les deux
coudes de la demande ambiguë. Entre 105 et 115 les ambigus ne détiennent rien, et seule
la demande de ceux qui connaissent la loi, $(110-p)/400$ divisée par deux, rencontre
l'offre : $\hat p=110-400\times0{,}005/0{,}5=106$.

L'écart type retenu par les ambigus hors de l'intervalle est pris égal à $\hat\sigma$ ; le
dessin n'en dépend qu'au-dehors de l'intervalle.

Usage : python courses/dup/figures/equilibre-sous-ambiguite.py > equilibre-sous-ambiguite.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

V, S, OFFRE, LAMBDA = 110.0, 20.0, 0.005, 0.5
VMIN, VMAX = 105.0, 115.0


def x_r(p):
    return (V - p) / S ** 2


def x_a(p):
    if p < VMIN:
        return (VMIN - p) / S ** 2
    if p > VMAX:
        return (VMAX - p) / S ** 2
    return 0.0


def agregee(p):
    return (1 - LAMBDA) * x_r(p) + LAMBDA * x_a(p)


P_HAT = V - S ** 2 * OFFRE / (1 - LAMBDA)          # 106

P0, P1 = 96.0, 124.0
f = Figure(xmin=P0, xmax=P1, ymin=-0.03, ymax=0.03, w=560, h=330,
           titre="L'offre coupe la demande agrégée à 106, dans l'intervalle d'abstention")
f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.10"/>'
       % (_n(f.px(VMIN)), _n(f.py(0.03)), _n(f.px(VMAX) - f.px(VMIN)),
          _n(f.py(-0.03) - f.py(0.03)), DOUX))
f.axes(xlab="prix p", ylab="demande par investisseur", xticks=(100, 105, 115, 120),
       yticks=(-0.02, 0.005, 0.02), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(P0, 0))

f.courbe([(P0, OFFRE), (P1, OFFRE)], couleur=AJOUT, epaisseur=2.0)
f.courbe([(p / 4.0, agregee(p / 4.0)) for p in range(int(P0 * 4), int(P1 * 4) + 1)],
         couleur=ACCENT, epaisseur=2.6)

f.segment(P_HAT, 0, P_HAT, OFFRE)
f.point(P_HAT, OFFRE, couleur=ENCRE)
f.texte(P_HAT, OFFRE, "prix d'équilibre 106", couleur=ENCRE, dx=8, dy=-8, gras=True, fond=True)
f.texte(123, OFFRE, "offre 0,005", couleur=AJOUT, ancre="end", dy=-8, taille=11.5, fond=True)
f.texte(110, -0.022, "les ambigus s'abstiennent", couleur=ENCRE, ancre="middle",
        taille=11.5, fond=True)
f.texte(99, agregee(99), "demande agrégée", couleur=ACCENT, dx=8, dy=-6, gras=True, fond=True)

sys.stdout.write(f.svg())
