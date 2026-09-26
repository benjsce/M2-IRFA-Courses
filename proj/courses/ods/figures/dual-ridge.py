#!/usr/bin/env python3
r"""
dual-ridge.svg — the data fits in memory; the matrices built from it do not.

Ce que la figure doit faire voir : sur une échelle logarithmique d'octets, la matrice
creuse X tient en 12 Mo ; la matrice duale XXᵀ demande 80 Go, X dense 800 Go et la
matrice primale XᵀX 8 To — tous au-delà de la mémoire d'un ordinateur portable (16 Go,
repère ajouté). C'est le tableau de la slide 12 : n = 10⁵, p = 10⁶, dix non-nuls par
ligne, float64 (8 octets) et indices sur 4 octets.

CSR : 10⁶ valeurs × 8 + 10⁶ indices × 4 + (n + 1) pointeurs × 4 ≈ 12,4 Mo.

Usage : python courses/ods/figures/dual-ridge.py > dual-ridge.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE, _n      # noqa: E402

n, p, nnz = 10 ** 5, 10 ** 6, 10 ** 6
lignes = [
    ("X, sparse (CSR)", nnz * 8 + nnz * 4 + (n + 1) * 4, "12 MB", ACCENT),
    ("XXᵀ, dual, n × n", n * n * 8, "80 GB", AJOUT),
    ("X, dense, n × p", n * p * 8, "800 GB", DOUX),
    ("XᵀX, primal, p × p", p * p * 8, "8 TB", AJOUT),
]
g = Figure(xmin=0, xmax=14.2, ymin=0, ymax=5.2, w=600, h=270, marges=(150, 10, 34, 12),
           titre="The problem is not the data, it is the matrices we build from it")
for k, (nom, octets, lab, c) in enumerate(lignes):
    y = 4.3 - k
    g.barre(math.log10(octets) / 2, y, math.log10(octets), couleur=c, opacite=0.85, y0=y - 0.55)
    g.texte(0, y - 0.35, nom, taille=12.5, ancre="end", dx=-8, couleur=ENCRE)
    g.texte(math.log10(octets), y - 0.35, lab, taille=12.5, dx=6, couleur=c, gras=True)
portable = math.log10(16e9)
g.segment(portable, 0.1, portable, 4.9, couleur=ENCRE, epaisseur=1.4, pointilles="5 4")
g.texte(portable, 5.0, "a laptop: 16 GB", taille=12, ancre="middle", fond=True)
g.axes(xticks=[6, 9, 12], fmt=lambda t: {6: "1 MB", 9: "1 GB", 12: "1 TB"}[t])
sys.stdout.write(g.svg())
