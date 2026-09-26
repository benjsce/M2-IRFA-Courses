#!/usr/bin/env python3
r"""
prix-future.svg — un seul flux pour le forward ; pour le future, un flux par règlement,
chacun replacé jusqu'en T à un taux qu'on ne connaît pas encore.

Ce que la figure doit faire voir : pourquoi le facteur du future est le compte
capitalisé B(t,T) et non le zéro-coupon. En haut, le forward : tout se règle en T, en
un seul flux. En bas, la stratégie qui réplique le future : on place H_t aujourd'hui
(le montant cherché, en pointillé) ; à chaque règlement, un appel de marge de montant
inconnu en t est encaissé ou payé, puis replacé jusqu'en T à un taux lui aussi inconnu
en t (deux de ces trajets sont dessinés, en arc) ; à l'échéance, le tout vaut
S_T/B(t,T). Les hauteurs ne viennent d'aucune donnée : seuls le nombre de flux, leurs
dates et leurs sens comptent.

Usage : python courses/fpp/figures/prix-future.py > prix-future.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

t, T = 1.8, 8.8
yF, yH = 3.0, -1.9
g = Figure(xmin=0, xmax=10, ymin=-5.2, ymax=4.9, w=640, h=380, marges=(8, 8, 8, 8),
           titre="Future : chaque appel de marge est replacé jusqu'en T à un taux inconnu")

for y0, nom in ((yF, "forward"), (yH, "future")):
    g.axe_temps(y0, 1.2, 9.7, [(t, "t"), (T, "T")])
    g.texte(0.05, y0 + 0.15, nom, taille=12, gras=True, couleur=ENCRE)

# forward : un seul flux, en T
g.fleche(T, yF + 0.35, T, yF + 1.6, couleur=ACCENT, epaisseur=2)
g.texte(T, yF + 0.9, "S_{T} − K, en une fois", couleur=ACCENT, gras=True, taille=12.5,
        dx=-9, ancre="end")

# future : H_t placé aujourd'hui, le montant cherché
g.fleche(t, yH - 0.85, t, yH - 2.2, couleur=ENCRE, epaisseur=2, pointilles="5 4")
g.texte(t, yH - 1.7, "Hₜ placé : cherché", couleur=ENCRE, gras=True, taille=12, dx=8)

# un appel de marge par règlement, de signe quelconque, de montant inconnu en t
hauteurs = (0.8, -0.6, 1.1, 0.5, -0.9, 0.7, -0.4, 0.9, -0.6)
pas = (T - t) / (len(hauteurs) + 1)
xs = []
for k, h in enumerate(hauteurs):
    xk = t + (k + 1) * pas
    y0 = yH + (0.3 if h > 0 else -0.3)
    g.fleche(xk, y0, xk, y0 + h, couleur=AJOUT, epaisseur=1.7)
    xs.append((xk, y0 + h))

# deux de ces flux, replacés jusqu'en T : trajet vers la droite, taux inconnu en t
for k in (0, 2):
    xk, yk = xs[k]
    g.fleche(xk + 0.05, yk + 0.15, T - 0.15, yH + 1.75, couleur=AJOUT, epaisseur=1.2,
             courbure=16, pointilles="3 3")
g.texte(t + 0.2, yH + 2.75, "chaque appel de marge, de montant inconnu en t, est replacé "
        "jusqu'en T", couleur=AJOUT, gras=True, taille=12)
g.texte(t + 0.2, yH + 2.2, "à un taux lui aussi inconnu en t", couleur=AJOUT, taille=11.5)

# en T, le tout
g.fleche(T, yH + 0.3, T, yH + 1.6, couleur=AJOUT, epaisseur=2.2)
g.texte(T, yH - 1.7, "en T, le tout vaut S_{T} / B(t,T)", couleur=AJOUT, gras=True,
        taille=12.5, dx=-9, ancre="end")
g.texte(t + 0.2, yH - 2.9, "le nombre de contrats est ajusté à chaque règlement",
        couleur=DOUX, taille=11.5)

sys.stdout.write(g.svg())
