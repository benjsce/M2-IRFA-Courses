# SPEC-INGESTION — le protocole hebdomadaire

Ce protocole s'applique chaque fois que du matériau nouveau arrive : un chapitre de poly,
des notes manuscrites, des slides, une feuille d'exercices, un corrigé. Il se suit dans
l'ordre. Chaque étape produit une trace qui va dans le rapport final.

Le danger de ce projet n'est pas l'erreur ponctuelle, c'est la **réécriture zélée** de ce
qui existe déjà. Tout le protocole est construit pour la rendre visible. Rien ne peut la
rendre impossible ; le rapport est la seule défense.

## Étape 0 — État initial

```
python tools/validate.py
```
Doit passer. Lire le dernier rapport de `rapports/` : dette en cours, abstractions en
attente, questions ouvertes. Noter dans le nouveau rapport ce qui a changé depuis.

## Étape 1 — Inventaire de la source (A13)

Lire le matériau nouveau **en entier avant d'écrire quoi que ce soit**. Ajouter à
`inventaire.yml` chaque élément indexable, dans l'ordre de la source :

- toute définition, tout théorème, proposition, lemme, corollaire, remarque numérotée ;
- toute équation numérotée ;
- tout exemple ou exercice numéroté ;
- tout titre de section et de sous-section.

À ce stade, chaque nouvel élément reçoit `a_venir` avec la date du jour. Aucune fiche n'est
écrite. Le rapport reproduit la liste des éléments ajoutés à l'inventaire : **c'est la
liste que l'utilisateur audite**, la seule où une omission peut passer sans être vue
ensuite. Elle doit être courte, lisible, dans l'ordre du document.

Mettre à jour `notation.yml` avec chaque symbole que la source définit ou emploie pour
la première fois, avec sa référence de première occurrence. Signaler dans le rapport tout
symbole qui entre en collision avec un autre cours.

## Étape 2 — Confrontation à l'existant

Cette étape se prépare avec `tools/confronter.py`, qui n'écrit rien et ne décide rien :
il imprime la liste de ce qui est à examiner. Quatre questions, quatre appels.

```
python tools/confronter.py --refs <code> refs.txt   # la suite d'un cours déjà ouvert
python tools/confronter.py --noms "<candidat>" …    # des noms, avant toute fiche
python tools/confronter.py --cours <code>           # un cours entier contre les autres
python tools/confronter.py --aval <id> …            # les chemins que je vais périmer
```

Le premier appel est le seul exact : il compare des références de source à l'inventaire,
et l'inventaire est exhaustif par A13. Pour la suite d'un cours, c'est lui qui tranche.
Les deux suivants sont approchés — ils rapprochent par les mots, et un cours peut nommer
autrement ce qu'un autre a déjà dit. Ils réduisent ce qu'il reste à lire ; ils ne
dispensent pas de le lire.

**Attention particulière** : une notion nouvelle qui entre dans le socle d'une fiche
existante rend le « chemin jusqu'ici » de cette fiche incomplet. Depuis que la rubrique
doit nommer chaque notion de son socle, le validateur le signale — sur la fiche *et* sur
toute sa descendance par $D^{-1}$, puisque le socle de chacune a grandi aussi. Le
signalement arrive une fois l'arête posée ; `--aval` donne la liste avant.

Pour chaque élément inventorié, chercher s'il correspond à une notion existante — par
`nom`, par `alias`, par `symbole`, et par le sens. Les trois premières routes sont
calculées par l'outil, la quatrième reste à faire. Trois issues :

- **Il existe déjà.** L'élément prend `absorbe: <id>` ou `notion: <id>` s'il en est la
  source principale. Si la fiche existante doit changer (précision, référence, limite
  nouvelle), la modification est faite **et déclarée** au rapport, ancien texte → nouveau.
- **Il est nouveau.** Il devient candidat à une fiche, ou à l'absorption dans une fiche
  nouvelle. Le critère de grain (SPEC-MODELE §5) tranche.
- **Il est hors périmètre.** `exclu` avec une raison écrite.

Interdit, **dans un même cours** : créer une fiche dont le nom ou un alias coïncide avec
une fiche existante. Le validateur le refuse (A12).

**Entre deux cours**, la coïncidence est permise et fréquente : « prime de risque » désigne
une grandeur dans `dup` et une autre dans `fpp`, sous le même $\pi$, et les deux fiches
doivent exister. Elle se déclare alors sous `homonymes` dans `notation.yml`, sinon le
validateur la signale. Déclarer n'est pas résoudre : c'est écrire, une fois, que le mot
ne suffit pas à distinguer.

