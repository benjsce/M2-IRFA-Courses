#!/usr/bin/env python3
r"""
processus-elementaire.svg — un escalier dont chaque marche est décidée à son départ.

Ce que la figure doit faire voir : X_t = Σ F_{t_i} 1_{[t_i, t_{i+1}[}(t) est constant sur
chaque intervalle [t_i, t_{i+1}[, et la hauteur F_{t_i} de la marche est une variable
aléatoire connue à la date t_i où la marche commence — pas avant.

Le monde du cours : la mise d'un joueur sur [0, 1], avec t₁ = 0, t₂ = ½, t₃ = T = 1. Il
mise F_{t₁} = 1 jusqu'à ½ ; en ½ une pièce est lancée, et il mise F_{t₂} = 2 si pile,
0 si face. Les deux trajectoires coïncident sur [0, ½[ et se séparent en ½ ; chaque marche
est fermée à gauche (rond plein) et ouverte à droite (rond vide). En T, la somme est vide :
X_T = 0.

Usage : python courses/cs/figures/processus-elementaire.py > processus-elementaire.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE, FOND   # noqa: E402

DATES = (0.0, 0.5, 1.0)
TRAJ = {"pile en ½": (1, 2), "face en ½": (1, 0)}
fr = lambda v: ("%g" % v).replace(".", ",")

f = Figure(-0.05, 1.25, 0, 2.6, w=580, h=330, marges=(40, 14, 46, 16),
           titre="X_t = Σ F_{t_i} 1_{[t_i, t_{i+1}[}(t) : chaque marche est connue à son départ")
f.axes(yticks=(1, 2), fmt=fr, croix=(0, 0))
f.texte(1.25, 0, "t", couleur=DOUX, ancre="end", dy=33)
for x, s in zip(DATES, ("t₁ = 0", "t₂ = ½", "t₃ = T = 1")):
    f.segment(x, 0, x, -0.05, couleur=DOUX, epaisseur=1.2, pointilles=None)
    f.texte(x, 0, s, couleur=DOUX, ancre="start" if x == 0 else "middle", dx=5 if x == 0 else 0, dy=18)
f.segment(0.5, 0, 0.5, 2.4, couleur=PALE, epaisseur=1.2)


def marche(x0, x1, h, couleur):
    f.courbe([(x0, h), (x1, h)], couleur=couleur, epaisseur=3.2)
    f.point(x0, h, couleur=couleur, r=4.4)
    f.point(x1, h, couleur=couleur, r=4.6)
    f.point(x1, h, couleur=FOND, r=2.8)


marche(0.0, 0.5, 1, ENCRE)
marche(0.5, 1.0, 2, ACCENT)
marche(0.5, 1.0, 0, AJOUT)
f.texte(0.25, 1, "F_{t₁} = 1, connu en 0", couleur=ENCRE, ancre="middle", dy=-10, gras=True)
f.texte(0.75, 2, "F_{t₂} = 2 si pile en ½", couleur=ACCENT, ancre="middle", dy=-10, gras=True)
f.texte(0.75, 0, "F_{t₂} = 0 si face en ½", couleur=AJOUT, ancre="middle", dy=-10, gras=True)
f.texte(0.5, 2.4, "la pièce est lancée en ½ : F_{t₂} est connu en t₂", couleur=ENCRE, ancre="middle", dy=-4, taille=12)
f.texte(1.0, 0, "X_{T} = 0", couleur=DOUX, dx=10, dy=-10, taille=12)

sys.stdout.write(f.svg())
