#!/usr/bin/env python3
r"""
echelonnement-de-la-variance.svg — l'écart type grandit comme la racine du temps.

L'exemple de la fiche : 20 % de volatilité annuelle. Le cône plein est $\pm20\,\%\sqrt t$ ;
à trois mois il vaut $\pm10\,\%$, la moitié de l'annuel et non le quart. Le cône pointillé
est la règle que la fiche interdit, $\pm20\,\%\,t$ : il sous-estime la dispersion à toute
date avant un an, et donnerait 5 % à trois mois.

Usage : python courses/fpp/figures/echelonnement-de-la-variance.py > echelonnement-de-la-variance.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

SIG = 20.0

f = Figure(xmin=0, xmax=1.12, ymin=-24, ymax=24, w=560, h=330,
           titre="À trois mois, 10 % et non 5 % : la racine du temps, pas le temps")
f.axes(xlab="horizon, en années", ylab="écart type, en %", xticks=(0.25, 0.5, 1),
       yticks=(-20, -10, 5, 10, 20), fmt=lambda t: {0.25: "¼", 0.5: "½", 1: "1"}[t],
       fmt_y=lambda t: "%+d" % t, croix=(0, 0))

ts = [k / 200 for k in range(201)]
cone = [(t, SIG * math.sqrt(t)) for t in ts] + [(t, -SIG * math.sqrt(t)) for t in reversed(ts)]
f._add('<path d="M%s Z" fill="%s" fill-opacity="0.18" stroke="none"/>'
       % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in cone), ACCENT))
for s in (1, -1):
    f.fonction(lambda t: s * SIG * math.sqrt(t), 0, 1, n=200, couleur=ACCENT, epaisseur=2.4)
    f.fonction(lambda t: s * SIG * t, 0, 1, couleur=DOUX, epaisseur=1.6, pointilles="6 4")
f.segment(0.25, -10, 0.25, 10)
f.point(0.25, 10, couleur=ACCENT)
f.point(0.25, 5, couleur=DOUX)
f.texte(0.25, 10, "σ√t : 10 %", couleur=ACCENT, ancre="end", dx=-8, dy=-6, gras=True, fond=True)
f.texte(0.25, 5, "σt : 5 %", couleur=DOUX, dx=8, dy=12, gras=True, fond=True)
f.texte(1, 20, "±20 % à un an", couleur=ENCRE, ancre="end", dy=-8, taille=11.5, fond=True)

sys.stdout.write(f.svg())
