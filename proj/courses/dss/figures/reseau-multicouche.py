#!/usr/bin/env python3
r"""
reseau-multicouche.svg — la couche cachée rend le OU exclusif linéaire.

Ce que la figure doit faire voir : dans le plan des entrées, aucune droite ne sépare les
sorties du OU exclusif ; la couche cachée envoie chaque point dans le plan de ses deux
sorties, où $(0,1)$ et $(1,0)$ tombent au même endroit, et une seule droite suffit alors.

Le réseau de l'exemple de la fiche, en neurones à seuil. Nœuds cachés :
$h_1=\text{seuil}(x_1+x_2-0{,}5)$, le OU ; $h_2=\text{seuil}(x_1+x_2-1{,}5)$, le ET. Sortie :
$\text{seuil}(h_1-h_2-0{,}5)$, la droite $h_1-h_2=0{,}5$ du second plan. Sorties désirées 1
pleines, 0 creuses.

Usage : python courses/dss/figures/reseau-multicouche.py > reseau-multicouche.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

XOU = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}
seuil = lambda a: 1 if a > 0 else 0
cache = lambda x1, x2: (seuil(x1 + x2 - 0.5), seuil(x1 + x2 - 1.5))
sortie = lambda h1, h2: seuil(h1 - h2 - 0.5)
assert all(sortie(*cache(*p)) == v for p, v in XOU.items())     # le réseau calcule le OU exclusif


def cadre(xlab, ylab, titre):
    g = Figure(xmin=-0.5, xmax=1.7, ymin=-0.5, ymax=1.6, w=300, h=300, marges=(50, 34, 44, 10))
    g.axes(xlab=xlab, ylab=ylab, xticks=(0, 1), yticks=(0, 1), fmt=lambda v: "%d" % v,
           fmt_y=lambda v: "%d" % v, croix=(-0.5, -0.5))
    g.texte(0.6, 1.6, titre, couleur=ENCRE, ancre="middle", dy=-16, gras=True)
    return g


def marque(g, p, q, v):
    if v:
        g.point(p, q, couleur=ACCENT, r=7)
    else:
        g.point(p, q, couleur=ENCRE, r=7)
        g.point(p, q, couleur="var(--card)", r=4.5)


# à gauche : le plan des entrées, les deux droites des nœuds cachés
g1 = cadre("x1", "x2", "entrées : aucune droite ne suffit")
for c in (0.5, 1.5):
    xa, xb = max(-0.5, c - 1.6), min(1.7, c + 0.5)
    g1.courbe([(xa, c - xa), (xb, c - xb)], couleur=DOUX, epaisseur=1.6, pointilles="5 4")
for (p, q), v in XOU.items():
    marque(g1, p, q, v)
    h = cache(p, q)
    g1.texte(p, q, "→ (%d, %d)" % h, couleur=AJOUT, dx=10, dy=-9, taille=11, fond=True)

# à droite : le plan des sorties cachées, une seule droite
g2 = cadre("h1 : OU", "h2 : ET", "sorties cachées : une droite")
g2.courbe([(0.0, -0.5), (1.7, 1.2)], couleur=AJOUT, epaisseur=2.2)      # h1 − h2 = 0,5
images = {}
for (p, q), v in XOU.items():
    images.setdefault(cache(p, q), []).append(((p, q), v))
for (h1, h2), liste in images.items():
    marque(g2, h1, h2, liste[0][1])
    noms = " et ".join("(%d, %d)" % pq for pq, _ in liste)
    g2.texte(h1, h2, noms, couleur=DOUX, dx=10, dy=-9, taille=11, fond=True)

p = Planche([g1, g2], signes=("→",), ecart=34,
            titre="La couche cachée replie le plan : le OU exclusif devient séparable par une droite")
sys.stdout.write(p.svg())
