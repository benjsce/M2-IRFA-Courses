#!/usr/bin/env python3
r"""
forward-action.svg — les deux jambes du forward sur action, avec dividendes.

La fiche : $F(t,T)=S_t\Phi/P(t,T)$, avec $\Phi=1-\sum_i d_i$ pour des dividendes
proportionnels. L'acheteur à terme reçoit l'action en T mais pas les dividendes versés
avant : la jambe « action » vaut donc $S_t\Phi$ en t, et non $S_t$. La jambe
« argent » vaut $F(t,T)P(t,T)$. Le contrat ne coûte rien à la signature : les deux
sont égales, et c'est la formule. Deux dividendes, pour que la somme se voie.

Ce que la figure doit faire voir : la jambe action est connue aujourd'hui (le comptant,
les dividendes, donc Φ) ; le seul montant cherché est F(t,T), en pointillé, que l'égalité
des deux jambes en t détermine.

Usage : python courses/fpp/figures/forward-action.py > forward-action.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T1, T2, T = 3.0, 4.9, 6.6, 8.6
g = Figure(xmin=0, xmax=10, ymin=-4.6, ymax=4.9, w=640, h=350, marges=(8, 8, 8, 8),
           titre="Forward sur action : la jambe action perd les dividendes d'avant T")
g.axe_temps(0, 1.3, 9.7, [(t, "t"), (T, "T")])
for x, s in ((T1, "T_{1}"), (T2, "T_{2}")):
    g.texte(x, 0, s, couleur=DOUX, taille=12.5, ancre="middle", dy=21)
    g.courbe([(x, -0.14), (x, 0.14)], couleur=DOUX, epaisseur=1.3)

g.texte(0.05, 3.2, "action", taille=12, gras=True, couleur=AJOUT)
g.texte(0.05, -3.4, "argent", taille=12, gras=True, couleur=ACCENT)

# les dividendes : versés au détenteur, pas à l'acheteur à terme
for x, s in ((T1, "d_{1}"), (T2, "d_{2}")):
    g.fleche(x, 0.45, x, 1.45, couleur=DOUX, epaisseur=1.4, pointilles="3 3")
    g.texte(x, 0.95, s, couleur=DOUX, taille=13, dx=7)
g.texte((T1 + T2) / 2, 1.9, "versés avant T, pas livrés", couleur=DOUX, taille=11,
        ancre="middle")

# jambe action : 1 action reçue en T
g.fleche(T, 0.45, T, 2.5, couleur=AJOUT, epaisseur=2)
g.texte(T, 1.5, "1 action", couleur=AJOUT, gras=True, taille=13.5, dx=9)
g.fleche(T - 0.2, 3.05, t + 0.95, 3.05, couleur=AJOUT, courbure=22)
g.texte(t, 2.95, "Sₜ·Φ", couleur=AJOUT, gras=True, taille=13.5, ancre="middle")
g.texte(t, 2.25, "Φ = 1 − d_{1} − d_{2}", couleur=AJOUT, taille=12, ancre="middle")
g.texte(t, 1.55, "connu aujourd'hui", couleur=DOUX, taille=11.5, ancre="middle")

# jambe argent : F(t,T) payé en T
g.fleche(T, -1.25, T, -3.1, couleur=ACCENT, epaisseur=2, pointilles="5 4")
g.texte(T, -2.0, "F(t,T)", couleur=ACCENT, gras=True, taille=13.5, dx=9)
g.texte(T, -2.6, "cherché", couleur=ACCENT, taille=11.5, dx=9)
g.fleche(T - 0.2, -3.5, t + 1.4, -3.5, couleur=ACCENT, courbure=-20)
g.texte(t, -3.4, "F(t,T)·P(t,T)", couleur=ACCENT, gras=True, taille=13.5, ancre="middle")
g.texte(t, -1.75, "égales à la signature", couleur=ENCRE, taille=12, ancre="middle")

sys.stdout.write(g.svg())
