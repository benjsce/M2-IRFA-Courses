#!/usr/bin/env python3
r"""
cash-and-carry.svg — deux échéanciers superposés, qui se lisent comme la Forme de la fiche.

En haut, le vendeur à terme porte l'action à crédit : il emprunte S_t, achète l'action, la
livre en T contre K et rembourse S_t / P(t,T). En bas, l'acheteur fait le montage inverse :
il vend l'action à découvert, place S_t, la reçoit en T contre K, la rend et récupère son
placement. Chaque jambe a sa couleur — le contrat à terme d'un côté, l'action portée à
crédit de l'autre — et sa somme est écrite sous l'échéancier. En bas, la somme des deux
jambes est la Forme mot pour mot : (S_T − K) − (S_T − S_t / P(t,T)) = S_t / P(t,T) − K.
Dans les deux cas S_T s'annule : le résultat est certain et sans mise, donc nul.

Usage : python courses/fpp/figures/cash-and-carry.py > cash-and-carry.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

# Le repère est en pixels, l'ordonnée comptée vers le bas : y = −pixel.
W, H = 720, 930
f = Figure(xmin=0, xmax=W, ymin=-H, ymax=0, w=W, h=H, marges=(0, 0, 0, 0),
           titre="Cash-and-carry et montage inverse : la somme des deux jambes en T "
                 "est S_t / P(t,T) − K, sans S_T")

T0, T1 = 150, 480          # abscisses des dates t et T
L = 92                     # longueur d'un flux


def flux(x, axe, monte, couleur, valeur, quoi, cote):
    """Un flux sur l'échéancier : il monte s'il est reçu, descend s'il est payé."""
    depart = axe - 6 if monte else axe + 6            # en pixels, comptés vers le bas
    arrivee = axe - L if monte else axe + L
    f.fleche(x, -depart, x, -arrivee, couleur=couleur, epaisseur=2.2)
    dx, ancre = (-9, "end") if cote == "g" else (9, "start")
    yv = axe - L + 14 if monte else axe + L - 24      # la valeur au bout de la flèche
    f.texte(x, -yv, valeur, couleur=ENCRE, ancre=ancre, dx=dx, gras=True, taille=14)
    f.texte(x, -(yv + 19), quoi, couleur=DOUX, ancre=ancre, dx=dx, taille=12.5)


def legende(y, couleur, s, gras=False):
    f.courbe([(24, -y), (58, -y)], couleur=couleur, epaisseur=3)
    f.texte(70, -y, s, couleur=ENCRE, dy=5, taille=14, gras=gras)


def panneau(haut, titre, arc, flux_list, jambes, somme):
    axe = haut + 185
    f.texte(20, -(haut + 20), titre, couleur=ENCRE, taille=15.5, gras=True)
    f.fleche(T0 + 20, -(haut + 70), T1 + 30, -(haut + 70), couleur=DOUX, courbure=10,
             epaisseur=1.2)
    f.texte((T0 + T1) / 2 + 25, -(haut + 50), arc, couleur=DOUX, ancre="middle", taille=12.5)
    f.courbe([(40, -axe), (680, -axe)], couleur=DOUX, epaisseur=1.3)
    f.fleche(679, -axe, 690, -axe, couleur=DOUX, epaisseur=1.3)
    for x, s in ((T0, "t"), (T1, "T")):
        f.courbe([(x, -(axe - 5)), (x, -(axe + 5))], couleur=DOUX, epaisseur=1.3)
        f.texte(x, -(axe + 24), s, couleur=DOUX, ancre="middle", taille=13)
    for args in flux_list:
        flux(args[0], axe, *args[1:])
    y = axe + 125
    for couleur, s in jambes:
        legende(y, couleur, s)
        y += 30
    f.texte(W / 2, -(y + 12), somme, couleur=ENCRE, ancre="middle", taille=15, gras=True)


panneau(0, "Vendeur à terme : cash-and-carry", "la dette grandit : ÷ P(t,T)",
        [(T0 - 12, True, AJOUT, "+ S_{t}", "emprunté", "g"),
         (T0 + 12, False, AJOUT, "− S_{t}", "achat de l'action", "d"),
         (T1 - 40, False, ACCENT, "− S_{T}", "action livrée", "g"),
         (T1 - 20, True, ACCENT, "+ K", "reçu", "g"),
         (T1 + 20, True, AJOUT, "+ S_{T}", "action détenue", "d"),
         (T1 + 40, False, AJOUT, "− S_{t} / P(t,T)", "dette remboursée", "d")],
        [(ACCENT, "vente à terme : + (K − S_{T})"),
         (AJOUT, "action portée à crédit : + (S_{T} − S_{t} / P(t,T))")],
        "somme en T : K − S_{t} / P(t,T)")

f.courbe([(20, -455), (700, -455)], couleur=PALE, epaisseur=1, pointilles="4 4")

panneau(470, "Acheteur à terme : reverse cash-and-carry",
        "le placement grandit : ÷ P(t,T)",
        [(T0 - 12, True, AJOUT, "+ S_{t}", "vente à découvert", "g"),
         (T0 + 12, False, AJOUT, "− S_{t}", "placé", "d"),
         (T1 - 40, True, ACCENT, "+ S_{T}", "action reçue", "g"),
         (T1 - 20, False, ACCENT, "− K", "payé", "g"),
         (T1 + 20, False, AJOUT, "− S_{T}", "action rendue", "d"),
         (T1 + 40, True, AJOUT, "+ S_{t} / P(t,T)", "placement récupéré", "d")],
        [(ACCENT, "achat à terme : + (S_{T} − K)"),
         (AJOUT, "action portée à crédit, en sens inverse : − (S_{T} − S_{t} / P(t,T))")],
        "somme en T : S_{t} / P(t,T) − K")

f.texte(W / 2, -(H - 18), "dans les deux cas S_{T} s'annule : résultat certain et sans mise, "
        "donc nul → K = S_{t} / P(t,T)", couleur=DOUX, ancre="middle", taille=13)
sys.stdout.write(f.svg())
