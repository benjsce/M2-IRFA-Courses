#!/usr/bin/env python3
r"""
theta.svg — le prix du call à la monnaie, à mesure que l'échéance approche.

L'exemple courant : sous-jacent et strike à 100, taux 4 %, volatilité 20 %, un an au
départ. On garde le sous-jacent à 100 et l'on fait passer le temps. Le prix part de 9,93
et tombe à zéro à l'échéance : tout le prix fond, pas seulement la valeur temps, car la
valeur intrinsèque au sens du cours, S − Ke^{-rτ}, tombe elle aussi de 3,92 à zéro. La
pente de la courbe du prix est le theta : −5,89 par an au départ, tracée en tangente, et
de plus en plus raide à la fin.

Usage : python courses/fpp/figures/theta.py > theta.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

N = NormalDist()
S, K, R, SIG = 100.0, 100.0, 0.04, 0.20


def call(tau):
    if tau <= 0:
        return max(S - K, 0.0)
    d1 = (math.log(S / K) + (R + SIG ** 2 / 2) * tau) / (SIG * math.sqrt(tau))
    return S * N.cdf(d1) - K * math.exp(-R * tau) * N.cdf(d1 - SIG * math.sqrt(tau))


iv = lambda tau: max(S - K * math.exp(-R * tau), 0.0)

f = Figure(xmin=0, xmax=1.08, ymin=0, ymax=11.5, w=560, h=320,
           titre="Tout le prix fond jusqu'à zéro, et de plus en plus vite à l'approche de l'échéance")
f.axes(xlab="temps écoulé, en années", ylab="valeur", xticks=(0, 0.5, 1), yticks=(3.92, 9.93),
       fmt=lambda t: {0: "0", 0.5: "½", 1: "1 : échéance"}[t],
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))

f.fonction(lambda t: iv(1 - t), 0, 1, couleur=DOUX, epaisseur=2.2)
f.fonction(lambda t: call(1 - t), 0, 1, n=300, couleur=ACCENT, epaisseur=2.6)
f.mesure(0.02, iv(1), call(1), couleur=AJOUT, etiquette="valeur temps 6,00")
f.point(1, 0, couleur=ENCRE)
h = 1e-5
theta = (call(1 - h) - call(1)) / h                   # −5,89 par an
f.segment(0, call(1), 0.6, call(1) + 0.6 * theta, couleur=ENCRE, epaisseur=1.4,
          pointilles="5 4")
f.texte(0.2, call(1) + 0.2 * theta, "pente Θ = %s par an" % ("%.2f" % theta).replace(".", ",").replace("-", "−"),
        couleur=ENCRE, dy=-12, fond=True)
f.texte(0.74, call(0.26), "prix du call", couleur=ACCENT, dy=-10, gras=True, fond=True)
f.texte(0.12, 1.2, "valeur intrinsèque, S − Ke^{−rτ}", couleur=DOUX, gras=True, fond=True)

sys.stdout.write(f.svg())
