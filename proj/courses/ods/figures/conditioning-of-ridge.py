#!/usr/bin/env python3
r"""
conditioning-of-ridge.svg — λ sets the condition number of ridge.

Ce que la figure doit faire voir : κ = (σ²max + λ)/(σ²min + λ) en fonction de λ, pour les
quatre observations du cours (σ² = 3,62 et 1,38) : κ va de 2,62 à λ = 0 vers 1 quand λ
grandit ; et le même σ²max avec σmin = 0, le cas n < p de la slide 26 : κ = (3,62 + λ)/λ
part à l'infini quand λ tend vers 0.

Usage : python courses/ods/figures/conditioning-of-ridge.py > conditioning-of-ridge.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

s2max, s2min = (5 + math.sqrt(5)) / 2, (5 - math.sqrt(5)) / 2
kap = lambda lam, smin2: (s2max + lam) / (smin2 + lam)

g = Figure(xmin=-2.2, xmax=2.2, ymin=0, ymax=3.1, w=560, h=360, marges=(58, 26, 40, 16),
           titre="The larger λ, the closer κ is to 1: regularization also makes the solve easy")
lx = [-2 + 4 * i / 120 for i in range(121)]
g.courbe([(x, math.log10(kap(10 ** x, 0.0))) for x in lx], couleur=AJOUT, epaisseur=2.2)
g.courbe([(x, math.log10(kap(10 ** x, s2min))) for x in lx], couleur=ACCENT, epaisseur=2.4)
g.point(0, math.log10(kap(1, s2min)), couleur=ACCENT)
g.texte(0.08, math.log10(kap(1, s2min)) + 0.12, "λ = 1: κ ≈ %.2f" % kap(1, s2min), couleur=ACCENT,
        taille=12, fond=True)
g.texte(-2.1, math.log10(s2max / s2min) + 0.12, "four observations: κ → 2.62 as λ → 0",
        couleur=ACCENT, taille=12, gras=True)
g.texte(-1.2, 2.55, "σ_{min} = 0 (n < p): κ = (3.62 + λ)/λ", couleur=AJOUT, taille=12, gras=True)
g.segment(-2.2, 0, 2.2, 0, couleur=PALE)
g.texte(2.1, 0.08, "κ = 1: trivial", couleur=DOUX, taille=11.5, ancre="end")
g.axes(xlab="λ", ylab="κ", xticks=[-2, -1, 0, 1, 2], yticks=[0, 1, 2, 3],
       fmt=lambda t: {-2: "0.01", -1: "0.1", 0: "1", 1: "10", 2: "100"}[t],
       fmt_y=lambda t: {0: "1", 1: "10", 2: "100", 3: "1000"}[t])
sys.stdout.write(g.svg())