## Étape 3 — Rédaction des fiches nouvelles

Une fiche par notion nouvelle, au format de SPEC-MODELE §2. Règles de rédaction :

- **Arêtes sortantes seulement.** `construite_a_partir_de` et `cas_de`. Rien d'entrant.
- **Dépendances directes seulement.** Si $x$ dépend de $y$ et que $y$ dépend déjà de $z$,
  ne pas lister $z$ (A8). Le validateur le signale ; le corriger.
- **Le symbole vient du registre** (A12). Si le cours n'en donne pas et qu'il en faut un,
  le déclarer `ajout: true` dans `notation.yml` d'abord.
- **Un symbole enregistré s'explique en français.** Dès que `notation.yml` attribue un
  symbole à la fiche, celle-ci porte « Ce que les symboles modélisent » et les nomme tous
  (SPEC-MODELE §2.1). Le `sens` du registre ne suffit pas : il sert à retrouver un symbole,
  pas à comprendre ce qu'il modélise.
- **Une phrase pour « Ce que c'est ».** Si ça ne tient pas en une phrase, le grain est
  mauvais : scinder.
- **Chaque paragraphe tracé** (A11). En cas de doute sur l'endroit exact : `[ajout]`.
- **Des phrases, pas des étiquettes.** Toute prose de fiche s'écrit en phrases complètes :
  un sujet, un verbe conjugué. « Deux fils. », « Quatre écritures bijectives du même objet. »,
  « Une seule brique : X. » sont des étiquettes ; elles se lisent vite et ne s'expliquent
  pas. La contrainte mord surtout quand on rédige en série, où la même tournure revient
  d'une fiche à l'autre sans qu'on s'en aperçoive. Relire une fiche au hasard, à froid,
  comme si c'était la seule page ouverte.
- **Une figure quand elle fait gagner trois phrases**, et jamais autrement (SPEC-MODELE
  §2.4). Elle se décide à la relecture, pas à l'écriture : on écrit la rubrique, on la
  relit, et si elle demande au lecteur de tenir deux courbes en tête, on la dessine. Le
  script va dans `courses/<code>/figures/`, la sortie SVG à côté, et le validateur vérifie
  que l'une reste la sortie de l'autre.
- **« Cesse d'être valide quand » est obligatoire**, et c'est la rubrique la plus utile.
  Si la source ne dit rien, écrire « la source ne fixe pas de limite [§x] » — c'est une
  information — et ouvrir une question dans le rapport.
- **« Le chemin jusqu'ici »** : dès que la fiche a un socle, deux à quatre paragraphes
  courts disant *en quoi ces notions-là mènent à celle-ci*. Il s'écrit **après** avoir
  posé les dépendances, puisqu'il les raconte, et il se relit dès qu'une dépendance change
  en amont — le socle se recalcule tout seul, la prose non. Format et interdits :
  SPEC-MODELE §2.1.
- **« Exemple minimal »** : une instance chiffrée, une ligne, sans calcul. Elle ne dépend
  d'aucun exercice et s'écrit dès la création de la fiche ; la laisser en dette est une
  faute de protocole. Le validateur la refuse : c'est une **E**, pas un avertissement.
  Deux règles de rédaction :
  - **toute valeur écrite est recalculée avant d'être écrite**, et le calcul est refait à la
    fin de la session sur l'ensemble des exemples. Un exemple faux est pire que pas
    d'exemple : il se recopie dans une copie d'examen ;
  - **un seul monde numérique par cours**, réutilisé d'une fiche à l'autre, pour que
    l'étudiant reconnaisse les mêmes nombres. `fpp` : courbe à 4 % et 5 %, action à 100.
    `dup` : $u(x)=\sqrt{x}$, le pari $(0,\tfrac12;100,\tfrac12)$. `pfo` : volatilités
    journalières de 1 % et 2 %, corrélation 0,5 ; au chapitre 3, deux actifs non corrélés
    à 6 % et 10 % de rendement, 10 % et 20 % de volatilité, taux sans risque 2 %. `dss` :
    une banque et ses 20 anciens clients en défaut — endettement, revenu, trois variables
    sans lien avec la perte, et la perte subie —, simulés par
    `courses/dss/figures/surapprentissage.py`, qui en est le générateur de référence ;
  - **un exemple qui traverse le récit.** Les exemples des étapes d'un même parcours se
    prennent dans ce monde, pour que le lecteur voie les mêmes données passer d'une fiche
    à la suivante. Une fiche sans formule n'est pas tenue d'avoir un exemple, mais une
    étape conceptuelle — une erreur de test, un surapprentissage — est celle où il sert
    le plus. *Constaté le 2026-09-25 : le parcours de dss sur la sélection de variables
    changeait de nombres à chaque fiche, n'en avait aucun sur ses trois étapes
    conceptuelles, et l'utilisateur n'y voyait pas où se plaçait la RSS.*
