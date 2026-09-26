#!/usr/bin/env python3
r"""
mesure-risque-neutre.svg — des prix d'états à la probabilité risque-neutre.

Ce que la figure doit faire voir : les prix d'aujourd'hui des flux « 1 dans cet état,
0 ailleurs » (les prix d'états) sont positifs, et leur somme est le prix de l'euro
certain, P(t,T) ; divisés par P(t,T), ils deviennent des nombres positifs de somme 1 :
une probabilité, Q. À gauche, les prix d'états ; à droite, les mêmes barres divisées
par P(t,T).

Trois états, pour l'exemple : baisse, milieu, hausse. Les probabilités 0,25, 0,45 et
0,30 sont choisies pour le dessin ; P(t,t+1) = 0,9608 est celui du cours, et chaque
prix d'état en est le produit par la probabilité.

Usage : python courses/fpp/figures/mesure-risque-neutre.py > mesure-risque-neutre.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

P = 0.9608
q = (0.25, 0.45, 0.30)
etats = ("baisse", "milieu", "hausse")
prix = [round(P * x, 4) for x in q]
virg = lambda v, n: ("%.*f" % (n, v)).replace(".", ",")


def cadre(valeurs, couleur, titre, somme, n):
    g = Figure(xmin=0, xmax=3.6, ymin=-0.13, ymax=0.66, w=300, h=270, marges=(10, 8, 8, 8))
    g.texte(1.8, 0.62, titre, couleur=couleur, gras=True, taille=12.5, ancre="middle")
    g.courbe([(0.2, 0), (3.4, 0)], couleur=DOUX, epaisseur=1.2)
    for k, (v, nom) in enumerate(zip(valeurs, etats)):
        x = 0.7 + 1.1 * k
        g.barre(x, v, 0.62, couleur=couleur, opacite=0.8, y0=0)
        g.texte(x, v + 0.02, virg(v, n), taille=12, ancre="middle")
        g.texte(x, -0.06, nom, couleur=DOUX, taille=11.5, ancre="middle")
    g.texte(1.8, -0.115, somme, couleur=ENCRE, gras=True, taille=12.5, ancre="middle")
    return g


gauche = cadre(prix, ACCENT, "prix d'états, aujourd'hui", "somme = P(t,T) = 0,9608", 4)
droite = cadre(q, AJOUT, "divisés par P(t,T) : Q", "somme = 1", 2)
sys.stdout.write(Planche([gauche, droite], signes=("→",), ecart=40,
                         titre="Des prix d'états positifs, divisés par P(t,T) : "
                               "une probabilité").svg())
