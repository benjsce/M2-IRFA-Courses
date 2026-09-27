#!/usr/bin/env python3
r"""
rdu.svg — la Forme en deux temps : les poids sont les sauts de φ, et U est une aire.

À gauche, la déformation du cours, $\varphi(p)=p^\beta/(p^\beta+(1-p)^\beta)^{1/\beta}$ avec
$\beta=0{,}7$, sur l'axe des probabilités cumulées. Pour une loterie de trois résultats
rangés $x_1<x_2<x_3$, de probabilités 0,2, 0,3 et 0,5 — celles du marché du cours —, on
porte les cumuls $p_1$, $p_1+p_2$ et 1 ; les sauts de $\varphi$ entre eux sont les poids,
$\pi_1=\varphi(p_1)$, $\pi_2=\varphi(p_1+p_2)-\varphi(p_1)$, $\pi_3=1-\varphi(p_1+p_2)$, soit
0,2560, 0,2013 et 0,5426. À droite, chaque résultat est une barre de largeur $\pi_i$ et de
hauteur $u(x_i)$ ; les barres se touchent et remplissent une largeur 1, et leur aire est
$U(P)=\sum\pi_iu(x_i)$. Les hauteurs ne sont pas chiffrées : la fiche ne fixe pas la loterie.

Usage : python courses/dup/figures/rdu.py > rdu.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

B = 0.7
phi = lambda p: p ** B / (p ** B + (1 - p) ** B) ** (1 / B) if 0 < p < 1 else float(p)
CUM = (0.2, 0.5, 1.0)
PI = [phi(CUM[0]), phi(CUM[1]) - phi(CUM[0]), 1 - phi(CUM[1])]
HAUT = (1.0, 1.8, 3.0)                  # u(x₁) < u(x₂) < u(x₃), sans échelle
COUL = (ACCENT, AJOUT, DOUX)


def fr(v):
    return ("%.2f" % v).replace(".", ",")


g = Figure(xmin=-0.32, xmax=1.08, ymin=0, ymax=1.14, w=300, h=320, marges=(8, 30, 48, 10))
g.axes(xticks=(0.2, 0.5, 1.0), fmt=lambda t: {0.2: "p₁", 0.5: "p₁ + p₂", 1.0: "1"}[t],
       croix=(0, 0))
g.segment(0, 0, 1, 1, couleur=PALE)
g.fonction(phi, 0.001, 0.999, couleur=ENCRE, epaisseur=2.3)
bas = 0.0
for k, c in enumerate(CUM):
    h = phi(c)
    g.segment(c, 0, c, h, couleur=PALE)
    g.segment(0, h, c, h, couleur=COUL[k], epaisseur=1.2, pointilles="4 3")
    g.mesure(-0.04, bas, h, couleur=COUL[k], etiquette="π_{%d} = %s" % (k + 1, fr(h - bas)),
             cote="left")
    bas = h
g.texte(0.72, phi(0.72), "φ", couleur=ENCRE, dx=8, dy=14, gras=True, taille=13)
g.texte(0.4, 1.14, "les poids : les sauts de φ", ancre="middle", dy=-12, gras=True, taille=12.5)
g.texte(0.4, 0, "probabilité cumulée", couleur=DOUX, ancre="middle", dy=36, taille=12)

d = Figure(xmin=-0.05, xmax=1.08, ymin=0, ymax=3.6, w=300, h=320, marges=(8, 30, 48, 10))
d.axes(xticks=(), croix=(0, 0))
x0 = 0.0
for k in range(3):
    d.barre(x0 + PI[k] / 2, HAUT[k], PI[k], couleur=COUL[k], opacite=0.8, y0=0)
    d.texte(x0 + PI[k] / 2, HAUT[k], "u(x_{%d})" % (k + 1), couleur=COUL[k], ancre="middle",
            dy=-6, gras=True, taille=12)
    d.texte(x0 + PI[k] / 2, 0, "π_{%d}" % (k + 1), couleur=COUL[k], ancre="middle", dy=17,
            gras=True, taille=12)
    x0 += PI[k]
d.texte(0.5, 3.6, "U(P) = Σ πᵢ u(xᵢ) : l'aire", ancre="middle", dy=-12, gras=True, taille=12.5)
d.texte(0.5, 0, "largeurs : π₁ + π₂ + π₃ = 1", couleur=DOUX, ancre="middle", dy=36, taille=12)

sys.stdout.write(Planche([g, d], signes=("→",), ecart=36,
                         titre="Les poids de décision sont les sauts de φ sur les cumuls, "
                               "et l'utilité est l'aire qu'ils pondèrent").svg())
