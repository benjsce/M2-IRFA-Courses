#!/usr/bin/env python3
r"""
actif-illiquide.svg — où peuvent aller les ressources de la période t.

Les deux contraintes de la Forme [L5 slide 43] dessinées comme des flux. À gauche, les
ressources : le revenu et le liquide rendu, $y_t+R\,x_{t-1}$, d'un côté ; l'illiquide
rendu, $R\,z_{t-1}$, de l'autre. À droite, leurs emplois : $c_t$, $x_t$, $z_t$. Tout peut
être replacé ; seul le premier bloc peut être consommé, $c_t\le y_t+R\,x_{t-1}$. La flèche
barrée est ce que l'actif illiquide interdit.

Usage : python courses/dup/figures/actif-illiquide.py > actif-illiquide.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

f = Figure(xmin=0, xmax=10, ymin=-1.2, ymax=7, w=560, h=330, marges=(10, 10, 10, 10),
           titre="Le revenu et le liquide rendu peuvent être consommés ; l'illiquide rendu ne peut qu'être replacé")

def boite(x, y, lib, c, larg=2.6, haut=1.1):
    f.barre(x, y + haut / 2, larg, couleur=c, opacite=0.25, y0=y - haut / 2)
    f.texte(x, y, lib, couleur=ENCRE, ancre="middle", dy=5, gras=True, taille=13)

SRC = {"liq": (1.8, 4.8), "ill": (1.8, 1.4)}
DST = {"c": (8.2, 5.6), "x": (8.2, 3.2), "z": (8.2, 0.8)}
boite(*SRC["liq"], "yₜ + R xₜ₋₁", ACCENT)
boite(*SRC["ill"], "R zₜ₋₁", AJOUT)
boite(*DST["c"], "cₜ", ACCENT, larg=1.6)
boite(*DST["x"], "xₜ", DOUX, larg=1.6)
boite(*DST["z"], "zₜ", DOUX, larg=1.6)

def relie(s, d, c, **kw):
    (x0, y0), (x1, y1) = SRC[s], DST[d]
    f.fleche(x0 + 1.35, y0, x1 - 0.85, y1, couleur=c, **kw)

relie("liq", "c", ACCENT, epaisseur=2.2)
relie("liq", "x", DOUX)
relie("liq", "z", DOUX)
relie("ill", "x", AJOUT, epaisseur=1.8)
relie("ill", "z", AJOUT, epaisseur=1.8)
relie("ill", "c", PALE, pointilles="4 4")
mx, my = (SRC["ill"][0] + 1.35 + DST["c"][0] - 0.85) / 2, (SRC["ill"][1] + DST["c"][1]) / 2
f.texte(mx, my, "✕", couleur=AJOUT, ancre="middle", dy=6, taille=20, gras=True, fond=True)

f.texte(5, -0.7, "cₜ ≤ yₜ + R xₜ₋₁   ;   cₜ + xₜ + zₜ = yₜ + R (zₜ₋₁ + xₜ₋₁)", couleur=ENCRE,
        ancre="middle", taille=13, gras=True)

sys.stdout.write(f.svg())
