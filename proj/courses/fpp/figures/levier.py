#!/usr/bin/env python3
r"""
levier.svg — le même bilan avant et après un gain ΔA des actifs, dette inchangée : les
capitaux propres gagnent aussi ΔA, donc ΔE/E = (A/E)(ΔA/A) = l_t ΔA/A.

Usage : python courses/fpp/figures/levier.py > levier.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402



def bilan(A, E, D, titre, lab_a, lab_e, lab_d, note_a="", note_e=""):
    f = Figure(xmin=0, xmax=10, ymin=-16, ymax=124, w=300, h=330, marges=(8, 8, 8, 8))

    def boite(x0, x1, y0, y1, couleur, etiquette):
        X0, X1, Y0, Y1 = f.px(x0), f.px(x1), f.py(y1), f.py(y0)
        f._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="0.18" '
               'stroke="%s" stroke-width="1.5"/>' % (_n(X0), _n(Y0), _n(X1 - X0), _n(Y1 - Y0), couleur, couleur))
        f.texte((x0 + x1) / 2, (y0 + y1) / 2, etiquette, ancre="middle", dy=5)

    boite(1.0, 4.6, 0, A, AJOUT, lab_a)
    boite(5.4, 9.0, D, D + E, ACCENT, lab_e)
    boite(5.4, 9.0, 0, D, DOUX, lab_d)
    f.texte(5.0, 118, titre, ancre="middle", gras=True)
    if note_a:
        f.texte(2.8, -11, note_a, ancre="middle", couleur=AJOUT, gras=True, taille=12)
        f.texte(7.2, -11, note_e, ancre="middle", couleur=ACCENT, gras=True, taille=12)
    return f


avant = bilan(100, 20, 80, "avant", "A_{t}", "E_{t}", "D_{t}")
apres = bilan(110, 30, 80, "après un gain ΔA", "A_{t} + ΔA", "E_{t} + ΔA", "D_{t}",
              "ΔA / A_{t}", "ΔA / E_{t} = l_{t} × ΔA / A_{t}")
sys.stdout.write(Planche([avant, apres], signes=["→"], ecart=36,
                 titre="Dette inchangée : le même gain ΔA pèse l_t = A_t / E_t fois plus sur les capitaux propres").svg())
