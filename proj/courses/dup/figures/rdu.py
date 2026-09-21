#!/usr/bin/env python3
r"""
rdu.svg — les mêmes trois courbures, lues une fois sur $u$ et une fois sur $\varphi$.

La fiche laisse deux objets libres et dit que chacun porte une part de l'attitude. Le
dessin pose côte à côte les trois formes que prend chacun — concave, droite, convexe —
et laisse voir ce que la table ne peut pas montrer : à gauche seule la courbure compte,
puisque $u$ n'est définie qu'à une transformation affine près ; à droite la diagonale
est une frontière, puisque $\varphi$ est fixée, et une $\varphi$ concave passe forcément
au-dessus.

Les trois courbes sont $\sqrt{t}$, $t$ et $t^2$ sur les deux cadres. La racine est la
déformation que la source elle-même trace (L4 slide 13) et l'utilité du monde numérique
du cours ; le carré est sa symétrique, et ne sert qu'à montrer l'autre côté.

Usage : python courses/dup/figures/rdu.py > rdu.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

LARGEUR, HAUTEUR = 264, 300


def cadre(titre, xlab, ylab, xmax, fmt_x, zones=()):
    # marge gauche généreuse : dans une planche, l'étiquette d'axe se pose à gauche du
    # cadre, et une marge courte la ferait tomber dans l'entre-deux.
    g = Figure(xmin=0, xmax=xmax * 1.05, ymin=0, ymax=1.16,
               w=LARGEUR, h=HAUTEUR, marges=(48, 30, 42, 14))
    g.axes(xlab=xlab, ylab=ylab, xticks=(0, xmax), yticks=(1.0,),
           fmt=fmt_x, fmt_y=lambda t: "1")

    concave = lambda t: (t / xmax) ** 0.5
    droite = lambda t: t / xmax
    convexe = lambda t: (t / xmax) ** 2

    g.fonction(convexe, 0, xmax, couleur=AJOUT, epaisseur=2.2)
    g.fonction(droite, 0, xmax, couleur=DOUX, epaisseur=1.6, pointilles="5 4")
    g.fonction(concave, 0, xmax, couleur=ACCENT, epaisseur=2.6)

    # Les trois étiquettes sont posées aux mêmes abscisses sur les deux cadres : c'est
    # le même dessin lu deux fois, et le lecteur doit pouvoir passer de l'un à l'autre.
    g.texte(0.25 * xmax, concave(0.25 * xmax), "concave", couleur=ACCENT,
            ancre="start", dx=3, dy=-9, taille=11.5, gras=True, fond=True)
    g.texte(0.63 * xmax, droite(0.63 * xmax), titre[1], couleur=DOUX,
            ancre="end", dx=-3, dy=-8, taille=11.5, fond=True)
    g.texte(0.63 * xmax, convexe(0.63 * xmax), "convexe", couleur=AJOUT,
            ancre="start", dx=3, dy=15, taille=11.5, gras=True, fond=True)

    for x, y, mot, couleur in zones:
        g.texte(x * xmax, y, mot, couleur=couleur, ancre="middle", taille=11,
                fond=True)

    g.texte(0.5 * xmax, 1.16, titre[0], couleur=ENCRE, ancre="middle", dy=-4,
            taille=12.5, gras=True)
    return g


p = Planche(
    [cadre(("la forme de u", "linéaire"), "richesse", "u", 100.0,
           lambda t: str(int(t))),
     cadre(("la forme de φ", "identité"), "probabilité cumulée", "φ", 1.0,
           lambda t: str(int(t)),
           zones=((0.18, 0.30, "pessimisme", ACCENT),
                  (0.80, 0.71, "optimisme", AJOUT)))],
    ecart=34,
    titre="À gauche seule la courbure compte ; à droite la diagonale est une frontière")

sys.stdout.write(p.svg())
