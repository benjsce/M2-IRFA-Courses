#!/usr/bin/env python3
r"""
payoff.svg — une trajectoire, plusieurs contrats : le payoff est ce qu'on lit dessus.

Ce que la figure doit faire voir : un payoff est une fonction $G$ des observations, et
non un nombre attaché au sous-jacent. Sur une seule et même trajectoire du sous-jacent, de
$t$ à $T$, on marque ce que la Déf. 11 nomme — la valeur finale, le maximum, le minimum,
la moyenne, le franchissement d'une barrière — et, à droite, cinq contrats qui lisent
chacun une de ces observations et paient chacun autre chose. Même trajectoire, cinq
montants : le contrat, c'est la fonction.

La trajectoire est choisie pour le dessin : douze observations mensuelles, qui partent
de 100 et finissent à 104,08, la valeur de l'exemple courant ; leur moyenne vaut 106.

Usage : python courses/fpp/figures/payoff.py > payoff.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX      # noqa: E402

CHEMIN = [100, 102, 98, 95, 99, 104, 109, 114, 117, 113, 110, 106.92, 104.08]
OBS = CHEMIN[1:]                          # les douze observations mensuelles
K, BARRIERE = 100.0, 115.0
ST, MAXI, MINI = CHEMIN[-1], max(CHEMIN), min(CHEMIN)
MOY = sum(OBS) / len(OBS)
iMax, iMin = CHEMIN.index(MAXI), CHEMIN.index(MINI)
v = lambda x: ("%.2f" % x).replace(".", ",").replace(",00", "")

f = Figure(xmin=0, xmax=25.5, ymin=86, ymax=124, w=700, h=330, marges=(46, 26, 40, 10),
           titre="Une trajectoire, cinq contrats : chacun est une fonction G de ce qu'on a observé")
f.axes(xticks=(0, 12), yticks=(90, 100, 110, 120), fmt=lambda x: "t" if x == 0 else "T",
       fmt_y=lambda y: "%d" % y)

# les lignes de lecture : barrière, moyenne
f.segment(0, BARRIERE, 12, BARRIERE, couleur=DOUX, pointilles="2 3")
f.texte(0.2, BARRIERE, "barrière 115", couleur=DOUX, taille=11, dy=-5)
f.segment(0, MOY, 12, MOY, couleur=AJOUT, pointilles="6 4", epaisseur=1.4)
f.texte(0.2, MOY, "moyenne " + v(MOY), couleur=AJOUT, taille=11, dy=-5)

# la trajectoire
f.courbe([(i, s) for i, s in enumerate(CHEMIN)], couleur=ENCRE, epaisseur=2)
f.point(iMax, MAXI, couleur=ACCENT)
f.texte(iMax, MAXI, "max " + v(MAXI), couleur=ACCENT, taille=11.5, ancre="middle", dy=-9)
f.point(iMin, MINI, couleur=ACCENT)
f.texte(iMin, MINI, "min " + v(MINI), couleur=ACCENT, taille=11.5, ancre="middle", dy=17)
f.point(12, ST, couleur=ACCENT)
f.texte(12, ST, "S_{T}\u00a0= " + v(ST), couleur=ACCENT, taille=11.5, dx=7, dy=4)

# à droite : cinq contrats lisent la même trajectoire
X0 = 16.2
f.texte(X0, 121, "ce que G lit", couleur=DOUX, taille=11.5)
f.texte(25.3, 121, "paie en T", couleur=DOUX, taille=11.5, ancre="end")
lignes = [
    ("la valeur finale", "(S_{T}\u00a0− 100)^{+}", max(ST - K, 0)),
    ("le maximum", "max − 100", MAXI - K),
    ("le minimum", "(100 − min)^{+}", max(K - MINI, 0)),
    ("la moyenne", "(moyenne − 100)^{+}", max(MOY - K, 0)),
    ("la barrière", "10 si 115 est touché", 10.0 if MAXI >= BARRIERE else 0.0),
]
for k, (quoi, g, montant) in enumerate(lignes):
    y = 114.5 - 6.3 * k
    f.texte(X0, y, quoi, couleur=ENCRE, taille=12, gras=True)
    f.texte(X0, y, g, couleur=DOUX, taille=11.5, dy=15)
    f.texte(25.3, y, v(montant), couleur=ACCENT, taille=13, ancre="end", gras=True, dy=7)

sys.stdout.write(f.svg())
