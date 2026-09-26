#!/usr/bin/env python3
r"""
contrat-future.svg — un prix future fictif sur dix jours, parti de 104,08, et les flux
quotidiens versés à l'acheteur : chaque barre est H(t_{i+1}) − H(t_i), positive quand le
prix monte, négative quand il baisse. Le dernier prix est le prix comptant.

Usage : python courses/fpp/figures/contrat-future.py > contrat-future.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

H = [104.08, 105.00, 103.50, 104.20, 104.90, 104.10, 102.80, 103.60, 104.40, 103.70, 104.60]
BASE_H = 97.0            # le haut de la figure trace H, décalé au-dessus des barres
f = Figure(xmin=-0.6, xmax=10.8, ymin=-2.2, ymax=10.2, w=560, h=340, marges=(46, 10, 10, 10),
           titre="Chaque jour, l'acheteur du future reçoit ou verse la variation du prix")


def y(h):
    return h - BASE_H


f.courbe([(-0.3, 0), (10.6, 0)], couleur=DOUX, epaisseur=1.2)
for k in range(len(H) - 1):
    d = H[k + 1] - H[k]
    f.barre(k + 1, d, 0.55, couleur=ACCENT if d > 0 else AJOUT, y0=0)
f.courbe([(k, y(h)) for k, h in enumerate(H)], couleur=ENCRE, epaisseur=2)
for k, h in enumerate(H):
    f.point(k, y(h), couleur=ENCRE, r=3)
f.texte(0, y(H[0]), "H(t_{0})", dy=20, taille=12, gras=True)
f.texte(10, y(H[-1]), "H(T) = S(T)", dy=-10, ancre="end", taille=12, gras=True)
f.texte(-0.5, 1.4, "flux", couleur=DOUX, ancre="end", taille=11.5, dx=-2)
f.texte(-0.5, y(104), "prix", couleur=DOUX, ancre="end", taille=11.5, dx=-2)
f.texte(1, 0.92, "H(t_{1}) − H(t_{0})", couleur=ACCENT, ancre="middle", dy=-6, taille=11.5)
f.texte(2, -1.5, "H(t_{2}) − H(t_{1})", couleur=AJOUT, ancre="start", dx=-10, dy=17, taille=11.5)
f.texte(5.3, -2.0, "jours de règlement", couleur=DOUX, ancre="middle", taille=11.5)
sys.stdout.write(f.svg())
