#!/usr/bin/env python3
"""
test_garde_fous.py — les garde-fous du validateur se déclenchent-ils vraiment ?

Un contrôle qu'on n'a jamais vu échouer n'est pas un contrôle : c'est une intention.
Ce module fabrique un corpus minuscule en dossier temporaire, y injecte une faute à la
fois, et vérifie que `validate.py` la voit — et qu'il se tait quand la faute est déclarée.

Il couvre les quatre garde-fous qui portent sur ce qui *se répète d'un cours à l'autre*
ou *change en amont d'une fiche déjà écrite* : homonymie, collision de symbole, cours
inexistant dans une déclaration, et croissance du socle d'une fiche existante.

Usage : python tools/tests/test_garde_fous.py
Sortie : une ligne par cas ; code de retour ≠ 0 si un garde-fou reste muet.

Dépendance : pyyaml.
"""
from __future__ import annotations
import shutil, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate import Rapport, valider          # noqa: E402

for _f in (sys.stdout, sys.stderr):            # cp1252 sous PowerShell
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------- le corpus d'essai

FICHE = """---
id: {code}/{slug}
nom: {nom}
type: notion
statut: source
construite_a_partir_de: [{dep}]
{extra}refs:
- p. 1
---
## Ce que c'est
{nom}, pour l'essai. [p. 1]
{chemin}
## Ce qui la définit
Rien de plus. [p. 1]

## Cesse d'être valide quand
L'essai est fini. [p. 1]
"""


def ecrire(root: Path, code: str, fiches, notation=""):
    d = root / "courses" / code
    (d / "notions").mkdir(parents=True)
    (d / "course.yml").write_text(
        "code: %s\ntitre: Essai %s\nsources: []\nrefs_pattern: ^p\\. \\d+$\ndepend_de: []\n"
        % (code, code), encoding="utf-8", newline="\n")
    (d / "notation.yml").write_text(notation or "symboles: []\n",
                                    encoding="utf-8", newline="\n")
    inv = ["elements:"]
    for f in fiches:
        champs = dict(code=code, extra="", chemin="", dep="")
        champs.update(f)
        (d / "notions" / (f["slug"] + ".md")).write_text(
            FICHE.format(**champs), encoding="utf-8", newline="\n")
        inv += ["- ref: p. 1 %s" % f["slug"], "  notion: %s/%s" % (code, f["slug"])]
    (d / "inventaire.yml").write_text("\n".join(inv) + "\n", encoding="utf-8", newline="\n")


def messages(root: Path):
    rap = Rapport()
    valider(root, rap)
    return ([f"E {a} {o}: {m}" for a, o, m in rap.E],
            [f"W {a} {o}: {m}" for a, o, m in rap.W])


# ---------------------------------------------------------------- les cas

ECHECS = []


def cas(titre, attendu, construire, doit_apparaitre=True, sous=""):
    """`attendu` est un fragment de message ; on le cherche dans E + W.
    `sous` : valider un sous-dossier, pour les contrôles qui regardent le dossier parent."""
    root = Path(tempfile.mkdtemp())
    try:
        construire(root)
        E, W = messages(root / sous if sous else root)
        vu = any(attendu in x for x in E + W)
        ok = vu is doit_apparaitre
        print(("  ok   " if ok else "  RATÉ ") + titre)
        if not ok:
            ECHECS.append(titre)
            for x in E + W:
                print("         " + x)
    finally:
        shutil.rmtree(root, ignore_errors=True)


def hom_non_declaree(root):
    ecrire(root, "aa", [dict(slug="prime", nom="Prime de risque")])
    ecrire(root, "bb", [dict(slug="prime", nom="Prime de risque")])


def hom_declaree(root):
    hom_non_declaree(root)
    (root / "courses" / "aa" / "notation.yml").write_text(
        "symboles: []\nhomonymes:\n- nom: Prime de risque\n  entre:\n  - aa/prime\n"
        "  - bb/prime\n  note: deux objets, le même mot\n",
        encoding="utf-8", newline="\n")


