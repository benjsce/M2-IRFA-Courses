#!/usr/bin/env python3
r"""
modele-de-fama-french.svg — le rendement attendu, monté facteur par facteur.

Ce que la figure doit faire voir : le rendement d'une action au-delà du taux sans risque
se construit en escalier. On part de α, puis chaque facteur ajoute sa marche : la
sensibilité au marché fois le mouvement du marché, s_i fois SMB, h_i fois HML. Une marche
peut descendre : une exposition et un facteur de même signe ajoutent, de signes opposés
retirent. Le dernier palier est la partie expliquée ; ε, ce qui reste, n'est pas dessiné.
La Forme est écrite dessous, terme sous marche.

Les chiffres de la fiche, choisis pour l'exemple : un mois où le marché fait 4 % au-delà
du taux sans risque, SMB = 2 % et HML = −2 % ; une petite entreprise de croissance, de
sensibilités β_i = 1,5, s_i = 0,6 et h_i = −0,4, d'alpha nul. Marches : 6, puis 1,2, puis
0,8 ; total 8 %.

Usage : python courses/pfo/figures/modele-de-fama-french.py > modele-de-fama-french.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, DOUX, ENCRE, PALE      # noqa: E402

ALPHA, MKT, SMB, HML = 0.0, 4.0, 2.0, -2.0
BETA, S, H = 1.5, 0.6, -0.4
MARCHES = (("α_{i}", ALPHA, "α = 0"),
           ("β_{i} (R_{m,t} − R_{f,t})", BETA * MKT, "1,5 × 4"),
           ("s_{i} SMB_{t}", S * SMB, "0,6 × 2"),
           ("h_{i} HML_{t}", H * HML, "−0,4 × (−2)"))
TOTAL = sum(m[1] for m in MARCHES)
assert abs(TOTAL - 8.0) < 1e-12

fr = lambda v, d=1: ("%.*f" % (d, v)).replace(".", ",").replace("-", "−")

f = Figure(xmin=0, xmax=5.2, ymin=-2.4, ymax=9.6, w=600, h=400, marges=(54, 16, 20, 18),
           titre="Le rendement au-delà du taux sans risque, monté facteur par facteur")
f.axes(ylab="au-delà du taux sans risque, en %", yticks=(0, 6, 7.2, 8),
       fmt=lambda t: fr(t, 1).replace(",0", ""), croix=(0, 0))
bas = 0.0
couleurs = (DOUX, ACCENT, AJOUT, AJOUT)
for k, (terme, val, calc) in enumerate(MARCHES):
    xc, lg = 0.55 + 1.0 * k, 0.56
    if val:
        f.barre(xc, bas + val, lg, couleur=couleurs[k], opacite=0.35, y0=bas)
        f.texte(xc, bas + val, "+ " + fr(val), couleur=ENCRE, ancre="middle", dy=-7,
                gras=True)
    else:
        f.segment(xc - lg / 2, bas, xc + lg / 2, bas, couleur=DOUX, epaisseur=2.0,
                  pointilles=None)
        f.texte(xc, bas, "0", couleur=ENCRE, ancre="middle", dy=-7, gras=True)
    if k < len(MARCHES) - 1:
        f.segment(xc + lg / 2, bas + val, xc + 1.0 - lg / 2, bas + val, couleur=PALE,
                  epaisseur=1.0)
    f.texte(xc, 0, terme, couleur=ENCRE, ancre="middle", dy=18, taille=11.5)
    f.texte(xc, 0, calc, couleur=DOUX, ancre="middle", dy=33, taille=11)
    bas += val
xc = 4.65
f.barre(xc, TOTAL, 0.5, couleur=ENCRE, opacite=0.18, y0=0)
f.texte(xc, TOTAL, fr(TOTAL, 0) + " %", couleur=ENCRE, ancre="middle", dy=-7, gras=True)
f.texte(xc, 0, "expliqué", couleur=ENCRE, ancre="middle", dy=18, taille=11.5)
f.texte(xc, 0, "+ ε_{i,t} à part", couleur=DOUX, ancre="middle", dy=33, taille=11)

f.texte(2.6, -2.4, "R_{i,t} − R_{f,t} = α_{i} + β_{i}(R_{m,t} − R_{f,t}) + s_{i} SMB_{t}"
        " + h_{i} HML_{t} + ε_{i,t}", couleur=ENCRE, ancre="middle", taille=13.5, gras=True,
        dy=-6)

sys.stdout.write(f.svg())
