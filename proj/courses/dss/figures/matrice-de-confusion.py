#!/usr/bin/env python3
r"""
matrice-de-confusion.svg — cent cas, dix positifs, un classifieur qui dit toujours « négatif ».

L'exemple de la fiche, un carré par cas. Les dix positifs réels sont colorés ; le
classifieur les prédit tous négatifs, comme les quatre-vingt-dix autres. Diviser par tous
les cas donne l'exactitude, 90 sur 100 ; diviser par la seule ligne des positifs réels
donne la sensibilité, 0 sur 10. Le même tableau, deux dénominateurs, deux verdicts.

Usage : python courses/dss/figures/matrice-de-confusion.py > matrice-de-confusion.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, _n      # noqa: E402

f = Figure(xmin=0, xmax=22, ymin=0, ymax=11.6, w=580, h=320, marges=(12, 12, 12, 12),
           titre="Exactitude 90 sur 100, sensibilité 0 sur 10 : le même tableau, deux dénominateurs")
for k in range(100):
    i, j = k % 10, k // 10
    positif = j == 9
    f.barre(i + 0.5, 10 - j, 0.84, couleur=AJOUT if positif else DOUX,
            opacite=0.85 if positif else 0.35, y0=10 - j - 0.84)
f.texte(5, 11.1, "100 cas, tous prédits « négatif »", couleur=ENCRE, ancre="middle", gras=True)
f.texte(10.3, 0.6, "← 10 positifs réels, tous manqués", couleur=AJOUT, taille=11.5, gras=True)
f.texte(10.3, 6.2, "← 90 négatifs, bien rejetés", couleur=DOUX, taille=11.5, gras=True)
f.texte(16.2, 8.6, "exactitude", couleur=ENCRE, gras=True)
f.texte(16.2, 7.4, "(TP + TN) / tous = 90 / 100", couleur=ENCRE, taille=11.5)
f.texte(16.2, 4.4, "sensibilité", couleur=AJOUT, gras=True)
f.texte(16.2, 3.2, "TP / positifs réels = 0 / 10", couleur=AJOUT, taille=11.5)

sys.stdout.write(f.svg())