def hom_meme_cours(root):
    ecrire(root, "aa", [dict(slug="prime", nom="Prime de risque"),
                        dict(slug="prime-bis", nom="Autre", extra="alias:\n- risk premium\n"),
                        dict(slug="prime-ter", nom="Encore", extra="alias:\n- risk premium\n")])


REG_UN = ("symboles:\n- symbole: $\\rho$\n  notion: aa/x\n  ref: p. 1\n  sens: un sens\n"
          "- symbole: $\\tau$\n  notion: aa/x\n  ref: p. 1\n  sens: un autre\n")


def sym_sans_rubrique(root):
    """Le registre attribue deux symboles à la fiche, elle n'explique aucun."""
    ecrire(root, "aa", [dict(slug="x", nom="Un", extra="symbole: $\\rho$\n")], REG_UN)


def sym_rubrique_partielle(root):
    """La rubrique est là, mais elle n'en nomme qu'un sur les deux."""
    ecrire(root, "aa", [dict(slug="x", nom="Un", extra="symbole: $\\rho$\n")], REG_UN)
    f = root / "courses" / "aa" / "notions" / "x.md"
    t = f.read_text(encoding="utf-8").replace(
        "## Ce qui la définit",
        "## Ce que les symboles modélisent\n$\\rho$ mesure une chose. [p. 1]\n\n"
        "## Ce qui la définit")
    f.write_text(t, encoding="utf-8", newline="\n")


def sym_rubrique_complete(root):
    """Les deux symboles sont nommés : le validateur se tait."""
    ecrire(root, "aa", [dict(slug="x", nom="Un", extra="symbole: $\\rho$\n")], REG_UN)
    f = root / "courses" / "aa" / "notions" / "x.md"
    t = f.read_text(encoding="utf-8").replace(
        "## Ce qui la définit",
        "## Ce que les symboles modélisent\n$\\rho$ mesure une chose, $\\tau$ en mesure "
        "une autre. [p. 1]\n\n## Ce qui la définit")
    f.write_text(t, encoding="utf-8", newline="\n")


def sym_non_declare(root):
    reg = "symboles:\n- symbole: $\\rho$\n  notion: %s/x\n  ref: p. 1\n  sens: un sens\n"
    ecrire(root, "aa", [dict(slug="x", nom="Un", extra="symbole: $\\rho$\n")], reg % "aa")
    ecrire(root, "bb", [dict(slug="x", nom="Deux", extra="symbole: $\\rho$\n")], reg % "bb")


def sym_declare(root):
    sym_non_declare(root)
    p = root / "courses" / "aa" / "notation.yml"
    p.write_text(p.read_text(encoding="utf-8")
                 + "collisions:\n- symbole: $\\rho$\n  ici: un sens\n  ailleurs:\n"
                   "    bb: un autre sens\n", encoding="utf-8", newline="\n")


def sym_declare_a_moitie(root):
    """Trois cours partagent le symbole, la déclaration n'en nomme que deux."""
    reg = "symboles:\n- symbole: $\\rho$\n  notion: %s/x\n  ref: p. 1\n  sens: un sens\n"
    for c in ("aa", "bb", "cc"):
        ecrire(root, c, [dict(slug="x", nom="N " + c, extra="symbole: $\\rho$\n")], reg % c)
    p = root / "courses" / "aa" / "notation.yml"
    p.write_text(p.read_text(encoding="utf-8")
                 + "collisions:\n- symbole: $\\rho$\n  ici: un sens\n  ailleurs:\n"
                   "    bb: un autre sens\n", encoding="utf-8", newline="\n")


