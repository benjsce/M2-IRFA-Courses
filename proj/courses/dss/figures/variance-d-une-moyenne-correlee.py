#!/usr/bin/env python3
r"""
variance-d-une-moyenne-correlee.svg — la variance d'une moyenne est la moyenne d'un tableau.

Ce que la figure doit faire voir : la variance de la moyenne de B arbres est la moyenne des
B × B cases du tableau de leurs covariances. Les B cases de la diagonale valent σ², la
variance d'un arbre ; les B(B − 1) autres valent ρσ², la covariance de deux arbres. Quand B
grandit, la diagonale pèse de moins en moins, et la moyenne des cases tend vers ρσ² : c'est
le plancher de la fiche.

Trois tableaux, ρ = 0,5, puis leur limite : B = 2, (2 + 2 × 0,5)/4 = 0,75 σ² ; B = 4, (4 + 12 × 0,5)/16 = 0,625 σ² ;
B = 10, (10 + 90 × 0,5)/100 = 0,55 σ² ; B très grand, ρσ² = 0,5 σ². Chaque valeur est aussi ρσ² + (1 − ρ)σ²/B, la forme de
la fiche. La teinte d'une case dit sa valeur : pleine pour σ², à moitié pour ρσ² = 0,5 σ².

Usage : python courses/dss/figures/variance-d-une-moyenne-correlee.py > variance-d-une-moyenne-correlee.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, FOND      # noqa: E402

RHO = 0.5
virg = lambda v: ("%g" % v).replace(".", ",")


def cadre(B):
    g = Figure(xmin=0, xmax=1, ymin=-0.62, ymax=1.12, w=196, h=250, marges=(18, 8, 8, 18))
    ecart = 0.012 if B > 4 else 0.02
    for i in range(B):
        for j in range(B):
            diag = i == j
            g.barre((j + 0.5) / B, 1 - i / B - ecart / 2, 1 / B - ecart, couleur=ACCENT,
                    opacite=0.9 if diag else 0.9 * RHO, y0=1 - (i + 1) / B + ecart / 2)
            if B <= 4:
                g.texte((j + 0.5) / B, 1 - (i + 0.5) / B, "σ²" if diag else "ρσ²",
                        couleur=FOND if diag else ENCRE, ancre="middle", dy=5,
                        taille=13 if B == 2 else 11.5, gras=diag)
    n_diag, n_hors = B, B * (B - 1)
    v = (n_diag + n_hors * RHO) / B ** 2
    g.texte(0.5, 1, "B = %d" % B, couleur=ENCRE, ancre="middle", dy=-8, gras=True, taille=13)
    g.texte(0.5, 0, "%d cases à σ², %d à ρσ²" % (n_diag, n_hors), couleur=DOUX,
            ancre="middle", dy=22, taille=11.5)
    g.texte(0.5, 0, "(%d + %d × %s) / %d" % (n_diag, n_hors, virg(RHO), B ** 2), couleur=ENCRE,
            ancre="middle", dy=44, taille=12)
    g.texte(0.5, 0, "= %s σ²" % virg(round(v, 4)), couleur=ACCENT, ancre="middle", dy=68,
            taille=14, gras=True)
    return g


def plancher():
    """Le dernier cadre, sans tableau : ce vers quoi tendent les moyennes."""
    g = Figure(xmin=0, xmax=1, ymin=-0.62, ymax=1.12, w=144, h=250, marges=(6, 8, 8, 6))
    g.texte(0.5, 1, "B très grand", couleur=ENCRE, ancre="middle", dy=-8, gras=True, taille=13)
    g.texte(0.5, 0.5, "la diagonale", couleur=DOUX, ancre="middle", dy=-8, taille=11.5)
    g.texte(0.5, 0.5, "ne pèse plus", couleur=DOUX, ancre="middle", dy=8, taille=11.5)
    g.texte(0.5, 0, "= ρσ² = %s σ²" % virg(RHO), couleur=ACCENT, ancre="middle", dy=68,
            taille=14, gras=True)
    return g


sys.stdout.write(Planche([cadre(2), cadre(4), cadre(10), plancher()], signes=("→", "→", "→"),
                         ecart=34,
                         titre="La variance de la moyenne est la moyenne des cases : "
                               "la diagonale s'efface, ρσ² reste").svg())
