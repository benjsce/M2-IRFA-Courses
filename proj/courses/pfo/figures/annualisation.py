#!/usr/bin/env python3
r"""
annualisation.svg — la moyenne croît comme le temps, l'écart type comme sa racine.

L'exemple de la fiche : un rendement espéré journalier de 0,04 % et une volatilité
journalière de 1 %. Sur $n$ séances, la moyenne vaut $0{,}04\,\%\times n$ et l'écart type
$1\,\%\times\sqrt n$ ; à 252 séances, 10,08 % et 15,87 %.

Usage : python courses/pfo/figures/annualisation.py > annualisation.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

MU, SIG, AN = 0.04, 1.0, 252

f = Figure(xmin=0, xmax=270, ymin=0, ymax=19, w=560, h=320,
           titre="Sur un an, l'écart type est multiplié par √252 ≈ 15,9, la moyenne par 252")
f.axes(xlab="nombre de séances n", ylab="en %", xticks=(0, 63, 126, 189, 252),
       yticks=(5, 10.08, 15.87), fmt=lambda t: "%d" % t,
       fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.fonction(lambda n: SIG * math.sqrt(n), 0, AN, n=300, couleur=ACCENT, epaisseur=2.6)
f.fonction(lambda n: MU * n, 0, AN, couleur=AJOUT, epaisseur=2.4)
f.segment(AN, 0, AN, SIG * math.sqrt(AN))
f.point(AN, SIG * math.sqrt(AN), couleur=ACCENT)
f.point(AN, MU * AN, couleur=AJOUT)
# ancrée au-dessus et à gauche d'un point de la courbe : à gauche, la courbe concave
# descend, le texte s'étend donc dans le vide, quelle que soit la police
f.texte(180, SIG * math.sqrt(180), "écart type : 1 % × √n", couleur=ACCENT, ancre="end",
        dx=-6, dy=-8, gras=True, fond=True)
f.texte(160, MU * 160, "moyenne : 0,04 % × n", couleur=AJOUT, dx=6, dy=16, gras=True,
        fond=True)

sys.stdout.write(f.svg())
