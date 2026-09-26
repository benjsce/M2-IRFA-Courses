#!/usr/bin/env python3
r"""
demande-sous-ambiguite.svg — la demande de l'investisseur ambigu, plate sur tout un intervalle.

L'exemple de la fiche : $v_{\min}=105$, $v_{\max}=115$, $\sigma_{\max}=20$. Au-dessous de
105 il achète $(105-p)/400$, au-dessus de 115 il vend, $(115-p)/400$ étant négatif ; entre
les deux sa demande est nulle. Au prix 100 il achète $5/400=0{,}0125$.

Usage : python courses/dup/figures/demande-sous-ambiguite.py > demande-sous-ambiguite.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

VMIN, VMAX, SMAX = 105.0, 115.0, 20.0


def demande(p):
    if p < VMIN:
        return (VMIN - p) / SMAX ** 2
    if p > VMAX:
        return (VMAX - p) / SMAX ** 2
    return 0.0


P0, P1 = 92.0, 128.0
f = Figure(xmin=P0, xmax=P1, ymin=-0.036, ymax=0.036, w=560, h=330,
           titre="Entre 105 et 115, l'investisseur ambigu ne détient rien")
f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.10"/>'
       % (_n(f.px(VMIN)), _n(f.py(0.036)), _n(f.px(VMAX) - f.px(VMIN)),
          _n(f.py(-0.036) - f.py(0.036)), DOUX))
f.axes(xlab="prix p", ylab="demande", xticks=(100, 105, 115, 125),
       yticks=(-0.025, 0.0125, 0.025), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(P0, 0))

f.courbe([(p / 4.0, demande(p / 4.0)) for p in range(int(P0 * 4), int(P1 * 4) + 1)],
         couleur=ACCENT, epaisseur=2.6)

f.segment(100, 0, 100, demande(100))
f.segment(P0, demande(100), 100, demande(100))
f.point(100, demande(100), couleur=ENCRE)
f.texte(100, demande(100), "prix 100 : achète 0,0125", couleur=ENCRE, dx=8, dy=-6,
        taille=11.5, fond=True)
f.texte(110, 0.024, "abstention", couleur=ENCRE, ancre="middle", gras=True, fond=True)
f.texte(96, 0.024, "achète", couleur=ACCENT, ancre="middle", dy=16, taille=11.5, fond=True)
f.texte(124, -0.02, "vend", couleur=ACCENT, ancre="middle", dy=-12, taille=11.5, fond=True)

sys.stdout.write(f.svg())
