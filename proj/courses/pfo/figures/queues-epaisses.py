#!/usr/bin/env python3
r"""
queues-epaisses.svg — la loi normale et une loi leptokurtique de même variance.

La fiche dit qu'à variance égale une loi d'excès de kurtosis positif a un pic plus haut
et des queues plus épaisses, et son exemple minimal prend la loi de Laplace de variance 1,
d'excès 3. La figure trace ces deux densités et rien d'autre. Le cadre de droite grossit
la queue, où l'écart ne se voit pas à l'échelle du pic.

Usage : python courses/pfo/figures/queues-epaisses.py > queues-epaisses.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX            # noqa: E402

B = 1 / math.sqrt(2)                       # Laplace d'échelle b : variance 2 b² = 1
normale = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
laplace = lambda x: math.exp(-abs(x) / B) / (2 * B)

g = Figure(xmin=-4.4, xmax=4.4, ymin=0, ymax=0.78, w=330, h=300, marges=(44, 16, 40, 12))
g.axes(xlab="écart à la moyenne, en écarts types", xticks=(-4, -2, 0, 2, 4),
       yticks=(0.2, 0.4, 0.6), fmt=lambda t: str(int(t)), fmt_y=lambda t: ("%.1f" % t).replace(".", ","))
g.fonction(normale, -4.3, 4.3, n=240, couleur=DOUX, epaisseur=2.0)
g.fonction(laplace, -4.3, 4.3, n=240, couleur=ACCENT, epaisseur=2.4)
g.texte(0, laplace(0), "leptokurtique", couleur=ACCENT, dx=8, dy=4, taille=11.5, gras=True)
g.texte(-1.3, normale(-1.3), "normale", couleur=DOUX, ancre="end", dx=-8, dy=0, taille=11.5)

d = Figure(xmin=2.4, xmax=4.6, ymin=0, ymax=0.052, w=300, h=300, marges=(46, 16, 40, 12))
d.axes(xlab="la queue, grossie", xticks=(3, 4), yticks=(0.02, 0.04), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%.2f" % t).replace(".", ","))
d.fonction(normale, 2.5, 4.5, couleur=DOUX, epaisseur=2.0)
d.fonction(laplace, 2.5, 4.5, couleur=ACCENT, epaisseur=2.4)
d.texte(2.9, laplace(2.9), "leptokurtique", couleur=ACCENT, dx=6, dy=-8, taille=11.5, gras=True)
d.texte(2.53, 0.0016, "normale", couleur=DOUX, taille=11.5)

sys.stdout.write(Planche([g, d], ecart=24,
                         titre="À variance égale : pic plus haut, queues plus épaisses").svg())
