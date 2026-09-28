#!/usr/bin/env python3
r"""
coherence-dynamique.svg — les trois problèmes de l'exemple, et les trois conditions.

Une grille : en abscisse la date du premier des deux gains, en ordonnée la date de la
décision. Le problème 1, $(100,0)$ contre $(110,4)$ décidé en 0 ; le problème 2, les mêmes
gains reculés de 26 semaines, décidé en 0 ; le problème 3, ces derniers gains décidés en 26
[L5 slide 18, L5 slide 20]. Chaque condition est un déplacement : la stationnarité recule les
gains (horizontale), l'invariance temporelle recule tout (diagonale), la cohérence dynamique
ne fait avancer que la décision (verticale). La diagonale puis la verticale refont
l'horizontale : c'est l'observation de la slide 21.

Usage : python courses/dup/figures/coherence-dynamique.py > coherence-dynamique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

f = Figure(xmin=-6, xmax=40, ymin=-9, ymax=33, w=560, h=380, marges=(58, 16, 44, 18),
           titre="Trois problèmes, trois déplacements : stationnarité, invariance temporelle, cohérence dynamique")
f.axes(xlab="date du premier gain", ylab="date de la décision", xticks=(0, 26), yticks=(0, 26),
       fmt=lambda t: str(int(t)), croix=(-6, -9))

P1, P2, P3 = (0, 0), (26, 0), (26, 26)
f.fleche(1.5, 0, 24.5, 0, couleur=AJOUT, epaisseur=2)
f.texte(13, 0, "stationnarité : violée", couleur=AJOUT, ancre="middle", dy=-9, gras=True, fond=True)
f.fleche(1.2, 1.2, 24.8, 24.8, couleur=ACCENT, epaisseur=2)
f.texte(11, 13.5, "invariance temporelle : tenue", couleur=ACCENT, ancre="end", dx=-4, gras=True, fond=True)
f.fleche(26, 24.5, 26, 1.5, couleur=AJOUT, epaisseur=2)
f.texte(26, 6, "cohérence dynamique : violée", couleur=AJOUT, ancre="end", dx=-8, gras=True, fond=True)

for (x, y), lib, sous in ((P1, "(100,0) ≻₀ (110,4)", "problème 1"),
                          (P2, "(100,26) ≺₀ (110,30)", "problème 2"),
                          (P3, "(100,26) ≻₂₆ (110,30)", "problème 3")):
    f.point(x, y, couleur=ENCRE, r=4.5)
    f.texte(x, y, lib, couleur=ENCRE, ancre="middle", dy=-12 if y else 26, gras=True, fond=True,
            dx=0 if x else 30)
    f.texte(x, y, sous, couleur=DOUX, ancre="middle", dy=-28 if y else 42, taille=11.5,
            dx=0 if x else 30)

f.texte(17, 31.5, "cohérence dynamique : (x,t) ≿₀ (y,s) ⟺ (x,t) ≿τ (y,s)", couleur=ENCRE,
        ancre="middle", taille=12.5, gras=True)

sys.stdout.write(f.svg())
