#!/usr/bin/env python3
r"""
valeur-a-risque-conditionnelle.svg — le seuil et la moyenne au-delà du seuil.

La fiche dit que la VaR est un seuil de perte, dépassé avec la probabilité α, et que la
CVaR est la moyenne des pertes qui le dépassent, donc plus loin dans la queue. La figure
trace une densité de perte, colore la queue de probabilité 5 % et place les deux
nombres. La loi est normale et graduée en écarts types : c'est le cas le plus simple où
les deux positions se calculent, 1,645 et φ(1,645)/0,05 = 2,063.

Usage : python courses/pfo/figures/valeur-a-risque-conditionnelle.py > valeur-a-risque-conditionnelle.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX              # noqa: E402

ALPHA = 0.05
densite = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
repartition = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))

# le quantile d'ordre 1 - α de la perte, par dichotomie : pas de dépendance
a, b = 0.0, 5.0
for _ in range(80):
    m = (a + b) / 2
    a, b = (m, b) if 1 - repartition(m) > ALPHA else (a, m)
VAR = (a + b) / 2                                  # 1,645
CVAR = densite(VAR) / ALPHA                        # 2,063

f = Figure(xmin=-3.6, xmax=3.9, ymin=0, ymax=0.47, w=560, h=320,
           titre="La VaR est un seuil ; la CVaR est la moyenne des pertes au-delà")
f.axes(xlab="perte, en écarts types", xticks=(-3, -2, -1, 0, 1, 2, 3),
       fmt=lambda t: str(int(t)))

PAS = 0.02
x = VAR + PAS / 2
while x < 3.8:
    f.barre(x, densite(x), PAS, couleur=ACCENT, opacite=0.28)
    x += PAS

f.fonction(densite, -3.5, 3.8, n=300, couleur=ENCRE, epaisseur=2.0)
f.segment(VAR, 0, VAR, 0.30, couleur=ENCRE, epaisseur=1.4, pointilles="4 3")
f.segment(CVAR, 0, CVAR, 0.20, couleur=ACCENT, epaisseur=1.6, pointilles=None)
f.point(CVAR, 0, couleur=ACCENT)

f.texte(VAR, 0.30, "VaR", couleur=ENCRE, ancre="middle", dy=-6, taille=12, gras=True)
f.texte(CVAR, 0.20, "CVaR", couleur=ACCENT, ancre="start", dx=4, dy=-6, taille=12, gras=True)
f.texte(2.6, densite(2.6), "5 % des pertes", couleur=ACCENT, dx=8, dy=-10, taille=11.5, fond=True)
f.texte(-1.4, 0.36, "scénarios ordinaires", couleur=DOUX, ancre="middle", taille=11.5)

sys.stdout.write(f.svg())
