#!/usr/bin/env python3
r"""
lasso.svg — les mêmes courbes de niveau de la RSS, face au disque de ridge et au losange du lasso.

La raison géométrique de la fiche. Deux coefficients ; l'estimation des moindres carrés est
le point central, marqué MCO, et les ellipses sont les courbes de niveau de la RSS autour de
lui : les mêmes quatre dans les deux cadres. La solution contrainte est le point où la
première d'entre elles, en partant du centre, touche la région : à gauche le disque de ridge,
$\beta_1^2+\beta_2^2\le1$, touché en un point de son bord où aucun coefficient n'est nul
(niveau 0,165) ; à droite le losange du lasso, $|\beta_1|+|\beta_2|\le1$, touché en un coin,
sur l'axe, où $\beta_2=0$ exactement (niveau 0,323). Dans chaque cadre, l'ellipse de contact
est en noir ; les autres restent grises. Les deux axes ont la même échelle, pour que le
disque soit rond. L'ellipse, son centre et son orientation sont choisis pour le dessin ; les
points et les niveaux de contact sont calculés.

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


def contact(bord):
    return min((Q(bord(4 * k / 40000)), bord(4 * k / 40000)) for k in range(40000))


QR, _ = contact(bord_disque)
QL, _ = contact(bord_losange)
NIVEAUX = (0.4 * QR, QR, QL, 1.7 * QL)            # les mêmes dans les deux cadres

XMIN, XMAX, YMIN = -1.3, 2.6, -1.3
W, H, MG, MH, MB, MD = 274, 270, 12, 30, 32, 12
YMAX = YMIN + (H - MH - MB) * (XMAX - XMIN) / (W - MG - MD)      # même échelle sur les deux axes


def cadre(titre, bord, couleur, legende):
    g = Figure(xmin=XMIN, xmax=XMAX, ymin=YMIN, ymax=YMAX, w=W, h=H, marges=(MG, MH, MB, MD))
    g.axes(xlab="β1", ylab="", xticks=(), yticks=(), croix=(0, 0))
    g.texte(0, YMAX, "β2", couleur=DOUX, ancre="end", dx=-6, dy=12, taille=12)
    region = [bord(4 * k / 400) for k in range(401)]
    g._add('<path d="M%s Z" fill="%s" fill-opacity="0.25" stroke="none"/>'
           % (" L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in region), couleur))
    g.courbe(region, couleur=couleur, epaisseur=2.0)
    q, b = contact(bord)
    for niv in NIVEAUX:
        noir = abs(niv - q) < 1e-9
        g.courbe(ellipse(niv), couleur=ENCRE if noir else DOUX, epaisseur=1.8 if noir else 1.1)
    g.point(*BH, couleur=ENCRE)
    g.texte(*BH, "MCO", couleur=ENCRE, dx=6, dy=-4, taille=11, gras=True, fond=True)
    g.point(*b, couleur=AJOUT, r=5)
    g.texte((XMIN + XMAX) / 2, YMAX, titre, couleur=couleur, ancre="middle", dy=-12, gras=True)
    g.texte((XMIN + XMAX) / 2, YMIN, legende, couleur=AJOUT, ancre="middle", dy=22, taille=11.5,
            gras=True)
    return g


gr = cadre("ridge : un disque", bord_disque, ACCENT, "le contact : aucun β nul")
gl = cadre("lasso : un losange", bord_losange, AJOUT, "le contact : un coin, β2 = 0")
sys.stdout.write(Planche([gr, gl], ecart=30,
                         titre="La première ellipse touche le disque sur son bord, le losange sur un coin").svg())
