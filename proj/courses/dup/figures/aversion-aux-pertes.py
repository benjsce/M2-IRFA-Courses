#!/usr/bin/env python3
r"""
aversion-aux-pertes.svg — le coude au point de référence.

La fiche donne la forme $u(x)=x^\beta$ pour $x\ge0$ et $-\lambda(-x)^\beta$ pour
$x\le0$ [L3 slide 39], et l'exemple minimal fixe $\beta=1$, $\lambda=2$ : gagner 100
vaut $+100$, perdre 100 vaut $-200$. La figure trace exactement cette fonction.

La droite pointillée est la même fonction avec $\lambda=1$, c'est-à-dire sans aversion
aux pertes. Elle n'est pas dans la source ; elle est là parce que le coude ne se voit
que par rapport à ce qu'il serait s'il n'y en avait pas. La légende le dit.

Usage : python courses/dup/figures/aversion-aux-pertes.py > aversion-aux-pertes.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

BETA, LAMBDA = 1.0, 2.0
X = 155.0


def u(x, lam=LAMBDA):
    return x ** BETA if x >= 0 else -lam * (-x) ** BETA


f = Figure(xmin=-X, xmax=X, ymin=-320, ymax=180, w=560, h=350,
           titre="Le même écart de 100 vaut +100 d’un côté et −200 de l’autre")

f.axes(xlab="gain ou perte, x", ylab="valeur",
       xticks=(-100, 100), yticks=(-200, 100), fmt=lambda t: str(int(t)),
       croix=(0, 0))

# ce que la fonction serait sans aversion aux pertes : lambda = 1
f.courbe([(-X, u(-X, 1.0)), (X, u(X, 1.0))], couleur=DOUX, epaisseur=1.4, pointilles="5 4")

f.segment(100, 0, 100, u(100))
f.segment(-100, 0, -100, u(-100))
f.segment(0, u(100), 100, u(100))
f.segment(0, u(-100), -100, u(-100))

f.courbe([(-X, u(-X)), (0, 0), (X, u(X))], couleur=ACCENT, epaisseur=2.6)
f.point(0, 0, couleur=ENCRE, r=4.2)
f.point(100, u(100), couleur=ACCENT, r=3.4)
f.point(-100, u(-100), couleur=ACCENT, r=3.4)

f.texte(0, 0, "le point de référence : le coude est ici", couleur=ENCRE,
        ancre="end", dx=-14, dy=-20, taille=11.5, fond=True)
f.texte(-70, u(-70, 1.0), "sans aversion aux pertes, λ = 1", couleur=DOUX,
        ancre="end", dx=-6, dy=-8, taille=11.5, fond=True)
f.texte(X, u(X), "λ = 2", couleur=ACCENT, ancre="end", dx=-4, dy=-10, gras=True)
f.texte(-100, u(-100), "perdre 100 coûte 200", couleur=ACCENT,
        dx=8, dy=16, taille=11.5, fond=True)
f.texte(100, u(100), "gagner 100 rapporte 100", couleur=ACCENT, ancre="end",
        dx=-8, dy=-12, taille=11.5, fond=True)

sys.stdout.write(f.svg())