def cours_fantome(root):
    ecrire(root, "aa", [dict(slug="x", nom="Un")],
           "symboles: []\ncollisions:\n- symbole: $P$\n  ici: un sens\n  ailleurs:\n"
           "    zz: ailleurs, dans un cours qui n'existe pas\n")


def socle_grandit(root):
    """Une notion nouvelle entre dans le socle d'une fiche déjà écrite, et dans celui
    de sa descendance : le « chemin jusqu'ici » de chacune devient incomplet."""
    ch = "\n## Le chemin jusqu'ici\nTout vient de %s. [p. 1]\n"
    ecrire(root, "aa", [
        dict(slug="base", nom="Base"),
        dict(slug="milieu", nom="Milieu", dep="aa/base, aa/neuve",
             chemin=ch % "aa/base"),
        dict(slug="aval", nom="Aval", dep="aa/milieu",
             chemin=ch % "aa/base, aa/milieu"),
        dict(slug="neuve", nom="Neuve"),
    ])


# ---------------------------------------------------------------- parcours (A14–A16)
# Trois fiches en chaîne : base ← milieu ← haut. Le parcours raconte milieu puis haut,
# et doit rattacher base à l'histoire, puisque milieu la suppose.

def _parcours(root, etapes, avant, slug="essai", ordre=1, fiches=True):
    ch = "\n## Le chemin jusqu'ici\nTout vient de %s. [p. 1]\n"
    if fiches:
        ecrire(root, "aa", [
            dict(slug="base", nom="Base"),
            dict(slug="milieu", nom="Milieu", dep="aa/base", chemin=ch % "aa/base"),
            dict(slug="haut", nom="Haut", dep="aa/milieu", chemin=ch % "aa/base, aa/milieu"),
        ])
    d = root / "courses" / "aa" / "parcours"
    d.mkdir(exist_ok=True)
    txt = ["---", "id: aa/parcours-%s" % slug, "ordre: %d" % ordre, "titre: Essai", "---", "",
           "## Point de départ", "On part de 100. [p. 1]", ""]
    if avant:
        txt += ["## À savoir avant"] + ["- aa/%s : son rôle ici. [p. 1]" % x for x in avant] + [""]
    txt += ["## Étapes"]
    for k, x in enumerate(etapes, 1):
        txt += ["%d. aa/%s" % (k, x), "   La question qui y mène. [p. 1]",
                "   Histoire : « 100 » — Ce que la fiche en reprend. [p. 1]", ""]
    txt += ["## Point d'arrivée", "On arrive là. [p. 1]"]
    (d / (slug + ".md")).write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")


def parcours_ok(root):
    _parcours(root, ["milieu", "haut"], ["base"])


def parcours_paraphrase(root):
    _parcours(root, ["milieu", "haut"], ["base"])
    f = root / "courses" / "aa" / "parcours" / "essai.md"
    f.write_text(f.read_text(encoding="utf-8").replace(
        "1. aa/milieu\n   La question qui y mène. [p. 1]",
        "1. aa/milieu\n   Milieu, pour l'essai. [p. 1]"), encoding="utf-8", newline="\n")


def parcours_depart_abstrait(root):
    """Un point de départ sans chiffre : le chiffre de la référence ne compte pas."""
    _parcours(root, ["milieu", "haut"], ["base"])
    f = root / "courses" / "aa" / "parcours" / "essai.md"
    f.write_text(f.read_text(encoding="utf-8").replace(
        "On part de 100. [p. 1]", "On part d'une idée générale. [p. 1]"),
        encoding="utf-8", newline="\n")


def _histoire(root, nouvelle):
    f = root / "courses" / "aa" / "parcours" / "essai.md"
    f.write_text(f.read_text(encoding="utf-8").replace(
        "Histoire : « 100 » — Ce que la fiche en reprend. [p. 1]", nouvelle, 1),
        encoding="utf-8", newline="\n")


