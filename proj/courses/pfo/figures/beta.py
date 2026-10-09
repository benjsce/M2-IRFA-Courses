#!/usr/bin/env python3
r"""
beta.svg — le bêta est la part de risque de marché qu'un actif apporte, rapportée à son poids.

Ce que la figure doit faire voir : chaque actif est une barre dont la largeur est son
poids dans le marché et la hauteur son bêta, Cov(R_i, R_m)/Var(R_m). L'aire d'une barre
est la part de la variance du marché que l'actif porte, et les aires font 1 ensemble :
le marché a un bêta de 1, tracé en pointillé. Un actif au-dessus de cette ligne porte plus
de risque de marché que son poids, un actif en dessous, moins.

Le monde du chapitre 3 : deux actifs non corrélés de volatilités 10 % et 20 %, détenus par
le marché à deux tiers et un tiers. Var(R_m) = 4/9 × 0,01 + 1/9 × 0,04 = 0,00889 ;
Cov(R_1, R_m) = 2/3 × 0,01 = 0,00667, β_1 = 0,75 ; Cov(R_2, R_m) = 1/3 × 0,04 = 0,01333,
β_2 = 1,5. Chaque actif porte la moitié du risque du marché : 2/3 × 0,75 = 1/3 × 1,5 = 0,5.

Usage : python courses/pfo/figures/beta.py > beta.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

W = (2 / 3, 1 / 3)
VAR = (0.01, 0.04)
var_m = sum(w * w * v for w, v in zip(W, VAR))
cov = [w * v for w, v in zip(W, VAR)]                 # actifs non corrélés
beta = [c / var_m for c in cov]
assert abs(var_m - 0.0088889) < 1e-6
assert abs(beta[0] - 0.75) < 1e-9 and abs(beta[1] - 1.5) < 1e-9
assert abs(sum(w * b for w, b in zip(W, beta)) - 1) < 1e-12

fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",")

f = Figure(xmin=-0.02, xmax=1.08, ymin=-0.62, ymax=1.85, w=560, h=380,
           marges=(54, 16, 20, 18),
           titre="Largeur : le poids dans le marché ; hauteur : le bêta ; "
                 "aire : la part du risque du marché")
f.axes(ylab="bêta", yticks=(0, 0.75, 1, 1.5), fmt=lambda t: fr(t, 2).rstrip("0").rstrip(","),
       croix=(-0.02, 0))

x = 0.0
couleurs = (ACCENT, AJOUT)
for i in range(2):
    f.barre(x + W[i] / 2, beta[i], W[i], couleur=couleurs[i], opacite=0.30, y0=0)
    f.courbe([(x, 0), (x, beta[i]), (x + W[i], beta[i]), (x + W[i], 0)],
             couleur=couleurs[i], epaisseur=1.8)
    f.texte(x + W[i] / 2, beta[i], "β_{%d} = Cov(R_{%d}, R_{m}) / Var(R_{m}) = %s"
            % (i + 1, i + 1, fr(beta[i])) if i == 0 else "β_{2} = " + fr(beta[i]),
            couleur=couleurs[i], ancre="middle", dy=-9, gras=True, taille=12)
    f.texte(x + W[i] / 2, beta[i] / 2, "aire w_{%d}^{M} β_{%d} = %s"
            % (i + 1, i + 1, fr(W[i] * beta[i], 1)), couleur=ENCRE, ancre="middle",
            dy=4, taille=12.5, fond=True)
    f.texte(x + W[i] / 2, 0, "actif %d : poids w_{%d}^{M} = %s" % (i + 1, i + 1,
            "2/3" if i == 0 else "1/3"), couleur=DOUX, ancre="middle", dy=18, taille=11.5)
    x += W[i]
f.segment(0, 1, 1.0, 1, couleur=ENCRE, epaisseur=1.3, pointilles="5 4")
f.texte(1.0, 1, "marché : β = 1", couleur=ENCRE, ancre="end", dy=-6, taille=11.5)

f.texte(0.5, -0.62, "β_{i} = Cov(R_{i}, R_{m}) / Var(R_{m})", couleur=ENCRE,
        ancre="middle", taille=14, gras=True, dy=-14)

sys.stdout.write(f.svg())
