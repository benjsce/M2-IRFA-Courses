#!/usr/bin/env python3
"""
recit.py — un parcours lu d'un seul tenant, comme l'étudiant le lit (SPEC-MODELE §8.6).

Imprime, sans marqueurs ni ids, le point de départ, puis pour chaque étape la transition,
la suite et la phrase de l'histoire, enfin le point d'arrivée. C'est le texte du test de
lecture : s'il ne se lit pas d'une traite, sans point d'arrêt, le parcours est à reprendre.

Usage : python tools/recit.py <code> [<parcours>]
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


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    code = sys.argv[1]
    dossier = RACINE / "courses" / code / "parcours"
    fichiers = sorted(dossier.glob("*.md"),
                      key=lambda p: int(re.search(r"^ordre:\s*(\d+)", p.read_text(encoding="utf-8"), re.M).group(1)))
    if len(sys.argv) > 2:
        fichiers = [dossier / f"{sys.argv[2]}.md"]
    sys.stdout.write("\n".join(recit(f) for f in fichiers))


if __name__ == "__main__":
    main()
