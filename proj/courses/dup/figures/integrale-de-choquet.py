#!/usr/bin/env python3
r"""
integrale-de-choquet.svg — l'escalier de la fiche, dont l'aire est l'intégrale.

La fiche lit l'intégrale comme un escalier : on part du pire résultat, acquis dans tous
les états, et l'on paie chaque marche au prix de la capacité de l'événement où on la
franchit. Sur son exemple, $X(L)=1$, $X(H)=3$, $\mu(H)=0{,}4$ : la première marche, de 0 à
1, est franchie partout et compte pour $\mu(S)=1$ ; la seconde, de 1 à 3, n'est franchie
que dans $H$ et compte pour $0{,}4$. L'aire totale vaut $1+2\times0{,}4=1{,}8$.

En abscisse, le niveau de paiement ; en ordonnée, la capacité de l'événement où le
paiement atteint ce niveau.

Usage : python courses/dup/figures/integrale-de-choquet.py > integrale-de-choquet.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE      # noqa: E402

XL, XH, MU_H = 1.0, 3.0, 0.4

f = Figure(xmin=0, xmax=3.5, ymin=0, ymax=1.2, w=560, h=330,
           titre="Première marche comptée pour 1, seconde pour 0,4 : l'aire vaut 1,8")
f.axes(xlab="niveau de paiement", ylab="capacité", xticks=(0, 1, 3), yticks=(0.4, 1),
       fmt=lambda t: str(int(t)), fmt_y=lambda t: ("%g" % t).replace(".", ","))

f.barre(XL / 2, 1.0, XL, couleur=ACCENT, opacite=0.30)
f.barre((XL + XH) / 2, MU_H, XH - XL, couleur=AJOUT, opacite=0.30)
f.courbe([(0, 1), (XL, 1), (XL, MU_H), (XH, MU_H), (XH, 0)], couleur=ENCRE, epaisseur=2.0)

f.texte(XL / 2, 0.62, "1 × 1", couleur=ACCENT, ancre="middle", gras=True)
f.texte(XL / 2, 0.62, "acquis partout", couleur=ACCENT, ancre="middle", dy=16, taille=11.5)
f.texte((XL + XH) / 2, 0.22, "(3 − 1) × μ(H) = 0,8", couleur=AJOUT, ancre="middle",
        gras=True)
f.texte((XL + XH) / 2, MU_H, "la marche, franchie dans H seulement", couleur=AJOUT,
        ancre="middle", dy=-9, taille=11.5, fond=True)

sys.stdout.write(f.svg())
