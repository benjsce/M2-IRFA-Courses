#!/usr/bin/env python3
r"""
developpement-de-cornish-fisher.svg — le connu, les trois corrections, le cherché.

Ce que la figure doit faire voir : on part d'un nombre connu, le quantile normal
z_α = −1,645 ; on ne connaît de la loi réelle que son asymétrie S et son excès de
kurtosis K ; le développement ajoute trois corrections, une par ligne, et arrive au
quantile cherché q_α. Le trou entre les deux est δ.

Les chiffres sont ceux de l'exemple de la fiche : α = 5 %, S = −0,5, K = 3. Le terme en S
pousse vers les pertes (−0,142) ; celui en K ramène vers la moyenne (+0,061), parce
qu'à 1,645 écart type on est encore sur le flanc, avant √3 ; celui en S² est minuscule
(+0,005). Arrivée : −1,722. L'axe est gradué en écarts types, les pertes à gauche.

Usage : python courses/pfo/figures/developpement-de-cornish-fisher.py > developpement-de-cornish-fisher.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX, PALE      # noqa: E402

S, K, ALPHA = -0.5, 3.0, 0.05
z = NormalDist().inv_cdf(ALPHA)                        # −1,6449
tS = S / 6 * (z * z - 1)                               # −0,1421
tK = K / 24 * (z ** 3 - 3 * z)                         # +0,0605
tS2 = -S * S / 36 * (2 * z ** 3 - 5 * z)               # +0,0047
q = z + tS + tK + tS2                                  # −1,7217
fr = lambda v, d=3: ("%+.*f" % (d, v)).replace(".", ",").replace("-", "−")
fn = lambda v, d=3: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")

f = Figure(xmin=-1.82, xmax=-1.47, ymin=-0.9, ymax=5.0, w=580, h=340,
           marges=(16, 12, 40, 16),
           titre="Du quantile normal, connu, au quantile corrigé, cherché : trois corrections")
# un seul axe, horizontal : la hauteur ne mesure rien, chaque ligne est une étape
f.courbe([(-1.82, -0.9), (-1.47, -0.9)], couleur=DOUX, epaisseur=1.2)
for t in (-1.8, -1.75, -1.7, -1.65, -1.6, -1.55, -1.5):
    f.segment(t, -0.9, t, -0.98, couleur=DOUX, pointilles=None)
    f.texte(t, -0.9, fn(t, 2), couleur=DOUX, ancre="middle", dy=17, taille=11.5)
f.texte(-1.47, -0.9, "en écarts types, les pertes à gauche", couleur=DOUX, ancre="end",
        dy=33, taille=12)

Y0, Y1, Y2, Y3, Y4 = 4.2, 3.2, 2.2, 1.2, 0.2
# les deux repères verticaux : le connu et le cherché
f.segment(z, Y0, z, -0.9, couleur=PALE)
f.segment(q, Y4, q, -0.9, couleur=PALE)

f.point(z, Y0, couleur=ENCRE, r=4.5)
f.texte(z, Y0, "connu : z_{α}\u00a0= " + fn(z), couleur=ENCRE, dx=10, dy=5, gras=True, taille=12.5)

a1, a2, a3 = z + tS, z + tS + tK, q
f.fleche(z, Y1, a1, Y1, couleur=ACCENT, epaisseur=2.2)
f.texte(z, Y1, "terme en S : " + fr(tS) + " (asymétrie, vers les pertes)", couleur=ACCENT,
        dx=10, dy=4, taille=12, fond=True)
f.segment(a1, Y1, a1, Y2, couleur=PALE)
f.fleche(a1, Y2, a2, Y2, couleur=AJOUT, epaisseur=2.2)
f.texte(a2, Y2, "terme en K : " + fr(tK) + " (kurtosis, vers la moyenne)", couleur=AJOUT,
        dx=10, dy=4, taille=12, fond=True)
f.segment(a2, Y2, a2, Y3, couleur=PALE)
f.fleche(a2, Y3, a3, Y3, couleur=DOUX, epaisseur=2.2)
f.texte(a3, Y3, "terme en S² : " + fr(tS2), couleur=DOUX, dx=10, dy=4, taille=12,
        fond=True)

f.point(q, Y4, couleur=ACCENT, r=4.5)
f.texte(q, Y4, "cherché : q_{α}\u00a0= " + fn(q), couleur=ACCENT, dx=10, dy=5, gras=True,
        taille=12.5, fond=True)
# le trou, δ, mesuré entre les deux repères, sous la dernière ligne
f.mesure_h(-0.35, q, z, couleur=ENCRE)
f.texte(q, -0.35, "δ = " + fn(q - z), couleur=ENCRE, ancre="end", dx=-8, dy=4, taille=12,
        gras=True)

sys.stdout.write(f.svg())
