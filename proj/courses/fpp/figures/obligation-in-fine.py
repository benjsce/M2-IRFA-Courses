#!/usr/bin/env python3
r"""
obligation-in-fine.svg — l'échéancier de l'obligation, qui se lit comme la Forme.

Un coupon r* à chaque date 1, 2, …, n, et le capital 1 à la dernière. Chaque flux revient
en 0 multiplié par 1/(1 + r)^i, le facteur de sa date : la somme de ces retours est le
prix, B(r*, r) = r* [1/(1 + r) + … + 1/(1 + r)^n] + 1/(1 + r)^n. Les coupons forment une
somme géométrique, d'où la seconde écriture de la Forme. Aucune valeur numérique.

Usage : python courses/fpp/figures/obligation-in-fine.py > obligation-in-fine.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.9, xmax=5.4, ymin=-1.85, ymax=2.1, w=640, h=420, marges=(8, 8, 8, 8),
           titre="Le prix d'une obligation in fine : chaque coupon et le capital, "
                 "ramenés en 0 par le facteur de leur date")
DATES = [(1, "1"), (2, "2"), (4.4, "n")]
f.axe_temps(0, -0.5, 5.2, [(0, "0")] + DATES)
f.texte(3.2, 0, "…", couleur=DOUX, ancre="middle", dy=21, taille=14)
H, C = 0.6, 0.55                           # hauteur d'un coupon, du capital empilé dessus
for x, s in DATES:
    f.fleche(x, 0.06, x, H, couleur=ACCENT, epaisseur=2.2)
    f.texte(x, H / 2, "r*", couleur=ACCENT, dx=7, gras=True, taille=13.5)
f.fleche(4.4, H + 0.04, 4.4, H + C, couleur=AJOUT, epaisseur=2.2)
f.texte(4.4, H + C / 2, "1 : le capital", couleur=AJOUT, dx=7, gras=True, taille=13.5)
# Les retours en 0 : chacun part du haut de son flux, et son facteur se lit au sommet.
RETOURS = [(1, H + 0.1, 0.9, "× 1/(1 + r)", 10), (2, H + 0.1, 1.2, "× 1/(1 + r)^{2}", 14),
           (4.4, H + C + 0.1, 1.55, "× 1/(1 + r)^{n}", 16)]
for x, y0, y1, s, c in RETOURS:
    f.fleche(x, y0, 0.08, y1, couleur=DOUX, courbure=c, epaisseur=1.2)
    f.texte((x + 0.08) / 2, (y0 + y1) / 2, s, couleur=DOUX, ancre="middle", dy=-c - 8, taille=12)
f.fleche(-0.1, -0.06, -0.1, -0.75, couleur=ENCRE, epaisseur=2.2)
f.texte(-0.1, -0.75, "− B(r*, r) : le prix, somme des retours", couleur=ENCRE, dx=10, dy=4,
        gras=True, taille=13)
f.texte(2.25, -1.25, "B(r*, r) = r* [ 1/(1 + r) + 1/(1 + r)^{2} + … + 1/(1 + r)^{n} ] + 1/(1 + r)^{n}",
        couleur=ENCRE, ancre="middle", gras=True, taille=13.5)
f.texte(2.25, -1.25, "somme géométrique : r* / r × (1 − 1/(1 + r)^{n}) + 1/(1 + r)^{n}",
        couleur=DOUX, ancre="middle", dy=24, taille=12.5)
sys.stdout.write(f.svg())