def parcours_citation_absente(root):
    """Une citation que le point de départ ne contient pas : le gras ne tomberait sur rien."""
    _parcours(root, ["milieu", "haut"], ["base"])
    _histoire(root, "Histoire : « 200 » — Ce que la fiche en reprend. [p. 1]")


def parcours_citation_coupe_formule(root):
    _parcours(root, ["milieu", "haut"], ["base"])
    f = root / "courses" / "aa" / "parcours" / "essai.md"
    f.write_text(f.read_text(encoding="utf-8").replace("On part de 100.", "On part de $x=100$."),
                 encoding="utf-8", newline="\n")
    _histoire(root, "Histoire : « $x=1 » — Ce que la fiche en reprend. [p. 1]")


def _suite_puis_cite(root, cite_a):
    """Une suite ajoutée à l'étape 2, citée par l'étape cite_a."""
    _parcours(root, ["milieu", "haut"], ["base"])
    f = root / "courses" / "aa" / "parcours" / "essai.md"
    t = f.read_text(encoding="utf-8").split("\n")
    k = [j for j, l in enumerate(t) if l.startswith("2. aa/")][0]
    t.insert(k + 1, "   Suite : Un second agent arrive. [p. 1]")
    j = [i for i, l in enumerate(t) if l.startswith("%d. aa/" % cite_a)][0] + 2
    t[j] = "   Histoire : « second agent » — Ce que la fiche en reprend. [p. 1]"
    f.write_text("\n".join(t), encoding="utf-8", newline="\n")


def parcours_cite_suite_future(root):
    _suite_puis_cite(root, 1)


def parcours_cite_suite_racontee(root):
    _suite_puis_cite(root, 2)


def parcours_histoire_sans_lien(root):
    _parcours(root, ["milieu", "haut"], ["base"])
    _histoire(root, "Histoire : « 100 » — [p. 1]")


def parcours_ordre_inverse(root):
    """Le premier parcours suppose base, que seul le second raconte."""
    _parcours(root, ["milieu", "haut"], ["base"], slug="un", ordre=1)
    _parcours(root, ["base"], [], slug="deux", ordre=2, fiches=False)


def parcours_ordre_juste(root):
    _parcours(root, ["base"], [], slug="un", ordre=1)
    _parcours(root, ["milieu", "haut"], ["base"], slug="deux", ordre=2, fiches=False)


def parcours_fiche_hors_recit(root):
    _parcours(root, ["haut"], ["milieu"])        # base : ni étape ni rôle


def parcours_hors_recit_declaree(root):
    _parcours(root, ["haut"], ["milieu"])
    cy = root / "courses" / "aa" / "course.yml"
    cy.write_text(cy.read_text(encoding="utf-8") + "hors_parcours:\n  aa/base: une digression\n",
                  encoding="utf-8", newline="\n")


def _sceller(root, fil, scelle="2026-09-01"):
    (root / "courses" / "aa" / "parcours" / "fil.yml").write_text(
        "scelle: '%s'\nfil: [%s]\n" % (scelle, ", ".join("aa/" + x for x in fil)),
        encoding="utf-8", newline="\n")


def fil_decoupe(root):
    """Un parcours base → milieu → haut, découpé en deux parcours consécutifs."""
    _parcours(root, ["base"], [], slug="un", ordre=1)
    _parcours(root, ["milieu", "haut"], ["base"], slug="deux", ordre=2, fiches=False)
    _sceller(root, ["base", "milieu", "haut"])


def fil_retire(root):
    _parcours(root, ["milieu", "haut"], ["base"])
    _sceller(root, ["base", "milieu", "haut"])          # base n'est plus une étape


def fil_reordonne(root):
    _parcours(root, ["base"], [], slug="un", ordre=2)
    _parcours(root, ["milieu", "haut"], ["base"], slug="deux", ordre=1, fiches=False)
    _sceller(root, ["base", "milieu", "haut"])


