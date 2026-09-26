#!/usr/bin/env python3
r"""
combinaison-d-options.svg — quatre payoffs construits avec des options : l'écart de calls
(S − K₁)^+ − (S − K₂)^+, le straddle |S − K|, le strangle (K₁ − S)^+ + (S − K₂)^+, le
papillon (S − K₁)^+ − 2(S − K₂)^+ + (S − K₃)^+.

Usage : python courses/fpp/figures/combinaison-d-options.py > combinaison-d-options.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402
p = lambda x: max(x, 0.0)
FORMES = [
    ("écart de calls", lambda s: p(s - 90) - p(s - 110), ACCENT, {90: "K₁", 110: "K₂"}, "(S − K_{1})^{+} − (S − K_{2})^{+}"),
    ("straddle", lambda s: abs(s - 100), AJOUT, {100: "K"}, "|S − K|"),
    ("strangle", lambda s: p(90 - s) + p(s - 110), DOUX, {90: "K₁", 110: "K₂"}, "(K_{1} − S)^{+} + (S − K_{2})^{+}"),
    ("papillon", lambda s: p(s - 90) - 2 * p(s - 100) + p(s - 110), ENCRE, {90: "K₁", 100: "K₂", 110: "K₃"},
     "(S−K_{1})^{+} − 2(S−K_{2})^{+} + (S−K_{3})^{+}"),
]
cadres = []
for nom, g, c, ticks, formule in FORMES:
    f = Figure(xmin=70, xmax=130, ymin=-2, ymax=32, w=200, h=230, marges=(10, 28, 50, 6))
    f.axes(xticks=tuple(ticks), fmt=lambda t, ticks=ticks: ticks[t])
    f.courbe([(s / 2, g(s / 2)) for s in range(140, 261)], couleur=c, epaisseur=2.6)
    f.texte(100, 32, nom, ancre="middle", dy=-12, couleur=c, gras=True, taille=12)
    f.texte(100, -2, formule, ancre="middle", dy=38, couleur=c, taille=10.5)
    cadres.append(f)
sys.stdout.write(Planche(cadres, ecart=14,
                 titre="Des calls et des puts additionnés dessinent la forme de paiement voulue").svg())
