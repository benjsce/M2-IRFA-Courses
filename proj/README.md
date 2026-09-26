# notions — base de notions par cours (M2 IRFA)

Une fiche par notion, deux relations, un validateur, un site généré. Les règles sont dans
`SPEC-MODELE.md` (modèle et axiomes), `SPEC-INGESTION.md` (protocole hebdomadaire),
`SPEC-SITE.md` (site et générateur). `CLAUDE.md` est le contrat d'exploitation de Claude Code.

## Démarrage

```
pip install -r requirements.txt
python tools/validate.py          # doit afficher 0 erreur (des avertissements de dette sont normaux)
python tools/build.py             # régénère site/ ; refuse de construire sur un graphe invalide
```

`build.py` accepte `--offline` (copie MathJax dans `site/vendor/`, pour un usage sans
réseau) et `--course <code>` (ne régénère qu'un cours). Il exécute lui-même le validateur
et le test de disposition, et s'arrête si l'un des deux échoue.

## Arborescence

```
CLAUDE.md  SPEC-MODELE.md  SPEC-INGESTION.md  SPEC-SITE.md
schema/            gabarits (fiche, cours, notation, inventaire, exercice)
courses/<code>/    course.yml · notation.yml · inventaire.yml · a-venir.yml
                   notions/*.md · exercices/*.md · sources/
tools/             validate.py · build.py · tests/test_layout.py
site/              généré ; publié sur GitHub Pages
rapports/          un rapport par ingestion
```

## État (2026-09-26)

Cinq cours. `fpp` a été vidé le 2026-09-26, puis réécrit de zéro le 2026-09-27 (rapport
`2026-09-27-fpp.md`) ; ses exercices restent à rédiger.

| cours | fiches | principes | abstraites | inventaire | source |
|---|---|---|---|---|---|
| `fpp` — Financial Products (Gaussel) | 54 | 3 | 2 | 127 éléments, dont 24 exercices à venir | poly, 16 p. ; livre d'exercices, 28 p. |
| `dup` — Decision under Uncertainty (Qu) | 86 | 4 | 7 | 225 éléments, couverts | 4 jeux de slides, 220 slides |
| `dss` — Data Science Software (Hassani) | 76 | 5 | 5 | 237 éléments, couverts | slides, 237 slides |
| `pfo` — Python for Finance and Optimisation (Mrad) | 45 | 3 | 5 | 126 éléments, couverts | poly, chapitres 1 à 3, 56 p. |
| `ods` — Optimization for Data Science (Vaiter, Gramfort) | 46 | 1 | 0 | 97 éléments, couverts | notes, 14 p. ; slides, 32 ; 5 notebooks |

Le validateur passe à 0 erreur. Les avertissements restants sont la dette de `fpp` : les
24 exercices et sections d'exercices de son livre, inventoriés mais pas encore rédigés.

## Ce qui reste ouvert

Le 2026-09-20, cinq décisions attendaient l'utilisateur ; elles sont posées en fin de
chaque rapport, avec une recommandation.

*Au 2026-09-26, tout ce qui suit et touche `fpp` est clos par sa refonte (rapport
`2026-09-26-fpp-13.md`) : `fpp/couverture` et les contradictions de son poly ne sont plus
ouverts. Ce qui touche `dup` reste tel qu'écrit le 2026-09-20.*

1. **Trois principes ont été créés** — `fpp/couverture`, `dup/courbure-de-l-utilite`,
   `dup/principe-d-unanimite`. Chacun s'appuie sur une phrase de la source, aucun n'y est
   présenté comme un principe. Ce sont eux qui permettent les abstractions : sans eux,
   A4 interdit tout arbre sur ces branches.
2. **Neuf contradictions de source** sont documentées et non arbitrées — dont la table des
   grecques du §8.2 de `fpp`, qui écrit le vega avec la fonction de répartition là où la
   densité est attendue.
3. **`dup/ordre-concave` n'a qu'un parent possible** : il est sous `accroissement-de-risque`
   plutôt que sous une `dominance-stochastique` à créer.
4. **Le recouvrement L1/L2 de `dup`** a été tranché en faveur de L2, plus complet, pour les
   slides communes.
5. **Deux abstractions restent en attente** dans `dup`, faute de paramètre générateur
   commun : `dominance-stochastique` et `mesure-de-risque`.
