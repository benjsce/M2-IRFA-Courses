#!/usr/bin/env python3
"""
figure.py — tracer une figure de fiche en SVG, sans dépendance et sans couleur en dur.

Pourquoi pas une image matplotlib : une PNG à fond transparent survit au changement de
thème, mais son encre, non. Des axes noirs disparaissent sur fond sombre. Un SVG inséré
dans la page hérite au contraire des variables CSS du site — `var(--fg)`, `var(--mut)`,
`var(--acc)` — et suit donc le thème en direct, y compris quand le lecteur bascule le
bouton. Il reste net à tout grossissement, pèse quelques kilo-octets, se lit dans un
diff, et n'ajoute aucune dépendance (SPEC-MODELE §7, « pyyaml, rien d'autre »).

Une figure de fiche s'écrit dans `courses/<code>/figures/<slug>.py`, un script qui
n'imprime rien d'autre que le SVG sur la sortie standard, et dont la sortie est déposée
à côté dans `<slug>.svg`. Le validateur rejoue le script et compare : une figure qui ne
correspond plus à son code est une figure qu'on ne sait plus refaire.

Le repère est celui des données ; la classe convertit. L'axe des ordonnées monte, comme
en mathématiques, pas comme en SVG.

Usage : importé par les scripts de figure, jamais lancé seul.
Dépendance : aucune.
"""
from __future__ import annotations
import math

# Les couleurs du site (voir CSS dans build.py). Une figure n'en nomme aucune autre.
ENCRE = "var(--fg)"          # le trait principal, le texte qui compte
DOUX = "var(--mut)"          # axes, graduations
PALE = "var(--li2)"          # traits de construction, pointillés
ACCENT = "var(--acc)"        # la courbe dont parle la fiche
AJOUT = "var(--ajo)"         # une seconde courbe, à distinguer de la première
FOND = "var(--card)"         # derrière une étiquette, pour qu'elle reste lisible


