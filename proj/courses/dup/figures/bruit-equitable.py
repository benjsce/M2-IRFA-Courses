#!/usr/bin/env python3
r"""
bruit-equitable.svg — l'exemple du cours, dessiné comme un tirage en deux temps.

$\tilde x$ est uniforme sur $\{40,60\}$ ; à chaque résultat on ajoute $\pm20$ à pile ou
face. 40 devient 20 ou 60, 60 devient 40 ou 80 : $\tilde y$ est uniforme sur
$\{20,40,60,80\}$. Chaque paire de flèches part d'un point et se sépare symétriquement :
c'est $\mathbb{E}[\tilde\varepsilon\mid\tilde x]=0$, lu sur le dessin. La moyenne, 50,
est la même des deux côtés.

Usage : python courses/dup/figures/bruit-equitable.py > bruit-equitable.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

G, D = 0.22, 0.78              # abscisses des deux colonnes
f = Figure(xmin=0, xmax=1, ymin=8, ymax=100, w=560, h=330, marges=(20, 14, 16, 20),
           titre="Chaque résultat se sépare en deux, symétriquement : la moyenne ne bouge pas")

f.segment(0.06, 50, 0.94, 50, couleur=DOUX, epaisseur=1.2, pointilles="5 4")
f.texte(0.94, 50, "moyenne 50", couleur=DOUX, ancre="end", dy=-6, taille=11.5, fond=True)

for x in (40, 60):
    for e, coul in ((-20, AJOUT), (20, ACCENT)):
        f.fleche(G + 0.02, x, D - 0.03, x + e, couleur=coul, epaisseur=1.6)
        t = 0.74                           # près de l'arrivée, où les quatre flèches sont séparées
        f.texte(G + t * (D - G), x + t * e, "+20" if e > 0 else "−20", couleur=coul,
                ancre="middle", dy=-7 if e > 0 else 17, taille=11.5, gras=True, fond=True)
    f.point(G, x, couleur=ENCRE, r=4.2)
    f.texte(G, x, str(x), couleur=ENCRE, ancre="end", dx=-10, dy=5, gras=True)

for y in (20, 40, 60, 80):
    f.point(D, y, couleur=ENCRE, r=4.2)
    f.texte(D, y, str(y), couleur=ENCRE, dx=10, dy=5, gras=True)

f.texte(G, 94, "x : ½ chacun", couleur=ENCRE, ancre="middle", gras=True)
f.texte(D, 94, "y = x + ε : ¼ chacun", couleur=ENCRE, ancre="middle", gras=True)

sys.stdout.write(f.svg())
