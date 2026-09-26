#!/usr/bin/env python3
r"""
erreur-out-of-bag.svg — qui est dans chaque sac, et qui en est absent.

Six échantillons bootstrap tirés parmi dix observations, avec une graine fixée. Chaque
ligne est un arbre ; chaque case dit combien de fois l'observation a été tirée pour lui, et
une case vide est une observation hors du sac. La colonne encadrée se lit comme la fiche le
demande : l'observation encadrée, la plus souvent hors du sac, est prédite par les seuls arbres pour lesquels elle était absente.
Les dix observations et les six arbres sont choisis pour le dessin.

Usage : python courses/dss/figures/erreur-out-of-bag.py > erreur-out-of-bag.svg
Dépendance : aucune.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

N, B = 10, 6
rng = random.Random(4)
sacs = []
for _ in range(B):
    tirage = [rng.randrange(N) for _ in range(N)]
    sacs.append([tirage.count(i) for i in range(N)])
# l'observation encadrée : celle qui est le plus souvent hors du sac
OBS = max(range(N), key=lambda i: (sum(1 for s in sacs if s[i] == 0), -i))

f = Figure(xmin=-2.6, xmax=14.5, ymin=-0.9, ymax=B + 1.2, w=580, h=300, marges=(8, 8, 8, 8),
           titre="Une observation est prédite par les seuls arbres dont elle est absente")
for b, sac in enumerate(sacs):
    y = B - b
    for i, c in enumerate(sac):
        dehors = c == 0
        f.barre(i + 0.5, y + 0.4, 0.86, couleur=(AJOUT if i == OBS else ACCENT) if dehors else DOUX,
                opacite=0.2 if dehors else 0.45, y0=y - 0.4)
        f.texte(i + 0.5, y, "%d" % c if c else "·", couleur=ENCRE, ancre="middle", dy=4, taille=11.5,
                gras=bool(c > 1))
    f.texte(-0.2, y, "arbre %d" % (b + 1), couleur=ENCRE, ancre="end", dy=4, taille=11.5)
    if sac[OBS] == 0:
        f.texte(10.3, y, "← prédit l'obs. %d" % (OBS + 1), couleur=AJOUT, dy=4, taille=11.5, gras=True)
f.courbe([(OBS + 0.02, 0.5), (OBS + 0.98, 0.5), (OBS + 0.98, B + 0.5), (OBS + 0.02, B + 0.5),
          (OBS + 0.02, 0.5)], couleur=AJOUT, epaisseur=2.0)
for i in range(N):
    f.texte(i + 0.5, B + 0.5, "%d" % (i + 1), couleur=DOUX, ancre="middle", dy=-6, taille=11)
f.texte(5, -0.5, "chaque case : nombre de tirages ; « · » : hors du sac", couleur=DOUX,
        ancre="middle", taille=11.5)

sys.stdout.write(f.svg())
