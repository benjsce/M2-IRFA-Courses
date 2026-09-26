#!/usr/bin/env python3
r"""
utilite-quadratique.svg — la parabole, son sommet, et le pari du cours.

L'exemple de la fiche : $U(x)=x-0{,}005\,x^2$ et le pari $(0,\tfrac12;100,\tfrac12)$, qui
vaut 25. Le dessin ajoute ce que la fiche met en garde : la parabole culmine au point de
satiété $-\alpha/2\beta=100$, et au-delà l'utilité décroît. Le pari du cours touche
exactement ce sommet par son bon résultat, ce qui se voit.

Usage : python courses/dup/figures/utilite-quadratique.py > utilite-quadratique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

ALPHA, BETA = 1.0, -0.005
U = lambda x: ALPHA * x + BETA * x * x
SAT = -ALPHA / (2 * BETA)                     # 100
EU = 0.5 * U(0) + 0.5 * U(100)                # 25

f = Figure(xmin=0, xmax=165, ymin=0, ymax=60, w=560, h=330,
           titre="La parabole culmine à 100 ; au-delà, plus de richesse fait baisser l'utilité")
f.axes(xlab="richesse x", ylab="U", xticks=(0, 50, 100, 150), yticks=(25, 50),
       fmt=lambda t: str(int(t)))

f.courbe([(0, U(0)), (100, U(100))], couleur=DOUX, epaisseur=1.6)
f.fonction(U, 0, SAT, couleur=ACCENT, epaisseur=2.4)
f.fonction(U, SAT, 160, couleur=AJOUT, epaisseur=2.4, pointilles="6 4")

f.segment(SAT, 0, SAT, U(SAT))
f.point(SAT, U(SAT), couleur=AJOUT)
f.texte(SAT, U(SAT), "satiété : −α/2β = 100", couleur=AJOUT, ancre="middle", dy=-10,
        gras=True, fond=True)

f.point(50, EU, couleur=ENCRE)
f.texte(50, EU, "le pari vaut 25", couleur=ENCRE, dx=8, dy=16, gras=True, fond=True)
f.texte(150, U(150), "U décroît", couleur=AJOUT, ancre="end", dx=-6, dy=-8, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
