#!/usr/bin/env python3
r"""
esperance-conditionnelle.svg — sur chaque atome de 𝒢, la même aire que X.

Ce que la figure doit faire voir : Z = E[X|𝒢] est constante là où l'information 𝒢 ne
distingue rien, et sur chacun de ces morceaux elle a la même aire que X, ce qui est
E[XU] = E[ZU] pour U l'indicatrice du morceau.

Le monde du cours : deux lancers d'une pièce équilibrée, Ω = {PP, PF, FP, FF}, chaque
issue de probabilité ¼ ; X est le nombre de piles, 2, 1, 1, 0 ; 𝒢 est l'information du
premier lancer, dont les deux atomes sont {premier = P} et {premier = F}. Chaque issue
est une barre de largeur ¼, sa probabilité, et de hauteur X : l'aire d'un groupe de
barres est donc E[X 1_A]. Z vaut 1,5 sur le premier atome, 0,5 sur le second, et ses
aires sont celles de X : ½ × 1,5 = ¼ × 2 + ¼ × 1 = 0,75 ; ½ × 0,5 = ¼ × 1 + ¼ × 0 = 0,25.

Usage : python courses/cs/figures/esperance-conditionnelle.py > esperance-conditionnelle.svg
Dépendance : aucune.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

ISSUES = ["PP", "PF", "FP", "FF"]
P = Fr(1, 4)
X = {w: w.count("P") for w in ISSUES}
ATOMES = {"premier lancer pile": ["PP", "PF"], "premier lancer face": ["FP", "FF"]}
Z = {}
for nom, A in ATOMES.items():
    z = sum(X[w] * P for w in A) / (P * len(A))
    for w in A:
        Z[w] = z
    assert sum(X[w] * P for w in A) == sum(Z[w] * P for w in A)     # E[X 1_A] = E[Z 1_A]
assert (Z["PP"], Z["FP"]) == (Fr(3, 2), Fr(1, 2))
fr = lambda q: ("%g" % float(q)).replace(".", ",")

f = Figure(0, 1, -0.75, 2.45, w=600, h=360, marges=(40, 16, 12, 14),
           titre="E(X|𝒢) a, sur chaque atome de 𝒢, la même aire que X")
# les axes à la main : celui des hauteurs s'arrête à 0, les atomes s'écrivent dessous
f.courbe([(0, 0), (1, 0)], couleur=DOUX, epaisseur=1.2)
f.courbe([(0, 0), (0, 2.45)], couleur=DOUX, epaisseur=1.2)
for t in (0.5, 1, 1.5, 2):
    f.segment(0, t, -0.008, t, couleur=DOUX, epaisseur=1.2, pointilles=None)
    f.texte(0, t, fr(t), couleur=DOUX, taille=11.5, ancre="end", dx=-8, dy=4)
for k, w in enumerate(ISSUES):
    x = (k + 0.5) * float(P)
    f.barre(x, X[w], float(P) * 0.96, couleur=ACCENT, opacite=0.35, y0=0)
    f.texte(x, X[w], "X = %d" % X[w], couleur=ACCENT, ancre="middle", dy=-6)
    f.texte(x, 0, w, couleur=DOUX, ancre="middle", dy=16)
    f.texte(x, 0, "proba ¼", couleur=DOUX, ancre="middle", dy=31, taille=11)

for nom, A in ATOMES.items():
    k0 = ISSUES.index(A[0])
    x0, x1 = k0 * float(P), (k0 + len(A)) * float(P)
    z = float(Z[A[0]])
    f.courbe([(x0, z), (x1, z)], couleur=AJOUT, epaisseur=3.4)
    f.texte((x0 + x1) / 2, z, "Z = E(X|𝒢) = " + fr(z), couleur=AJOUT, ancre="middle", dy=-8, gras=True)
    # l'atome, sous les issues
    f.courbe([(x0 + 0.01, -0.42), (x1 - 0.01, -0.42)], couleur=ENCRE, epaisseur=1.4)
    f.segment(x0 + 0.01, -0.42, x0 + 0.01, -0.36, couleur=ENCRE, epaisseur=1.4, pointilles=None)
    f.segment(x1 - 0.01, -0.42, x1 - 0.01, -0.36, couleur=ENCRE, epaisseur=1.4, pointilles=None)
    f.texte((x0 + x1) / 2, -0.42, nom, couleur=ENCRE, ancre="middle", dy=17)
    aire = sum(X[w] * P for w in A)
    f.texte((x0 + x1) / 2, -0.42, "E(X 1_{A}) = E(Z 1_{A}) = " + fr(aire), couleur=ENCRE,
            ancre="middle", dy=35, gras=True)

sys.stdout.write(f.svg())
