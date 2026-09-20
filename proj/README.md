# notions — base de notions par cours (M2 IRFA)

Une fiche par notion, deux relations, un validateur, un site généré. Les règles sont dans
`SPEC-MODELE.md` (modèle et axiomes), `SPEC-INGESTION.md` (protocole hebdomadaire),
`SPEC-SITE.md` (site et générateur). `CLAUDE.md` est le contrat d'exploitation de Claude Code.

## Démarrage

```
pip install -r requirements.txt
python tools/validate.py          # doit afficher 0 erreur (des avertissements de dette sont normaux)
python tools/build.py             # à implémenter par Claude Code selon SPEC-SITE.md
```

## Arborescence

```
CLAUDE.md  SPEC-MODELE.md  SPEC-INGESTION.md  SPEC-SITE.md
schema/            gabarits (fiche, cours, notation, inventaire, exercice)
courses/<code>/    course.yml · notation.yml · inventaire.yml · a-venir.yml
                   notions/*.md · exercices/*.md · sources/
tools/             validate.py (fait) · build.py (à faire) · tests/test_layout.py (à faire)
site/              généré ; publié sur GitHub Pages
rapports/          un rapport par ingestion
```

## État de l'amorçage (2026-09-20)

`courses/fpp/` contient 25 fiches couvrant les sections 2 à 5 du poly de Gaussel, un
registre de 26 symboles, un inventaire de 90 éléments (35 traités, 55 à venir), et trois
exercices résolus. Le validateur passe sans erreur.

Deux réserves à connaître sur l'amorçage :

1. **Les références de la rubrique « Ce que c'est » et « Ce qui la définit » sont celles
   de la fiche entière**, pas d'un paragraphe précis. Elles sont correctes au niveau de la
   section mais n'ont pas été vérifiées ligne à ligne. La première ingestion doit les
   auditer contre le poly (SPEC-INGESTION, étape 2). Tout ce qui est de l'opérateur est
   marqué `[ajout]`, en particulier toutes les rubriques « Cesse d'être valide quand »
   sauf six.
2. **« Exemple minimal » et « Geste de calcul type » sont à venir** sur les 15 fiches qui
   ont une forme. C'est la dette la plus utile à résorber, exercice par exercice.

## Premier travail pour Claude Code

Dans l'ordre : (1) lire `CLAUDE.md` puis les trois specs ; (2) écrire `tools/build.py` et
`tools/tests/test_layout.py` selon `SPEC-SITE.md`, sans toucher à `courses/` ; (3)
produire `site/` et vérifier qu'il s'ouvre en `file://` ; (4) seulement ensuite, première
ingestion : audit des références de l'amorçage, puis section 1 du poly.
