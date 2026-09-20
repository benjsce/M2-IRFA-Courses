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

## État (2026-09-20)

Deux cours, **123 fiches**, et **aucune dette** : chaque élément des sources a reçu son
image, chaque fiche à formule porte son exemple minimal et son geste de calcul, aucun lien
ne pointe vers une notion non écrite.

| cours | fiches | principes | abstraites | inventaire | source |
|---|---|---|---|---|---|
| `fpp` — Financial Products (Gaussel) | 55 | 3 | 10 | 93 éléments, couverts | poly, 17 p. |
| `dup` — Decision under Uncertainty (Qu) | 68 | 4 | 6 | 158 éléments, couverts | 3 jeux de slides, 153 slides |

Le validateur passe à 0 erreur. Les 4 avertissements restants sont stylistiques
(« Ce que c'est » en plusieurs phrases), aucun n'est de la dette.

Les deux réserves de l'amorçage sont levées : les références ont été auditées ligne à
ligne contre le poly (rapport `2026-09-20-fpp-2.md`), et les exemples minimaux sont
écrits. Depuis, `validate.py` refuse un « Exemple minimal » laissé en dette — c'est une
**erreur**, pas un avertissement, conformément à SPEC-INGESTION étape 3.

## Ce qui reste ouvert

Rien n'est en dette, mais cinq décisions attendent l'utilisateur ; elles sont posées en
fin de chaque rapport, avec une recommandation.

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
