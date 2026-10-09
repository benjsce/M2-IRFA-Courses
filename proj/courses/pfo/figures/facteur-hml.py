#!/usr/bin/env python3
r"""
facteur-hml.svg — le book-to-market compare ce que disent les comptes à ce que dit la bourse.

Ce que la figure doit faire voir : deux entreprises au même bilan — 100 d'actifs, 80 de
dette, donc 20 de capitaux propres comptables, A − D — que la bourse valorise très
différemment, 25 pour l'une, 100 pour l'autre. Le ratio book-to-market, capitaux propres
comptables sur capitalisation, les sépare : 0,8 pour la première, rangée du côté
« High », dite Value ; 0,2 pour la seconde, du côté « Low », dite Growth. Le facteur HML
est le rendement du premier groupe moins celui du second, écrit dessous.

Le bilan est celui de la fiche fpp/bilan (actifs 100, dette 80, capitaux propres 20). Les
deux capitalisations sont choisies pour le dessin.

Usage : python courses/pfo/figures/facteur-hml.py > facteur-hml.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, Colonne, ACCENT, AJOUT, DOUX, ENCRE, PALE   # noqa: E402

A, D = 100.0, 80.0
E = A - D
CAPS = (25.0, 100.0)
BM = [E / c for c in CAPS]
assert BM == [0.8, 0.2]

fr = lambda v, d=1: ("%.*f" % (d, v)).replace(".", ",")
ECH = 0.028                       # hauteur par unité monétaire


def entreprise(nom, cap, bm, style, couleur):
    f = Figure(xmin=0, xmax=1, ymin=-0.62, ymax=3.55, w=290, h=400, marges=(6, 6, 6, 6))
    f.texte(0.5, 3.42, nom + " : " + style, couleur=couleur, ancre="middle", gras=True,
            taille=13)
    # le bilan : actifs à gauche ; capitaux propres et dette à droite
    f.texte(0.27, 3.17, "bilan (comptes)", couleur=DOUX, ancre="middle", taille=11)
    f.barre(0.15, A * ECH, 0.2, couleur=DOUX, opacite=0.25, y0=0)
    f.texte(0.15, A * ECH / 2, "actifs 100", couleur=ENCRE, ancre="middle", taille=10.5)
    f.barre(0.39, D * ECH, 0.2, couleur=PALE, opacite=0.6, y0=0)
    f.texte(0.39, D * ECH / 2, "dette 80", couleur=ENCRE, ancre="middle", taille=10.5)
    f.barre(0.39, A * ECH, 0.2, couleur=couleur, opacite=0.35, y0=D * ECH)
    f.texte(0.39, (A + D) / 2 * ECH, "E = 20", couleur=ENCRE, ancre="middle", dy=4,
            taille=10.5)
    # la bourse : la capitalisation
    f.texte(0.76, 3.17, "bourse", couleur=DOUX, ancre="middle", taille=11)
    f.barre(0.76, cap * ECH, 0.2, couleur=couleur, opacite=0.6, y0=0)
    f.texte(0.76, cap * ECH, "capitalisation " + fr(cap, 0), couleur=ENCRE, ancre="middle",
            dy=-6, taille=10.5, fond=True)
    f.segment(0, 0, 1, 0, couleur=DOUX, epaisseur=1.0, pointilles=None)
    f.texte(0.5, -0.25, "book-to-market = 20 / " + fr(cap, 0) + " = " + fr(bm), couleur=ENCRE,
            ancre="middle", taille=12.5, gras=True)
    f.texte(0.5, -0.5, "rangée dans « %s B/M »" % ("High" if bm > 0.5 else "Low"),
            couleur=couleur, ancre="middle", taille=11.5)
    return f


g = entreprise("entreprise 1", CAPS[0], BM[0], "Value", ACCENT)
d = entreprise("entreprise 2", CAPS[1], BM[1], "Growth", AJOUT)
pied = Figure(xmin=0, xmax=1, ymin=0, ymax=1, w=620, h=44, marges=(0, 0, 0, 0))
pied.texte(0.5, 0.35, "HML = R_{High B/M} − R_{Low B/M}", couleur=ENCRE, ancre="middle",
           taille=14, gras=True)
sys.stdout.write(Colonne([Planche([g, d], ecart=40), Planche([pied])], ecart=4,
                         titre="Même bilan, deux capitalisations : le book-to-market les "
                               "range en Value et en Growth").svg())
