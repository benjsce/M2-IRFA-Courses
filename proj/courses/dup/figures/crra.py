#!/usr/bin/env python3
r"""
crra.svg — la prime d'un pari de ±30 % selon γ, et la lecture inverse.

Le geste de la fiche estime $\gamma$ sur une réponse : on demande la prime qu'on paierait
pour éviter un pari de $\pm30\,\%$ de sa richesse à pile ou face, et l'on résout
$u(1-\pi)=\tfrac12u(0{,}7)+\tfrac12u(1{,}3)$ en $\pi$. La courbe est cette équation
résolue pour chaque $\gamma$ ; lire la courbe à l'envers, c'est le geste. L'exemple de la
fiche, $\gamma=4$ et $16{,}0\,\%$, est recalculé ici.

Usage : python courses/dup/figures/crra.py > crra.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402

ALPHA = 0.30


def prime(g):
    """En pourcentage de la richesse, pour u(z) = z^(1-γ)/(1-γ), et ln z en γ = 1."""
    if g == 0:
        return 0.0
    if abs(g - 1) < 1e-12:
        c = math.exp(0.5 * math.log(1 - ALPHA) + 0.5 * math.log(1 + ALPHA))
    else:
        eu = 0.5 * (1 - ALPHA) ** (1 - g) + 0.5 * (1 + ALPHA) ** (1 - g)
        c = eu ** (1 / (1 - g))
    return 100 * (1 - c)


P4 = prime(4)

f = Figure(xmin=0, xmax=10.6, ymin=0, ymax=27, w=560, h=330,
           titre="Une réponse de 16 % se lit γ = 4 sur la courbe")
f.axes(xlab="aversion relative γ", ylab="prime, en %", xticks=(0, 1, 2, 4, 6, 8, 10),
       yticks=(5, 10, 16, 20, 25), fmt=lambda t: str(int(t)))

f.fonction(prime, 0, 10, couleur=ACCENT, epaisseur=2.4)
f.segment(0, P4, 4, P4, couleur=AJOUT)
f.segment(4, 0, 4, P4, couleur=AJOUT)
f.point(4, P4, couleur=AJOUT)
f.texte(4, P4, "la réponse, " + ("%.1f" % P4).replace(".", ",") + " %", couleur=AJOUT,
        dx=10, dy=12, gras=True, fond=True)
f.texte(1, prime(1), "logarithme", couleur=DOUX, dx=8, dy=10, taille=11.5, fond=True)
f.point(1, prime(1), couleur=DOUX, r=3)

sys.stdout.write(f.svg())