def _n(v):
    """Un nombre court et stable d'une machine à l'autre : deux décimales, pas de -0."""
    s = "%.2f" % (v + 0.0)
    s = s.rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class Figure:
    """Un cadre de tracé. `xmin…ymax` sont en unités de données, `w`/`h` en pixels."""

    def __init__(self, xmin, xmax, ymin, ymax, w=560, h=340,
                 marges=(54, 16, 40, 18), titre=""):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.w, self.h = w, h
        self.mg, self.mh, self.mb, self.md = marges      # gauche, haut, bas, droite
        self.titre = titre
        self.corps = []

    # -- repère -----------------------------------------------------------
    def px(self, x):
        return self.mg + (x - self.xmin) / (self.xmax - self.xmin) * (self.w - self.mg - self.md)

    def py(self, y):
        return self.h - self.mb - (y - self.ymin) / (self.ymax - self.ymin) * (self.h - self.mh - self.mb)

    # -- primitives -------------------------------------------------------
    def _add(self, s):
        self.corps.append(s)

    def courbe(self, points, couleur=ACCENT, epaisseur=2.0, pointilles=None):
        d = "M" + " L".join("%s %s" % (_n(self.px(x)), _n(self.py(y))) for x, y in points)
        self._add('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s '
                  'stroke-linecap="round" stroke-linejoin="round"/>'
                  % (d, couleur, _n(epaisseur),
                     ' stroke-dasharray="%s"' % pointilles if pointilles else ""))

    def fonction(self, f, x0, x1, n=160, **kw):
        self.courbe([(x0 + (x1 - x0) * i / n, f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)], **kw)

    def segment(self, x0, y0, x1, y1, couleur=PALE, epaisseur=1.2, pointilles="4 3"):
        self.courbe([(x0, y0), (x1, y1)], couleur=couleur, epaisseur=epaisseur,
                    pointilles=pointilles)

    def point(self, x, y, couleur=ENCRE, r=3.6):
        self._add('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
                  % (_n(self.px(x)), _n(self.py(y)), _n(r), couleur))

    def barre(self, x, y, largeur, couleur=ACCENT, opacite=1.0, y0=None):
        """Une masse de probabilité : un rectangle posé sur l'axe, largeur en unités de
        données pour qu'il reste à sa place quel que soit le cadrage."""
        yb = self.ymin if y0 is None else y0
        X0, X1 = self.px(x - largeur / 2), self.px(x + largeur / 2)
        Y0, Y1 = self.py(yb), self.py(y)
        self._add('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"%s rx="1.5"/>'
                  % (_n(X0), _n(min(Y0, Y1)), _n(X1 - X0), _n(abs(Y0 - Y1)), couleur,
                     ' fill-opacity="%s"' % _n(opacite) if opacite < 1 else ""))

    def texte(self, x, y, s, couleur=ENCRE, taille=12.5, ancre="start",
              dx=0, dy=0, gras=False, fond=False):
        X, Y = self.px(x) + dx, self.py(y) + dy
        if fond:      # une étiquette posée sur un trait reste lisible
            self._add('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
                      'stroke="%s" stroke-width="3.2" stroke-linejoin="round" '
                      'fill="none" font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(X), _n(Y), ancre, _n(taille), FOND, _echap(s)))
        self._add('<text x="%s" y="%s" text-anchor="%s" font-size="%s" fill="%s"%s '
                  'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                  % (_n(X), _n(Y), ancre, _n(taille), couleur,
                     ' font-weight="600"' if gras else "", _echap(s)))

    def mesure(self, x, y0, y1, couleur=ENCRE, etiquette="", cote="right"):
        """La mesure d'un écart vertical : un trait, deux embouts, une étiquette.
        Des embouts droits plutôt que des pointes de flèche : sur un écart court, deux
        pointes se touchent et le trait devient illisible."""
        X, Y0, Y1 = self.px(x), self.py(y0), self.py(y1)
        self._add('<path d="M%s %s L%s %s M%s %s l-4 0 M%s %s l-4 0" stroke="%s" '
                  'stroke-width="1.4" fill="none" stroke-linecap="round"/>'
                  % (_n(X), _n(Y0), _n(X), _n(Y1), _n(X), _n(Y0), _n(X), _n(Y1), couleur))
        if etiquette:
            dx, ancre = (7, "start") if cote == "right" else (-7, "end")
            self.texte(0, 0, etiquette, couleur=couleur, taille=12, ancre=ancre,
                       dx=X - self.px(0) + dx, dy=(Y0 + Y1) / 2 - self.py(0) + 4, fond=True)

    def mesure_h(self, y, x0, x1, couleur=ENCRE):
        """La même mesure, couchée : un écart en abscisse. Une prime de risque se lit
        sur l'axe des richesses, pas sur celui des utilités."""
        Y, X0, X1 = self.py(y), self.px(x0), self.px(x1)
        self._add('<path d="M%s %s L%s %s M%s %s l0 -4 M%s %s l0 -4" stroke="%s" '
                  'stroke-width="1.4" fill="none" stroke-linecap="round"/>'
                  % (_n(X0), _n(Y), _n(X1), _n(Y), _n(X0), _n(Y + 2), _n(X1), _n(Y + 2), couleur))

    # -- axes -------------------------------------------------------------
    def axes(self, xlab="", ylab="", xticks=(), yticks=(), fmt=str, croix=None, fmt_y=None):
        """`croix=(x, y)` fait passer les axes par ce point des données au lieu du coin
        bas-gauche. Indispensable dès que zéro est au milieu : une fonction qui change
        de pente en zéro ne se lit pas si l'axe est ailleurs."""
        fy = fmt_y or fmt          # les deux axes n'ont pas toujours la même unité
        cx, cy = croix if croix else (self.xmin, self.ymin)
        x0, y0 = self.px(cx), self.py(cy)
        self._add('<path d="M%s %s L%s %s M%s %s L%s %s" fill="none" stroke="%s" stroke-width="1.2"/>'
                  % (_n(x0), _n(self.py(self.ymax)), _n(x0), _n(self.py(self.ymin)),
                     _n(self.px(self.xmin)), _n(y0), _n(self.px(self.xmax)), _n(y0), DOUX))
        for t in xticks:
            X = self.px(t)
            self._add('<path d="M%s %s l0 4" stroke="%s" stroke-width="1.2"/>' % (_n(X), _n(y0), DOUX))
            self._add('<text x="%s" y="%s" text-anchor="middle" font-size="11.5" fill="%s" '
                      'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(X), _n(y0 + 17), DOUX, _echap(fmt(t))))
        for t in yticks:
            Y = self.py(t)
            self._add('<path d="M%s %s l-4 0" stroke="%s" stroke-width="1.2"/>' % (_n(x0), _n(Y), DOUX))
            self._add('<text x="%s" y="%s" text-anchor="end" font-size="11.5" fill="%s" '
                      'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(x0 - 8), _n(Y + 4), DOUX, _echap(fy(t))))
        if xlab:
            self._add('<text x="%s" y="%s" text-anchor="end" font-size="12" fill="%s" '
                      'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(self.px(self.xmax)), _n(y0 + 33), DOUX, _echap(xlab)))
        if ylab:
            self._add('<text x="%s" y="%s" text-anchor="start" font-size="12" fill="%s" '
                      'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(x0 - 44), _n(self.py(self.ymax) - 6), DOUX, _echap(ylab)))

    # -- sortie -----------------------------------------------------------
    def svg(self):
        t = ("<title>%s</title>" % _echap(self.titre)) if self.titre else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                'width="100%%" height="auto" role="img" '
                'style="color:%s;max-width:%dpx;height:auto">%s%s</svg>\n'
                % (self.w, self.h, ENCRE, self.w, t, "".join(self.corps)))


class Planche:
    """Plusieurs cadres côte à côte, séparés par un signe.

    Il y a des identités qu'un cadre unique cache au lieu de les montrer : superposer
    le payoff d'un call, celui d'un put et leur différence donne trois traits qui se
    recouvrent deux à deux, et on ne voit qu'une droite. Posés côte à côte avec un
    « + » et un « = », les mêmes trois traits disent l'identité d'un coup d'œil.
    """

    def __init__(self, figures, signes=(), ecart=30, titre=""):
        self.figures = list(figures)
        self.signes = list(signes)
        self.ecart = ecart
        self.titre = titre

    def svg(self):
        h = max(f.h for f in self.figures)
        w = sum(f.w for f in self.figures) + self.ecart * (len(self.figures) - 1)
        morceaux, x = [], 0
        for k, f in enumerate(self.figures):
            if k:
                signe = self.signes[k - 1] if k - 1 < len(self.signes) else ""
                if signe:
                    morceaux.append('<text x="%s" y="%s" text-anchor="middle" '
                                    'font-size="20" fill="%s" '
                                    'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                                    % (_n(x - self.ecart / 2), _n(h / 2 + 7), DOUX, _echap(signe)))
            morceaux.append('<g transform="translate(%s 0)">%s</g>' % (_n(x), "".join(f.corps)))
            x += f.w + self.ecart
        t = ("<title>%s</title>" % _echap(self.titre)) if self.titre else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                'width="100%%" height="auto" role="img" '
                'style="color:%s;max-width:%dpx;height:auto">%s%s</svg>\n'
                % (w, h, ENCRE, w, t, "".join(morceaux)))


def _echap(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
