#!/usr/bin/env python3
r"""
dual-ridge.svg — the two formulas of the Forme, drawn as products of matrices at scale.

Ce que la figure doit faire voir : les deux écritures des poids ridge mènent au même ŵ,
et l'on choisit celle dont la matrice à inverser est la plus petite. Chaque matrice est un
rectangle à l'échelle de ses dimensions, p = 10 n (n = 10⁵ observations, p = 10⁶
features) : à gauche, le primal inverse un carré p × p ; à droite, le dual un carré
n × n, dix fois plus étroit, entre Xᵀ et y. Les tailles mémoire, en float64, sont celles de
la slide 12 : 8 TB pour XᵀX, 80 GB pour XXᵀ, toutes deux au-delà des 16 GB d'un portable.

Usage : python courses/ods/figures/dual-ridge.py > dual-ridge.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

W, H = 590, 330
f = Figure(xmin=0, xmax=W, ymin=-H, ymax=0, w=W, h=H, marges=(0, 0, 0, 0),
           titre="Primal and dual give the same weights; invert the smaller matrix")
P, N, V = 150, 15, 4          # p, n, and the width of a vector, in pixels
TOP = 50


def rect(x, y, w, h, couleur, opacite=0.85):
    """A matrix of w columns and h rows, top-left corner at (x, y) in pixels."""
    f.barre(x + w / 2, -y, w, couleur=couleur, opacite=opacite, y0=-(y + h))


def lab(x, y, s, couleur=ENCRE, ancre="middle", gras=False, taille=12.5):
    f.texte(x, -y, s, couleur=couleur, ancre=ancre, gras=gras, taille=taille)


# Primal: (XᵀX + λI_p)⁻¹ · Xᵀ · y
x = 20
rect(x, TOP, P, P, AJOUT)
lab(x + P / 2, TOP + P / 2, "(XᵀX + λIₚ)⁻¹", couleur=ENCRE, gras=True)
lab(x + P / 2, TOP + P + 20, "p × p : 8 TB", couleur=AJOUT, gras=True)
x += P + 16
rect(x, TOP, N, P, DOUX)
lab(x + N / 2, TOP - 8, "Xᵀ")
x += N + 12
rect(x, TOP, V, N, ENCRE)
lab(x + V / 2, TOP - 8, "y")
lab(x + 30, TOP + P / 2 + 6, "=", couleur=DOUX, taille=22)
lab(20 + (x + V - 20) / 2, TOP - 30, "primal", couleur=DOUX, gras=True, taille=13)

# Dual: Xᵀ · (XXᵀ + λI_n)⁻¹ · y
x0 = x + 70
x = x0
rect(x, TOP, N, P, DOUX)
lab(x + N / 2, TOP - 8, "Xᵀ")
x += N + 12
rect(x, TOP, N, N, ACCENT)
lab(x, TOP + N + 20, "(XXᵀ + λIₙ)⁻¹", couleur=ENCRE, ancre="start", gras=True)
lab(x, TOP + N + 40, "n × n : 80 GB", couleur=ACCENT, ancre="start", gras=True)
x += N + 12
rect(x, TOP, V, N, ENCRE)
lab(x + V / 2, TOP - 8, "y")
lab(x0 + (x + V - x0) / 2, TOP - 30, "dual", couleur=DOUX, gras=True, taille=13)
x += 100
lab(x - 20, TOP + P / 2 + 6, "=", couleur=DOUX, taille=22)
rect(x, TOP, V, P, ENCRE)
lab(x + V / 2, TOP - 8, "ŵ")
lab(x + 12, TOP + P / 2, "p weights", couleur=DOUX, ancre="start", taille=12)

lab(W / 2, TOP + P + 62, "ŵ = (XᵀX + λIₚ)⁻¹ Xᵀy = Xᵀ(XXᵀ + λIₙ)⁻¹ y", gras=True, taille=14)
lab(W / 2, TOP + P + 86, "same weights; with n = p / 10, invert the n × n matrix — "
    "though neither fits in a laptop's 16 GB", couleur=DOUX, taille=12.5)
sys.stdout.write(f.svg())
