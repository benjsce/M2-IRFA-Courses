#!/usr/bin/env python3
r"""
modele-black-scholes.svg — la moyenne sous Q ne dépend pas de la volatilité.

L'exemple de la fiche : $S_0=100$, $r=4\,\%$, un an, et
$\mathbb{E}^{\mathbb{Q}}(S_t)=S_0e^{rt}$ quelle que soit $\sigma$. On trace, pour deux
volatilités, 20 % et 40 %, la bande où tombent 90 % des trajectoires à chaque date, entre
les quantiles 5 % et 95 % de la loi log-normale de la forme exponentielle. Les deux bandes
s'écartent très différemment ; la moyenne, elle, est la même courbe, qui arrive à 104,08.
Les deux volatilités sont choisies pour le dessin.

Usage : python courses/fpp/figures/modele-black-scholes.py > modele-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE, _n      # noqa: E402

S0, R = 100.0, 0.04
Z = NormalDist().inv_cdf(0.95)


def quantile(t, sig, z):
    return S0 * math.exp((R - sig * sig / 2) * t + z * sig * math.sqrt(t))


f = Figure(xmin=0, xmax=1.36, ymin=45, ymax=205, w=560, h=340,
           titre="Deux volatilités, deux bandes, une seule moyenne sous Q")
f.axes(xlab="temps, en années", ylab="S", xticks=(0, 0.5, 1), yticks=(60, 100, 150, 200),
       fmt=lambda t: {0: "0", 0.5: "½", 1: "1"}[t],
       fmt_y=lambda t: ("%.2f" % t).replace(".", ",") if t % 1 else "%d" % t)

ts = [k / 100 for k in range(101)]
for sig, coul, op in ((0.40, AJOUT, 0.16), (0.20, ACCENT, 0.28)):
    haut = [(t, quantile(t, sig, Z)) for t in ts]
    bas = [(t, quantile(t, sig, -Z)) for t in reversed(ts)]
    f._add('<path d="M%s Z" fill="%s" fill-opacity="%s" stroke="none"/>'
           % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in haut + bas), coul, op))
f.fonction(lambda t: S0 * math.exp(R * t), 0, 1, couleur=ENCRE, epaisseur=2.6)
f.point(1, S0 * math.exp(R), couleur=ENCRE)
f.texte(1, S0 * math.exp(R), "E^{Q}(S_{1}) = 104,08", couleur=ENCRE, dx=8, dy=4, gras=True)
f.texte(1, quantile(1, 0.40, Z), "σ = 40 %", couleur=AJOUT, dx=8, dy=4, gras=True)
f.texte(1, quantile(1, 0.20, Z), "σ = 20 %", couleur=ACCENT, dx=8, dy=4, gras=True)
f.texte(0.5, 60, "90 % des trajectoires dans chaque bande", couleur=DOUX, ancre="middle",
        taille=11.5)

sys.stdout.write(f.svg())
