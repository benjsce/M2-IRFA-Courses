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
import re

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
            # Un rectangle de la couleur du fond, à la taille du texte, posé dessous : un
            # filtre qui remplit la boîte du texte. L'ancien halo, un contour autour de
            # chaque lettre, laissait passer le trait dans les espaces entre les mots
            # (constaté le 2026-09-26 : « l'action-est-portée,-sans-aucun-geste »).
            if not getattr(self, "_filtre_fond", False):
                self._add('<defs><filter id="fond-etiquette" x="-0.03" y="-0.12" '
                          'width="1.06" height="1.24"><feFlood style="flood-color:%s"/>'
                          '</filter></defs>' % FOND)
                self._filtre_fond = True
            self._add('<text x="%s" y="%s" text-anchor="%s" font-size="%s" fill="none" '
                      'filter="url(#fond-etiquette)" '
                      'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(X), _n(Y), ancre, _n(taille), _exposants(s, taille)))
        self._add('<text x="%s" y="%s" text-anchor="%s" font-size="%s" fill="%s"%s '
                  'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                  % (_n(X), _n(Y), ancre, _n(taille), couleur,
                     ' font-weight="600"' if gras else "", _exposants(s, taille)))

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

    # -- échéanciers -----------------------------------------------------
    def fleche(self, x0, y0, x1, y1, couleur=ENCRE, epaisseur=1.5, courbure=0.0,
               pointilles=None):
        """Une flèche de (x0, y0) vers (x1, y1), pointe à l'arrivée. `courbure` est en
        pixels : le sommet de l'arc s'écarte d'autant de la corde, vers le haut de
        l'image quand elle est positive. Un flux reçu monte, un flux payé descend ; un
        flux qu'on actualise revient vers la gauche en arc, comme au tableau."""
        X0, Y0, X1, Y1 = self.px(x0), self.py(y0), self.px(x1), self.py(y1)
        if courbure:
            L = math.hypot(X1 - X0, Y1 - Y0) or 1.0
            nx, ny = (Y1 - Y0) / L, -(X1 - X0) / L          # une normale à la corde
            if ny > 0:                                       # tournée vers le haut
                nx, ny = -nx, -ny
            cx = (X0 + X1) / 2 + 2 * courbure * nx
            cy = (Y0 + Y1) / 2 + 2 * courbure * ny
            d = "M%s %s Q%s %s %s %s" % (_n(X0), _n(Y0), _n(cx), _n(cy), _n(X1), _n(Y1))
            tx, ty = X1 - cx, Y1 - cy
        else:
            d = "M%s %s L%s %s" % (_n(X0), _n(Y0), _n(X1), _n(Y1))
            tx, ty = X1 - X0, Y1 - Y0
        t = math.hypot(tx, ty) or 1.0
        ux, uy = tx / t, ty / t
        a, b = 8.0, 4.0                                      # longueur, demi-largeur
        p1 = (X1 - a * ux + b * uy, Y1 - a * uy - b * ux)
        p2 = (X1 - a * ux - b * uy, Y1 - a * uy + b * ux)
        self._add('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s '
                  'stroke-linecap="round"/>'
                  % (d, couleur, _n(epaisseur),
                     ' stroke-dasharray="%s"' % pointilles if pointilles else ""))
        self._add('<path d="M%s %s L%s %s L%s %s Z" fill="%s"/>'
                  % (_n(X1), _n(Y1), _n(p1[0]), _n(p1[1]), _n(p2[0]), _n(p2[1]), couleur))

    def axe_temps(self, y, x0, x1, dates):
        """L'axe du temps d'un échéancier : un trait, et une graduation étiquetée par
        date. `dates` est une liste de couples (abscisse, étiquette)."""
        self.courbe([(x0, y), (x1, y)], couleur=DOUX, epaisseur=1.3)
        self.fleche(x1 - 0.01, y, x1, y, couleur=DOUX, epaisseur=1.3)
        for x, s in dates:
            X, Y = self.px(x), self.py(y)
            self._add('<path d="M%s %s l0 10" stroke="%s" stroke-width="1.3"/>'
                      % (_n(X), _n(Y - 5), DOUX))
            self._add('<text x="%s" y="%s" text-anchor="middle" font-size="12.5" fill="%s" '
                      'font-style="italic" font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                      % (_n(X), _n(Y + 21), DOUX, _echap(s)))

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
        w, h, corps = self.contenu()
        t = ("<title>%s</title>" % _echap(self.titre)) if self.titre else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                'width="100%%" height="auto" role="img" '
                'style="color:%s;max-width:%dpx;height:auto">%s%s</svg>\n'
                % (w, h, ENCRE, w, t, corps))

    def contenu(self):
        """Largeur, hauteur et tracé de la planche, sans l'enveloppe SVG : ce qu'une
        `Colonne` empile."""
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
        return w, h, "".join(morceaux)


class Colonne:
    """Des planches empilées, chacune sous son intitulé.

    Une Forme qui écrit deux identités côte à côte — le straddle et le call spread — se
    lit mieux en deux lignes qu'en une planche de six cadres : chaque ligne est une
    identité, et le lecteur la refait de gauche à droite.
    """

    def __init__(self, planches, intitules=(), ecart=18, titre=""):
        self.planches = list(planches)
        self.intitules = list(intitules)
        self.ecart = ecart
        self.titre = titre

    def svg(self):
        blocs, w, y = [], 0, 0
        for k, p in enumerate(self.planches):
            pw, ph, corps = p.contenu()
            if k < len(self.intitules) and self.intitules[k]:
                y += 22
                blocs.append('<text x="4" y="%s" font-size="14" font-weight="600" fill="%s" '
                             'font-family="ui-sans-serif,system-ui,sans-serif">%s</text>'
                             % (_n(y - 6), ENCRE, _exposants(self.intitules[k], 14)))
            blocs.append('<g transform="translate(0 %s)">%s</g>' % (_n(y), corps))
            y += ph + self.ecart
            w = max(w, pw)
        h = y - self.ecart
        t = ("<title>%s</title>" % _echap(self.titre)) if self.titre else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
                'width="100%%" height="auto" role="img" '
                'style="color:%s;max-width:%dpx;height:auto">%s%s</svg>\n'
                % (w, h, ENCRE, w, t, "".join(blocs)))


def _exposants(s, taille):
    """`P^{f}(t,T)`, `H_{tₖ}` : l'exposant monte, l'indice descend, d'un tiers de corps,
    et tous deux rapetissent. Les caractères exposants d'Unicode (ᶠ) existent, mais la
    police de secours qui les dessine les pose à côté de la lettre au lieu d'au-dessus."""
    morceaux = re.split(r"([\^_])\{([^}]*)\}", str(s))
    out = _echap(morceaux[0])
    for k in range(1, len(morceaux), 3):
        h = taille * (0.35 if morceaux[k] == "^" else -0.25)
        out += ('<tspan dy="%s" font-size="%s">%s</tspan><tspan dy="%s">%s</tspan>'
                % (_n(-h), _n(taille * 0.72), _echap(morceaux[k + 1]), _n(h),
                   _echap(morceaux[k + 2])))
    return out


def _echap(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
