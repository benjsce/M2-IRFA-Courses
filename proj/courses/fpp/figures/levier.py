#!/usr/bin/env python3
r"""
levier.svg — le même bilan avant et après un choc de +10 % sur les actifs, dette
inchangée : les capitaux propres gagnent 50 %, cinq fois plus, le levier.

Usage : python courses/fpp/figures/levier.py > levier.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, _n      # noqa: E402


def bilan(A, E, D, titre, note_a, note_e):
    f = Figure(xmin=0, xmax=10, ymin=-14, ymax=124, w=300, h=320, marges=(8, 8, 8, 8))

    def boite(x0, x1, y0, y1, couleur, etiquette):
        X0, X1, Y0, Y1 = f.px(x0), f.px(x1), f.py(y1), f.py(y0)
        f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.18" '
               'stroke="%s" stroke-width="1.5"/>'
               % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), couleur, couleur))
        f.texte((x0 + x1) / 2, (y0 + y1) / 2, etiquette, ancre="middle", dy=5)

    boite(1.0, 4.6, 0, A, AJOUT, "actifs %d" % A)
    boite(5.4, 9.0, D, D + E, ACCENT, "c. propres %d" % E)
    boite(5.4, 9.0, 0, D, DOUX, "dette %d" % D)
    f.texte(5.0, 118, titre, ancre="middle", gras=True)
    if note_a:
        f.texte(2.8, -10, note_a, ancre="middle", couleur=AJOUT, gras=True)
        f.texte(7.2, -10, note_e, ancre="middle", couleur=ACCENT, gras=True)
    return f


avant = bilan(100, 20, 80, "avant", "", "")
apres = bilan(110, 30, 80, "après", "+10 %", "+50 %")
p = Planche([avant, apres], signes=["→"], ecart=36,
            titre="Actifs +10 %, dette inchangée : capitaux propres +50 %, soit 5 fois plus")
sys.stdout.write(p.svg())
