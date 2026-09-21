#!/usr/bin/env python3
r"""
assurance-de-portefeuille.svg — le plancher plat, et le meilleur état plus haut.

La fiche dit en trois phrases ce qu'un profil montre d'un coup : par rapport à l'utilité
espérée, la pondération par rang relève la richesse dans le pire état et dans le meilleur,
et abaisse celle du milieu pour les financer. Le dessin pose les deux profils sur le même
repère ; le segment bas devenu plat est l'assurance dont parle la rubrique.

Les deux profils sont les seuls nombres que la fiche donne, repris tels quels : les
recalculer demanderait les prix d'état et la déformation, que cette page ne nomme pas.

Usage : python courses/dup/figures/assurance-de-portefeuille.py > assurance-de-portefeuille.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

EU = (0.328, 0.903, 1.577)       # l'exemple minimal de la fiche
RDU = (0.437, 0.437, 1.845)
ETATS = (1, 2, 3)

f = Figure(xmin=0.6, xmax=3.6, ymin=0, ymax=2.1, w=560, h=330,
           titre="La pondération par rang aplatit le bas du profil et relève le haut")

f.axes(xlab="état", ylab="richesse",
       xticks=ETATS, yticks=(0.5, 1.0, 1.5, 2.0),
       fmt=lambda t: "s%d" % t,
       fmt_y=lambda t: ("%.1f" % t).replace(".", ","))

for s in ETATS:
    f.segment(s, 0, s, max(EU[s - 1], RDU[s - 1]))

f.courbe(list(zip(ETATS, EU)), couleur=AJOUT, epaisseur=1.8, pointilles="5 4")
f.courbe(list(zip(ETATS, RDU)), couleur=ACCENT, epaisseur=2.8)

for s in ETATS:
    f.point(s, EU[s - 1], couleur=AJOUT, r=3.2)
    f.point(s, RDU[s - 1], couleur=ACCENT)

f.texte(1.5, (RDU[0] + RDU[1]) / 2, "le plancher est plat", couleur=ACCENT,
        ancre="middle", dy=-11, gras=True, fond=True)
f.texte(2, EU[1], "utilité espérée", couleur=AJOUT, ancre="middle", dy=-12,
        taille=11.5, fond=True)
f.texte(3, RDU[2], "plus haut dans le meilleur état", couleur=ENCRE, ancre="end",
        dx=-8, dy=-6, taille=11.5, fond=True)

sys.stdout.write(f.svg())
