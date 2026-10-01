#!/usr/bin/env python3
r"""
densite-des-processus-elementaires.svg — des escaliers de plus en plus fins.

Ce que la figure doit faire voir : un processus progressivement mesurable de carré
intégrable est approché, pour la norme de L²_prog, par des processus élémentaires ; l'écart
E[∫₀ᵀ (X_s − Xⁿ_s)² ds] tend vers 0 quand le pas se resserre.

L'exemple : X_t = t sur [0, 1], un processus sans aléa, donc adapté à toute filtration.
L'escalier Xⁿ prend sur [t_i, t_{i+1}[ la valeur de X au départ de la marche, X_{t_i} = t_i,
connue en t_i : c'est un processus élémentaire. Sur une marche de longueur h = 1/n,
l'écart vaut ∫₀ʰ u² du = h³/3, et sur les n marches n h³/3 = 1/(3n²) : 1/12 pour n = 2,
1/48 pour n = 4. Les triangles colorés sont l'écart X − Xⁿ, dont la norme mesure le carré.

Usage : python courses/cs/figures/densite-des-processus-elementaires.py > densite-des-processus-elementaires.svg
Dépendance : aucune.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, AJOUT, DOUX, ENCRE, FOND   # noqa: E402


def ecart(n):
    """E[∫₀¹ (X_s − Xⁿ_s)² ds] pour X_s = s : somme sur les marches de ∫ (s − t_i)² ds."""
    h = Fr(1, n)
    return sum(h ** 3 / 3 for _ in range(n))


assert ecart(2) == Fr(1, 12) and ecart(4) == Fr(1, 48)
fr = lambda v: ("%g" % v).replace(".", ",")


def cadre(n):
    f = Figure(-0.04, 1.08, 0, 1.12, w=300, h=280, marges=(30, 10, 58, 8))
    f.axes(xticks=(0, 0.5, 1), yticks=(0.5, 1), fmt=fr, croix=(0, 0))
    f.texte(1.08, 0, "t", couleur=DOUX, ancre="end", dy=-6)
    for i in range(n):
        a, b = i / n, (i + 1) / n
        # le triangle d'écart entre X et la marche
        f._add('<path d="M%.2f %.2f L%.2f %.2f L%.2f %.2f Z" fill="%s" fill-opacity="0.35"/>'
               % (f.px(a), f.py(a), f.px(b), f.py(b), f.px(b), f.py(a), AJOUT))
        f.courbe([(a, a), (b, a)], couleur=ENCRE, epaisseur=2.6)
        f.point(a, a, couleur=ENCRE, r=3.6)
        f.point(b, a, couleur=ENCRE, r=3.8)
        f.point(b, a, couleur=FOND, r=2.2)
    f.courbe([(0, 0), (1, 1)], couleur=ACCENT, epaisseur=2.2)
    f.texte(0.02, 1.0, "X_{t} = t", couleur=ACCENT, gras=True)
    f.texte(0.02, 1.0, "escalier X^{n}, n = %d" % n, couleur=ENCRE, dy=18, gras=True)
    e = ecart(n)
    f.texte(0.5, 0, "E(∫(X_{s} − X^{n}_{s})² ds) = 1/(3n²) = %d/%d" % (e.numerator, e.denominator),
            couleur=AJOUT, ancre="middle", dy=46, gras=True, taille=12)
    return f


sys.stdout.write(Planche([cadre(2), cadre(4)], signes=("→",), ecart=34,
                         titre="Le pas se resserre, l'écart tend vers 0 : ℰ est dense dans L²_prog").svg())
