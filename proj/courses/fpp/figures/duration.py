#!/usr/bin/env python3
r"""
duration.svg — ce que perd chaque zéro-coupon quand le taux monte de 100 points de base.

La fiche dit que la sensibilité relative d'un zéro-coupon est sa maturité : un titre à
$t$ ans perd $t\,\%$ pour 100 points de base. Sur un échéancier, chaque zéro-coupon est
posé à sa maturité, et sa perte descend d'autant plus que la maturité est lointaine. Le
titre à 5 ans est celui de l'exemple ; ceux à 1, 2 et 10 ans sont ajoutés pour le dessin.
Les pertes sont celles de la dérivée, $-t\times1\,\%$.

Usage : python courses/fpp/figures/duration.py > duration.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

MAT = (1, 2, 5, 10)

f = Figure(xmin=-0.5, xmax=11.2, ymin=-12.6, ymax=2.2, w=560, h=320, marges=(46, 12, 12, 12),
           titre="Une hausse de taux coûte à chaque zéro-coupon sa maturité en pour cent")
f.axe_temps(0, -0.2, 11, [(0, "t")] + [(m, "%d an%s" % (m, "s" if m > 1 else "")) for m in MAT])
for m in MAT:
    f.fleche(m, -1.4, m, -1.4 - m, couleur=AJOUT if m == 5 else ACCENT, epaisseur=2.4)
    f.texte(m, -1.4 - m, "−%d %%" % m, couleur=AJOUT if m == 5 else ACCENT, dx=8, dy=10, gras=True)
f.texte(10.9, 1.4, "taux : +100 points de base", couleur=ENCRE, ancre="end", gras=True)

sys.stdout.write(f.svg())
