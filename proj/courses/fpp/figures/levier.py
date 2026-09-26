#!/usr/bin/env python3
r"""
levier.svg — deux bilans, avant et après une baisse de l'actif.

L'exemple de la fiche : un actif de 100 financé par 30 de capitaux propres et 70 de
dette, soit $l=3{,}33$. Si l'actif perd 10 %, il vaut 90 ; la dette ne bouge pas, et toute
la perte tombe sur les capitaux propres, qui passent de 30 à 20 : $-33\,\%$, soit $l$ fois
$-10\,\%$. C'est l'identité de la fiche quand le rendement de la dette est nul. Le choc de
10 % est choisi pour le dessin ; la fiche le reprend dans « Retrouver la formule ».

Usage : python courses/fpp/figures/levier.py > levier.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402


def bilan(titre, A, E, D, note):
    g = Figure(xmin=0, xmax=2.4, ymin=0, ymax=118, w=250, h=300, marges=(14, 30, 30, 14))
    g.barre(0.7, A, 0.8, couleur=DOUX, opacite=0.45)
    g.texte(0.7, A / 2, "actif %d" % A, couleur=ENCRE, ancre="middle", gras=True)
    g.barre(1.7, D, 0.8, couleur=DOUX, opacite=0.25)
    g.barre(1.7, D + E, 0.8, couleur=ACCENT, opacite=0.75, y0=D)
    g.texte(1.7, D / 2, "dette %d" % D, couleur=ENCRE, ancre="middle")
    g.texte(1.7, D + E / 2, "E = %d" % E, couleur=ENCRE, ancre="middle", dy=4, gras=True)
    g.courbe([(0.2, 0), (2.2, 0)], couleur=DOUX, epaisseur=1.2)
    g.texte(1.2, 118, titre, couleur=ENCRE, ancre="middle", dy=-10, gras=True)
    g.texte(1.2, 0, note, couleur=ACCENT, ancre="middle", dy=20, gras=True)
    return g


p = Planche([bilan("avant", 100, 30, 70, "l = 100 / 30 = 3,33"),
             bilan("l'actif perd 10 %", 90, 20, 70, "E : −33 % = 3,33 × (−10 %)")],
            signes=("→",), ecart=40,
            titre="La dette ne bouge pas : toute la perte de l'actif tombe sur les capitaux propres")
sys.stdout.write(p.svg())
