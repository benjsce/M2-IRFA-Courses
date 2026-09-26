#!/usr/bin/env python3
r"""
lasso.svg — la même ellipse de RSS, face au disque de ridge et au losange du lasso.

La raison géométrique de la fiche. Deux coefficients ; l'estimation des moindres carrés est
le point central, marqué MCO, et les ellipses sont les courbes de niveau de la RSS autour de lui. La
solution contrainte est le premier point où une ellipse touche la région : à gauche le
disque de ridge, $\beta_1^2+\beta_2^2\le1$, touché en un point quelconque de son bord, où
aucun coefficient n'est nul ; à droite le losange du lasso, $|\beta_1|+|\beta_2|\le1$,
touché en un coin, sur l'axe, où $\beta_2=0$ exactement. L'ellipse, son centre et son
orientation sont choisis pour le dessin ; les points de contact sont calculés.

Usage : python courses/dss/figures/lasso.py > lasso.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, ENCRE, DOUX, AJOUT, _n      # noqa: E402

BH = (1.3, 0.45)                                  # l'estimation des moindres carrés
A = ((1.0, 0.45), (0.45, 0.55))                   # la forme quadratique de la RSS


def Q(b):
    u, v = b[0] - BH[0], b[1] - BH[1]
    return A[0][0] * u * u + 2 * A[0][1] * u * v + A[1][1] * v * v


def bord_losange(t):
    t = t % 4
    if t < 1:
        return (1 - t, t)
    if t < 2:
        return (-(t - 1), 1 - (t - 1))
    if t < 3:
        return (-(3 - t), -(t - 2))
    return (t - 3, -(4 - t))


def bord_disque(t):
    a = 2 * math.pi * t / 4
    return (math.cos(a), math.sin(a))


def ellipse(niveau, n=160):
    # points de Q(b) = niveau : on résout le long de chaque direction depuis le centre
    pts = []
    for k in range(n + 1):
        a = 2 * math.pi * k / n
        c, s = math.cos(a), math.sin(a)
        q = A[0][0] * c * c + 2 * A[0][1] * c * s + A[1][1] * s * s
        r = math.sqrt(niveau / q)
        pts.append((BH[0] + r * c, BH[1] + r * s))
    return pts


def cadre(titre, bord, couleur):
    g = Figure(xmin=-1.4, xmax=3.0, ymin=-1.4, ymax=1.9, w=280, h=260, marges=(24, 30, 26, 10))
    g.axes(xlab="β1", ylab="", xticks=(), yticks=(), croix=(0, 0))
    g.texte(0, 1.9, "β2", couleur=DOUX, dx=6, dy=10, taille=12)
    region = [bord(4 * k / 400) for k in range(401)]
    g._add('<path d="M%s Z" fill="%s" fill-opacity="0.25" stroke="none"/>'
           % (" L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in region), couleur))
    g.courbe(region, couleur=couleur, epaisseur=2.0)
    q, b = min((Q(bord(4 * k / 40000)), bord(4 * k / 40000)) for k in range(40000))
    for m in (1.0, 2.2, 3.8):
        g.courbe(ellipse(q * m if m > 1 else q), couleur=DOUX if m > 1 else ENCRE,
                 epaisseur=1.2 if m > 1 else 1.8)
    g.point(*BH, couleur=ENCRE)
    g.texte(*BH, "MCO", couleur=ENCRE, dx=6, dy=-4, taille=11, gras=True)
    g.point(*b, couleur=AJOUT, r=5)
    g.texte(0.45, 1.9, titre, couleur=couleur, ancre="middle", dy=-10, gras=True)
    return g, b


gr, br = cadre("ridge : un disque", bord_disque, ACCENT)
gl, bl = cadre("lasso : un losange", bord_losange, AJOUT)
gr.texte(0.8, -1.3, "le contact : aucun β nul", couleur=AJOUT, ancre="middle", taille=11.5, gras=True)
gl.texte(0.8, -1.3, "le contact : un coin, β2 = 0", couleur=AJOUT, ancre="middle", taille=11.5,
         gras=True)
sys.stdout.write(Planche([gr, gl], ecart=30,
                         titre="L'ellipse touche le disque sur son bord, le losange sur un coin").svg())
