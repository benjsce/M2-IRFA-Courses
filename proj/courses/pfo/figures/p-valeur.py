#!/usr/bin/env python3
r"""
p-valeur.svg — la p-valeur comme aire, pour les deux p-valeurs de l'exemple.

La fiche définit la p-valeur comme la probabilité, sous l'hypothèse nulle, d'une
statistique au moins aussi extrême que celle observée : c'est l'aire de la queue au-delà
de la valeur observée. Il faut une loi pour la dessiner ; on prend celle de la statistique
de Jarque-Bera sous l'hypothèse nulle, $\chi^2(2)$, dont la queue vaut exactement
$e^{-x/2}$. Les deux p-valeurs de l'exemple, 0,40 et 0,03, correspondent alors aux
statistiques $-2\ln p$ : 1,83 et 7,01. Le niveau de 5 % correspond au seuil 5,99.

Usage : python courses/pfo/figures/p-valeur.py > p-valeur.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

dens = lambda x: 0.5 * math.exp(-x / 2)
SEUIL = -2 * math.log(0.05)
fr = lambda v: ("%.2f" % v).replace(".", ",")


def cadre(p, verdict, couleur):
    x0 = -2 * math.log(p)
    g = Figure(xmin=0, xmax=10.5, ymin=0, ymax=0.56, w=290, h=270, marges=(20, 30, 40, 10))
    g.axes(xlab="statistique", xticks=(0, x0), fmt=fr)
    pas = 0.05
    x = x0 + pas / 2
    while x < 10.4:
        g.barre(x, dens(x), pas, couleur=couleur, opacite=0.35)
        x += pas
    g.fonction(dens, 0, 10.4, couleur=ENCRE, epaisseur=2.0)
    g.segment(SEUIL, 0, SEUIL, 0.22, couleur=DOUX, epaisseur=1.4)
    g.texte(SEUIL, 0.22, "seuil 5,99", couleur=DOUX, ancre="middle", dy=-5, taille=10.5)
    g.segment(x0, 0, x0, dens(x0) + 0.12, couleur=couleur, epaisseur=1.8, pointilles=None)
    g.texte(x0, dens(x0) + 0.12, "observée", couleur=couleur, ancre="middle", dy=-5, taille=11)
    g.texte(8.6, 0.34, "aire = " + fr(p), couleur=couleur, ancre="middle", gras=True, fond=True)
    g.texte(5.2, 0.56, verdict, couleur=ENCRE, ancre="middle", dy=-8, gras=True)
    return g


sys.stdout.write(Planche([cadre(0.40, "p = 0,40 : on ne rejette pas", DOUX),
                          cadre(0.03, "p = 0,03 : on rejette", AJOUT)], ecart=26,
                         titre="La p-valeur est l'aire de la queue au-delà de la statistique observée").svg())
