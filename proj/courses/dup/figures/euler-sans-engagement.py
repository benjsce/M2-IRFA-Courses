#!/usr/bin/env python3
r"""
euler-sans-engagement.svg — le facteur d'actualisation effectif comme l'aire d'une barre.

Un euro de plus transmis au moi 2, en abscisse de 0 à 1, découpé comme le moi 2 le découpe
[L5 slide 29] : la part $c_2'$ qu'il consomme, que le moi 1 pèse $\beta\delta$, et la part
$1-c_2'$ qu'il épargne, qui revient au moi 1 avec le poids $\delta$. L'aire est le crochet
de la Forme, $c_2'\beta\delta+(1-c_2')\delta$.

Les valeurs sont celles de l'exemple de la fiche [ajout] : $u=\ln$, $\beta=\tfrac12$,
$\delta=R=1$, d'où $c_2(w_2)=w_2/(1+\beta\delta)$, $c_2'=\tfrac23$ et un facteur de $\tfrac23$.

Usage : python courses/dup/figures/euler-sans-engagement.py > euler-sans-engagement.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

BETA, DELTA = 0.5, 1.0
C2P = 1 / (1 + BETA * DELTA)                   # pente de la règle du moi 2 sous u = ln
EFF = C2P * BETA * DELTA + (1 - C2P) * DELTA   # 2/3
assert abs(EFF - 2 / 3) < 1e-12

f = Figure(xmin=-0.08, xmax=1.42, ymin=0, ymax=1.3, w=560, h=330, marges=(58, 16, 40, 18),
           titre="La part consommée compte βδ, la part épargnée δ : l'aire est le facteur effectif")
f.axes(xlab="un euro de plus pour le moi 2", ylab="poids pour le moi 1",
       xticks=(0, C2P, 1), yticks=(BETA * DELTA, EFF, DELTA),
       fmt=lambda t: {0: "0", 1: "1"}.get(t, "c₂′ = ⅔"),
       fmt_y=lambda t: {0.5: "βδ = ½", 1.0: "δ = 1"}.get(round(t, 6), "⅔"), croix=(0, 0))

f.barre(C2P / 2, BETA * DELTA, C2P, couleur=ACCENT, opacite=0.8)
f.barre(C2P + (1 - C2P) / 2, DELTA, 1 - C2P, couleur=AJOUT, opacite=0.7)
f.texte(C2P / 2, BETA * DELTA / 2, "consommé : c₂′ × βδ", couleur=ENCRE, ancre="middle", gras=True, fond=True)
f.texte(C2P + (1 - C2P) / 2, DELTA / 2, "épargné :", couleur=ENCRE, ancre="middle", gras=True, fond=True, dy=-8)
f.texte(C2P + (1 - C2P) / 2, DELTA / 2, "(1 − c₂′) × δ", couleur=ENCRE, ancre="middle", gras=True, fond=True, dy=10)

f.segment(0, EFF, 1.06, EFF, couleur=ENCRE, epaisseur=1.4, pointilles="6 4")
f.texte(1.07, EFF, "facteur effectif", couleur=ENCRE, dy=-4, taille=12, gras=True)
f.texte(1.07, EFF, "= ⅔ × ½ + ⅓ × 1 = ⅔", couleur=ENCRE, dy=12, taille=12)

f.texte(0.66, 1.18, "u′(c₁) = [c₂′βδ + (1 − c₂′)δ] R u′(c₂)", couleur=ENCRE, ancre="middle",
        taille=13.5, gras=True)

sys.stdout.write(f.svg())