def fil_refonte_declaree(root):
    fil_retire(root)
    cy = root / "courses" / "aa" / "course.yml"
    cy.write_text(cy.read_text(encoding="utf-8")
                  + "refonte_du_recit:\n- date: '2026-09-02'\n  raison: essai\n",
                  encoding="utf-8", newline="\n")


def cours_sans_parcours(root):
    ecrire(root, "aa", [dict(slug="base", nom="Base")])


def parcours_desordre(root):
    _parcours(root, ["haut", "milieu"], ["base"])


def parcours_sans_rattachement(root):
    _parcours(root, ["milieu", "haut"], [])


def parcours_rattachement_inutile(root):
    _parcours(root, ["base", "milieu", "haut"], ["base"])


def lois_divergentes(root):
    """Les quatre documents de loi vivent en double, racine et proj/. Un texte modifié
    d'un seul côté se découvre le jour où les deux se contredisent."""
    ecrire(root / "proj", "aa", [dict(slug="x", nom="Un")])
    (root / "CLAUDE.md").write_text("la loi\n", encoding="utf-8", newline="\n")
    (root / "proj" / "CLAUDE.md").write_text("la loi, retouchée\n",
                                             encoding="utf-8", newline="\n")


def lois_identiques(root):
    lois_divergentes(root)
    (root / "proj" / "CLAUDE.md").write_text("la loi\n", encoding="utf-8", newline="\n")


SCRIPT_FIG = '''import sys
sys.stdout.write("<svg xmlns=\'http://www.w3.org/2000/svg\'><title>t</title></svg>\\n")
'''


def _fig(root, code="aa", svg=None, script=True, citee=True):
    d = root / "courses" / code / "figures"
    d.mkdir(parents=True, exist_ok=True)
    if script:
        (d / "f.py").write_text(SCRIPT_FIG, encoding="utf-8", newline="\n")
    (d / "f.svg").write_text(
        svg if svg is not None
        else "<svg xmlns='http://www.w3.org/2000/svg'><title>t</title></svg>\n",
        encoding="utf-8", newline="\n")


def _retrouver(corps):
    return "\n## Retrouver la formule\n" + corps + "\n"


def retrouver_ok(root):
    corps = ("![Une l\u00e9gende.](figures/f.svg) [p. 1]\n\n"
             "On raisonne. [p. 1]\n\n$$a=b$$ [p. 1]")
    ecrire(root, "aa", [dict(slug="x", nom="Un", chemin=_retrouver(corps))])
    _fig(root)


def retrouver_sans_formule(root):
    """Le raisonnement s'arrête avant la formule qu'il devait retrouver."""
    corps = "On raisonne. [p. 1]\n\n$$a=b$$ [p. 1]\n\nEt on conclut en prose. [p. 1]"
    ecrire(root, "aa", [dict(slug="x", nom="Un", chemin=_retrouver(corps))])


def retrouver_figure_apres(root):
    """La figure arrive après le raisonnement qu'elle devait porter."""
    corps = ("On raisonne. [p. 1]\n\n![Une l\u00e9gende.](figures/f.svg) [p. 1]\n\n"
             "$$a=b$$ [p. 1]")
    ecrire(root, "aa", [dict(slug="x", nom="Un", chemin=_retrouver(corps))])
    _fig(root)


def fig_ok(root):
    appel = "\n![Une l\u00e9gende.](figures/f.svg) [p. 1]\n"
    ecrire(root, "aa", [dict(slug="x", nom="Un", chemin=appel)])
    _fig(root)


def fig_derive(root):
    """Le SVG a été retouché à la main : on ne sait plus le refaire."""
    fig_ok(root)
    (root / "courses" / "aa" / "figures" / "f.svg").write_text(
        "<svg xmlns='http://www.w3.org/2000/svg'><title>autre</title></svg>\n",
        encoding="utf-8", newline="\n")


