#!/usr/bin/env python3
r"""
combinaison-d-options.svg — quatre payoffs construits avec des options, en fonction du
prix final : l'écart de calls 90–110, plafonné ; le straddle de strike 100, en V ; le
strangle 90–110, en V à fond plat ; le papillon 90–100–110, qui ne paie qu'autour de 100.

Usage : python courses/fpp/figures/combinaison-d-options.py > combinaison-d-options.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

p = lambda x: max(x, 0.0)
FORMES = [
    ("écart de calls", lambda s: p(s - 90) - p(s - 110), ACCENT),
    ("straddle", lambda s: abs(s - 100), AJOUT),
    ("strangle", lambda s: p(90 - s) + p(s - 110), DOUX),
    ("papillon", lambda s: p(s - 90) - 2 * p(s - 100) + p(s - 110), ENCRE),
]
cadres = []
for nom, g, c in FORMES:
    f = Figure(xmin=70, xmax=130, ymin=-2, ymax=32, w=180, h=210, marges=(26, 28, 30, 6))
    f.axes(xticks=(80, 100, 120), yticks=(0, 10, 20, 30), fmt=lambda t: "%d" % t)
    f.courbe([(s / 2, g(s / 2)) for s in range(140, 261)], couleur=c, epaisseur=2.6)
    f.texte(100, 32, nom, ancre="middle", dy=-12, couleur=c, gras=True, taille=12)
    cadres.append(f)
sys.stdout.write(Planche(cadres, ecart=16,
                 titre="Des calls et des puts additionnés dessinent la forme de paiement voulue").svg())
