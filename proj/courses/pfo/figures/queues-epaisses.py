#!/usr/bin/env python3
r"""
queues-epaisses.svg — la loi normale et une loi leptokurtique de même variance.

La fiche dit qu'à variance égale une loi d'excès de kurtosis positif a un pic plus haut
et des queues plus épaisses, et son exemple minimal prend la loi de Laplace de variance 1,
d'excès 3 : elle s'écarte de plus de trois écarts types de sa moyenne avec une probabilité
de 1,4 %, contre 0,27 % pour la loi normale. Le cadre de gauche trace les deux densités.
Celui de droite grossit la queue droite et colore, sous chaque courbe, l'aire au-delà de
trois écarts types : c'est la probabilité de l'exemple, d'un seul côté, $e^{-3\sqrt2}/2$
pour la loi de Laplace (0,72 %) et $\Phi(-3)$ pour la loi normale (0,135 %). La figure
montre ainsi le chiffre de l'exemple, et non une différence de hauteur de densité.

Les deux chiffres sont écrits dans le coin vide du cadre, chacun de la couleur de son
aire, alignés à gauche : rien ne dépend de la largeur de la police.

Usage : python courses/pfo/figures/queues-epaisses.py > queues-epaisses.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, ENCRE, _n       # noqa: E402

B = 1 / math.sqrt(2)                       # Laplace d'échelle b : variance 2 b² = 1
normale = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
laplace = lambda x: math.exp(-abs(x) / B) / (2 * B)
P_LAP = math.exp(-3 / B) / 2               # 0,72 % au-delà de 3, d'un côté
P_NOR = NormalDist().cdf(-3)               # 0,135 %
pc = lambda p, d: ("%.*f %%" % (d, 100 * p)).replace(".", ",")

g = Figure(xmin=-4.4, xmax=4.4, ymin=0, ymax=0.78, w=330, h=300, marges=(44, 16, 40, 12))
g.axes(xlab="écart à la moyenne, en écarts types", xticks=(-4, -2, 0, 2, 4),
       yticks=(0.2, 0.4, 0.6), fmt=lambda t: str(int(t)).replace("-", "−"),
       fmt_y=lambda t: ("%.1f" % t).replace(".", ","))
g.fonction(normale, -4.3, 4.3, n=240, couleur=DOUX, epaisseur=2.0)
g.fonction(laplace, -4.3, 4.3, n=240, couleur=ACCENT, epaisseur=2.4)
g.texte(0, laplace(0), "Laplace", couleur=ACCENT, dx=8, dy=4, taille=11.5, gras=True)
g.texte(-1.3, normale(-1.3), "normale", couleur=DOUX, ancre="end", dx=-8, dy=0, taille=11.5)

X0, X1 = 3.0, 6.2
d = Figure(xmin=2.4, xmax=6.4, ymin=0, ymax=0.026, w=320, h=300, marges=(50, 16, 40, 12))


def aire(f, couleur, opacite):
    pts = [(X0 + (X1 - X0) * i / 120, f(X0 + (X1 - X0) * i / 120)) for i in range(121)]
    pts += [(X1, 0), (X0, 0)]
    d._add('<path d="M%s Z" fill="%s" fill-opacity="%s" stroke="none"/>'
           % (" L".join("%s %s" % (_n(d.px(x)), _n(d.py(y))) for x, y in pts), couleur,
              _n(opacite)))


aire(laplace, ACCENT, 0.28)
aire(normale, DOUX, 0.55)
d.axes(xlab="la queue droite, grossie", xticks=(3, 4, 5, 6), yticks=(0.01, 0.02),
       fmt=lambda t: str(int(t)), fmt_y=lambda t: ("%.2f" % t).replace(".", ","))
d.fonction(normale, 2.5, X1, couleur=DOUX, epaisseur=2.0)
d.fonction(laplace, 2.5, X1, couleur=ACCENT, epaisseur=2.4)
d.segment(X0, 0, X0, laplace(X0), couleur=ENCRE, epaisseur=1.2, pointilles=None)


# La légende des aires, dans le coin vide du cadre : chaque chiffre a la couleur de son aire.
d.texte(3.7, 0.0225, "aire au-delà de 3 :", couleur=ENCRE, taille=11.5)
d.texte(3.7, 0.0225, "Laplace : " + pc(P_LAP, 2), couleur=ACCENT, dy=18, taille=11.5, gras=True)
d.texte(3.7, 0.0225, "normale : " + pc(P_NOR, 3), couleur=DOUX, dy=36, taille=11.5, gras=True)

sys.stdout.write(Planche([g, d], ecart=24,
                         titre="À variance égale : pic plus haut, queues plus épaisses").svg())
