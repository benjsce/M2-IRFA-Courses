#!/usr/bin/env python3
r"""
taux-forward.svg — le taux forward bouche le trou.

Ce que la figure doit faire voir : deux façons de placer de t à S, deux choses connues
(le taux à deux ans, le taux à un an) et une inconnue, le taux de la seconde année ; le
taux forward est le bloc qui manque pour que les deux lignes rapportent autant.

Chaque bloc a pour largeur une durée et pour hauteur un taux : son aire est ce qu'il
rapporte, puisqu'en capitalisation continue taux × durée s'additionnent. En haut, 5 % sur
deux ans, aire 10 %. En bas, 4 % sur la première année, aire 4 %, puis le trou, sur la
seconde année : pour faire aussi 10 %, il doit avoir une aire de 6 %, donc une hauteur de
6 %. Les taux sortent des prix de la fiche, 0,9608 et 0,9048.

Usage : python courses/fpp/figures/taux-forward.py > taux-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

P1, P2 = 0.9608, 0.9048
R1 = -math.log(P1) * 100                 # 4 % par an sur un an
R2 = -math.log(P2) / 2 * 100             # 5 % par an sur deux ans
F12 = math.log(P1 / P2) * 100            # 6 % pour la seconde année
pc = lambda v: "%.0f %%" % v

t, T, S = 1.0, 4.4, 7.8                  # une année = 3,4 unités
k = 0.34                                 # hauteur par point de pourcentage
yA, yB = 3.1, 0.35                       # bases des deux lignes

g = Figure(xmin=0, xmax=10.6, ymin=-0.8, ymax=5.9, w=640, h=360, marges=(8, 8, 8, 8),
           titre="Le taux forward bouche le trou : les deux lignes doivent rapporter autant")
g.axe_temps(0, 0.4, 10.3, [(t, "t"), (T, "T"), (S, "S")])


def bloc(x0, x1, y0, taux, couleur, pointilles=None, remplir=True):
    y1 = y0 + k * taux
    if remplir:
        g.barre((x0 + x1) / 2, y1, x1 - x0, couleur=couleur, opacite=0.16, y0=y0)
    g.courbe([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], couleur=couleur,
             epaisseur=1.8, pointilles=pointilles)
    return y1


# en haut : d'un coup, de t à S, au taux à deux ans (connu)
hA = bloc(t, S, yA, R2, AJOUT)
g.texte(t, hA + 0.35, "placer d'un coup, de t à S", couleur=AJOUT, gras=True, taille=12.5)
g.texte((t + S) / 2, yA + 0.95, pc(R2) + " par an pendant 2 ans", taille=13, ancre="middle")
g.texte((t + S) / 2, yA + 0.35, "connu aujourd'hui", couleur=DOUX, taille=11.5, ancre="middle")
g.texte(S + 0.25, yA + 0.62, "= " + pc(2 * R2), couleur=AJOUT, gras=True, taille=14)

# en bas : jusqu'en T au taux à un an (connu), puis le trou, de T à S
hB1 = bloc(t, T, yB, R1, ACCENT)
hB2 = bloc(T, S, yB, F12, ENCRE, pointilles="5 4", remplir=False)
g.texte(t, hB2 + 0.3, "placer jusqu'en T, puis replacer jusqu'en S", couleur=ACCENT,
        gras=True, taille=12.5)
g.texte((t + T) / 2, yB + 0.72, pc(R1) + " pendant 1 an", taille=13, ancre="middle")
g.texte((t + T) / 2, yB + 0.22, "connu aujourd'hui", couleur=DOUX, taille=11.5, ancre="middle")
g.texte((T + S) / 2, yB + 1.22, "le trou : F pendant 1 an", taille=13, ancre="middle", gras=True)
g.texte((T + S) / 2, yB + 0.62, "F = %s − %s = %s" % (pc(2 * R2), pc(R1), pc(F12)),
        taille=12.5, ancre="middle")
g.texte(S + 0.25, yB + 0.62, "= " + pc(R1) + " + F", couleur=ACCENT, gras=True, taille=14)

# les deux totaux doivent être égaux
g.texte(S + 0.25, 2.25, "égaux", couleur=DOUX, taille=12)
g.courbe([(S + 0.55, yA + 0.35), (S + 0.55, 2.55)], couleur=DOUX, epaisseur=1.2)
g.courbe([(S + 0.55, 1.95), (S + 0.55, yB + 0.95)], couleur=DOUX, epaisseur=1.2)

sys.stdout.write(g.svg())
