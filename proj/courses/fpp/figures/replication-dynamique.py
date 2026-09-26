#!/usr/bin/env python3
r"""
replication-dynamique.svg — à chaque règlement, les futures bouchent le trou.

Ce que la figure doit faire voir : à chaque date, la richesse visée, prix future divisé par
le compte capitalisé, est faite de deux morceaux ; le placement de la richesse d'avant,
connu dès le début de la période, et le trou, que bouche l'appel de marge multiplié par le
nombre de futures. Ce nombre, 1/B(t_0, t_{i+1}), grossit d'une période à l'autre.

Un échéancier à trois dates, une année entre deux règlements, les taux de la fiche du
compte capitalisé : 4 % la première année, 6 % la seconde. Le chemin du prix future,
110, 115 puis 122, n'est qu'un exemple : la stratégie marche pour tous. Les barres partent
de 100 pour que les deux morceaux se voient ; seul le haut de chaque barre compte.

Usage : python courses/fpp/figures/replication-dynamique.py > replication-dynamique.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

P01 = math.exp(-0.04)              # zéro-coupon de la première année, 0,9608
P12 = math.exp(-0.06)              # celui de la seconde, 0,9418, connu dans un an
B1, B2 = P01, P01 * P12            # compte capitalisé : 0,9608 puis 0,9048
H0, H1, H2 = 110.0, 115.0, 122.0   # prix future ; à l'échéance, H = S_T

n0, n1 = 1 / B1, 1 / B2            # 1,0408 puis 1,1052 futures
W0 = H0                            # ce que coûte la stratégie
plac1, W1 = W0 / P01, H1 / B1      # 114,49 puis 119,69
plac2, W2 = W1 / P12, H2 / B2      # 127,09 puis 134,83
v = lambda x, d=2: ("%.*f" % (d, x)).replace(".", ",")

x0, x1, x2 = 1.6, 5.2, 8.8         # les trois dates
L = 1.1                            # largeur des barres
BAS = 100.0

g = Figure(xmin=0, xmax=11.4, ymin=84, ymax=150, w=660, h=400, marges=(8, 8, 8, 8),
           titre="À chaque règlement, le placement est connu et les futures bouchent le trou")
g.axe_temps(96, 0.4, 11.1, [(x0, "t₀"), (x1, "t₁"), (x2, "t₂ = T")])


def boite(x, y0, y1, couleur, pointilles=None, remplir=True):
    if remplir:
        g.barre(x, y1, L, couleur=couleur, opacite=0.18, y0=y0)
    g.courbe([(x - L / 2, y0), (x + L / 2, y0), (x + L / 2, y1), (x - L / 2, y1),
              (x - L / 2, y0)], couleur=couleur, epaisseur=1.7, pointilles=pointilles)


# t0 : ce que coûte la stratégie, H(t0) placé ; les futures ne coûtent rien
boite(x0, BAS, W0, AJOUT)
g.texte(x0, W0 + 1.6, v(W0, 0), ancre="middle", gras=True, taille=13)
g.texte(x0, W0 + 5.2, "on place H_{t₀}", couleur=AJOUT, ancre="middle", taille=12)

# t1 et t2 : placement (connu au début de la période) + trou (futures)
for (xa, xb, Wa, plac, Wb, n, dH, Pz, taux, Hb) in (
        (x0, x1, W0, plac1, W1, n0, H1 - H0, P01, "4 %", "H_{t₁} = 115"),
        (x1, x2, W1, plac2, W2, n1, H2 - H1, P12, "6 %", "H_{T} = S_{T} = 122")):
    boite(xb, BAS, plac, ACCENT)
    boite(xb, plac, Wb, ENCRE, pointilles="5 4", remplir=False)
    g.fleche(xa + L / 2 + 0.08, Wa, xb - L / 2 - 0.08, plac, couleur=ACCENT, courbure=14)
    g.texte((xa + xb) / 2, max(Wa, plac) + 5.6, "placé à " + taux, couleur=ACCENT,
            ancre="middle", taille=12)
    g.texte((xa + xb) / 2, max(Wa, plac) + 3.1, "÷ " + v(Pz, 4), couleur=ACCENT,
            ancre="middle", taille=12)
    g.texte(xb, (BAS + plac) / 2 + 0.6, v(plac), ancre="middle", taille=12.5)
    g.texte(xb, (BAS + plac) / 2 - 2.2, "connu", couleur=DOUX, ancre="middle", taille=11)
    g.texte(xb + L / 2 + 0.12, (plac + Wb) / 2 + 1.0, "le trou :", ancre="start",
            taille=12.5, gras=True)
    g.texte(xb + L / 2 + 0.12, (plac + Wb) / 2 - 1.6,
            "%s × %s = %s" % (v(dH, 0), v(n, 4), v(Wb - plac)), ancre="start", taille=12)
    g.texte(xb, Wb + 1.6, v(Wb), ancre="middle", gras=True, taille=13)
    g.texte(xb, 88.2, Hb, couleur=DOUX, ancre="middle", taille=11.5)
    g.texte((xa + xb) / 2, 99.2, "%s futures" % v(n, 4), couleur=ENCRE, ancre="middle",
            taille=12, gras=True)

g.texte(x0, 88.2, "H_{t₀} = 110", couleur=DOUX, ancre="middle", taille=11.5)
g.texte(x2, W2 + 5.2, "= S_{T} / B(t₀, T)", ancre="middle", taille=12.5, couleur=AJOUT,
        gras=True)

sys.stdout.write(g.svg())