def fig_absente(root):
    appel = "\n![Une l\u00e9gende.](figures/manquante.svg) [p. 1]\n"
    ecrire(root, "aa", [dict(slug="x", nom="Un", chemin=appel)])
    _fig(root)


def fig_sans_script(root):
    fig_ok(root)
    (root / "courses" / "aa" / "figures" / "f.py").unlink()


def fig_orpheline(root):
    ecrire(root, "aa", [dict(slug="x", nom="Un")])
    _fig(root)


def projection():
    """A11 garantit qu'effacer tout ce qui est marqué « ajout » laisse un objet cohérent.
    Une figure marquée ainsi doit donc porter la classe que la feuille de style masque —
    sinon le bouton « masquer les ajouts » laisse un dessin que le cours ne contient pas.
    Oublié à l'écriture du bloc figure, vu à l'écran le 2026-09-21."""
    import build                                         # noqa: E402
    racine = Path(tempfile.mkdtemp())
    try:
        d = racine / "courses" / "aa" / "figures"
        d.mkdir(parents=True)
        (d / "f.svg").write_text("<svg/>", encoding="utf-8", newline="\n")
        ctx = {"m": {"racine": racine, "N": {}, "exercices": {}}, "rel": "", "code": "aa"}
        for marque, attendu in (("ajout", True), ("p. 1", False)):
            html = build._figure(["![Une l\u00e9gende.](figures/f.svg) [%s]" % marque], ctx)
            vu = 'class="fig is-ajout"' in html
            ok = vu is attendu
            print(("  ok   " if ok else "  RAT\u00c9 ")
                  + "figure marqu\u00e9e [%s] %s masqu\u00e9e avec les ajouts"
                  % (marque, "est" if attendu else "n'est pas"))
            if not ok:
                ECHECS.append("projection [%s]" % marque)
    finally:
        shutil.rmtree(racine, ignore_errors=True)


