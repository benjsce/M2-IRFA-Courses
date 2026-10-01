#!/usr/bin/env python3
r"""
filtration.svg — l'information grandit : Ω se découpe de plus en plus finement.

Ce que la figure doit faire voir : 𝓕_s ⊂ 𝓕_t pour s ≤ t, c'est-à-dire qu'une information
acquise n'est jamais perdue ; à chaque date, ce qu'on sait se lit sur un découpage de Ω,
et le découpage d'une date affine celui de la précédente.

Le monde du cours : une pièce lancée en t = ½, une autre en t = 1 ; Ω = {PP, PF, FP, FF}.
Avant ½, on ne sait rien : un seul bloc, Ω. Entre ½ et 1, on connaît le premier lancer :
deux blocs. En 1, on connaît les deux : quatre blocs. Chaque cadre dessine Ω en carré, les
issues en quatre cases, et les traits épais séparent ce que l'information distingue.

Usage : python courses/cs/figures/filtration.py > filtration.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE   # noqa: E402

CASES = {"PP": (0, 1), "PF": (1, 1), "FP": (0, 0), "FF": (1, 0)}   # colonne = second lancer


def cadre(titre, sous_titre, coupe_premier, coupe_second):
    f = Figure(-0.1, 2.1, -0.75, 2.45, w=190, h=210, marges=(4, 4, 4, 4))
    # le carré Ω et ses issues
    f.courbe([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)], couleur=ACCENT, epaisseur=2.6)
    f.segment(1, 0, 1, 2, couleur=PALE, epaisseur=1.0)
    f.segment(0, 1, 2, 1, couleur=PALE, epaisseur=1.0)
    for w, (i, j) in CASES.items():
        f.texte(i + 0.5, j + 0.5, w, couleur=DOUX, ancre="middle", dy=5, taille=13)
    if coupe_premier:            # premier lancer connu : haut (P…) / bas (F…)
        f.courbe([(0, 1), (2, 1)], couleur=ACCENT, epaisseur=2.6)
    if coupe_second:             # second lancer connu : gauche (…P) / droite (…F)
        f.courbe([(1, 0), (1, 2)], couleur=ACCENT, epaisseur=2.6)
    f.texte(1, 2.45, titre, couleur=ENCRE, ancre="middle", dy=10, gras=True)
    f.texte(1, -0.75, sous_titre, couleur=ENCRE, ancre="middle", dy=-24, taille=12)
    return f


cadres = [cadre("t < ½", "rien n'est connu", False, False),
          cadre("½ ≤ t < 1", "le premier lancer", True, False),
          cadre("t = 1", "les deux lancers", True, True)]
for f, s in zip(cadres, ("𝓕_{t} = {∅, Ω}", "𝓕_{t} : 2 blocs", "𝓕_{1} : 4 blocs")):
    f.texte(1, -0.75, s, couleur=AJOUT, ancre="middle", dy=-6, gras=True, taille=12.5)

sys.stdout.write(Planche(cadres, signes=("⊂", "⊂"), ecart=34,
                         titre="Une filtration : 𝓕_s ⊂ 𝓕_t pour s ≤ t, le découpage de Ω s'affine").svg())
