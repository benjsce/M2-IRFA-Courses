#!/usr/bin/env python3
r"""
replication-statique.svg — le montage du vendeur à terme : trois flux connus, un cherché.

Ce que la figure doit faire voir : du côté du vendeur à terme, celui qui livre, tout est
connu dès t sauf K. En t, il emprunte S_t et achète l'action avec : solde nul. En T, il
livre l'action contre K (le trou, en pointillé) et rembourse S_t/P(t,T), connu dès t.
Le solde en T ne contient pas S_T ; le montage n'a rien coûté ; il est donc nul, ce qui
fixe K. Un flux reçu monte, un flux payé descend ; l'action ne passe que par la ligne
pointillée du bas, sans aucun geste entre t et T.

Usage : python courses/fpp/figures/replication-statique.py > replication-statique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

t, T = 2.4, 7.8
g = Figure(xmin=0, xmax=10, ymin=-4.3, ymax=4.1, w=620, h=330, marges=(8, 8, 8, 8),
           titre="Réplication statique, côté vendeur : tout est connu en t, sauf K")
g.axe_temps(0, 1.0, 9.7, [(t, "t"), (T, "T")])
g.texte(0.25, 3.7, "le vendeur à terme : emprunter, acheter, porter, livrer",
        couleur=ENCRE, gras=True, taille=12.5)

# en t : il emprunte S_t, il achète l'action avec
g.fleche(t, 0.45, t, 2.2, couleur=AJOUT, epaisseur=2)
g.texte(t, 1.55, "Sₜ emprunté", couleur=AJOUT, gras=True, taille=12.5, dx=9)
g.texte(t, 1.0, "connu", couleur=DOUX, taille=11.5, dx=9)
g.fleche(t, -1.25, t, -3.0, couleur=ACCENT, epaisseur=2)
g.texte(t, -1.95, "Sₜ : achat de l'action", couleur=ACCENT, gras=True, taille=12.5, dx=9)
g.texte(t, -2.5, "connu", couleur=DOUX, taille=11.5, dx=9)

# en T : il livre l'action contre K (cherché), il rembourse (connu)
g.fleche(T, 0.45, T, 2.2, couleur=ENCRE, epaisseur=2, pointilles="5 4")
g.texte(T, 1.55, "K, contre l'action", couleur=ENCRE, gras=True, taille=12.5, dx=-9,
        ancre="end")
g.texte(T, 1.0, "cherché", couleur=ENCRE, taille=11.5, dx=-9, ancre="end")
g.fleche(T, -1.25, T, -3.0, couleur=AJOUT, epaisseur=2)
g.texte(T, -1.95, "Sₜ / P(t,T) : remboursement", couleur=AJOUT, gras=True, taille=12.5,
        dx=-9, ancre="end")
g.texte(T, -2.5, "connu dès t", couleur=DOUX, taille=11.5, dx=-9, ancre="end")

# l'action, portée sans aucun geste
g.segment(t + 0.2, -3.75, T - 0.2, -3.75, couleur=DOUX, epaisseur=1.3)
g.texte((t + T) / 2, -3.75, "l'action est portée, sans aucun geste", couleur=DOUX,
        taille=11.5, ancre="middle", fond=True, dy=4)
g.texte(t, 2.75, "solde : 0", couleur=ENCRE, taille=12, ancre="middle")
g.texte(T, 2.75, "solde : K − Sₜ / P(t,T), sans S_{T}, donc nul", couleur=ENCRE, taille=12,
        ancre="middle")

sys.stdout.write(g.svg())
