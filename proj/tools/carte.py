#!/usr/bin/env python3
"""
carte.py — la base entière en quelques pages, pour ne pas relire tous les cours.

Une session travaille sur un cours. Relire les fiches des autres coûte des dizaines de
milliers de tokens et ne sert qu'à une chose : reconnaître un lien — une notion déjà
écrite ailleurs (pfo s'appuie sur fpp/volatilite), un homonyme, un symbole en collision.
Pour cela une ligne par fiche suffit : identifiant, nom, alias, symbole, et la phrase
« Ce que c'est ». La carte donne cette ligne pour toute la base, et le détail du graphe
pour le seul cours travaillé. On n'ouvre ensuite une fiche étrangère que si la carte a
désigné un lien. Voir LECTURE.md.

N'écrit rien, ne décide rien.

Usage :
  python tools/carte.py                 # vue d'ensemble : cours, tailles, parcours, rapports
  python tools/carte.py pfo             # le cours pfo en détail, et les autres en une ligne
  python tools/carte.py pfo --seul      # le cours pfo seulement, sans les autres

Dépendance : pyyaml.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import lire_fiche, lire_parcours, copie_de_conflit      # noqa: E402

import yaml

for _f in (sys.stdout, sys.stderr):            # cp1252 sous PowerShell
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

MARQ = re.compile(r"\s*\[[^\[\]]+\]\s*$")


def charger(root: Path):
    cours = {}
    for cdir in sorted(p for p in (root / "courses").iterdir() if p.is_dir()):
        meta = yaml.safe_load((cdir / "course.yml").read_text(encoding="utf-8")) or {}
        fiches = {}
        for f in sorted((cdir / "notions").glob("*.md")):
            if copie_de_conflit(f):
                continue
            m, secs = lire_fiche(f)
            cc = MARQ.sub("", dict(secs).get("Ce que c'est", "")).strip()
            fiches[m["id"]] = dict(meta=m, cc=cc)
        parcours = []
        pdir = cdir / "parcours"
        if pdir.is_dir():
            for f in sorted(pdir.glob("*.md")):
                if copie_de_conflit(f):
                    continue
                m, _, et, av = lire_parcours(f)
                parcours.append((m.get("ordre", 999), f.stem, m.get("titre", ""),
                                 [i for _, i, _ in et], [i for i, _ in av]))
        parcours.sort()
        inv = yaml.safe_load((cdir / "inventaire.yml").read_text(encoding="utf-8")) or {}
        cours[cdir.name] = dict(meta=meta, fiches=fiches, parcours=parcours,
                                inventaire=inv.get("elements", []) or [])
    return cours


def rapports(root: Path, code=None):
    """(rapports du dernier jour, dernier rapport du cours). Le nom ne dit pas l'ordre de
    deux sujets le même jour, seulement celui des sessions d'un même sujet : `dup.md`,
    puis `dup-2.md`… On trie donc par date et par suffixe, et le dernier jour est rendu
    en entier."""
    rx = re.compile(r"^(\d{4}-\d\d-\d\d)-(.+?)(?:-(\d+))?\.md$")
    tous = []
    for r in (root / "rapports").glob("*.md"):
        mo = rx.match(r.name)
        if mo and not copie_de_conflit(r):
            tous.append((mo.group(1), mo.group(2), int(mo.group(3) or 1), r.name))
    tous.sort()
    jour = tous[-1][0] if tous else None
    derniers = ", ".join(n for d, _, _, n in tous if d == jour) or "—"
    du_cours = [n for _, suj, _, n in tous if suj == code]
    return derniers, (du_cours[-1] if du_cours else "—")


def court(s, n):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def ensemble(root, cours):
    print("# La base en un coup d'œil\n")
    print("| cours | titre | fiches | parcours | inventaire à venir | dernier rapport du cours |")
    print("|---|---|---|---|---|---|")
    for code, c in cours.items():
        av = sum(1 for e in c["inventaire"] if "a_venir" in e)
        print("| %s | %s | %d | %d | %d | %s |" % (code, court(c["meta"].get("titre", ""), 50),
              len(c["fiches"]), len(c["parcours"]), av, rapports(root, code)[1]))
    print("\nrapports du dernier jour, tous sujets : " + rapports(root)[0])
    liens = []
    for code, c in cours.items():
        for i, f in c["fiches"].items():
            for d in f["meta"].get("construite_a_partir_de") or []:
                if not str(d).startswith(code + "/"):
                    liens.append("%s → %s" % (i, d))
    print("\n## Arêtes entre cours\n")
    print("\n".join("- " + l for l in liens) if liens else "aucune")


def detail(root, cours, code, seul):
    c = cours[code]
    m = c["meta"]
    print("# %s — %s (%s)\n" % (code, m.get("titre", ""), m.get("enseignant", "")))
    print("sources : " + ", ".join(str(s.get("fichier")) for s in m.get("sources") or []))
    print("dépend de : " + (", ".join(m.get("depend_de") or []) or "aucun cours"))
    d, dc = rapports(root, code)
    print("rapports à lire : %s (dernier du cours) · du dernier jour : %s\n" % (dc, d))

    print("## Fiches — id · type · nom · symbole · cas de · construite à partir de\n")
    for i, f in sorted(c["fiches"].items()):
        mt = f["meta"]
        dep = ", ".join(x.replace(code + "/", "") for x in mt.get("construite_a_partir_de") or [])
        print("- %s · %s%s · %s%s%s%s" % (
            i.split("/", 1)[1], mt.get("type", "?"), " (ajout)" if mt.get("statut") == "ajout" else "",
            mt.get("nom", ""), (" · " + str(mt["symbole"])) if mt.get("symbole") else "",
            (" · cas de " + mt["cas_de"].replace(code + "/", "")) if mt.get("cas_de") else "",
            (" · ← " + dep) if dep else ""))

    print("\n## Parcours\n")
    if not c["parcours"]:
        print("aucun")
    for o, slug, titre, et, av in c["parcours"]:
        print("%s. %s — %s\n   étapes : %s%s" % (o, slug, titre,
              " → ".join(x.split("/", 1)[1] for x in et),
              ("\n   à savoir avant : " + ", ".join(av)) if av else ""))
    hors = m.get("hors_parcours") or {}
    if hors:
        print("   hors parcours : " + ", ".join(hors))

    inv = c["inventaire"]
    k = {x: sum(1 for e in inv if x in e) for x in ("notion", "absorbe", "exclu", "a_venir")}
    print("\n## Inventaire\n\n%d éléments : %d notions, %d absorbés, %d exclus, %d à venir ; "
          "dernier élément : %s" % (len(inv), k["notion"], k["absorbe"], k["exclu"], k["a_venir"],
                                    inv[-1].get("ref") if inv else "—"))

    if seul:
        return
    print("\n## Les autres cours, une ligne par fiche\n")
    print("id · nom · alias · symbole · ce que c'est. Une fiche ne s'ouvre que si cette ligne "
          "suggère un lien : même objet, homonyme, symbole partagé.\n")
    for autre, ca in cours.items():
        if autre == code:
            continue
        print("### %s\n" % autre)
        for i, f in sorted(ca["fiches"].items()):
            mt = f["meta"]
            al = ", ".join(str(a) for a in (mt.get("alias") or [])[:3])
            print("- %s · %s%s%s · %s" % (i, mt.get("nom", ""), (" (" + al + ")") if al else "",
                  (" · " + str(mt["symbole"])) if mt.get("symbole") else "", court(f["cc"], 130)))
        print()


def main():
    ap = argparse.ArgumentParser(description="la base en quelques pages (voir LECTURE.md)")
    ap.add_argument("cours", nargs="?")
    ap.add_argument("--seul", action="store_true", help="sans les autres cours")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    root = Path(a.root)
    cours = charger(root)
    if not a.cours:
        ensemble(root, cours)
    elif a.cours not in cours:
        print("cours inconnu : %s (connus : %s)" % (a.cours, ", ".join(cours)), file=sys.stderr)
        return 1
    else:
        detail(root, cours, a.cours, a.seul)
    return 0


if __name__ == "__main__":
    sys.exit(main())
