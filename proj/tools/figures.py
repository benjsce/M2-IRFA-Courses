#!/usr/bin/env python3
"""
figures.py — chaque Forme en face de la légende de sa figure (SPEC-MODELE §2.4, règle 5).

Quand c'est possible, une figure fait retrouver la Forme de sa fiche : ses termes, dans son
sens, et non seulement le résultat qu'on en tire. Le validateur ne peut pas juger qu'un
dessin mène à une formule ; ce tableau se relit en quelques minutes, fiche par fiche.

Usage : python tools/figures.py <code> [<slug>]
Dépendance : aucune.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
MARQUEUR = re.compile(r"\s*\[[^\[\]]*\]\s*$")


def rubrique(t, nom):
    m = re.search(r"^## %s\n(.*?)(?=^## |\Z)" % re.escape(nom), t, re.M | re.S)
    return m.group(1).strip() if m else ""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    code = sys.argv[1]
    dossier = RACINE / "courses" / code / "notions"
    fiches = sorted(dossier.glob("*.md"))
    if len(sys.argv) > 2:
        fiches = [dossier / f"{sys.argv[2]}.md"]
    for f in fiches:
        t = f.read_text(encoding="utf-8")
        figs = re.findall(r"!\[(.*?)\]\((figures/[^)]+)\)", t)
        if not figs:
            continue
        nom = re.search(r"^nom:\s*(.+)$", t, re.M).group(1).strip()
        forme = " ".join(MARQUEUR.sub("", l).strip() for l in rubrique(t, "Forme").splitlines())
        print(f"=== {code}/{f.stem} — {nom}")
        print(f"FORME    {forme or '(aucune)'}")
        for legende, chemin in figs:
            print(f"FIGURE   {chemin} : {legende}")
        print()


if __name__ == "__main__":
    main()
