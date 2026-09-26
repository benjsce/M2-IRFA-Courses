#!/usr/bin/env python3
r"""
taux-forward.svg — deux façons de placer 1 de t à S, connues toutes deux aujourd'hui.

① En une fois, au taux zéro-coupon R(t,S) : 1 devient e^{R(t,S)(S−t)}.
② En deux temps : jusqu'à T au taux R(t,T), 1 devient e^{R(t,T)(T−t)} ; puis de T à S au
   taux K fixé aujourd'hui par le FRA, il devient e^{R(t,T)(T−t)} · e^{K(S−T)}.
③ Même mise, deux résultats certains : ils sont égaux. Les exposants s'ajoutent :
   R(t,T)(T−t) + K(S−T) = R(t,S)(S−t), d'où K.

Usage : python courses/fpp/figures/taux-forward.py > taux-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.45, xmax=3.2, ymin=-2.85, ymax=2.35, w=680, h=510, marges=(10, 10, 10, 10),
           titre="Placer 1 de t à S en une fois ou en deux temps : même résultat, d'où le taux forward K")
f.axe_temps(0, -0.3, 2.3, [(0, "t"), (1, "T"), (2, "S")])


def noeud(x, y, s, couleur, dy=-10):
    f.point(x, y, couleur=couleur, r=4)
    f.texte(x, y, s, couleur=couleur, ancre="middle", dy=dy, gras=True)


# ① en une fois
noeud(0, 1.1, "1", ACCENT)
noeud(2, 1.1, "e^{R(t,S)(S−t)}", ACCENT, dy=24)
f.fleche(0.06, 1.18, 1.94, 1.18, couleur=ACCENT, courbure=30, epaisseur=2)
f.texte(1, 1.18, "① en une fois, au taux R(t,S) :", couleur=ACCENT, ancre="middle", dy=-66, gras=True, taille=12.5)
f.texte(1, 1.18, "× e^{R(t,S)(S−t)}", couleur=ACCENT, ancre="middle", dy=-48, taille=12.5)

# ② en deux temps
noeud(0, -1.2, "1", AJOUT)
noeud(1, -1.2, "e^{R(t,T)(T−t)}", AJOUT)
noeud(2, -1.2, "e^{R(t,T)(T−t)} · e^{K(S−T)}", AJOUT)
f.fleche(0.06, -1.3, 0.94, -1.3, couleur=AJOUT, courbure=-22, epaisseur=2)
f.fleche(1.06, -1.3, 1.94, -1.3, couleur=AJOUT, courbure=-22, epaisseur=2, pointilles="6 4")
f.texte(0.5, -1.3, "② jusqu'à T, au taux R(t,T) :", couleur=AJOUT, ancre="middle", dy=62, gras=True, taille=12)
f.texte(0.5, -1.3, "× e^{R(t,T)(T−t)}", couleur=AJOUT, ancre="middle", dy=79, taille=12)
f.texte(1.5, -1.3, "puis de T à S, au taux K fixé", couleur=AJOUT, ancre="middle", dy=62, gras=True, taille=12)
f.texte(1.5, -1.3, "aujourd'hui par le FRA : × e^{K(S−T)}", couleur=AJOUT, ancre="middle", dy=79, taille=12)

# ③ égalité à l'arrivée
f.courbe([(2.55, 1.0), (2.55, -1.1)], couleur=ENCRE, epaisseur=1.4)
f.texte(2.55, 0.35, "③ égaux :", couleur=ENCRE, dx=8, gras=True, taille=12.5)
f.texte(2.55, 0.35, "connus tous deux", couleur=DOUX, dx=8, dy=16, taille=11.5)
f.texte(2.55, 0.35, "aujourd'hui, sinon", couleur=DOUX, dx=8, dy=31, taille=11.5)
f.texte(2.55, 0.35, "arbitrage", couleur=DOUX, dx=8, dy=46, taille=11.5)

f.texte(1.1, -2.5, "les exposants s'ajoutent : R(t,T)(T − t) + K(S − T) = R(t,S)(S − t)", couleur=ENCRE,
        ancre="middle", gras=True, taille=12.5)
f.texte(1.1, -2.5, "d'où K = F(t,T,S) = [R(t,S)(S − t) − R(t,T)(T − t)] / (S − T)", couleur=ENCRE,
        ancre="middle", dy=21, taille=12.5)
sys.stdout.write(f.svg())