- **« Geste de calcul type »** : comment on s'en sert, sur un cas, trois lignes. S'il n'y a
  pas encore d'exercice pour l'alimenter, `à venir [ajout]` : c'est de la dette, elle est
  comptée.

Les liens vers des notions pas encore écrites (un chapitre futur) sont autorisés s'ils
sont déclarés dans `a-venir.yml` (A2). Ils sont de la dette et apparaissent au rapport.

## Étape 4 — Remontée d'abstraction (par le bas, jamais par le haut)

Pour chaque notion nouvelle, poser la question : *est-elle le cas particulier de quelque
chose dont une autre notion, existante ou nouvelle, est aussi un cas ?*

- **Oui, et l'abstraction existe** : ajouter `cas_de` et `valeur` à la nouvelle fiche.
  Vérifier que la valeur est distincte de celles des membres existants (A6). Si elle
  coïncide avec l'un d'eux, la nouvelle notion est peut-être ce membre-là : question au
  rapport.
- **Oui, et l'abstraction n'existe pas encore, mais un second membre existe** : créer
  l'abstraite (statut `ajout` sauf si la source la nomme), nommer son paramètre, donner
  une valeur à chacun des membres, écrire « Pourquoi ce niveau existe ». Voir §4.1 pour
  l'insertion.
- **Oui, mais aucun second membre** : ne rien créer. L'abstraction pressentie va au
  rapport, section « abstractions en attente », avec le nom du membre unique et le
  paramètre envisagé. La semaine où un second membre apparaît, elle sort de l'attente.

Une abstraction ne se justifie jamais par son élégance. Elle se justifie par ses membres.

### 4.1 Insertion d'un nœud entre des nœuds existants

Cas fréquent : deux notions existantes $x_1, x_2$ pointent vers un parent $p$, et l'on
découvre qu'elles partagent une abstraction intermédiaire $y$ que $p$ ne capture pas.
L'opération est :

1. créer $y$ avec `cas_de: p` et sa `valeur` pour le paramètre de $p$ ;
2. rediriger `cas_de` de $x_1$ et $x_2$ vers $y$, et remplacer leurs `valeur` par leurs
   valeurs pour le paramètre de $y$ ;
3. vérifier A5 pour $p$ : si $p$ n'a plus qu'un enfant ($y$), $p$ doit encore être l'un
   d'au moins deux enfants de son propre parent, sinon $p$ et $y$ sont à fusionner ;
4. vérifier A7 : aucune dépendance de $x_1, x_2$ ne pointe vers $y$ ou $p$ ;
5. déclarer au rapport, ligne par ligne, chaque `cas_de` et `valeur` modifiés.

Une insertion touche plusieurs fiches existantes : c'est l'opération la plus risquée du
protocole, et la seule où modifier plusieurs fiches à la fois est légitime.

## Étape 4 bis — Le récit (SPEC-MODELE §8)

Chaque fiche nouvelle trouve sa place dans un parcours, ou reçoit une raison de ne pas en
avoir (A16). Trois cas :

- **Elle prolonge un fil existant** : l'insérer comme étape à l'endroit où sa question se
  pose, écrire sa transition, et **relire la transition de l'étape suivante**, qui menait
  jusque-là à une autre fiche. C'est une modification de parcours : elle se déclare au
  rapport comme une modification de fiche, ancien texte → nouveau texte.
- **Elle ouvre un fil nouveau** (un chapitre, une question que le cours n'avait pas
  posée) : écrire un parcours, lui donner son `ordre`, et vérifier qu'il ne suppose rien
  qu'un parcours d'ordre supérieur raconte (A14).
- **Elle est une digression** : la déclarer `hors_parcours` dans `course.yml`, avec sa
  raison.

