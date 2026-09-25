#!/usr/bin/env python3
r"""
replication-statique.svg — acheter, porter, livrer : les quatre flux du cash and carry.

La fiche : acheter le sous-jacent à crédit, le porter, le livrer contre K. En t, l'achat
et l'emprunt s'annulent ; en T, on reçoit K et on rembourse $S_t/P(t,T)$. Le solde en T
est certain et le montage n'a rien coûté : il est donc nul, ce qui fixe K. Un flux reçu
monte, un flux payé descend ; l'action elle-même ne passe que par la ligne pointillée.

Usage : python courses/fpp/figures/replication-statique.py > replication-statique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

t, T = 2.4, 7.8
g = Figure(xmin=0, xmax=10, ymin=-4.3, ymax=3.4, w=620, h=300, marges=(8, 8, 8, 8),
           titre="Réplication statique : quatre flux, un solde certain en T")
g.axe_temps(0, 1.0, 9.7, [(t, "t"), (T, "T")])

# en t : on emprunte S_t, on achète l'action avec
g.fleche(t, 0.45, t, 2.2, couleur=AJOUT, epaisseur=2)
g.texte(t, 1.5, "Sₜ emprunté", couleur=AJOUT, gras=True, taille=12.5, dx=9)
g.fleche(t, -1.25, t, -3.0, couleur=ACCENT, epaisseur=2)
g.texte(t, -2.0, "Sₜ : achat de l'action", couleur=ACCENT, gras=True, taille=12.5, dx=9)

# en T : on livre l'action contre K, on rembourse
g.fleche(T, 0.45, T, 2.2, couleur=ACCENT, epaisseur=2)
g.texte(T, 1.5, "K : livraison", couleur=ACCENT, gras=True, taille=12.5, dx=-9, ancre="end")
g.fleche(T, -1.25, T, -3.0, couleur=AJOUT, epaisseur=2)
g.texte(T, -2.0, "Sₜ / P(t,T) : remboursement", couleur=AJOUT, gras=True, taille=12.5,
        dx=-9, ancre="end")

# l'action, portée sans aucun geste
g.segment(t + 0.2, -3.75, T - 0.2, -3.75, couleur=DOUX, epaisseur=1.3)
g.texte((t + T) / 2, -3.75, "l'action est portée, sans aucun geste", couleur=DOUX,
        taille=11.5, ancre="middle", fond=True, dy=4)
g.texte(t, 2.75, "solde : 0", couleur=ENCRE, taille=12, ancre="middle")
g.texte(T, 2.75, "solde : K − Sₜ / P(t,T), certain", couleur=ENCRE, taille=12, ancre="middle")

sys.stdout.write(g.svg())
