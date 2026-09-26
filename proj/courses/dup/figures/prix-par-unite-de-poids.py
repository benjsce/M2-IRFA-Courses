#!/usr/bin/env python3
r"""
prix-par-unite-de-poids.svg — les deux rapports, état par état.

L'exemple de la fiche : $q=(0{,}3;0{,}3;0{,}4)$, $p=(0{,}2;0{,}3;0{,}5)$ et
$\pi=(0{,}2560;0{,}2013;0{,}5426)$. Le prix par unité de probabilité $q_s/p_s$ vaut
$(1{,}5;1;0{,}8)$ ; le prix par unité de poids $q_s/\pi_s$ vaut $(1{,}17;1{,}49;0{,}74)$.
Les barres montrent ce que la fiche dit en « Cesse d'être valide quand » : les deux
rapports ne classent pas les états dans le même ordre — le premier état est le plus cher
par unité de probabilité, le deuxième l'est par unité de poids.

Usage : python courses/dup/figures/prix-par-unite-de-poids.py > prix-par-unite-de-poids.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, ENCRE      # noqa: E402

Q = (0.3, 0.3, 0.4)
PROBA = (0.2, 0.3, 0.5)
POIDS = (0.2560, 0.2013, 0.5426)
LARG, DECAL = 0.30, 0.17


def fr(v):
    return ("%.2f" % v).rstrip("0").rstrip(".").replace(".", ",")


f = Figure(xmin=0.4, xmax=3.6, ymin=0, ymax=1.8, w=560, h=330,
           titre="Par unité de probabilité l'état 1 est le plus cher, par unité de poids c'est l'état 2")
f.axes(xlab="état", ylab="prix rapporté", xticks=(1, 2, 3), yticks=(0.5, 1, 1.5),
       fmt=lambda t: str(int(t)), fmt_y=lambda t: ("%g" % t).replace(".", ","))

for s in range(3):
    a, b = Q[s] / PROBA[s], Q[s] / POIDS[s]
    f.barre(s + 1 - DECAL, a, LARG, couleur=DOUX, opacite=0.55)
    f.barre(s + 1 + DECAL, b, LARG, couleur=ACCENT)
    f.texte(s + 1 - DECAL, a, fr(a), couleur=DOUX, ancre="middle", dy=-6, taille=11.5)
    f.texte(s + 1 + DECAL, b, fr(b), couleur=ACCENT, ancre="middle", dy=-6, taille=11.5,
            gras=True)

f.barre(2.72, 1.66, 0.08, couleur=DOUX, opacite=0.55, y0=1.60)
f.texte(2.8, 1.6, "qs / ps", couleur=DOUX, taille=11.5)
f.barre(2.72, 1.51, 0.08, couleur=ACCENT, y0=1.45)
f.texte(2.8, 1.45, "qs / πs", couleur=ACCENT, taille=11.5, gras=True)

sys.stdout.write(f.svg())
