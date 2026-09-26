#!/usr/bin/env python3
r"""
option.svg — un call de strike K à maturité T, dans deux scénarios : si S_T > K, le
détenteur exerce et gagne S_T − K ; si S_T < K, il n'exerce pas et ne reçoit rien.

Usage : python courses/fpp/figures/option.py > option.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
f = Figure(xmin=-0.1, xmax=2.05, ymin=70, ymax=130, w=560, h=300,
           titre="Le détenteur n'exerce que si S_T > K : il reçoit (S_T − K)^+")
f.axes(xlab="temps", ylab="prix de l'action", xticks=(0, 1), yticks=(100,),
       fmt=lambda t: "t" if t == 0 else "T", fmt_y=lambda t: "K")
f.segment(0, 100, 2.0, 100)
f.texte(2.0, 100, "strike K", couleur=DOUX, ancre="end", dy=-6, taille=12)
f.courbe([(0, 100), (0.3, 104), (0.55, 99), (0.8, 111), (1, 120)], couleur=ACCENT, epaisseur=2.2)
f.courbe([(0, 100), (0.25, 97), (0.5, 101), (0.75, 90), (1, 80)], couleur=AJOUT, epaisseur=2.2)
f.point(1, 120, couleur=ACCENT)
f.point(1, 80, couleur=AJOUT)
f.mesure(1.06, 100, 120, couleur=ACCENT, etiquette="S_{T} > K : exerce, gagne S_{T} − K")
f.texte(1, 80, "S_{T} < K : n'exerce pas, reçoit 0", couleur=AJOUT, dx=12, dy=4, gras=True)
sys.stdout.write(f.svg())