def main():
    print("homonymie")
    cas("nom identique entre deux cours, non déclaré → signalé",
        "homonymie non déclarée", hom_non_declaree)
    cas("nom identique entre deux cours, déclaré → silence",
        "homonymie non déclarée", hom_declaree, doit_apparaitre=False)
    cas("alias identique dans le même cours → erreur",
        "un cours ne nomme pas deux notions de la même façon", hom_meme_cours)

    print("collision de symbole")
    cas("symbole dans deux registres, non déclaré → signalé",
        "collision non déclarée", sym_non_declare)
    cas("symbole dans deux registres, déclaré → silence",
        "collision non déclarée", sym_declare, doit_apparaitre=False)
    cas("déclaration qui n'en nomme que deux sur trois → signalé",
        "collision non déclarée pour cc", sym_declare_a_moitie)
    cas("déclaration nommant un cours inexistant → erreur",
        "qui n'existe pas", cours_fantome)

    print("symboles laissés sans explication française")
    cas("fiche porteuse sans la rubrique → signalée",
        "« Ce que les symboles modélisent » à écrire", sym_sans_rubrique)
    cas("rubrique qui en oublie un → signalée",
        "ne nomme pas 1 symbole(s) du registre", sym_rubrique_partielle)
    cas("rubrique qui les nomme tous → silence",
        "Ce que les symboles modélisent", sym_rubrique_complete, doit_apparaitre=False)

    print("socle qui grandit sous une fiche déjà écrite")
    cas("la fiche elle-même → signalée",
        "aa/milieu: « Le chemin jusqu'ici » ne nomme pas", socle_grandit)
    cas("sa descendance aussi → signalée",
        "aa/aval: « Le chemin jusqu'ici » ne nomme pas", socle_grandit)

    print("documents de loi en double")
    cas("une copie retouchée seule → erreur",
        "ne portent plus le même texte", lois_divergentes, sous="proj")
    cas("les deux copies identiques → silence",
        "ne portent plus le même texte", lois_identiques, doit_apparaitre=False, sous="proj")

    print("retrouver la formule")
    cas("figure, raisonnement, formule → silence",
        "Retrouver la formule", retrouver_ok, doit_apparaitre=False)
    cas("raisonnement qui ne finit pas sur la formule → erreur",
        "ne finit pas sur la formule", retrouver_sans_formule)
    cas("figure posée après le raisonnement → erreur",
        "la figure vient après le raisonnement", retrouver_figure_apres)

    print("figures")
    cas("figure conforme à son script → silence",
        "figures", fig_ok, doit_apparaitre=False)
    cas("SVG retouché à la main → erreur",
        "ne correspond plus", fig_derive)
    cas("fiche appelant une figure absente → erreur",
        "qui n'existe pas", fig_absente)
    cas("SVG sans script → erreur",
        "sans script", fig_sans_script)
    cas("SVG qu'aucune fiche n'appelle → signalé",
        "n'est appelée par aucune fiche", fig_orpheline)

    print("parcours (A14–A17)")
    cas("parcours conforme → silence",
        "parcours", parcours_ok, doit_apparaitre=False)
    cas("transition qui redit la définition de sa fiche → signalée",
        "la transition redit", parcours_paraphrase)
    cas("point de départ sans aucun chiffre → signalé",
        "sans aucun chiffre", parcours_depart_abstrait)
    cas("citation absente du point de départ → erreur",
        "pas pris mot pour mot", parcours_citation_absente)
    cas("citation qui coupe une formule → erreur",
        "coupe une formule", parcours_citation_coupe_formule)
    cas("citation d'une suite qu'une étape suivante racontera → erreur",
        "pas pris mot pour mot", parcours_cite_suite_future)
    cas("citation d'une suite racontée à cette étape → silence",
        "pas pris mot pour mot", parcours_cite_suite_racontee, doit_apparaitre=False)
    cas("ligne « Histoire : » sans phrase → erreur",
        "sans phrase de lien", parcours_histoire_sans_lien)
    cas("étape placée avant son prérequis → erreur",
        "arrive avant son prérequis", parcours_desordre)
    cas("prérequis supposé sans rôle dans l'histoire → erreur",
        "n'est pas rattaché à l'histoire", parcours_sans_rattachement)
    cas("rattachement d'une fiche qu'aucune étape ne suppose → erreur",
        "dont aucune étape ne dépend directement", parcours_rattachement_inutile)
    cas("parcours qui suppose ce qu'un parcours suivant raconte → erreur",
        "ne raconte qu'ensuite", parcours_ordre_inverse)
    cas("parcours lus dans le bon ordre → silence",
        "ne raconte qu'ensuite", parcours_ordre_juste, doit_apparaitre=False)
    cas("fiche sans place dans aucun parcours → signalée",
        "aa/base: n'a de place dans aucun parcours", parcours_fiche_hors_recit)
    cas("fiche hors récit déclarée avec sa raison → silence",
        "n'a de place dans aucun parcours", parcours_hors_recit_declaree, doit_apparaitre=False)
    cas("parcours découpé en deux consécutifs → le fil est contenu, silence",
        "n'est plus", fil_decoupe, doit_apparaitre=False)
    cas("étape retirée du récit scellé → erreur",
        "E A17", fil_retire)
    cas("parcours réordonnés → erreur",
        "E A17", fil_reordonne)
    cas("refonte déclarée → avertissement, pas erreur",
        "E A17", fil_refonte_declaree, doit_apparaitre=False)
    cas("cours sans aucun parcours → compté en dette",
        "le cours n'est raconté nulle part", cours_sans_parcours)

    print("projection « masquer les ajouts » (A11)")
    projection()

    print()
    if ECHECS:
        print("%d garde-fou(s) muet(s) : %s" % (len(ECHECS), ", ".join(ECHECS)))
        sys.exit(1)
    print("tous les garde-fous se déclenchent")


if __name__ == "__main__":
    main()
