#!/usr/bin/env python3
r"""
prix-future.svg — la stratégie qui caractérise le prix future. À chaque date t_i, elle
détient 1/B(t_0,t_i) contrats et place H(t_i)/B(t_0,t_i) jusqu'à la date suivante ; sa
valeur part de H(t_0) et finit à S(T)/B(t_0,T), puisque H(T) = S(T).

Usage : python courses/fpp/figures/prix-future.py > prix-future.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.3, xmax=3.45, ymin=-1.3, ymax=1.6, w=600, h=300, marges=(10, 10, 10, 10),
           titre="La richesse de la stratégie vaut H(tᵢ)/B(t₀,tᵢ) à chaque date : de H(t₀) à S(T)/B(t₀,T)")
f.axe_temps(0, -0.15, 3.35, [(0, "t₀"), (1, "t₁"), (2, "t₂"), (3, "T")])
RICHE = ["H(t_{0})", "H(t_{1}) / B(t_{0},t_{1})", "H(t_{2}) / B(t_{0},t_{2})", "S(T) / B(t_{0},T)"]
CONTRATS = ["1 contrat", "1 / B(t_{0},t_{1}) contrats", "1 / B(t_{0},t_{2}) contrats", ""]
for k in range(4):
    f.texte(k, 0.75, RICHE[k], couleur=ACCENT if k < 3 else ENCRE, ancre="middle", gras=True, taille=12.5)
    if CONTRATS[k]:
        f.texte(k, -0.75, CONTRATS[k], couleur=AJOUT, ancre="middle", taille=11.5)
    if k < 3:
        f.fleche(k + 0.12, 0.35, k + 0.88, 0.35, couleur=DOUX, epaisseur=1.3, courbure=8)
f.texte(1.5, -1.2, "marges reçues + placement d'une période : la richesse se reporte d'une date à l'autre",
        couleur=DOUX, ancre="middle", taille=11.5)
sys.stdout.write(f.svg())
