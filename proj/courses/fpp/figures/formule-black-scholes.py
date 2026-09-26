#!/usr/bin/env python3
r"""
formule-black-scholes.svg — les deux termes de la formule, lus sur la loi de $S_T$.

Ce que la figure doit faire voir : le call ne paie que dans les états où $S_T>K$ ; dans
ces états, on reçoit l'action et on paie le strike. La formule est donc « ce qu'on reçoit
si l'on exerce, moins ce qu'on paie si l'on exerce », chacun ramené en $t$. L'aire ombrée
sous la densité est la probabilité risque-neutre d'exercer, $N(d_2)$ ; le terme payé en
est $Ke^{-rT}N(d_2)$, le terme reçu $S_0N(d_1)$.

La densité est celle de $S_T$ sous $\mathbb{Q}$ dans le modèle de Black et Scholes, avec
les chiffres de l'exemple : $S_0=100$, $K=100$, $r=4\,\%$, $\sigma=20\,\%$, un an. Donc
$\ln S_T$ gaussien de moyenne $\ln 100+(r-\sigma^2/2)$ et d'écart type $0{,}2$.

Usage : python courses/fpp/figures/formule-black-scholes.py > formule-black-scholes.svg
Dépendance : aucune.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, AJOUT, ENCRE, DOUX, _n      # noqa: E402

S0, K, R, SIG, T = 100.0, 100.0, 0.04, 0.20, 1.0
N = NormalDist().cdf
d1 = (math.log(S0 / K) + (R + SIG ** 2 / 2) * T) / (SIG * math.sqrt(T))
d2 = d1 - SIG * math.sqrt(T)
DK = K * math.exp(-R * T)
RECU, PAYE = S0 * N(d1), DK * N(d2)
M, E = math.log(S0) + (R - SIG ** 2 / 2) * T, SIG * math.sqrt(T)


def dens(s):
    """Densité log-normale de S_T sous Q, multipliée par 100 pour se lire en % par unité."""
    return 100 * math.exp(-(math.log(s) - M) ** 2 / (2 * E * E)) / (s * E * math.sqrt(2 * math.pi))


v = lambda x, n=2: ("%.*f" % (n, x)).replace(".", ",")
X0, X1 = 50.0, 180.0

f = Figure(xmin=X0, xmax=X1, ymin=0, ymax=2.75, w=660, h=360, marges=(20, 20, 40, 14),
           titre="Le call vaut ce qu'on reçoit si l'on exerce, moins ce qu'on paie si l'on exerce")
f.axes(xlab="sous-jacent en T", xticks=(60, K, 140, 180), fmt=lambda x: "%d" % x)

# l'aire des états où l'on exerce
pts = [(K, 0)] + [(K + (X1 - K) * i / 160, dens(K + (X1 - K) * i / 160)) for i in range(161)] + [(X1, 0)]
f._add('<path d="M%s Z" fill="%s" fill-opacity="0.22" stroke="none"/>'
       % (" L".join("%s %s" % (_n(f.px(x)), _n(f.py(y))) for x, y in pts), ACCENT))
f.fonction(dens, X0 + 1, X1, couleur=ENCRE, epaisseur=2)
f.segment(K, 0, K, dens(K) + 0.25, couleur=DOUX, pointilles="4 3")
f.texte(K, dens(K) + 0.25, "strike K", couleur=DOUX, taille=11.5, ancre="middle", dy=-6)

# à gauche : on n'exerce pas
f.texte(72, 2.45, "si S_{T}\u00a0≤ K, on n'exerce pas :", couleur=DOUX, taille=12, ancre="middle")
f.texte(72, 2.45, "le call ne paie rien", couleur=DOUX, taille=12, ancre="middle", dy=16)

# dans l'aire : la probabilité d'exercer
f.texte(118, 0.62, "probabilité d'exercer", couleur=ACCENT, taille=12, ancre="middle", gras=True)
f.texte(118, 0.62, "N(d_{2}) = " + v(N(d2), 4), couleur=ACCENT, taille=12, ancre="middle", dy=16)

# à droite : ce que l'exercice échange, ramené à aujourd'hui
f.texte(128, 2.45, "si S_{T}\u00a0> K, on exerce ; ramené à aujourd'hui :", couleur=ENCRE, taille=12.5, gras=True)
f.texte(128, 2.45, "on reçoit l'action : S_{0}N(d_{1}) = " + v(RECU, 3), couleur=AJOUT,
        taille=12, dy=20)
f.texte(128, 2.45, "on paie K : Ke^{−rT}N(d_{2}) = " + v(PAYE, 3), couleur=ACCENT,
        taille=12, dy=38)
f.texte(128, 2.45, "C = %s − %s = %s" % (v(RECU, 3), v(PAYE, 3), v(RECU - PAYE, 3)),
        couleur=ENCRE, taille=12.5, gras=True, dy=60)

sys.stdout.write(f.svg())
