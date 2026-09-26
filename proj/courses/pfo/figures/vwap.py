#!/usr/bin/env python3
r"""
vwap.svg — deux exécutions, leurs volumes, et les deux moyennes qu'on peut en tirer.

L'exemple de la fiche : 300 titres échangés à 100 et 100 titres à 101. Chaque barre porte
le volume d'une exécution ; le VWAP, 100,25, tombe près de la grosse barre, alors que la
moyenne simple des deux prix, 100,50, tombe au milieu comme si les deux exécutions
pesaient autant.

Usage : python courses/pfo/figures/vwap.py > vwap.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

EXEC = [(100.0, 300), (101.0, 100)]
VWAP = sum(p * v for p, v in EXEC) / sum(v for _, v in EXEC)      # 100,25
SIMPLE = sum(p for p, _ in EXEC) / len(EXEC)                       # 100,50

f = Figure(xmin=99.55, xmax=101.45, ymin=0, ymax=380, w=560, h=330,
           titre="Le VWAP penche vers l'exécution la plus grosse")
f.axes(xlab="prix d'exécution", ylab="volume", xticks=(100, 100.25, 100.5, 101),
       yticks=(100, 300), fmt=lambda t: ("%g" % t).replace(".", ","),
       fmt_y=lambda t: str(int(t)))

for p, v in EXEC:
    f.barre(p, v, 0.14, couleur=DOUX, opacite=0.6)
    f.texte(p, v, "%d titres" % v, couleur=DOUX, ancre="middle", dy=-6, taille=11.5)

f.segment(VWAP, 0, VWAP, 350, couleur=ACCENT, epaisseur=2.2, pointilles=None)
f.texte(VWAP, 350, "VWAP 100,25", couleur=ACCENT, ancre="middle", dy=-6, gras=True)
f.segment(SIMPLE, 0, SIMPLE, 250, couleur=AJOUT, epaisseur=1.8)
f.texte(SIMPLE, 250, "moyenne simple 100,50", couleur=AJOUT, dx=6, dy=-6, taille=11.5,
        fond=True)

sys.stdout.write(f.svg())
