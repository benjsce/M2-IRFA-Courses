#!/usr/bin/env python3
r"""
theorie-des-perspectives.svg — la perte renversée reste au-dessus du gain.

La rubrique énonce une inégalité : $v(x)<-v(-x)$, « la courbe est plus raide du côté des
pertes ». Une inégalité entre deux valeurs d'une même fonction se lit mal en prose et se
voit d'un coup : on trace $v$, puis on rabat sa branche des pertes dans le quadrant des
gains, et la branche rabattue passe partout au-dessus.

La courbe n'est pas graduée, et c'est voulu : la fiche ne donne aucune échelle pour $v$.
Ses seules propriétés sont celles que la rubrique nomme — elle passe par le point de
référence, elle est plus raide du côté des pertes, et elle se courbe fortement près de
zéro. Le rapport constant entre les deux branches est un artefact de la forme choisie, non
un énoncé de la fiche.

Usage : python courses/dup/figures/theorie-des-perspectives.py > theorie-des-perspectives.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

E = 50.0                 # l'étendue tracée de part et d'autre du point de référence
COURBURE = 0.7           # < 1 : la courbe se couche en s'éloignant de la référence
RAIDEUR = 2.0            # la branche des pertes descend plus vite qu'elle ne monte

v = lambda x: (x / E) ** COURBURE if x >= 0 else -RAIDEUR * ((-x) / E) ** COURBURE
rabattue = lambda x: -v(-x)          # la branche des pertes, renversée sur les gains

X = 35.0                 # l'abscisse où l'écart est mesuré

f = Figure(xmin=-E - 6, xmax=E + 16, ymin=-RAIDEUR - 0.2, ymax=RAIDEUR + 0.25,
           w=560, h=360, marges=(30, 20, 44, 16),
           titre="La branche des pertes, rabattue sur les gains, passe partout au-dessus")

f.axes(xlab="écart au point de référence", ylab="v", croix=(0, 0))

f.segment(X, v(X), X, rabattue(X), couleur=PALE)
f.fonction(rabattue, 0.6, E, couleur=AJOUT, epaisseur=1.9, pointilles="5 4")
f.fonction(v, -E, -0.6, couleur=ACCENT, epaisseur=2.6)
f.fonction(v, 0.6, E, couleur=ACCENT, epaisseur=2.6)

f.point(0, 0, couleur=ENCRE)
f.mesure(X, v(X), rabattue(X), couleur=ENCRE, etiquette="v(x) < −v(−x)", cote="left")

f.texte(0, 0, "point de référence", couleur=ENCRE, ancre="start", dx=7, dy=-9,
        taille=11.5, gras=True, fond=True)
f.texte(E, v(E), "v", couleur=ACCENT, ancre="start", dx=5, dy=4, taille=12.5, gras=True)
f.texte(E, rabattue(E), "−v(−x)", couleur=AJOUT, ancre="end", dx=-4, dy=-9,
        taille=11.5, gras=True, fond=True)
f.texte(-E, v(-E), "pertes", couleur=DOUX, ancre="start", dx=2, dy=-8, taille=11.5)
f.texte(E * 0.55, v(E * 0.55), "gains", couleur=DOUX, ancre="middle", dy=17, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
