#!/usr/bin/env python3
r"""
propriete-de-la-tour.svg — deux chemins, même arrivée : moyenner en deux temps ou d'un coup.

Ce que la figure doit faire voir : conditionner d'abord par l'information riche 𝒢, puis
par la pauvre 𝒢', donne la même chose que conditionner directement par 𝒢'.

Le monde du cours : deux lancers, X le nombre de piles (2, 1, 1, 0 sur PP, PF, FP, FF),
𝒢 l'information du premier lancer. 𝒢' est ici l'information vide, celle qui ne
distingue aucune issue : conditionner par elle, c'est prendre l'espérance. La ligne du
haut moyenne X sur chaque atome de 𝒢 (1,5 et 0,5), puis moyenne le résultat sur tout Ω ;
la ligne du bas moyenne X sur tout Ω d'un coup. Les deux arrivent à 1 sur chaque issue.

Usage : python courses/cs/figures/propriete-de-la-tour.py > propriete-de-la-tour.svg
Dépendance : aucune.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, Colonne, ACCENT, AJOUT, DOUX, ENCRE   # noqa: E402

ISSUES = ["PP", "PF", "FP", "FF"]
X = [Fr(w.count("P")) for w in ISSUES]


def moyenne_par(atomes, v):
    out = list(v)
    for A in atomes:
        m = sum(v[i] for i in A) / len(A)        # issues équiprobables
        for i in A:
            out[i] = m
    return out


G = [[0, 1], [2, 3]]                 # premier lancer
G_VIDE = [[0, 1, 2, 3]]              # aucune information
EG = moyenne_par(G, X)
EEG = moyenne_par(G_VIDE, EG)
EG2 = moyenne_par(G_VIDE, X)
assert EEG == EG2 == [Fr(1)] * 4 and EG == [Fr(3, 2), Fr(3, 2), Fr(1, 2), Fr(1, 2)]
fr = lambda q: ("%g" % float(q)).replace(".", ",")


def cadre(valeurs, titre, couleur, coupures=()):
    f = Figure(0, 1, -0.32, 2.5, w=210, h=170, marges=(8, 22, 6, 8))
    f.courbe([(0, 0), (1, 0)], couleur=DOUX, epaisseur=1.2)
    for k, v in enumerate(valeurs):
        x = (k + 0.5) / 4
        f.barre(x, float(v), 0.24, couleur=couleur, opacite=0.4, y0=0)
        f.texte(x, float(v), fr(v), couleur=couleur, ancre="middle", dy=-5, taille=12, gras=True)
        f.texte(x, 0, ISSUES[k], couleur=DOUX, ancre="middle", dy=15, taille=11)
    for c in coupures:
        f.segment(c, -0.3, c, 2.3, couleur=ENCRE, epaisseur=1.2)
    f.texte(0.5, 2.5, titre, couleur=ENCRE, ancre="middle", dy=-6, gras=True, taille=12.5)
    return f


haut = Planche([cadre(X, "X", ACCENT),
                cadre(EG, "E(X|𝒢)", AJOUT, coupures=(0.5,)),
                cadre(EEG, "E(E(X|𝒢)|𝒢')", ENCRE)], signes=("→", "→"), ecart=34)
# la ligne du bas saute l'étape du milieu : une seule flèche longue à sa place
saut = Figure(0, 1, -0.32, 2.5, w=210 + 2 * 34, h=170, marges=(0, 22, 6, 0))
saut.fleche(0.04, 0.9, 0.96, 0.9, couleur=DOUX, epaisseur=1.6)
saut.texte(0.5, 0.9, "moyenner sur Ω entier", couleur=DOUX, ancre="middle", dy=-10, taille=12)
bas = Planche([cadre(X, "X", ACCENT), saut, cadre(EG2, "E(X|𝒢')", ENCRE)], ecart=0)

sys.stdout.write(Colonne(
    [haut, bas],
    intitules=["En deux temps : moyenner sur chaque atome de 𝒢, puis sur ceux de 𝒢'",
               "D'un coup, sur les atomes de 𝒢' — ici l'information vide, un seul atome : même arrivée"],
    titre="E(E(X|𝒢)|𝒢') = E(X|𝒢') : moyenner en deux temps ou d'un coup").svg())
