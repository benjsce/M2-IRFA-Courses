#!/usr/bin/env python3
r"""
coefficient-d-asymetrie.svg — ce que chaque observation apporte au coefficient.

La série de la fiche, $\{-2, -1, 0, 1, 2, -10\}$ en %, de moyenne $-1{,}67\,\%$ et
d'écart type $3{,}94\,\%$. Le coefficient est la moyenne des cubes des écarts réduits ;
chaque barre est le cube d'une observation. Les écarts se comptent depuis la moyenne,
$-1{,}67\,\%$ : c'est pourquoi $-2\,\%$ ne contribue presque rien et $-1\,\%$ contribue
positivement. Cinq barres restent près de zéro, et la sixième, celle de $-10\,\%$, vaut
$-9{,}43$ à elle seule : divisée par six, elle emporte le signe et la valeur de
l'ensemble, $-1{,}37$. L'écart type est celui de `stats.skew`, sans correction de petit
échantillon.

Les étiquettes s'ancrent aux barres : celle de la grande barre finit à six pixels de son
bord gauche, quelle que soit la police.

Usage : python courses/pfo/figures/coefficient-d-asymetrie.py > coefficient-d-asymetrie.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

X = [-2, -1, 0, 1, 2, -10]
m = sum(X) / len(X)
s = math.sqrt(sum((x - m) ** 2 for x in X) / len(X))
CUBES = [((x - m) / s) ** 3 for x in X]
S = sum(CUBES) / len(X)                                   # -1,37

moins = lambda t: t.replace("-", "−")
LARG = 0.55                                               # largeur d'une barre

f = Figure(xmin=0.3, xmax=6.7, ymin=-10.5, ymax=2.8, w=560, h=320,
           titre="Une seule perte lointaine, élevée au cube, fait tout le coefficient")
f.axes(xlab="", ylab="cube de l'écart réduit", xticks=(), yticks=(-9, -6, -3, 1),
       fmt_y=lambda t: moins("%d" % t), croix=(0.3, 0))

for k, (x, c) in enumerate(zip(X, CUBES), start=1):
    grosse = abs(c) > 2
    f.barre(k, c, LARG, couleur=AJOUT if grosse else ACCENT, y0=0)
    f.texte(k, 2.2, moins(("%+d %%" % x).replace("+0", "0")), couleur=ENCRE,
            ancre="middle", dy=4, taille=11.5, gras=grosse)
    if not grosse:
        f.texte(k, max(c, 0), ("%.2f" % abs(c) if abs(c) >= 0.005 else "0").replace(".", ","),
                couleur=DOUX, ancre="middle", dy=-6, taille=10.5)
f.texte(6 - LARG / 2, CUBES[-1], moins(("%.2f" % CUBES[-1]).replace(".", ",")), couleur=AJOUT,
        ancre="end", dx=-6, dy=4, gras=True)
f.segment(0.3, S, 6.7, S, couleur=ENCRE, epaisseur=1.4)
f.texte(2.4, S, "moyenne des six : " + moins(("%.2f" % S).replace(".", ",")), couleur=ENCRE,
        ancre="middle", dy=18, gras=True, fond=True)

sys.stdout.write(f.svg())
