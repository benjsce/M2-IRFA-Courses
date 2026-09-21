#!/usr/bin/env python3
r"""
couverture-de-l-ambiguite.svg — deux droites qui se croisent, et le maxmin qui passe dessous.

La fiche donne toute la géométrie en trois phrases : les deux actes $f=(0,2)$ et
$g=(2,0)$ en unités d'utilité, l'ensemble $K=\{(p,1-p):1/4\le p\le3/4\}$, chaque prior
qui donne une droite en fonction du poids de mélange, et le maxmin qui en retient
l'enveloppe inférieure. Le dessin les montre d'un coup, et laisse voir ce que la prose
peine à dire : le creux est aux extrémités, pas au milieu.

Les deux droites sont **calculées** depuis les vecteurs d'utilité et les deux priors
extrêmes que la fiche nomme, et non recopiées. Les priors intérieurs ne sont pas tracés :
la fiche n'en parle pas, et l'enveloppe ne dépend que des deux bords.

Usage : python courses/dup/figures/couverture-de-l-ambiguite.py > couverture-de-l-ambiguite.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

F = (0.0, 2.0)                 # l'acte f, en unités d'utilité
G = (2.0, 0.0)                 # l'acte g
P_BAS, P_HAUT = 0.25, 0.75     # les deux bords de K

melange = lambda t: ((1 - t) * F[0] + t * G[0], (1 - t) * F[1] + t * G[1])
esperance = lambda p: (lambda t: p * melange(t)[0] + (1 - p) * melange(t)[1])
maxmin = lambda t: min(esperance(P_BAS)(t), esperance(P_HAUT)(t))

f = Figure(xmin=-0.04, xmax=1.12, ymin=0, ymax=1.75, w=560, h=330,
           titre="Chaque prior donne une droite ; le maxmin passe sous les deux")

f.axes(xlab="poids du mélange, t", ylab="valeur",
       xticks=(0, 0.5, 1), yticks=(0.5, 1.0, 1.5),
       fmt=lambda t: ("%.1f" % t).replace(".", ","),
       fmt_y=lambda t: ("%.1f" % t).replace(".", ","))

f.segment(0.5, 0, 0.5, maxmin(0.5))

f.fonction(esperance(P_BAS), 0, 1, couleur=AJOUT, epaisseur=1.8, pointilles="5 4")
f.fonction(esperance(P_HAUT), 0, 1, couleur=AJOUT, epaisseur=1.8, pointilles="5 4")
f.fonction(maxmin, 0, 1, couleur=ACCENT, epaisseur=2.8)

for t in (0.0, 0.5, 1.0):
    f.point(t, maxmin(t), couleur=ACCENT)

# Chaque droite n'est visible que sur la moitié où elle passe au-dessus de l'enveloppe :
# c'est là qu'on la nomme, et non à son extrémité, où elle se confond avec le trait plein.
f.texte(0.22, esperance(P_BAS)(0.22), "p = 1/4", couleur=AJOUT, ancre="end",
        dx=-4, dy=-6, taille=11.5, fond=True)
f.texte(0.78, esperance(P_HAUT)(0.78), "p = 3/4", couleur=AJOUT,
        dx=4, dy=-6, taille=11.5, fond=True)
f.texte(0.5, maxmin(0.5), "le mélange à parts égales vaut 1", couleur=ENCRE,
        ancre="middle", dy=-13, gras=True, fond=True)
f.texte(0.0, maxmin(0.0), "f et g valent 0,5 chacun", couleur=ENCRE,
        dx=8, dy=14, taille=11.5, fond=True)

sys.stdout.write(f.svg())
