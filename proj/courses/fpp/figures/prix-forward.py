#!/usr/bin/env python3
r"""
prix-forward.svg — deux façons de détenir l'action en T, qui ne coûtent rien aujourd'hui.
① Acheter à terme : rien en t ; en T, payer F et recevoir l'action. ② Acheter aujourd'hui
à crédit : emprunter S_t et acheter l'action ; en T, rembourser S_t / P(t,T). ③ Même
action, même coût initial : même paiement en T, F(t,T) = S_t / P(t,T).

Usage : python courses/fpp/figures/prix-forward.py > prix-forward.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

f = Figure(xmin=-0.75, xmax=2.7, ymin=-2.75, ymax=2.3, w=660, h=500, marges=(10, 10, 10, 10),
           titre="Deux façons d'avoir l'action en T, gratuites aujourd'hui : elles coûtent la même chose en T")
f.axe_temps(0, -0.35, 1.7, [(0, "t"), (1.4, "T")])


def noeud(x, y, s, couleur, dy=-10):
    f.point(x, y, couleur=couleur, r=4)
    f.texte(x, y, s, couleur=couleur, ancre="middle", dy=dy, gras=True)


f.texte(-0.7, 1.75, "① acheter à terme", couleur=ACCENT, gras=True, taille=12.5)
noeud(0, 1.1, "rien à payer", ACCENT)
noeud(1.4, 1.1, "payer F, recevoir l'action", ACCENT)
f.fleche(0.06, 1.1, 1.34, 1.1, couleur=ACCENT, epaisseur=1.6, pointilles="6 4")
f.texte(0.7, 1.1, "le contrat attend l'échéance", couleur=DOUX, ancre="middle", dy=18, taille=11.5)

f.texte(-0.7, -0.75, "② acheter aujourd'hui à crédit", couleur=AJOUT, gras=True, taille=12.5)
noeud(0, -1.35, "emprunter S_{t},", AJOUT, dy=24)
f.texte(0, -1.35, "acheter l'action", couleur=AJOUT, ancre="middle", dy=40, gras=True)
noeud(1.4, -1.35, "rembourser S_{t} / P(t,T),", AJOUT, dy=24)
f.texte(1.4, -1.35, "garder l'action", couleur=AJOUT, ancre="middle", dy=40, gras=True)
f.fleche(0.06, -1.3, 1.34, -1.3, couleur=AJOUT, courbure=18, epaisseur=2)
f.texte(0.7, -1.3, "la dette grandit : ÷ P(t,T)", couleur=AJOUT, ancre="middle", dy=-34, taille=12)

f.courbe([(1.95, 1.0), (1.95, -1.25)], couleur=ENCRE, epaisseur=1.4)
f.texte(1.95, 0.35, "③ même action,", couleur=ENCRE, dx=8, gras=True, taille=12.5)
f.texte(1.95, 0.35, "même coût", couleur=ENCRE, dx=8, dy=16, gras=True, taille=12.5)
f.texte(1.95, 0.35, "aujourd'hui (rien) :", couleur=DOUX, dx=8, dy=32, taille=11.5)
f.texte(1.95, 0.35, "même paiement en T", couleur=DOUX, dx=8, dy=47, taille=11.5)

f.texte(0.85, -2.4, "F(t,T) = S_{t} / P(t,T)", couleur=ENCRE, ancre="middle", gras=True, taille=14)
f.texte(0.85, -2.4, "la base F(t,T) − S_{t} est l'intérêt de l'emprunt", couleur=ENCRE, ancre="middle", dy=20, taille=12.5)
sys.stdout.write(f.svg())
