#!/usr/bin/env python3
r"""
lemme-de-gel.svg — geler la variable connue, moyenner sur l'autre.

Ce que la figure doit faire voir : pour calculer E[Φ(X, Y)|𝒢] quand Y est connue et X
indépendante de 𝒢, on fige Y à chacune de ses valeurs y, on moyenne Φ(X, y) sur X seule
— c'est ψ(y) —, puis on remet Y à la place de y.

Le monde du cours : deux lancers d'une pièce équilibrée ; 𝒢 l'information du premier ;
Y vaut 1 si le premier lancer donne pile, 0 sinon, et elle est connue dans 𝒢 ; X vaut 1
si le second donne pile, 0 sinon, et elle est indépendante de 𝒢. Avec Φ(x, y) = (x + y)²,
Φ(X, Y) est le carré du nombre de piles. Un cadre par valeur gelée de Y ; dans chacun,
les deux valeurs de X, de probabilité ½, en barres de hauteur Φ(x, y). La moyenne est ψ(y) :
ψ(1) = ½ × 4 + ½ × 1 = 2,5 ; ψ(0) = ½ × 1 + ½ × 0 = 0,5.

Usage : python courses/cs/figures/lemme-de-gel.py > lemme-de-gel.svg
Dépendance : aucune.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE   # noqa: E402

PHI = lambda x, y: (x + y) ** 2
psi = lambda y: Fr(1, 2) * PHI(1, y) + Fr(1, 2) * PHI(0, y)
assert (psi(1), psi(0)) == (Fr(5, 2), Fr(1, 2))
# contrôle direct : sachant le premier lancer, la moyenne du carré du nombre de piles
for y in (0, 1):
    assert Fr(sum((y + x) ** 2 for x in (0, 1)), 2) == psi(y)
fr = lambda q: ("%g" % float(q)).replace(".", ",")


def cadre(y):
    f = Figure(0, 1, -0.9, 4.7, w=300, h=250, marges=(10, 18, 6, 10))
    f.courbe([(0, 0), (1, 0)], couleur=DOUX, epaisseur=1.2)
    for k, x in enumerate((1, 0)):
        c = 0.25 + 0.5 * k
        v = PHI(x, y)
        f.barre(c, v, 0.46, couleur=ACCENT, opacite=0.4, y0=0)
        f.texte(c, v, "Φ(%d, %d) = %d" % (x, y, v), couleur=ACCENT, ancre="middle", dy=-6, gras=True)
        f.texte(c, 0, "X = %d, proba ½" % x, couleur=DOUX, ancre="middle", dy=16, taille=11.5)
    p = float(psi(y))
    f.courbe([(0, p), (1, p)], couleur=AJOUT, epaisseur=3.0)
    f.texte(0.03, p, "ψ(%d) = %s" % (y, fr(psi(y))), couleur=AJOUT, dy=-7, gras=True)
    f.texte(0.5, 4.7, "Y = %d gelée : premier lancer %s" % (y, "pile" if y else "face"),
            couleur=ENCRE, ancre="middle", dy=-2, gras=True)
    f.texte(0.5, -0.9, "ψ(%d) = E(Φ(X, %d)), moyenne sur X seule" % (y, y), couleur=ENCRE,
            ancre="middle", dy=-4, taille=12)
    return f


sys.stdout.write(Planche([cadre(1), cadre(0)], ecart=30,
                         titre="E(Φ(X,Y)|𝒢) = ψ(Y), avec ψ(y) = E(Φ(X,y))").svg())
