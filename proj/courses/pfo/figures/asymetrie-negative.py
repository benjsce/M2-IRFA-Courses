#!/usr/bin/env python3
r"""
asymetrie-negative.svg — deux lois de même moyenne et de même volatilité.

La fiche dit que deux actifs peuvent avoir même moyenne et même volatilité et des lois
très différentes : l'un fait des gains et des pertes symétriques, l'autre beaucoup de
petits gains et quelques très grosses pertes. Les deux lois dessinées sont construites
pour cela, et ne viennent pas du cours : à gauche $\pm1\,\%$ avec une chance sur deux ; à
droite $+\tfrac13\,\%$ avec probabilité 0,9 et $-3\,\%$ avec probabilité 0,1. Les deux ont
une moyenne nulle et un écart type de 1 % ; seule la seconde est asymétrique à gauche,
avec un coefficient d'asymétrie de $0{,}9\,(1/3)^3+0{,}1\,(-3)^3=-2{,}67$, que le titre de
chaque cadre écrit.

Usage : python courses/pfo/figures/asymetrie-negative.py > asymetrie-negative.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

SYM = [(-1.0, 0.5), (1.0, 0.5)]
ASY = [(-3.0, 0.1), (1.0 / 3.0, 0.9)]
for loi in (SYM, ASY):          # les deux ont bien la même moyenne et le même écart type
    m = sum(x * p for x, p in loi)
    v = sum(p * (x - m) ** 2 for x, p in loi)
    assert abs(m) < 1e-12 and abs(v - 1) < 1e-12
asym = lambda loi: sum(p * x ** 3 for x, p in loi)       # moyenne 0 et écart type 1 : S = E(X³)
fr = lambda v: ("%.2f" % v).rstrip("0").rstrip(",.").replace(".", ",").replace("-", "−")


def cadre(loi, titre, couleur, noms):
    g = Figure(xmin=-3.8, xmax=2.0, ymin=0, ymax=1.08, w=290, h=280, marges=(40, 30, 40, 10))
    g.axes(xlab="rendement, en %", xticks=(-3, -1, 0, 1), yticks=(0.5, 1),
           fmt=lambda t: ("%+d" % t if t else "0").replace("-", "−"),
           fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(-3.8, 0))
    for (x, p), nom in zip(loi, noms):
        g.barre(x, p, 0.34, couleur=couleur)
        g.texte(x, p, nom, couleur=couleur, ancre="middle", dy=-6, taille=11)
    g.texte(-0.9, 1.08, titre, couleur=ENCRE, ancre="middle", dy=-8, gras=True)
    return g


p = Planche([cadre(SYM, "symétrique : S = " + fr(asym(SYM)), DOUX, ("−1 %, ½", "+1 %, ½")),
             cadre(ASY, "asymétrique à gauche : S = " + fr(asym(ASY)), AJOUT,
                   ("−3 %, 0,1", "+⅓ %, 0,9"))],
            ecart=24,
            titre="Même moyenne nulle, même écart type de 1 %, deux lois différentes")
sys.stdout.write(p.svg())
