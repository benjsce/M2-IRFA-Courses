#!/usr/bin/env python3
r"""
decroissance-des-poids.svg — un poids que rien ne renforce fond, sans jamais atteindre zéro.

Ce que la figure doit faire voir : avec λ = 0,1, chaque mise à jour retire au poids un
dixième de sa propre valeur ; s'il n'est pas renforcé, il est multiplié par 0,9 à chaque
fois : 1 ; 0,9 ; 0,81 ; … ; 0,35 après dix mises à jour ; 0,12 après vingt. La suite tend
vers zéro sans l'atteindre : la connexion reste. Sans la pénalité, le même poids resterait
à 1.

λ = 0,1 est la valeur typique de la slide 184 ; le poids de départ, 1, est choisi pour le
dessin.

Usage : python courses/dss/figures/decroissance-des-poids.py > decroissance-des-poids.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

LAMBDA, N = 0.1, 20
w = [(1 - LAMBDA) ** t for t in range(N + 1)]
virg = lambda v: ("%.2f" % v).rstrip("0").rstrip(".").replace(".", ",")

f = Figure(xmin=-0.8, xmax=N + 0.8, ymin=0, ymax=1.32, w=560, h=300,
           marges=(46, 22, 40, 14),
           titre="Chaque mise à jour retire au poids un dixième de lui-même : il fond, sans toucher zéro")
f.axes(xlab="mise à jour", ylab="poids", xticks=(0, 5, 10, 15, 20), yticks=(0, 0.5, 1),
       fmt=lambda v: "%d" % v, fmt_y=virg)

f.segment(-0.5, 1, N + 0.5, 1, couleur=DOUX, epaisseur=1.3)
f.texte(N + 0.5, 1, "sans décroissance : le poids reste à 1", couleur=DOUX, ancre="end",
        dy=-7, taille=11.5)
for t, v in enumerate(w):
    f.barre(t, v, 0.66, couleur=ACCENT, opacite=0.85)
for t in (1, 2, 10, 20):
    f.texte(t, w[t], virg(w[t]), ancre="middle", dy=-6, taille=11.5, gras=t in (10, 20))
f.texte(3.2, 0.9, "× 0,9 à chaque mise à jour", couleur=ACCENT, gras=True, taille=12.5)

sys.stdout.write(f.svg())
