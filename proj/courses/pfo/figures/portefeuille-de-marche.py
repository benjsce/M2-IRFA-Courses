#!/usr/bin/env python3
r"""
portefeuille-de-marche.svg — le poids d'un actif est sa capitalisation, pas le prix de son action.

Ce que la figure doit faire voir : la capitalisation est le prix d'une action multiplié
par le nombre d'actions, et c'est elle, rapportée au total, qui fait le poids dans le
portefeuille de marché. Trois cadres côte à côte, « × » puis « = » : prix P_i, nombre
d'actions N_i, capitalisation P_i N_i. Le second actif a l'action la plus chère et le plus
petit poids. La Forme est écrite dessous.

Les chiffres : le premier actif, 2 milliards d'actions à 10 €, vaut 20 milliards ; le
second, 500 millions d'actions à 20 €, vaut 10 milliards ; le marché vaut 30 milliards,
et les poids sont deux tiers et un tiers.

Usage : python courses/pfo/figures/portefeuille-de-marche.py > portefeuille-de-marche.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, Colonne, ACCENT, AJOUT, DOUX, ENCRE   # noqa: E402

P, N = (10.0, 20.0), (2.0, 0.5)                  # € par action, milliards d'actions
CAP = [p * n for p, n in zip(P, N)]               # 20 et 10 milliards
W = [c / sum(CAP) for c in CAP]
assert CAP == [20.0, 10.0] and abs(W[0] - 2 / 3) < 1e-12

fr = lambda v: ("%g" % v).replace(".", ",")


def cadre(titre, valeurs, unite, haut, pieds=None):
    f = Figure(xmin=0, xmax=1, ymin=-0.42, ymax=1.25, w=190, h=300, marges=(6, 6, 6, 6))
    f.texte(0.5, 1.15, titre, couleur=ENCRE, ancre="middle", gras=True, taille=12.5)
    for k, v in enumerate(valeurs):
        xc, c = 0.28 + 0.44 * k, (ACCENT, AJOUT)[k]
        f.barre(xc, v / haut, 0.3, couleur=c, opacite=0.4, y0=0)
        f.texte(xc, v / haut, fr(v) + unite, couleur=ENCRE, ancre="middle", dy=-6,
                taille=11.5, gras=True)
        f.texte(xc, 0, "actif %d" % (k + 1), couleur=DOUX, ancre="middle", dy=16, taille=11)
        if pieds:
            f.texte(xc, 0, pieds[k], couleur=c, ancre="middle", dy=33, taille=12, gras=True)
    f.segment(0.05, 0, 0.95, 0, couleur=DOUX, epaisseur=1.0, pointilles=None)
    return f


prix = cadre("prix d'une action P_{i}", P, " €", 24)
nombre = cadre("nombre d'actions N_{i}", N, " Md", 2.4)
cap = cadre("capitalisation P_{i} N_{i}", CAP, " Md", 24, ("w₁ᴹ = 2/3", "w₂ᴹ = 1/3"))
pied = Figure(xmin=0, xmax=1, ymin=0, ymax=1, w=630, h=44, marges=(0, 0, 0, 0))
pied.texte(0.5, 0.35, "w_{i}^{M} = Capitalisation_{i} / Σ_{j} Capitalisation_{j} "
           "= P_{i} N_{i} / Σ_{j} P_{j} N_{j}", couleur=ENCRE, ancre="middle", taille=14,
           gras=True)
sys.stdout.write(Colonne([Planche([prix, nombre, cap], signes=("×", "="), ecart=30),
                          Planche([pied])], ecart=4,
                         titre="Prix fois nombre d'actions : la capitalisation fait le poids, "
                               "pas le prix").svg())
