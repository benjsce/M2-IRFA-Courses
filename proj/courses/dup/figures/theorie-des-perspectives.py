#!/usr/bin/env python3
r"""
theorie-des-perspectives.svg — la Forme en trois cadres : v, π, puis leur produit sommé.

Un pari symétrique, gagner ou perdre le même écart $x$ à pile ou face : $p=q=\tfrac12$ et
$y=-x$. À gauche, la fonction de valeur $v$, nulle au point de référence et plus raide du
côté des pertes, lit $v(x)$ et $v(y)$. Au milieu, la fonction de poids $\pi$, qui s'applique
à chaque probabilité prise isolément, lit $\pi(p)$ et $\pi(q)$. À droite, chaque branche est
un rectangle de largeur $\pi$ et de hauteur $v$, au-dessus de l'axe pour le gain, au-dessous
pour la perte : $V=\pi(p)v(x)+\pi(q)v(y)$ est l'aire signée, négative ici parce que la perte
pèse plus que le gain, $v(x)<-v(-x)$. Rien n'est gradué : la fiche ne donne d'échelle ni
pour $v$ ni pour $\pi$. Les formes tracées — $v$ de courbure 0,7 et deux fois plus raide
côté pertes, $\pi$ en S inversé — sont des choix de dessin.

Usage : python courses/dup/figures/theorie-des-perspectives.py > theorie-des-perspectives.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

E, C, R = 50.0, 0.7, 2.0
v = lambda x: (x / E) ** C if x >= 0 else -R * ((-x) / E) ** C
B = 0.7
pi = lambda p: p ** B / (p ** B + (1 - p) ** B) ** (1 / B) if 0 < p < 1 else float(p)
X, P = 35.0, 0.5
VX, VY, PP = v(X), v(-X), pi(P)
H, LBL = 250, 13

g = Figure(xmin=-E, xmax=E, ymin=-R - 0.1, ymax=1.5, w=230, h=H, marges=(6, 30, 40, 6))
g.axes(croix=(0, 0))
g.fonction(v, -E, -0.5, couleur=ENCRE, epaisseur=2.3)
g.fonction(v, 0.5, E, couleur=ENCRE, epaisseur=2.3)
g.segment(X, 0, X, VX, couleur=PALE)
g.segment(-X, 0, -X, VY, couleur=PALE)
g.point(X, VX, couleur=ACCENT)
g.point(-X, VY, couleur=AJOUT)
g.texte(X, VX, "v(x)", couleur=ACCENT, ancre="middle", dy=-9, gras=True, taille=12)
g.texte(-X, VY, "v(y)", couleur=AJOUT, ancre="start", dx=7, dy=4, gras=True, taille=12)
g.texte(X, 0, "x", couleur=ACCENT, ancre="middle", dy=16, taille=12)
g.texte(-X, 0, "y", couleur=AJOUT, ancre="middle", dy=-6, taille=12)
g.texte(0, 1.5, "la valeur v", ancre="middle", dy=-12, gras=True, taille=12.5)
g.texte(0, -R - 0.1, "écart au point de référence", couleur=DOUX, ancre="middle", dy=30, taille=11.5)

m = Figure(xmin=0, xmax=1.05, ymin=0, ymax=1.12, w=210, h=H, marges=(10, 30, 40, 6))
m.axes(xticks=(0.5,), fmt=lambda t: "p = q", croix=(0, 0))
m.segment(0, 0, 1, 1, couleur=PALE)
m.fonction(pi, 0.001, 0.999, couleur=ENCRE, epaisseur=2.3)
m.segment(P, 0, P, PP, couleur=PALE)
m.segment(0, PP, P, PP, couleur=ACCENT, epaisseur=1.2, pointilles="4 3")
m.point(P, PP, couleur=ENCRE)
m.texte(0, PP, "π(p) = π(q)", couleur=ENCRE, ancre="start", dx=4, dy=-6, gras=True, taille=12)
m.texte(0.5, 1.12, "le poids π", ancre="middle", dy=-12, gras=True, taille=12.5)
m.texte(0.5, 0, "probabilité", couleur=DOUX, ancre="middle", dy=30, taille=11.5)

d = Figure(xmin=-0.05, xmax=1.0, ymin=-R - 0.1, ymax=1.5, w=230, h=H, marges=(6, 30, 40, 6))
d.axes(croix=(0, 0))
d.barre(PP / 2, VX, PP, couleur=ACCENT, opacite=0.8, y0=0)
d.barre(PP + PP / 2, VY, PP, couleur=AJOUT, opacite=0.8, y0=0)
d.texte(PP / 2, VX, "π(p) v(x)", couleur=ACCENT, ancre="middle", dy=-7, gras=True, taille=12)
d.texte(PP * 1.5, VY, "π(q) v(y)", couleur=AJOUT, ancre="middle", dy=16, gras=True, taille=12)
d.texte(0.47, 1.5, "V : l'aire signée", ancre="middle", dy=-12, gras=True, taille=12.5)
d.texte(0.47, -R - 0.1, "V = π(p) v(x) + π(q) v(y) < 0", couleur=ENCRE, ancre="middle", dy=30,
        gras=True, taille=12)

sys.stdout.write(Planche([g, m, d], signes=("×", "="), ecart=30,
                         titre="Chaque branche : sa valeur fois le poids de sa probabilité ; "
                               "la perspective vaut leur somme").svg())
