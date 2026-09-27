#!/usr/bin/env python3
"""
recit.py — un parcours lu d'un seul tenant, comme l'étudiant le lit (SPEC-MODELE §8.6).

Imprime, sans marqueurs ni ids, le point de départ, puis pour chaque étape la transition,
la suite et la phrase de l'histoire, enfin le point d'arrivée. C'est le texte du test de
lecture : s'il ne se lit pas d'une traite, sans point d'arrêt, le parcours est à reprendre.

Avec --questions, imprime pour chaque étape les mots en gras en face du nom de la fiche :
« mots en gras » ? → Nom. C'est le test de la notion (SPEC-MODELE §8.5) : la réponse,
explicite ou implicite, à la question que posent les mots en gras doit être la notion de la
fiche. Le validateur ne peut pas lire le sens ; ce tableau se lit en une minute.

Usage : python tools/recit.py [--questions] <code> [<parcours>]
Dépendance : aucune.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
MARQUEUR = re.compile(r"\s*\[[^\[\]]*\]\s*$")


def net(s):
    return " ".join(MARQUEUR.sub("", l.strip()) for l in s.strip().splitlines() if l.strip())


def recit(chemin):
    t = chemin.read_text(encoding="utf-8")
    titre = re.search(r"^titre:\s*(.+)$", t, re.M).group(1)
    ordre = re.search(r"^ordre:\s*(\d+)", t, re.M).group(1)
    out = [f"=== {ordre}. {titre}", ""]
    dep = t.split("## Point de départ\n", 1)[1].split("\n## ", 1)[0]
    out += ["DÉPART  " + net(dep), ""]
    for m in re.finditer(r"^(\d+)\. (\S+)\n((?:   .*\n?)+)", t, re.M):
        lignes = [l.strip() for l in m.group(3).splitlines() if l.strip()]
        out.append(f"{m.group(1)}. [{m.group(2)}]  {net(lignes[0])}")
        for l in lignes[1:]:
            if l.startswith("Suite :"):
                out.append("   SUITE  " + net(l[len("Suite :"):]))
            elif l.startswith("Histoire :"):
                out.append("   RÉPONSE  " + net(l[len("Histoire :"):]))
        out.append("")
    if "## Point d'arrivée\n" in t:
        arr = t.split("## Point d'arrivée\n", 1)[1].split("\n## ", 1)[0]
        out += ["ARRIVÉE  " + net(arr), ""]
    return "\n".join(out)


def nom_de(i):
    code, slug = i.split("/", 1)
    t = (RACINE / "courses" / code / "notions" / f"{slug}.md").read_text(encoding="utf-8")
    return re.search(r"^nom:\s*(.+)$", t, re.M).group(1).strip()


def questions(chemin):
    t = chemin.read_text(encoding="utf-8")
    titre = re.search(r"^titre:\s*(.+)$", t, re.M).group(1)
    ordre = re.search(r"^ordre:\s*(\d+)", t, re.M).group(1)
    out = [f"=== {ordre}. {titre}"]
    for m in re.finditer(r"^(\d+)\. (\S+)\n((?:   .*\n?)+)", t, re.M):
        h = [l.strip() for l in m.group(3).splitlines() if l.strip().startswith("Histoire :")]
        tete = h[0][len("Histoire :"):].split(" — ", 1)[0] if h else ""
        cits = re.findall(r"«\s*(.*?)\s*»", tete)
        suite = any(l.strip().startswith("Suite :") for l in m.group(3).splitlines())
        gras = " | ".join(f"« {c} »" for c in cits) or "(aucune citation)"
        out.append(f"{m.group(1):>3}. {'S' if suite else ' '} {gras} ? → {nom_de(m.group(2))}")
    return "\n".join(out) + "\n"


def main():
    args = [a for a in sys.argv[1:] if a != "--questions"]
    if not args:
        sys.exit(__doc__)
    code = args[0]
    dossier = RACINE / "courses" / code / "parcours"
    fichiers = sorted(dossier.glob("*.md"),
                      key=lambda p: int(re.search(r"^ordre:\s*(\d+)", p.read_text(encoding="utf-8"), re.M).group(1)))
    if len(args) > 1:
        fichiers = [dossier / f"{args[1]}.md"]
    lire = questions if "--questions" in sys.argv else recit
    sys.stdout.write("\n".join(lire(f) for f in fichiers))


if __name__ == "__main__":
    main()
