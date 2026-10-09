#!/usr/bin/env python3
r"""
facteur-statistique.svg — les loadings restent fixes ; le facteur, lui, bouge chaque jour.

Ce que la figure doit faire voir : la valeur du facteur un jour donné est une somme
pondérée des rendements de ce jour, les poids étant les loadings, les mêmes tous les
jours. Chaque jour est une barre empilée : la part de l'actif 1, v_11 R_1,t, et celle de
l'actif 2, v_21 R_2,t ; leur somme, marquée d'un trait, est PC_1,t. Une barre par jour,
trois jours : la série du facteur.

Le monde du chapitre 2 (voir analyse-en-composantes-principales.py) : loadings du premier
facteur v_11 = 0,29 et v_21 = 0,96. Trois jours de rendements, choisis pour le dessin :
(1 % ; 2 %), (−1 % ; −0,5 %), (0,5 % ; −1 %). PC_1 vaut 2,20 %, −0,77 % et −0,81 %.

Usage : python courses/pfo/figures/facteur-statistique.py > facteur-statistique.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

a, c, d = 252 * 1e-4, 252 * 0.5 * 1e-4 * 2, 252 * 4e-4
l1 = (a + d + math.sqrt((a - d) ** 2 + 4 * c * c)) / 2
v = (c, l1 - a)
nv = math.hypot(*v)
v = (v[0] / nv, v[1] / nv)
assert abs(v[0] - 0.2898) < 1e-4 and abs(v[1] - 0.9571) < 1e-4
JOURS = ((1.0, 2.0), (-1.0, -0.5), (0.5, -1.0))
PC = [v[0] * r1 + v[1] * r2 for r1, r2 in JOURS]
assert [round(p, 2) for p in PC] == [2.20, -0.77, -0.81]

fr = lambda x, n=2: ("%.*f" % (n, x)).replace(".", ",").replace("-", "−")

f = Figure(xmin=0, xmax=3.3, ymin=-3.1, ymax=2.9, w=560, h=430, marges=(54, 16, 20, 18),
           titre="Mêmes loadings chaque jour ; la valeur du facteur suit les rendements du jour")
f.axes(ylab="contribution au facteur, en %", yticks=(-2, -1, 0, 1, 2),
       fmt=lambda t: fr(t, 0), croix=(0, 0))

for k, (r1, r2) in enumerate(JOURS):
    xc, lg = 0.6 + 1.0 * k, 0.5
    c1, c2 = v[0] * r1, v[1] * r2
    # parts positives empilées vers le haut depuis zéro, négatives vers le bas
    haut, bas = 0.0, 0.0
    for part, coul in ((c1, ACCENT), (c2, AJOUT)):
        if part >= 0:
            y0, haut = haut, haut + part
        else:
            y0, bas = bas, bas + part
        f.barre(xc, y0 + part, lg, couleur=coul, opacite=0.35, y0=y0)
        f.texte(xc + lg / 2, y0 + part / 2, fr(part), couleur=coul, dx=6, dy=4, taille=11)
    tot = c1 + c2
    f.segment(xc - lg / 2 - 0.08, tot, xc + lg / 2 + 0.08, tot, couleur=ENCRE, epaisseur=2.6,
              pointilles=None)
    f.texte(xc, tot, "PC_{1,t} = " + fr(tot), couleur=ENCRE, ancre="middle",
            dy=-10 if tot > 0 else 34, gras=True, fond=True)
    f.texte(xc, -2.1, "jour %d" % (k + 1), couleur=DOUX, ancre="middle", dy=-24, taille=12)
    f.texte(xc, -2.1, "R = (%s ; %s)" % (fr(r1, 1), fr(r2, 1)), couleur=DOUX,
            ancre="middle", dy=-9, taille=11)
f.texte(2.4, 2.65, "v_{11} R_{1,t} : actif 1, poids " + fr(v[0]), couleur=ACCENT, taille=11.5)
f.texte(2.4, 2.35, "v_{21} R_{2,t} : actif 2, poids " + fr(v[1]), couleur=AJOUT, taille=11.5)

f.texte(1.65, -3.1, "PC_{1,t} = v_{11} R_{1,t} + v_{21} R_{2,t}", couleur=ENCRE,
        ancre="middle", taille=14, gras=True, dy=-8)

sys.stdout.write(f.svg())
