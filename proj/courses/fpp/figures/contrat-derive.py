#!/usr/bin/env python3
r"""
contrat-derive.svg — un moteur, deux nombres : l'un est donné, l'autre est le trou.

Ce que la figure doit faire voir : un contrat dérivé fixe deux nombres, la prime et le
strike ; la même équation, prime = P(t,T) × E^Q(paiement), les relie. Pour l'engagement
ferme, la prime est donnée, nulle, et le strike est le trou ; pour l'option, le strike est
donné, 100, et la prime est le trou.

Deux lignes, la même équation écrite deux fois ; chaque nombre est dans une case, pleine
quand il est connu, en pointillé quand on le cherche. Les chiffres sont ceux du cours :
action à 100, taux de 4 % continu, zéro-coupon à un an 0,9608 ; le forward vaut
100/0,9608 = 104,08, le call de strike 100 vaut 9,93 dans le modèle de Black et Scholes
(volatilité 20 %), soit 0,9608 × 10,33.

Usage : python courses/fpp/figures/contrat-derive.py > contrat-derive.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

r, sig, S, K, T = 0.04, 0.20, 100.0, 100.0, 1.0
P = math.exp(-r * T)                                    # 0,9608
N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
d1 = (math.log(S / K) + (r + sig ** 2 / 2) * T) / (sig * math.sqrt(T))
d2 = d1 - sig * math.sqrt(T)
call = S * N(d1) - K * P * N(d2)                        # 9,93
moy = call / P                                          # 10,33 : E^Q((S_T - K)^+)
fwd = S / P                                             # 104,08 : E^Q(S_T)
v = lambda x, d=2: ("%.*f" % (d, x)).replace(".", ",")

g = Figure(xmin=0, xmax=14.2, ymin=0.2, ymax=9.4, w=580, h=330, marges=(8, 8, 8, 8),
           titre="Le même moteur : on donne la prime et l'on cherche le strike, ou l'inverse")


def case(x0, x1, y, contenu, connu, couleur):
    h = 0.62
    if connu:
        g.barre((x0 + x1) / 2, y + h, x1 - x0, couleur=couleur, opacite=0.18, y0=y - h)
    g.courbe([(x0, y - h), (x1, y - h), (x1, y + h), (x0, y + h), (x0, y - h)],
             couleur=couleur if connu else ENCRE, epaisseur=1.8,
             pointilles=None if connu else "5 4")
    g.texte((x0 + x1) / 2, y - 0.2, contenu, ancre="middle", taille=16, gras=True)


def ligne(y, titre, prime_connue, paiement_avant, paiement_apres, reponse):
    g.texte(0.5, y + 1.75, titre, couleur=AJOUT, gras=True, taille=13)
    # la prime
    case(0.6, 2.4, y, "0" if prime_connue else "?", prime_connue, ACCENT)
    g.texte(1.5, y - 1.25, "prime connue" if prime_connue else "prime cherchée",
            couleur=DOUX, ancre="middle", taille=11.5)
    # le moteur
    # le texte du moteur s'arrête au bord gauche de la case, la parenthèse repart de son
    # bord droit : l'écart ne dépend plus de la largeur réelle des caractères
    xk = 7.3
    g.texte(xk - 0.12, y - 0.2, "=  %s × E^{Q}%s" % (v(P, 4), paiement_avant), taille=16,
            ancre="end")
    case(xk, xk + 1.8, y, "?" if prime_connue else "100", not prime_connue, ACCENT)
    g.texte(xk + 0.9, y - 1.25, "strike cherché" if prime_connue else "strike connu",
            couleur=DOUX, ancre="middle", taille=11.5)
    g.texte(xk + 1.92, y - 0.2, paiement_apres, taille=16)
    g.texte(13.8, y - 0.2, reponse, ancre="end", taille=14, gras=True)


ligne(6.9, "engagement ferme : la prime est donnée, nulle",
      True, "(S_{T}\u00a0−", ")", "K = %s" % v(fwd))
ligne(2.0, "option, ici un call : le strike est donné",
      False, "((S_{T}\u00a0−", ")^{+})", "prime = %s" % v(call))
g.texte(13.8, 6.9 - 1.25, "= E^{Q}(S_{T})", couleur=DOUX, ancre="end", taille=11.5)
g.texte(13.8, 2.0 - 1.25, "= %s × %s" % (v(P, 4), v(moy)), couleur=DOUX, ancre="end",
        taille=11.5)

sys.stdout.write(g.svg())
