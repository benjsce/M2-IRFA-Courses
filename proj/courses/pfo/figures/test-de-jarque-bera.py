#!/usr/bin/env python3
r"""
test-de-jarque-bera.svg — les couples (asymétrie, excès de kurtosis) qui passent le test.

Pour $T=1000$ rendements, le test ne rejette pas au niveau de 5 % tant que
$JB=\tfrac{T}{6}\big(S^2+K_{\mathrm{ex}}^2/4\big)<5{,}99$ : c'est l'intérieur d'une ellipse
centrée sur la loi normale, $S=0$ et $K_{\mathrm{ex}}=0$, de demi-axes 0,19 en asymétrie et
0,38 en excès de kurtosis. Le point est l'exemple de la fiche, $S=-0{,}5$ et
$K_{\mathrm{ex}}=3$, où $JB=416{,}7$ : très loin dehors.

Usage : python courses/pfo/figures/test-de-jarque-bera.py > test-de-jarque-bera.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

T = 1000
SEUIL = -2 * math.log(0.05)                     # 5,99
R2 = 6 * SEUIL / T                              # S² + K²/4 = R2
AS, AK = math.sqrt(R2), 2 * math.sqrt(R2)       # 0,19 et 0,38
S0, K0 = -0.5, 3.0
JB = T / 6 * (S0 ** 2 + K0 ** 2 / 4)            # 416,7

f = Figure(xmin=-0.8, xmax=0.8, ymin=-0.8, ymax=3.5, w=480, h=380, marges=(54, 16, 40, 18),
           titre="Le test ne laisse passer qu'une petite ellipse autour de la loi normale")
f.axes(xlab="asymétrie S", ylab="excès de kurtosis", xticks=(-0.5, 0, 0.5), yticks=(1, 2, 3),
       fmt=lambda t: ("%g" % t).replace(".", ","), fmt_y=lambda t: "%d" % t, croix=(0, 0))

pts = [(AS * math.cos(2 * math.pi * k / 120), AK * math.sin(2 * math.pi * k / 120))
       for k in range(121)]
f._add('<path d="M%s Z" fill="%s" fill-opacity="0.25" stroke="none"/>'
       % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in pts), ACCENT))
f.courbe(pts, couleur=ACCENT, epaisseur=2.0)
f.texte(AS, 0, "JB < 5,99", couleur=ACCENT, dx=8, dy=-10, gras=True, fond=True)
f.point(0, 0, couleur=ENCRE)
f.texte(0, 0, "loi normale", couleur=ENCRE, dx=-10, dy=-8, ancre="end", taille=11.5, fond=True)
f.point(S0, K0, couleur=AJOUT, r=5)
f.texte(S0, K0, "l'exemple : JB = " + ("%.1f" % JB).replace(".", ","), couleur=AJOUT, dx=10,
        dy=4, gras=True, fond=True)
f.texte(0.78, 3.2, "T = 1 000", couleur=DOUX, ancre="end", taille=11.5)

sys.stdout.write(f.svg())
