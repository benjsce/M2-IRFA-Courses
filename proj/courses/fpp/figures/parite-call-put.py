#!/usr/bin/env python3
r"""
parite-call-put.svg — deux profils brisés dont la somme est une droite.

La fiche donne l'identité de payoff $(S_T-K)^+-(K-S_T)^+=S_T-K$ [Prop. 7] et précise
qu'elle est « vraie état par état ». Superposer les trois traits sur un seul cadre ne
montrerait rien : au-dessus du strike le call est déjà la droite, en dessous c'est le
put, et l'œil ne voit qu'une droite. Trois cadres côte à côte, avec le « moins » et le
« égale », disent l'identité d'un coup d'œil.

Le strike vaut 100, comme dans l'exemple minimal de la fiche. Aucun prix n'y figure : la
figure illustre l'identité de payoff, pas l'identité de prix, qui demande en plus
l'actualisation.

Usage : python courses/fpp/figures/parite-call-put.py > parite-call-put.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

K = 100.0
S0, S1 = 58.0, 142.0


def cadre(titre, f_payoff, couleur, epaisseur=2.4):
    g = Figure(xmin=S0 - 3, xmax=S1 + 3, ymin=-52, ymax=58, w=232, h=280,
               marges=(40, 26, 40, 14))
    g.axes(xticks=(K,), yticks=(-40, 0, 40),
           fmt=lambda t: ("K" if t == K else str(int(t))))
    g.segment(K, -52, K, 46)
    g.courbe([(S0, f_payoff(S0)), (K, f_payoff(K)), (S1, f_payoff(S1))],
             couleur=couleur, epaisseur=epaisseur)
    g.point(K, f_payoff(K), couleur=ENCRE, r=3)
    g.texte((S0 + S1) / 2, 58, titre, couleur=couleur, ancre="middle", dy=-2,
            taille=12.5, gras=True)
    return g


p = Planche(
    [cadre("le call", lambda s: max(s - K, 0.0), DOUX),
     cadre("le put", lambda s: max(K - s, 0.0), AJOUT),
     cadre("le forward", lambda s: s - K, ACCENT, 2.8)],
    signes=("−", "="), ecart=34,
    titre="Le payoff du call moins celui du put vaut celui du forward, état par état")

sys.stdout.write(p.svg())
