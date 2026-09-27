#!/usr/bin/env python3
r"""
dividendes-intermediaires.svg — le cash-and-carry avec un dividende en T₁ : on emprunte en
deux fois, et seul le second emprunt fixe le prix forward.

Le vendeur à terme achète l'action S_t en t. Il sait qu'il touchera en T₁ le dividende
d₁ S_t / P(t,T₁) ; il emprunte donc d₁ S_t jusqu'à T₁ seulement, que ce dividende rembourse
exactement, et le reste, (1 − d₁) S_t, jusqu'à T. En T₁, rien ne reste : dividende reçu,
premier emprunt remboursé. En T, les jambes se somment comme au cash-and-carry, mais avec
un emprunt plus petit : F − (1 − d₁) S_t / P(t,T), certain et obtenu sans mise, donc nul,
F(t,T) = S_t / P(t,T) × (1 − d₁), la Forme de la fiche. Aucune valeur numérique.

Usage : python courses/fpp/figures/dividendes-intermediaires.py > dividendes-intermediaires.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE      # noqa: E402

# Le repère est en pixels, l'ordonnée comptée vers le bas : y = −pixel.
W, H = 960, 540
f = Figure(xmin=0, xmax=W, ymin=-H, ymax=0, w=W, h=H, marges=(0, 0, 0, 0),
           titre="Avec un dividende, le vendeur à terme n'emprunte jusqu'à T que "
                 "(1 − d₁) S_t : F = S_t / P(t,T) × (1 − d₁)")
T0, T1, T2 = 190, 420, 700         # abscisses de t, T₁ et T
AXE, L = 245, 92                   # ordonnée de l'axe, longueur d'un flux


def flux(x, monte, couleur, valeur, quoi, cote):
    depart = AXE - 6 if monte else AXE + 6
    arrivee = AXE - L if monte else AXE + L
    f.fleche(x, -depart, x, -arrivee, couleur=couleur, epaisseur=2.2)
    dx, ancre = (-9, "end") if cote == "g" else (9, "start")
    yv = AXE - L + 14 if monte else AXE + L - 24
    f.texte(x, -yv, valeur, couleur=ENCRE, ancre=ancre, dx=dx, gras=True, taille=13.5)
    f.texte(x, -(yv + 19), quoi, couleur=DOUX, ancre=ancre, dx=dx, taille=12)


def legende(y, couleur, s, gras=False):
    f.courbe([(24, -y), (58, -y)], couleur=couleur, epaisseur=3)
    f.texte(70, -y, s, couleur=ENCRE, dy=5, taille=13.5, gras=gras)


f.texte(20, -24, "Vendeur à terme : cash-and-carry avec un dividende en T₁", couleur=ENCRE,
        taille=15.5, gras=True)
# Les deux emprunts, chacun avec son arc : le court finit en T₁, le long en T.
f.fleche(T0 + 5, -118, T1 - 25, -118, couleur=ENCRE, courbure=8, epaisseur=1.2)
f.texte((T0 + T1) / 2 - 10, -96, "emprunt court : ÷ P(t,T₁)", couleur=DOUX, ancre="middle", taille=12)
f.fleche(T0 + 5, -72, T2 + 30, -72, couleur=AJOUT, courbure=10, epaisseur=1.2)
f.texte((T0 + T2) / 2 + 10, -50, "emprunt long : ÷ P(t,T)", couleur=AJOUT, ancre="middle", taille=12)

f.courbe([(40, -AXE), (930, -AXE)], couleur=DOUX, epaisseur=1.3)
f.fleche(929, -AXE, 940, -AXE, couleur=DOUX, epaisseur=1.3)
for x, s in ((T0, "t"), (T1, "T₁"), (T2, "T")):
    f.courbe([(x, -(AXE - 5)), (x, -(AXE + 5))], couleur=DOUX, epaisseur=1.3)
    f.texte(x, -(AXE + 24), s, couleur=DOUX, ancre="middle", taille=13)

flux(T0 - 26, True, ENCRE, "+ d₁ S_{t}", "emprunté jusqu'à T₁", "g")
flux(T0 - 8, True, AJOUT, "", "", "g")
f.texte(T0 - 8, -(AXE - L + 14) + 40, "+ (1 − d₁) S_{t}", couleur=AJOUT, ancre="end", dx=-27,
        gras=True, taille=13.5)
f.texte(T0 - 8, -(AXE - L + 33) + 40, "emprunté jusqu'à T", couleur=AJOUT, ancre="end", dx=-27, taille=12)
flux(T0 + 12, False, AJOUT, "− S_{t}", "achat de l'action", "d")
flux(T1 - 10, True, ENCRE, "+ d₁ S_{t} / P(t,T₁)", "dividende reçu", "g")
flux(T1 + 10, False, ENCRE, "− d₁ S_{t} / P(t,T₁)", "emprunt court\u00a0remboursé", "d")
flux(T2 - 40, False, ACCENT, "− S_{T}", "action livrée", "g")
flux(T2 - 20, True, ACCENT, "+ F", "reçu", "g")
flux(T2 + 20, True, AJOUT, "+ S_{T}", "action détenue", "d")
flux(T2 + 40, False, AJOUT, "− (1 − d₁) S_{t} / P(t,T)", "emprunt long remboursé", "d")

y = AXE + 130
legende(y, ENCRE, "emprunt court, payé par le dividende : net nul en T₁")
legende(y + 30, ACCENT, "vente à terme : + (F − S_{T})")
legende(y + 60, AJOUT, "action portée à crédit, emprunt long : + (S_{T} − (1 − d₁) S_{t} / P(t,T))")
f.texte(W / 2, -(y + 102), "somme en T : F − (1 − d₁) S_{t} / P(t,T)", couleur=ENCRE,
        ancre="middle", taille=15, gras=True)
f.texte(W / 2, -(y + 130), "certaine et sans mise, donc nulle → F(t,T) = S_{t} / P(t,T) × (1 − d₁)",
        couleur=DOUX, ancre="middle", taille=13)
sys.stdout.write(f.svg())
