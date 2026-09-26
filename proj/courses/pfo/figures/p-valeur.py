#!/usr/bin/env python3
r"""
p-valeur.svg — la p-valeur comme aire, et la règle p < α lue sur la même loi.

La fiche définit la p-valeur comme la probabilité, sous l'hypothèse nulle, d'une
statistique au moins aussi extrême que celle observée : c'est l'aire de la queue au-delà
de la valeur observée. Le niveau α est, sur la même loi, l'aire au-delà du seuil. Il faut
une loi pour les dessiner ; on prend celle de la statistique de Jarque-Bera sous
l'hypothèse nulle, $\chi^2(2)$, dont la queue vaut exactement $e^{-x/2}$. Les deux
p-valeurs de l'exemple, 0,40 et 0,03, correspondent alors aux statistiques $-2\ln p$ :
1,83 et 7,01 ; le niveau de 5 % correspond au seuil 5,99.

Dans chaque cadre, l'aire colorée est la p-valeur, l'aire grise est α. À gauche, l'aire p
contient l'aire α : on ne rejette pas. À droite, l'aire p tient dans l'aire α : on rejette.
Le cadre de droite grossit la queue, où une aire de 0,03 serait invisible à l'échelle de
la loi entière.

Les étiquettes partent du haut des traits verticaux qu'elles nomment, alignées à gauche.

Usage : python courses/pfo/figures/p-valeur.py > p-valeur.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, Planche, ACCENT, DOUX, ENCRE, _n      # noqa: E402

dens = lambda x: 0.5 * math.exp(-x / 2)
SEUIL = -2 * math.log(0.05)
fr = lambda v: ("%.2f" % v).replace(".", ",")


def aire(g, x0, x1, couleur, opacite):
    pts = [(x0 + (x1 - x0) * i / 150, dens(x0 + (x1 - x0) * i / 150)) for i in range(151)]
    pts += [(x1, 0), (x0, 0)]
    g._add('<path d="M%s Z" fill="%s" fill-opacity="%s" stroke="none"/>'
           % (" L".join("%s %s" % (_n(g.px(x)), _n(g.py(y))) for x, y in pts), couleur,
              _n(opacite)))


def cadre(p, verdict, xmin, xmax, ymax, xticks, xlab, h_obs, h_seuil, cote_seuil):
    x0 = -2 * math.log(p)
    g = Figure(xmin=xmin, xmax=xmax, ymin=0, ymax=ymax, w=290, h=270, marges=(20, 30, 40, 10))
    # La plus petite des deux aires est posée sur l'autre, pour que sa couleur reste pure.
    p_aire, a_aire = (lambda: aire(g, x0, xmax, ACCENT, 0.40)), (lambda: aire(g, SEUIL, xmax, DOUX, 0.50))
    for tracer in ((p_aire, a_aire) if x0 < SEUIL else (a_aire, p_aire)):
        tracer()
    g.axes(xlab=xlab, xticks=xticks, fmt=lambda t: fr(t).replace(",00", ""))
    g.fonction(dens, xmin, xmax, couleur=ENCRE, epaisseur=2.0)
    g.segment(SEUIL, 0, SEUIL, h_seuil, couleur=DOUX, epaisseur=1.4)
    ancre, dx = ("end", 4) if cote_seuil == "gauche" else ("start", -4)
    g.texte(SEUIL, h_seuil, "seuil 5,99", couleur=DOUX, ancre=ancre, dx=dx, dy=-19, taille=10.5)
    g.texte(SEUIL, h_seuil, "aire grise α = 0,05", couleur=DOUX, ancre=ancre, dx=dx, dy=-5,
            taille=10.5, gras=True)
    g.segment(x0, 0, x0, h_obs, couleur=ACCENT, epaisseur=1.8, pointilles=None)
    g.texte(x0, h_obs, "observée " + fr(x0), couleur=ACCENT, dx=-4, dy=-19, taille=11)
    g.texte(x0, h_obs, "aire colorée p = " + fr(p), couleur=ACCENT, dx=-4, dy=-5, taille=11,
            gras=True)
    g.texte((xmin + xmax) / 2, ymax, verdict, couleur=ENCRE, ancre="middle", dy=-8, gras=True)
    return g


gauche = cadre(0.40, "p = 0,40 > α : on ne rejette pas", 0, 10.5, 0.56, (0, 1.83),
               "statistique", h_obs=0.34, h_seuil=0.20, cote_seuil="gauche")
droite = cadre(0.03, "p = 0,03 < α : on rejette", 4, 12, 0.075, (4, 8, 12),
               "la queue, grossie", h_obs=0.034, h_seuil=0.060, cote_seuil="droite")
sys.stdout.write(Planche([gauche, droite], ecart=26,
                         titre="La p-valeur est l'aire au-delà de la statistique observée ; "
                               "α, l'aire au-delà du seuil").svg())
