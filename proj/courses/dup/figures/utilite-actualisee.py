#!/usr/bin/env python3
r"""
utilite-actualisee.svg — chaque utilité ramenée aujourd'hui par son poids, puis sommée.

La Forme de la fiche, $U=u_0+D(1)u_1+D(2)u_2+D(3)u_3$, dessinée en échéancier : l'utilité
de chaque date monte au-dessus de l'axe ; une flèche courbe la ramène en 0 en portant le
facteur $D(t)$ ; en 0, les utilités ramenées s'empilent, et la pile est $U$.

Les hauteurs sont schématiques : le principe ne fixe ni les $u_t$ ni la forme de $D$, et
la figure n'a donc aucune graduation. Seul compte que chaque barre ramenée soit plus
courte que l'originale, $D(t)<1$, et que $D(0)=1$.

Usage : python courses/dup/figures/utilite-actualisee.py > utilite-actualisee.svg
Dépendance : aucune.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from figure import Figure, ACCENT, ENCRE, DOUX, AJOUT, PALE      # noqa: E402

U = [3.0, 4.0, 4.0, 3.2]          # u_0 … u_3, schématiques
D = [1.0, 0.62, 0.5, 0.42]        # D(0) = 1, puis décroissante
LIB = ["u₀", "u₁", "u₂", "u₃"]

f = Figure(xmin=-2.3, xmax=3.6, ymin=-1.9, ymax=11.4, w=560, h=380, marges=(20, 16, 20, 18),
           titre="Chaque utilité revient en 0 multipliée par D(t), et les utilités ramenées s'empilent en U")
f.axe_temps(0, -2.2, 3.5, [(0, "0"), (1, "1"), (2, "2"), (3, "3")])

# les utilités à leur date
for t in (1, 2, 3):
    f.barre(t, U[t], 0.34, couleur=DOUX, opacite=0.55, y0=0)
    f.texte(t, U[t], LIB[t], couleur=DOUX, ancre="middle", dy=-6, gras=True)

# la pile en 0 : u_0, puis chaque D(t) u_t
bas = 0.0
X0 = -0.75
for t in range(4):
    h = D[t] * U[t]
    f.barre(X0, bas + h, 0.5, couleur=ACCENT if t else ENCRE, opacite=0.9 - 0.15 * t, y0=bas)
    lib = "u₀" if t == 0 else "D(%d)u%s" % (t, "₁₂₃"[t - 1])
    f.texte(X0 - 0.3, bas + h / 2, lib, couleur=ENCRE, ancre="end", dy=4, taille=12)
    if t:
        ya = bas + h * 0.5
        yb = U[t] + 0.75
        k = 14 + 8 * t
        f.fleche(t, yb, X0 + 0.27, ya, couleur=AJOUT, courbure=k)
        f.texte((t + X0 + 0.27) / 2, (ya + yb) / 2, "× D(%d)" % t, couleur=AJOUT,
                ancre="middle", dy=-k - 6, taille=12, gras=True, fond=True)
    bas += h
f.texte(X0, bas, "U", couleur=ENCRE, ancre="middle", dy=-8, gras=True)

f.texte(1.1, -1.65, "U = u₀ + D(1)u₁ + D(2)u₂ + D(3)u₃", couleur=ENCRE, ancre="middle",
        taille=13.5, gras=True)

sys.stdout.write(f.svg())
