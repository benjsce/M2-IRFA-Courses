#!/usr/bin/env python3
r"""
existence-on-a-compact.svg — the three ways a minimum can be missing or present.

Ce que la figure doit faire voir : la même question — y a-t-il un point le plus bas ? —
sur trois domaines. Sur toute la droite, f(x) = x descend sans fin. Sur la demi-droite
x > 0, 1/x s'approche de 0 sans l'atteindre : les points qui minimisent s'enfuient.
Sur l'intervalle fermé et borné [1, 3], la même 1/x a un point le plus bas, en x = 3.
Ce sont les exemples des notes (§1.2), le dernier restreint à un compact.

Usage : python courses/ods/figures/existence-on-a-compact.py > existence-on-a-compact.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402


def cadre(titre):
    g = Figure(xmin=-0.3, xmax=4.3, ymin=-1.6, ymax=3.4, w=220, h=230, marges=(12, 30, 12, 12))
    g.axes(croix=(0, 0))
    g.texte(0.12, 3.2, titre, taille=12.5, gras=True, couleur=ENCRE, fond=True)
    return g


# 1. toute la droite : f(x) = x
g1 = Figure(xmin=-2.3, xmax=2.3, ymin=-2.4, ymax=2.6, w=220, h=230, marges=(12, 30, 12, 12))
g1.axes(croix=(0, 0))
g1.texte(-2.2, 2.4, "Ω = the whole line", taille=12.5, gras=True, fond=True)
g1.fonction(lambda x: x, -2.1, 2.1, couleur=AJOUT, epaisseur=2.2)
g1.fleche(-1.6, -1.6, -2.1, -2.1, couleur=AJOUT, epaisseur=2.2)
g1.texte(0.15, -1.55, "f(x) = x", couleur=AJOUT, taille=12)
g1.texte(0.15, -2.05, "goes down forever", couleur=DOUX, taille=11.5)

# 2. la demi-droite ouverte : 1/x sur x > 0
g2 = cadre("Ω = {x > 0}")
g2.fonction(lambda x: 1 / x, 0.31, 4.2, couleur=AJOUT, epaisseur=2.2)
g2.segment(0, 0, 4.2, 0, couleur=AJOUT, epaisseur=1.4, pointilles="4 3")
g2.fleche(3.3, 0.55, 4.15, 0.3, couleur=AJOUT, epaisseur=1.4)
g2.texte(1.1, 1.75, "f(x) = 1/x", couleur=AJOUT, taille=12)
g2.texte(0.2, -0.55, "infimum 0,", couleur=DOUX, taille=11.5)
g2.texte(0.2, -1.05, "never reached", couleur=DOUX, taille=11.5)

# 3. l'intervalle [1, 3] : le minimum est atteint en 3
g3 = cadre("Ω = [1, 3]")
g3.fonction(lambda x: 1 / x, 0.31, 4.2, couleur=PALE, epaisseur=1.4)
g3.fonction(lambda x: 1 / x, 1, 3, couleur=ACCENT, epaisseur=3)
g3.segment(1, 0, 1, 1, couleur=PALE)
g3.segment(3, 0, 3, 1 / 3, couleur=PALE)
g3.point(3, 1 / 3, couleur=ACCENT, r=4.5)
g3.texte(3, 0.85, "minimum 1/3", couleur=ACCENT, taille=12, gras=True, ancre="middle")
g3.texte(1, -0.55, "1", couleur=DOUX, taille=11.5, ancre="middle")
g3.texte(3, -0.55, "3", couleur=DOUX, taille=11.5, ancre="middle")
g3.texte(0.2, -1.05, "attained at x = 3", couleur=DOUX, taille=11.5)

sys.stdout.write(Planche([g1, g2, g3], ecart=24,
                         titre="Unbounded, not closed, compact: only the last one is sure to have a minimum").svg())
