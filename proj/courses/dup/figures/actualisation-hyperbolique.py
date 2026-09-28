#!/usr/bin/env python3
r"""
actualisation-hyperbolique.svg — le prix d'une attente de quatre semaines selon son départ.

Pour chaque semaine $t$, le rapport $D(t)/D(t+4)$ : ce qu'il faut d'utilité en $t+4$ pour
compenser une unité en $t$. Avec $u(x)=x$, l'agent prend 100 en $t$ plutôt que 110 en
$t+4$ exactement quand ce rapport dépasse $110/100=1{,}1$ : la droite horizontale.

Les modèles sont ceux du parcours [ajout] : exponentiel à $\delta=1$, rapport 1 ;
quasi-hyperbolique à $\beta=\tfrac12$, $\delta=1$ [L5 slide 14], rapport 2 en 0 puis 1 ;
hyperbolique à $\alpha=\gamma=0{,}05$ par semaine, $D(\tau)=1/(1+0{,}05\tau)$, dont le
rapport $(1+0{,}05(t+4))/(1+0{,}05t)$ baisse à chaque semaine et passe sous 1,1 à la
semaine 20 : l'impatience fortement décroissante.

Usage : python courses/dup/figures/actualisation-hyperbolique.py > actualisation-hyperbolique.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

BETA, DELTA, ALPHA, GAMMA, TAU, SEUIL = 0.5, 1.0, 0.05, 0.05, 4, 1.1
def D_hyp(t):
    return (1 + ALPHA * t) ** (-GAMMA / ALPHA)
def D_qh(t):
    return 1.0 if t == 0 else BETA * DELTA ** t
T = list(range(0, 31))
r_hyp = {t: D_hyp(t) / D_hyp(t + TAU) for t in T}
assert r_hyp[1] > SEUIL > r_hyp[26]            # les deux choix de la seconde personne

f = Figure(xmin=-1, xmax=32, ymin=0.94, ymax=1.3, w=560, h=330, marges=(58, 16, 40, 18),
           titre="Le prix d'une attente de quatre semaines baisse à chaque semaine sous l'actualisation hyperbolique")
f.axes(xlab="semaine t où l'attente commence", ylab="D(t)/D(t+4)", xticks=(0, 1, 26, 30),
       yticks=(1, 1.1, 1.2), fmt=lambda t: str(int(t)),
       fmt_y=lambda t: ("%g" % t).replace(".", ","), croix=(-1, 0.94))

f.segment(-1, SEUIL, 32, SEUIL, couleur=ENCRE, epaisseur=1.2, pointilles="6 4")
f.texte(3, SEUIL, "110/100 — au-dessus, il prend le plus tôt ;", couleur=ENCRE, ancre="start", dy=-9, taille=11.5, fond=True)
f.texte(3, SEUIL, "en dessous, il attend", couleur=ENCRE, ancre="start", dy=15, taille=11.5, fond=True)

f.courbe([(t, 1 / DELTA ** TAU) for t in T], couleur=DOUX, epaisseur=1.6, pointilles="3 3")
qh = [(t, D_qh(t) / D_qh(t + TAU)) for t in T]
assert qh[0][1] == 2.0
f.courbe([(0, 1.3), (0, qh[0][1] if qh[0][1] < 1.3 else 1.3)], couleur=AJOUT, epaisseur=1.8)
f.fleche(0, 1.24, 0, 1.3, couleur=AJOUT, epaisseur=1.8)
f.courbe([(0, 1.3), (1, 1.0)] + qh[2:], couleur=AJOUT, epaisseur=1.8)
f.courbe([(t, r_hyp[t]) for t in T], couleur=ACCENT, epaisseur=2.4)
for t in (1, 26):
    f.point(t, r_hyp[t], couleur=ACCENT, r=4)

f.texte(0, 1.3, "quasi-hyperbolique : 2 en 0, puis 1", couleur=AJOUT, dx=10, dy=12, taille=12, gras=True)
f.texte(1, r_hyp[1], "semaine 1 : 1,19", couleur=ACCENT, dx=8, dy=-8, taille=11.5)
f.texte(26, r_hyp[26], "semaine 26 : 1,09", couleur=ACCENT, ancre="middle", dy=18, taille=11.5)
f.texte(9, r_hyp[9], "hyperbolique", couleur=ACCENT, dy=-10, taille=12, gras=True)
f.texte(20, 1.0, "exponentiel, δ = 1 : toujours 1", couleur=DOUX, dy=-6, taille=11.5)

sys.stdout.write(f.svg())
