#!/usr/bin/env python3
r"""
bilan.svg — le bilan de l'entreprise du cours : 100 d'actifs, 20 de capitaux propres,
80 de dette.

La forme reproduit la figure 1 du poly (§1.2) ; les montants sont ceux du monde du cours.

Usage : python courses/fpp/figures/bilan.py > bilan.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, _n      # noqa: E402

A, E, D = 100, 20, 80
f = Figure(xmin=0, xmax=10, ymin=-8, ymax=112, w=440, h=320, marges=(10, 10, 10, 10),
           titre="Actif = capitaux propres + dette : 100 = 20 + 80")


def boite(x0, x1, y0, y1, couleur, etiquette, valeur):
    X0, X1, Y0, Y1 = f.px(x0), f.px(x1), f.py(y1), f.py(y0)
    f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.18" '
           'stroke="%s" stroke-width="1.6"/>'
           % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), couleur, couleur))
    f.texte((x0 + x1) / 2, (y0 + y1) / 2, etiquette, ancre="middle", dy=-2)
    f.texte((x0 + x1) / 2, (y0 + y1) / 2, valeur, ancre="middle", dy=15, gras=True)


boite(1.0, 4.4, 0, A, AJOUT, "actifs", "100")
boite(5.6, 9.0, D, A, ACCENT, "capitaux propres", "20")
boite(5.6, 9.0, 0, D, DOUX, "dette", "80")
f.texte(2.7, 104, "actif", ancre="middle", couleur=DOUX, taille=12)
f.texte(7.3, 104, "passif", ancre="middle", couleur=DOUX, taille=12)
f.texte(5.0, 50, "=", ancre="middle", taille=20, couleur=DOUX, dy=7)

sys.stdout.write(f.svg())
