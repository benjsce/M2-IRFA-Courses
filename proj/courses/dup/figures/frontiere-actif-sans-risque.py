#!/usr/bin/env python3
r"""
frontiere-actif-sans-risque.svg — la droite des mélanges, et son prolongement par l'emprunt.

Les nombres sont ceux de l'exemple de la fiche : $r_0=2\,\%$, $\mu_r=8\,\%$,
$\sigma_r=20\,\%$. Trois points de la droite portent une valeur de $a$ : $a=1$ (tout sans
risque), $a=\tfrac12$ (l'exemple, $\sigma_p=10\,\%$ et $\mu_p=5\,\%$), $a=0$ (tout
risqué). Au-delà, $a<0$ : l'agent emprunte au taux $r_0$, et la droite continue. La pente,
0,3 point de moyenne par point d'écart type, est celle du geste de la fiche.

Usage : python courses/dup/figures/frontiere-actif-sans-risque.py > frontiere-actif-sans-risque.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, DOUX, AJOUT, ENCRE      # noqa: E402

R0, MU, SIG = 2.0, 8.0, 20.0


def point(a):
    return (abs(1 - a) * SIG, a * R0 + (1 - a) * MU)


f = Figure(xmin=0, xmax=42, ymin=0, ymax=15, w=560, h=330,
           titre="Chaque point d'écart type achète 0,3 point de moyenne, jusqu'au bout de l'emprunt")
f.axes(xlab="écart type σp, en %", ylab="moyenne μp, en %", xticks=(0, 10, 20, 30, 40),
       yticks=(2, 5, 8, 11, 14), fmt=lambda t: str(int(t)))

f.courbe([point(1), point(0)], couleur=ACCENT, epaisseur=2.6)
f.courbe([point(0), point(-1)], couleur=AJOUT, epaisseur=2.2, pointilles="6 4")

for a, nom, dx, dy, ancre in ((1, "a = 1 : tout sans risque", 8, 16, "start"),
                              (0.5, "a = ½ : σp = 10, μp = 5", 8, 16, "start"),
                              (0, "a = 0 : tout risqué", 8, 16, "start")):
    x, y = point(a)
    f.point(x, y, couleur=ENCRE)
    f.texte(x, y, nom, couleur=ENCRE, dx=dx, dy=dy, ancre=ancre, taille=12, fond=True)

x, y = point(-0.75)
f.texte(x, y, "a < 0 : emprunt à r0", couleur=AJOUT, ancre="end", dx=-10, dy=-4,
        gras=True, fond=True)

sys.stdout.write(f.svg())
