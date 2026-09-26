#!/usr/bin/env python3
r"""
forward-de-change.svg — les deux jambes du forward de change, chacune ramenée en t.

La fiche donne $K(t,T)=X_tP(t,T)/P^f(t,T)$ et dit que le forward est le rapport de deux
facteurs d'actualisation, un par devise. Le dessin du tableau le montre en une fois :
en T on paie 1 en devise locale et on reçoit K en devise étrangère ; chaque flux
revient en t par le zéro-coupon de sa propre devise ; la jambe étrangère change
ensuite de devise par $X_t$. Le contrat ne coûte rien à la signature : les deux
valeurs en t sont égales, et c'est la formule.

Ce que la figure doit faire voir, en plus : tout est connu aujourd'hui (X_t, les deux
zéro-coupons) sauf K, le montant en pointillé ; et le change se fait en t, à l'aplomb
de la date, pas avant.

Les devises sont celles de l'exemple minimal : EUR locale, USD étrangère, $X_t$ en
dollars par euro. Aucun nombre : la figure montre la construction, pas l'exemple.

Usage : python courses/fpp/figures/forward-de-change.py > forward-de-change.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

t, T = 3.2, 8.5
g = Figure(xmin=0, xmax=10, ymin=-5, ymax=5, w=640, h=360, marges=(8, 8, 8, 8),
           titre="Forward de change : chaque jambe revient en t dans sa devise")

g.axe_temps(0, 1.5, 9.7, [(t, "t"), (T, "T")])

# les deux lignes, une par devise
g.texte(0.05, 3.1, "$", taille=17, gras=True, couleur=AJOUT)
g.texte(0.05, 2.35, "étrangère", taille=11, couleur=DOUX)
g.texte(0.05, -3.3, "€", taille=17, gras=True, couleur=ACCENT)
g.texte(0.05, -4.05, "locale", taille=11, couleur=DOUX)

# jambe étrangère : on reçoit K dollars en T
g.fleche(T, 0.45, T, 2.6, couleur=AJOUT, epaisseur=2, pointilles="5 4")
g.texte(T, 1.75, "K", couleur=AJOUT, gras=True, taille=14, dx=10)
g.texte(T, 1.05, "cherché", couleur=AJOUT, taille=11.5, dx=10)
g.fleche(T - 0.25, 3.2, t + 0.95, 3.2, couleur=AJOUT, courbure=22)
g.texte(t, 3.05, "K·P^{f}(t,T)", couleur=AJOUT, gras=True, taille=13.5, ancre="middle")
g.texte((t + T) / 2, 4.55, "actualisé au taux étranger", couleur=DOUX, taille=11,
        ancre="middle")

# jambe locale : on paie 1 euro en T
g.fleche(T, -1.25, T, -3.3, couleur=ACCENT, epaisseur=2)
g.texte(T, -2.3, "1", couleur=ACCENT, gras=True, taille=14, dx=10)
g.fleche(T - 0.25, -3.7, t + 1.15, -3.7, couleur=ACCENT, courbure=-18)
g.texte(t + 0.1, -3.6, "P(t,T)", couleur=ACCENT, gras=True, taille=13.5)
g.texte((t + T) / 2 + 0.4, -4.85, "actualisé au taux local", couleur=DOUX, taille=11,
        ancre="middle")

# en t, à l'aplomb de la date, la jambe étrangère change de devise ; le trait
# s'interrompt pour laisser lire l'axe et son étiquette
g.segment(t, 2.5, t, 0.5, couleur=DOUX, epaisseur=1.5, pointilles="4 3")
g.fleche(t, -1.1, t, -3.0, couleur=DOUX, pointilles="4 3")
g.texte(t, 1.5, "÷ Xₜ, au comptant", couleur=ENCRE, taille=12.5, dx=8)
g.texte(t - 0.05, -3.6, "K·P^{f}(t,T) / Xₜ  =", couleur=ENCRE, taille=12.5, ancre="end")

sys.stdout.write(g.svg())
