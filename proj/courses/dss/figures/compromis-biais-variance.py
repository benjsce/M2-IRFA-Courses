#!/usr/bin/env python3
r"""
compromis-biais-variance.svg — les deux erreurs qui se croisent, et leur somme en U.

La fiche dit : « Quand le paramètre de pénalité augmente, le biais monte, la variance
descend, et l'erreur quadratique moyenne passe par un minimum avant de remonter »
[slide 54]. La source ne donne aucun chiffre, la figure n'en porte donc aucun : pas de
graduation sur les deux axes, seulement les formes et l'endroit où la somme est minimale.
Les courbes sont deux fonctions choisies pour avoir la bonne allure, pas un modèle.

Usage : python courses/dss/figures/compromis-biais-variance.py > compromis-biais-variance.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

# Deux allures, rien de plus : la variance décroît vers zéro, le biais au carré croît.
var = lambda l: 9.0 / (1.0 + 2.2 * l) ** 1.6
biais = lambda l: 0.55 * l ** 1.7
somme = lambda l: var(l) + biais(l)

L0, L1 = 0.0, 4.2
PAS = 0.002
LMIN = min((L0 + i * PAS for i in range(int((L1 - L0) / PAS) + 1)), key=somme)

f = Figure(xmin=-0.15, xmax=4.5, ymin=0, ymax=10.4, w=560, h=330,
           titre="Le biais monte, la variance descend, et leur somme passe par un minimum")

f.axes(xlab="pénalité", ylab="erreur")

f.segment(LMIN, 0, LMIN, somme(LMIN))

f.fonction(var, L0, L1, couleur=DOUX, epaisseur=2.0)
f.fonction(biais, L0, L1, couleur=AJOUT, epaisseur=2.0)
f.fonction(somme, L0, L1, couleur=ACCENT, epaisseur=2.6)
f.point(LMIN, somme(LMIN), couleur=ACCENT)

f.texte(0.45, var(0.45), "variance", couleur=DOUX, dx=6, dy=-8, gras=True)
f.texte(3.55, biais(3.55), "biais²", couleur=AJOUT, dx=6, dy=6, gras=True)
f.texte(2.9, somme(2.9), "erreur quadratique moyenne", couleur=ACCENT,
        ancre="end", dx=-4, dy=-12, gras=True)
f.texte(LMIN, 0, "le réglage qui minimise l’erreur",
        couleur=ENCRE, ancre="middle", dy=18, taille=11.5)

sys.stdout.write(f.svg())
