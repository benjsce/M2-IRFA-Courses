#!/usr/bin/env python3
r"""
obligation-in-fine.svg — le prix B(r*, r) d'une obligation de coupon r* en fonction du taux
du marché r : il vaut 1 exactement quand r = r*, plus quand r < r*, moins quand r > r*.
Tracé avec r* = 5 % sur deux ans ; aucun nombre écrit.

Usage : python courses/fpp/figures/obligation-in-fine.py > obligation-in-fine.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

RS, N = 0.05, 2


def B(r):
    return RS * sum((1 + r) ** -i for i in range(1, N + 1)) + (1 + r) ** -N


f = Figure(xmin=0, xmax=0.10, ymin=0.9, ymax=1.11, w=560, h=320,
           titre="B(r*, r) = 1 quand r = r* : au-dessus du pair si r < r*, en dessous si r > r*")
f.axes(xlab="taux du marché r", ylab="prix B(r*, r)", xticks=(0.05,), yticks=(1.0,),
       fmt=lambda t: "r*", fmt_y=lambda t: "1")
f.segment(0, 1, 0.10, 1)
f.segment(0.05, 0.9, 0.05, 1)
f.fonction(B, 0, 0.10, couleur=ACCENT, epaisseur=2.6)
f.point(0.05, 1, couleur=ENCRE)
f.texte(0.003, 1.0, "r < r* : au-dessus du pair, B > 1", couleur=DOUX, dy=-8, taille=12)
f.texte(0.097, 1.0, "r > r* : en dessous du pair, B < 1", couleur=DOUX, ancre="end", dy=17, taille=12)
f.texte(0.05, 1, "au pair", couleur=ENCRE, dx=8, dy=-8, taille=12)
sys.stdout.write(f.svg())
