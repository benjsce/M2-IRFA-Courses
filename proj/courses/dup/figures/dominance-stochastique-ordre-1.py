#!/usr/bin/env python3
r"""
dominance-stochastique-ordre-1.svg — deux fonctions de répartition, l'une sous l'autre.

L'exemple de la fiche : $(0,\tfrac12;100,\tfrac12)$ domine $(0,\tfrac34;100,\tfrac14)$.
Le geste de la fiche compare les deux répartitions : celle qui est partout au-dessous
domine. Entre 0 et 100 elles valent $\tfrac12$ et $\tfrac34$ ; l'écart, un quart, est la
masse déplacée de 0 vers 100. Ailleurs elles coïncident.

Usage : python courses/dup/figures/dominance-stochastique-ordre-1.py > dominance-stochastique-ordre-1.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT      # noqa: E402


def escalier(p0):
    """La répartition de (0, p0 ; 100, 1 - p0), de -15 à 118."""
    return [(-15, 0), (0, 0), (0, p0), (100, p0), (100, 1), (118, 1)]


f = Figure(xmin=-15, xmax=120, ymin=0, ymax=1.12, w=560, h=330,
           titre="La répartition du meilleur pari reste partout au-dessous de l'autre")
f.axes(xlab="résultat", ylab="F", xticks=(0, 50, 100), yticks=(0.5, 0.75, 1),
       fmt=lambda t: str(int(t)),
       fmt_y=lambda t: {0.5: "½", 0.75: "¾", 1: "1"}[t], croix=(0, 0))

f.courbe(escalier(0.75), couleur=AJOUT, epaisseur=2.2)
f.courbe(escalier(0.5), couleur=ACCENT, epaisseur=2.6)

f.mesure(60, 0.5, 0.75, couleur=DOUX, etiquette="¼ déplacé de 0 vers 100")
f.texte(50, 0.75, "(0, ¾ ; 100, ¼)", couleur=AJOUT, ancre="middle", dy=-9, gras=True,
        fond=True)
f.texte(50, 0.5, "(0, ½ ; 100, ½) : domine", couleur=ACCENT, ancre="middle", dy=20,
        gras=True, fond=True)

sys.stdout.write(f.svg())
