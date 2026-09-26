#!/usr/bin/env python3
r"""
portage.svg — le comptant paie deux choses : le dividende, et l'action livrée en T.

Ce que la figure doit faire voir : le détenteur d'une action reçoit, d'ici T, un
dividende, puis l'action elle-même. Ramenées en t, ces deux choses font ensemble le
comptant, connu, 100. Le dividende est connu aussi : 2 % de la valeur, il vaut 2
aujourd'hui (le poly le fixe à $d_1S_t/P(t,T_1)$ en $T_1$, soit $d_1S_t$ en t). Le trou
est la valeur aujourd'hui de l'action livrée en T : ce qui reste, 98, soit $\Phi S_t$ avec
$\Phi=0{,}98$. Les chiffres sont ceux du cours : action 100, dividende 2 %.

Usage : python courses/fpp/figures/portage.py > portage.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT      # noqa: E402

S0, D1 = 100, 0.02
DIV = D1 * S0                      # le dividende ramené en t
RESTE = S0 - DIV                   # l'action livrée en T, en valeur de t
PHI = RESTE / S0
n = lambda v: ("%g" % v).replace(".", ",")

t, T1, T = 5.0, 7.0, 9.6
g = Figure(xmin=0, xmax=10.6, ymin=-0.9, ymax=3.9, w=680, h=300, marges=(8, 8, 8, 8),
           titre="Le comptant paie le dividende et l'action livrée en T : le portage est ce qui reste")
g.axe_temps(0, 4.6, 10.3, [(t, "t"), (T, "T")])
g.courbe([(T1, -0.14), (T1, 0.14)], couleur=DOUX, epaisseur=1.3)
g.texte(T1, 0, "T_{1}", couleur=DOUX, ancre="middle", dy=21)

# le dividende, reçu en T1, ramené en t
g.fleche(T1, 0.35, T1, 1.2, couleur=AJOUT, epaisseur=2)
g.texte(T1, 0.72, "dividende", couleur=AJOUT, taille=12.5, dx=8)
g.fleche(T1 - 0.08, 1.45, t + 0.15, 1.45, couleur=AJOUT, courbure=12)

# l'action, reçue en T, ramenée en t
g.fleche(T, 0.35, T, 2.6, couleur=ACCENT, epaisseur=2.2)
g.texte(T, 1.45, "l'action", couleur=ACCENT, taille=12.5, ancre="end", dx=-8)
g.fleche(T - 0.08, 2.95, t + 0.15, 2.95, couleur=ACCENT, courbure=16)

# en t : ce que valent aujourd'hui ces deux choses
xl = t - 0.12
g.texte(xl, 3.3, "l'action livrée en T : le trou", couleur=ENCRE, gras=True, ancre="end")
g.texte(xl, 2.7, "%s − %s = %s = Φ·S_{t}" % (n(S0), n(DIV), n(RESTE)), couleur=ACCENT,
        gras=True, taille=13.5, ancre="end")
g.texte(xl, 1.6, "le dividende : connu", couleur=ENCRE, ancre="end")
g.texte(xl, 1.05, "%s = d_{1}·S_{t}" % n(DIV), couleur=AJOUT, gras=True, taille=13.5,
        ancre="end")

# les deux ensemble : le comptant, connu
xb = 2.0
g.courbe([(xb + 0.12, 0.8), (xb, 0.8), (xb, 3.55), (xb + 0.12, 3.55)], couleur=DOUX,
         epaisseur=1.4)
g.texte(xb - 0.1, 2.35, "S_{t} = %s" % n(S0), couleur=ENCRE, gras=True, taille=13.5, ancre="end")
g.texte(xb - 0.1, 1.8, "connu", couleur=DOUX, taille=12, ancre="end")
g.texte(xb + 0.2, -0.6, "portage : Φ = %s / %s = %s" % (n(RESTE), n(S0), n(PHI)),
        couleur=ACCENT, gras=True, taille=13)

sys.stdout.write(g.svg())
