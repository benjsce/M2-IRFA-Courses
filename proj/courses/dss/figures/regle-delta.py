#!/usr/bin/env python3
r"""
regle-delta.svg — une correction de la règle delta, avant et après, sur le OU logique.

Ce que la figure doit faire voir : un point mal classé fait bouger la frontière vers lui ;
seuls bougent les poids des entrées actives, et la frontière passe de l'autre côté du
point.

L'exemple de la fiche : le OU logique, poids de départ $(w_0,w_1,w_2)=(-0{,}5\,;0{,}45\,;1)$,
$\eta=0{,}1$. Au point $(1,0)$, dont la sortie désirée est 1, la somme vaut $-0{,}05$ et le
neurone répond 0 : $d=1$. Les poids deviennent $(-0{,}4\,;0{,}55\,;1)$ — $w_2$ ne bouge pas,
parce que $x_2=0$ —, la somme au même point vaut $0{,}15$, et le point passe du bon côté.
Sorties désirées 1 pleines, 0 creuses ; la frontière est la droite où la somme s'annule.

Usage : python courses/dss/figures/regle-delta.py > regle-delta.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

OU = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
ETA = 0.1
AVANT = (-0.5, 0.45, 1.0)
x, t = (1.0, 0.0), 1
a = AVANT[0] + AVANT[1] * x[0] + AVANT[2] * x[1]
y = 1 if a > 0 else 0
d = t - y
APRES = tuple(w + ETA * d * xi for w, xi in zip(AVANT, (1.0,) + x))
virg = lambda v: ("%.2f" % v).rstrip("0").rstrip(".").replace(".", ",").replace("-", "−")


def cadre(titre, w, legende):
    g = Figure(xmin=-0.5, xmax=2.1, ymin=-0.5, ymax=1.6, w=330, h=300, marges=(50, 34, 48, 10))
    g.axes(xlab="x1", ylab="x2", xticks=(0, 1), yticks=(0, 1), fmt=lambda v: "%d" % v,
           fmt_y=lambda v: "%d" % v, croix=(-0.5, -0.5))
    w0, w1, w2 = w
    droite = lambda u: -(w0 + w1 * u) / w2          # la somme s'annule : w0 + w1 x1 + w2 x2 = 0
    xa, xb = -0.5, 2.1
    pts = [(u, droite(u)) for u in (xa, xb)]
    # coupe au cadre en ordonnée
    (u0, v0), (u1, v1) = pts
    if v1 < -0.5:
        u1 = -(w0 + w2 * -0.5) / w1
        v1 = -0.5
    g.courbe([(u0, v0), (u1, v1)], couleur=AJOUT, epaisseur=2.2)
    for (p, q), s in OU.items():
        somme = w0 + w1 * p + w2 * q
        juste = (1 if somme > 0 else 0) == s
        if s:
            g.point(p, q, couleur=ACCENT, r=7)
        else:
            g.point(p, q, couleur=ENCRE, r=7)
            g.point(p, q, couleur="var(--card)", r=4.5)
        if (p, q) == (1, 0):
            g.texte(p, q, "somme " + virg(somme) + (" : 1" if somme > 0 else " : 0"),
                    couleur=ENCRE if juste else ACCENT, dx=12, dy=-10, taille=11.5,
                    gras=not juste, fond=True)
    g.texte(0.8, 1.6, titre, couleur=ENCRE, ancre="middle", dy=-14, gras=True)
    g.texte(0.8, 1.6, legende, couleur=DOUX, ancre="middle", dy=2, taille=11)
    return g


p = Planche([cadre("avant", AVANT, "poids (%s ; %s ; %s)" % tuple(virg(v) for v in AVANT)),
             cadre("après un pas", APRES, "poids (%s ; %s ; %s)" % tuple(virg(v) for v in APRES))],
            signes=("→",), ecart=34,
            titre="Un point mal classé tire la frontière vers lui ; le poids d'une entrée nulle ne bouge pas")
sys.stdout.write(p.svg())
