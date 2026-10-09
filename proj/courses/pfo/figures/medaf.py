#!/usr/bin/env python3
r"""
medaf.svg — le MEDAF empile, sur le taux sans risque, la prime du marché prise β fois.

Ce que la figure doit faire voir : chaque barre est un rendement espéré. Son socle, le
même pour tous, est le taux sans risque R_f ; au-dessus, un bloc de hauteur
E(R_m) − R_f, la prime de risque du marché, pris autant de fois que le bêta de l'actif —
trois quarts de bloc pour le premier actif, un bloc pour le marché, un bloc et demi pour
le second. La Forme se lit en montant la barre : R_f + β_i (E(R_m) − R_f).

Le monde du chapitre 3 : R_f = 2 %, le marché (deux tiers, un tiers) rapporte 7,33 %,
donc une prime de 5,33 points ; β_1 = 0,75 et β_2 = 1,5 (voir beta.py). Le MEDAF redonne
exactement 6 % et 10 %, les rendements espérés de départ : sur ce marché, chaque actif est
rémunéré exactement pour son risque de marché.

Usage : python courses/pfo/figures/medaf.py > medaf.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

RF = 2.0
EM = 2 / 3 * 6 + 1 / 3 * 10                          # 7,33 %
PRIME = EM - RF                                        # 5,33 points
BARRES = (("actif 1", 0.75, 6.0), ("marché", 1.0, EM), ("actif 2", 1.5, 10.0))
for _nom, b, mu in BARRES:
    assert abs(RF + b * PRIME - mu) < 1e-9

fr = lambda v, d=2: ("%.*f" % (d, v)).replace(".", ",")

f = Figure(xmin=0, xmax=4.4, ymin=-2.6, ymax=11.8, w=560, h=400, marges=(54, 16, 20, 18),
           titre="Sur le taux sans risque, la prime du marché prise β fois")
f.axes(ylab="rendement espéré, en %", yticks=(0, 2, 6, 7.33, 10),
       fmt=lambda t: fr(t, 2).rstrip("0").rstrip(","), croix=(0, 0))

for k, (nom, b, mu) in enumerate(BARRES):
    xc, lg = 0.6 + 1.1 * k, 0.62
    f.barre(xc, RF, lg, couleur=DOUX, opacite=0.30, y0=0)
    f.texte(xc, RF / 2, "R_{f}", couleur=ENCRE, ancre="middle", dy=5, taille=12.5)
    # les blocs de prime, entiers puis la fraction
    reste, bas = b, RF
    while reste > 1e-9:
        part = min(1.0, reste)
        f.barre(xc, bas + part * PRIME, lg, couleur=ACCENT if k != 1 else AJOUT,
                opacite=0.30, y0=bas)
        f.courbe([(xc - lg / 2, bas), (xc - lg / 2, bas + part * PRIME),
                  (xc + lg / 2, bas + part * PRIME), (xc + lg / 2, bas)],
                 couleur=ACCENT if k != 1 else AJOUT, epaisseur=1.4)
        f.texte(xc, bas + part * PRIME / 2, "× 1" if part == 1 else "× " + fr(part),
                couleur=ENCRE, ancre="middle", dy=5, taille=11.5, fond=True)
        bas += part * PRIME
        reste -= part
    f.texte(xc, mu, fr(mu).rstrip("0").rstrip(",") + " %", couleur=ENCRE, ancre="middle", dy=-8, gras=True)
    f.texte(xc, 0, nom, couleur=DOUX, ancre="middle", dy=17, taille=12)
    f.texte(xc, 0, "β = " + fr(b), couleur=DOUX, ancre="middle", dy=32, taille=11.5)

f.mesure(3.55, RF, EM, couleur=AJOUT, etiquette="", cote="right")
f.texte(3.55, (RF + EM) / 2, "E(R_{m}) − R_{f}", couleur=AJOUT, ancre="start", dx=8, dy=-4,
        taille=11.5)
f.texte(3.55, (RF + EM) / 2, "= " + fr(PRIME) + " points", couleur=AJOUT, ancre="start", dx=8,
        dy=11, taille=11.5)
f.segment(2.2 + 0.31, EM, 3.55, EM, couleur=PALE, epaisseur=1.0)
f.segment(2.2 + 0.31, RF, 3.55, RF, couleur=PALE, epaisseur=1.0)

f.texte(2.0, -2.6, "E(R_{i}) = R_{f} + β_{i} (E(R_{m}) − R_{f})", couleur=ENCRE,
        ancre="middle", taille=14, gras=True, dy=-12)

sys.stdout.write(f.svg())