Un cours qui commence tient souvent en un seul parcours ; il se découpe quand il grandit.
Le découpage se fait en parcours consécutifs qui reproduisent exactement la suite des
étapes, et jamais en réordonnant ce qui a déjà été lu (A17 ; règles d'écriture en
SPEC-MODELE §8.4). Toute insertion, tout découpage se déclare au rapport, avec l'ancienne
et la nouvelle suite d'étapes. Une refonte se déclare en plus dans `course.yml`.

Une fiche nouvelle qui devient le prérequis direct d'une étape existante oblige à la
raconter plus tôt, ou à l'ajouter « à savoir avant » avec son rôle (A15) ; le validateur le
signale. Pour un cours qui n'a encore aucun parcours, les écrire tous est une session à
part entière : la dette « cours sans parcours » le rappelle.

## Étape 5 — Exercices et corrigés

Un exercice n'est pas une notion. Il vit dans `courses/<code>/exercices/<slug>.md` avec
l'énoncé, la solution officielle si elle existe, et la résolution faite ici. Ce qu'un
exercice produit pour la base :

- une entrée « Origine » dans chaque fiche qu'il a exercée, avec ce qu'il a révélé ;
- le contenu de « Geste de calcul type » quand la rubrique était `à venir` ;
- une ligne de « Cesse d'être valide quand » quand une convention non fixée a fait
  diverger deux réponses ;
- une entrée au rapport, section « contradictions source », quand le corrigé officiel
  contredit une formule du cours — l'écart est documenté, jamais arbitré en silence.

Les résolutions utilisent les notations du registre. Elles montrent le geste, pas
seulement le résultat.

## Étape 6 — Validation, construction, rapport

```
python tools/validate.py      # E → corriger ; W → traiter ou déclarer en dette
python tools/build.py         # régénère site/
```

Puis, l'arbre de travail étant propre, **un commit**, dont le message renvoie au rapport.
Le dépôt ne conserve que l'état final : découper après coup en commits reconstitués
donnerait un historique faux, et une session vaut donc un commit.

Le rapport `rapports/AAAA-MM-JJ-<code>.md` est obligatoire et suit ce plan. Quand une
session ne porte sur aucun cours — le générateur, une spec, le validateur — `<code>` est
remplacé par le sujet : `2026-09-20-site.md`. Deux sessions le même jour sur le même sujet
reçoivent un suffixe numérique : `2026-09-20-fpp-2.md`. L'écart à la convention est signalé
en tête du rapport.

```markdown
# Rapport d'ingestion — <cours> — <date>

## Matériau traité
Fichiers, pages, sections.

## Inventaire ajouté (à auditer par l'utilisateur)
Liste ordonnée : réf · intitulé · image (notion / absorbe / exclu / a_venir).

## Notations ajoutées ou en collision

## Fiches créées
id · nom · type · cas_de · construite_a_partir_de.

## Fiches modifiées
Pour chaque fiche : rubrique · ancien texte → nouveau texte · raison.
(Une fiche modifiée sans cette entrée est une faute de protocole.)

## Abstractions créées / insérées
Avec le paramètre, les membres et leurs valeurs.

## Abstractions en attente
Membre unique · paramètre envisagé · ce qui manque.

## Parcours
Créés, étapes insérées ou déplacées, transitions réécrites (ancien → nouveau), fiches
déclarées hors_parcours.

## Dette
Liens a-venir · gestes à venir · éléments d'inventaire a_venir. Total et variation.

**Le rapport recopie ce qui reste ouvert** — dette, abstractions en attente, questions sans
réponse, contradictions non tranchées — au lieu de renvoyer à un rapport antérieur : la
session suivante ne lit que le dernier (LECTURE.md).

## Contradictions source
Corrigé vs cours, source vs source, avec les deux valeurs et la référence.

## Questions pour l'utilisateur
Une ligne chacune, avec recommandation.

## Validation
Sortie du validateur (résumé : E, W, dette).
```

Un rapport sans section « Fiches modifiées » n'est acceptable que si aucune fiche
existante n'a été touchée, et le validateur le confirme par comparaison avec le commit
précédent.

## Ce que le protocole ne couvre pas

- La fusion de deux fiches (quand A3 ou A6 révèle qu'elles sont une seule notion) : à
  proposer au rapport, jamais à exécuter sans accord. L'id survivant garde l'autre en
  alias (A1).
- Le changement de paramètre d'une abstraction existante : idem.
- La suppression : jamais. Une notion abandonnée reçoit `statut: retiree` avec une raison
  et sort du site, mais reste dans le dépôt pour que les identifiants restent valides.
