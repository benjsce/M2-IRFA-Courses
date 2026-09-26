#!/usr/bin/env python3
r"""
diversification.svg — l'écart type du portefeuille selon la part du premier actif.

L'exemple de la fiche : deux actifs à $\sigma=20\,\%$ chacun. En trait plein, covariance
nulle : la courbe descend sous 20 % et touche 14,1 % à parts égales. En pointillé, la
corrélation parfaite de « Cesse d'être valide quand » : l'écart type reste la moyenne
pondérée des deux, donc 20 % partout, et le gain disparaît.

Usage : python courses/dup/figures/diversification.py > diversification.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

S1 = S2 = 20.0


def sigma_p(a, cov):
    return math.sqrt(a * a * S1 * S1 + (1 - a) ** 2 * S2 * S2 + 2 * a * (1 - a) * cov)


f = Figure(xmin=0, xmax=1.04, ymin=0, ymax=24, w=560, h=330,
           titre="Sans covariance, le mélange est moins dispersé que chacun des deux actifs")
f.axes(xlab="part a du premier actif", ylab="σp, en %", xticks=(0, 0.5, 1),
       yticks=(10, 14.1, 20), fmt=lambda t: {0: "0", 0.5: "½", 1: "1"}[t],
       fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.fonction(lambda a: sigma_p(a, S1 * S2), 0, 1, couleur=DOUX, epaisseur=2.0, pointilles="6 4")
f.fonction(lambda a: sigma_p(a, 0.0), 0, 1, couleur=ACCENT, epaisseur=2.6)

m = sigma_p(0.5, 0.0)
f.segment(0.5, 0, 0.5, m)
f.point(0.5, m, couleur=ENCRE)
f.mesure(0.5, m, 20, couleur=AJOUT, etiquette="le gain, " + ("%.1f" % (20 - m)).replace(".", ",") + " points")
f.texte(0.5, m, "14,1 %", couleur=ENCRE, ancre="middle", dy=18, gras=True, fond=True)
f.texte(0.08, 20, "corrélation parfaite : 20 % partout", couleur=DOUX, dy=-8, taille=11.5,
        fond=True)
f.texte(0.2, 12, "covariance nulle", couleur=ACCENT, ancre="middle", gras=True, fond=True)

sys.stdout.write(f.svg())
