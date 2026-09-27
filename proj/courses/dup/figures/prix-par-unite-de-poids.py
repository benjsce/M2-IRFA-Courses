#!/usr/bin/env python3
r"""
prix-par-unite-de-poids.svg — la Forme lue sur la courbe de l'utilité marginale.

L'exemple de la fiche : $q=(0{,}3;0{,}3;0{,}4)$ et $\pi=(0{,}2560;0{,}2013;0{,}5426)$, d'où
$q_s/\pi_s=(1{,}17;1{,}49;0{,}74)$, avec l'utilité du cours $u(x)=x^{0{,}6}$ et un budget
de 1, $\sum_s q_sx_s=1$, qui fixe le multiplicateur $\eta\approx0{,}639$. Pour chaque état,
on part de la hauteur $\eta\,q_s/\pi_s$ sur l'axe de $u'$, on rejoint la courbe, et l'on
descend sur l'axe des richesses : c'est $x_s=(u')^{-1}(\eta\,q_s/\pi_s)$, soit 0,58, 0,32
et 1,83. Le rapport le plus haut, celui de l'état 2, donne la richesse la plus basse.

Usage : python courses/dup/figures/prix-par-unite-de-poids.py > prix-par-unite-de-poids.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

Q = (0.3, 0.3, 0.4)
POIDS = (0.2560, 0.2013, 0.5426)
R = [q / p for q, p in zip(Q, POIDS)]
up = lambda x: 0.6 * x ** -0.4                      # u'(x) pour u(x) = x^0,6
inv = lambda y: (y / 0.6) ** -2.5                   # (u')⁻¹


def budget(eta):
    return sum(q * inv(eta * r) for q, r in zip(Q, R))


lo, hi = 1e-3, 10.0
for _ in range(200):                                 # η tel que Σ q_s x_s = 1
    m = (lo + hi) / 2
    lo, hi = (m, hi) if budget(m) > 1 else (lo, m)
ETA = (lo + hi) / 2
X = [inv(ETA * r) for r in R]


def fr(v):
    return ("%.2f" % v).replace(".", ",")


f = Figure(xmin=0, xmax=2.3, ymin=0, ymax=1.25, w=620, h=360, marges=(140, 16, 50, 16),
           titre="Chaque état reçoit la richesse où l'utilité marginale égale η q_s / π_s")
f.axes(xlab="richesse x", ylab="u′(x)", xticks=(), yticks=())
f.fonction(up, 0.22, 2.25, couleur=ENCRE, epaisseur=2.4)
f.texte(2.25, up(2.25), "u′(x) = 0,6 x^{−0,4}", couleur=ENCRE, ancre="end", dy=-10, taille=12)
COUL = (ACCENT, AJOUT, DOUX)
for s in range(3):
    y, x = ETA * R[s], X[s]
    f.segment(0, y, x, y, couleur=COUL[s], epaisseur=1.4, pointilles="5 3")
    f.fleche(x, y - 0.02, x, 0.03, couleur=COUL[s], epaisseur=1.6)
    f.texte(0, y, "η q_{%d} / π_{%d} = %s" % (s + 1, s + 1, fr(y)), couleur=COUL[s],
            ancre="end", dx=-6, dy=4, taille=11.5, gras=True)
    f.texte(x, 0, "x_{%d} = %s" % (s + 1, fr(x)), couleur=COUL[s], ancre="middle", dy=18,
            taille=11.5, gras=True)
f.texte(1.25, 1.12, "u′(x_{s}) = η q_{s} / π_{s}   ⟹   x_{s} = (u′)^{−1}(η q_{s} / π_{s})",
        couleur=ENCRE, ancre="middle", gras=True, taille=13)
f.texte(1.25, 1.12, "le rapport le plus haut, celui de l'état 2, donne la richesse la plus basse",
        couleur=DOUX, ancre="middle", dy=20, taille=12)
sys.stdout.write(f.svg())
