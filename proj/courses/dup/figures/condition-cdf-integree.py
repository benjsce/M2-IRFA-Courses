#!/usr/bin/env python3
r"""
condition-cdf-integree.svg — les deux répartitions, puis l'intégrale de leur écart.

Le geste de la fiche en deux temps, sur son exemple : $\tilde x$ uniforme sur
$\{40,60\}$ (répartition $F$) et $\tilde y$ uniforme sur $\{20,40,60,80\}$ (répartition
$F^*$), sur $[0,80]$. À gauche, les deux répartitions se croisent : $F^*$ est au-dessus
entre 20 et 40, au-dessous entre 60 et 80. À droite, l'intégrale de $F^*-F$ depuis 0 :
elle monte à 5 entre 20 et 40, reste à 5 jusqu'à 60, redescend et s'annule en 80 — positive
avant, nulle au bout, exactement la condition.

Usage : python courses/dup/figures/condition-cdf-integree.py > condition-cdf-integree.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

X = [40, 60]
Y = [20, 40, 60, 80]
M = 80


def repartition(support):
    return lambda t: sum(1 for s in support if s <= t) / len(support)


F, Fs = repartition(X), repartition(Y)


def escalier(support, x0=0, x1=90):
    pts, niveau = [(x0, 0.0)], 0.0
    for s in support:
        pts.append((s, niveau))
        niveau += 1.0 / len(support)
        pts.append((s, niveau))
    pts.append((x1, niveau))
    return pts


def integrale(x, pas=0.25):
    n = int(round(x / pas))
    return sum((Fs((k + 0.5) * pas) - F((k + 0.5) * pas)) * pas for k in range(n))


gauche = Figure(xmin=0, xmax=92, ymin=0, ymax=1.14, w=300, h=300, marges=(44, 30, 42, 10))
gauche.axes(xlab="t", ylab="", xticks=(20, 40, 60, 80), yticks=(0.5, 1),
            fmt=lambda t: str(int(t)), fmt_y=lambda t: {0.5: "½", 1: "1"}[t])
gauche.courbe(escalier(X), couleur=DOUX, epaisseur=2.2)
gauche.courbe(escalier(Y), couleur=ACCENT, epaisseur=2.4)
gauche.texte(46, 1.14, "les répartitions se croisent", couleur=ENCRE, ancre="middle",
             dy=-6, gras=True)
gauche.texte(22, 0.25, "F*", couleur=ACCENT, dx=2, dy=-8, gras=True)
gauche.texte(64, 1.0, "F", couleur=DOUX, dx=2, dy=-8, gras=True)

xs = [k * 0.5 for k in range(0, 181)]
droite = Figure(xmin=0, xmax=106, ymin=-0.6, ymax=6.6, w=300, h=300, marges=(44, 30, 42, 10))
droite.axes(xlab="x", ylab="", xticks=(20, 40, 60, 80), yticks=(5,),
            fmt=lambda t: str(int(t)), croix=(0, 0))
droite.courbe([(x, integrale(x)) for x in xs], couleur=AJOUT, epaisseur=2.6)
droite.point(M, 0, couleur=ENCRE)
droite.texte(M, 1.0, "nulle en 80", couleur=ENCRE, dx=2, taille=11.5, fond=True)
droite.texte(50, 5, "positive avant", couleur=AJOUT, ancre="middle", dy=-9, taille=11.5,
             fond=True)
droite.texte(53, 6.6, "∫ (F* − F) depuis 0", couleur=ENCRE, ancre="middle", dy=-6,
             gras=True)

sys.stdout.write(Planche([gauche, droite], signes=("→",), ecart=34,
                         titre="L'aire entre les répartitions reste positive et s'annule au bout").svg())
