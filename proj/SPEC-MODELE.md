# SPEC-MODELE — le modèle de données et ses axiomes

Ce document est la référence. Le validateur (`tools/validate.py`) en est l'implémentation ;
en cas de divergence, c'est le validateur qui est faux.

## 0. Principe directeur

Le livrable est une **base de notions** ; le site s'en déduit. L'unité est la **notion** —
un objet que l'étudiant cherche par son nom — et non une distinction que l'organisateur a
faite. Une fiche par notion, rubriques fixes dans un ordre fixe. Deux relations entre
fiches, et seulement deux. **Aucune relation inverse n'est jamais écrite** : elle est
calculée. C'est ce qui rend l'alimentation hebdomadaire sûre.

## 1. Les objets

- Un ensemble de cours $\mathcal C$. Un cours a un code court en minuscules (`fpp`, `cs`,
  `dup`, `ml`), un dossier `courses/<code>/`, un fichier `course.yml`.
- Pour chaque cours, un ensemble fini de notions $N_c$ ; $N = \bigsqcup_c N_c$.
- Chaque notion $n$ porte :
  - un identifiant $\mathrm{id}(n)$ de la forme `<code>/<slug>` (slug en minuscules,
    ASCII, tirets), unique dans $N$ ;
  - un type $\kappa(n) \in \{\text{principe}, \text{notion}, \text{abstraite}\}$ ;
  - un statut $\sigma(n) \in \{\text{source}, \text{ajout}\}$ ;
  - des assertions (le contenu des rubriques), chacune tracée.
- Deux relations sur $N$ :
  - $D \subset N \times N$, la **dépendance** : $(x, y) \in D$ ⇔ « $x$ est construite à
    partir de $y$ ». Clé `construite_a_partir_de`.
  - $A \subset N \times N$, l'**abstraction** : $(x, y) \in A$ ⇔ « $x$ est un cas de $y$ ».
    Clé `cas_de`.
- Pour chaque cours, un **registre de notations** $\Sigma_c$ (`notation.yml`) et un
  **inventaire de la source** $I_c$ (`inventaire.yml`).

Rien d'autre. Toute information supplémentaire est soit du contenu de fiche, soit dérivée.

## 2. Le format d'une fiche

Un fichier `courses/<code>/notions/<slug>.md`, UTF-8, LF. En-tête YAML puis sections
Markdown. Les formules sont en LaTeX, `$...$` en ligne et `$$...$$` hors ligne.

```markdown
---
id: fpp/prix-a-terme
nom: Prix à terme
symbole: '$F$, $K$, $H$'                 # facultatif ; guillemets simples ou aucun — jamais doubles (les \ LaTeX y sont des échappements YAML)
type: abstraite                          # principe | notion | abstraite
statut: source                           # source | ajout
cas_de: fpp/contrat-prime-nulle          # facultatif ; absent pour un principe
valeur: un actif ou un taux, livré à une date        # obligatoire si le parent est une abstraite
parametre: 'le couple (portage $\Phi$, facteur d''actualisation $D$)'   # obligatoire si type = abstraite
construite_a_partir_de: [fpp/facteur-actualisation, fpp/portage, fpp/replication-statique]
alias: [forward price, prix forward]     # facultatif
refs: ['Prop. 2', 'Prop. 3', 'Déf. 8']  # indicatif ; la traçabilité est par paragraphe
---

## Ce que c'est
Une phrase. [Prop. 2]

## Forme
$$K = \dfrac{S_t\,\Phi}{D}$$ [ajout]

## Ce que les membres partagent          ← « Ce qui la définit » pour un principe ou une notion
... [Prop. 2, Prop. 3]

## Pourquoi ce niveau existe             ← abstraites seulement
... [ajout]

## Exemple minimal
... [ajout]

## Geste de calcul type
... [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| portage $\Phi$ | action sans dividende | $1$ |
[§3.1, §3.2]

## Cesse d'être valide quand
... [Prop. 4]

## Origine
- exercice fpp/ex-01-c : la convention cum/ex n'était pas fixée [ajout]
```

### 2.1 Les rubriques, dans cet ordre, et rien d'autre

| # | Rubrique | Types | Obligation |
|---|---|---|---|
| 1 | Ce que c'est | tous | obligatoire ; **une phrase**, ≤ 220 caractères |
| 2 | Forme | tous | si la notion a une formule |
| 3 | Ce qui la définit / Ce que les membres partagent | tous | obligatoire |
| 4 | Pourquoi ce niveau existe | abstraite | obligatoire |
| 5 | Exemple minimal | tous | obligatoire si Forme ; une instance concrète chiffrée, sans calcul |
| 6 | Geste de calcul type | tous | obligatoire si Forme ; peut être `à venir [ajout]` → dette |
| 7 | Ce qui reste libre | tous | facultatif ; table |
| 8 | Cesse d'être valide quand | tous | obligatoire ; peut être « rien dans le périmètre du cours [réf] » |
| 9 | Origine | tous | facultatif ; liste d'exercices |

Une rubrique absente qui n'est pas obligatoire est simplement omise. Une rubrique hors de
cette liste est une erreur. L'ordre est une erreur s'il n'est pas respecté.

### 2.2 Ce qui n'est jamais dans une fiche (dérivé, A9)

Cas particulier de (au-delà de `cas_de`) · Membres · Le paramètre qui les distingue (la
table) · Sert ensuite à · Socle · Niveau. Le générateur les affiche ; le validateur refuse
toute section portant l'un de ces titres.

### 2.3 Traçabilité par paragraphe

Chaque paragraphe, chaque item de liste, chaque table d'une rubrique se termine par un
marqueur entre crochets :

- une ou plusieurs références à la source : `[§3.1]`, `[Déf. 4]`, `[Prop. 2, Prop. 3]`,
  `[Th. 1]`, `[Ex. 2]`, `[éq. 16]`, `[p. 9]`, `[slide 14]` ;
- ou le marqueur `[ajout]`.

La grammaire des références est fixée par cours dans `course.yml` (clé `refs_pattern`).
Le validateur refuse un paragraphe sans marqueur.

**Plusieurs sources dans un même cours.** Si `course.yml` déclare plus d'une source, toute
référence est préfixée de l'identifiant de la source, sans quoi `slide 12` est ambigu.
`courses/dup/` le fait : `L1 slide 12`, `L2 éq. 1`. Le numéro retenu est celui que
l'étudiant lit sur le document — le numéro imprimé sur la slide, pas la page du PDF, les
deux divergeant dès qu'une slide est en plusieurs temps.

## 3. Les axiomes de structure

Chaque axiome dit ce qu'il interdit et la sévérité : **E** (erreur, build refusé),
**W** (avertissement, corrigé ou compté en dette).

**A1 — Unicité et stabilité des identifiants. [E]**
$\mathrm{id}$ est injective ; un fichier par identifiant ; le slug du fichier est celui de
l'id ; l'id commence par le code du dossier. Un identifiant ne change jamais : renommer,
c'est ajouter un alias. *Empêche* : les liens qui cassent d'une semaine à l'autre.

**A2 — Fermeture des références. [E / W]**
Tout id apparaissant dans `cas_de` ou `construite_a_partir_de` existe, ou est déclaré
dans `courses/<code>/a-venir.yml` avec une justification et une date. Une référence
déclarée « à venir » est un **W** et entre dans la dette $\Delta$ ; une référence non
déclarée est un **E**. *Empêche* : les liens morts invisibles.

**A3 — Acyclicité de $D$. [E]**
$(N, D)$ est un graphe orienté acyclique. *Empêche* : deux notions définies l'une par
l'autre — toujours le symptôme soit d'une seule notion, soit d'un principe manquant. Sans
A3, le socle n'existe pas.

**A4 — $A$ est une forêt enracinée dans les principes. [E]**
Chaque notion a au plus un `cas_de` ; $A$ est sans cycle ; les racines de $A$ (notions sans
`cas_de` qui ont des membres) sont de type `principe` ; et $(x, y) \in A \Rightarrow
\kappa(y) \in \{\text{abstraite}, \text{principe}\}$. *Empêche* : une notion cas
particulier de deux choses — symptôme d'un paramètre non identifié.

*Exception documentée pour les principes.* Un principe n'est pas une généralisation avec
un paramètre ; c'est un axiome. Ses enfants dans $A$ sont ses premières constructions
(« découle directement de »), et A6 ne s'applique pas à lui. Le générateur affiche
« découle de » et non « cas de » pour ces arêtes.

*Créer un principe.* A4 a une conséquence qu'il faut nommer : une abstraction justifiée par
ses membres reste **interdite** tant qu'aucun principe ne la surplombe. Quand le cas se
présente — des membres réels, un paramètre réel, pas de racine — la réponse n'est pas de
renoncer à l'abstraction, c'est de chercher le principe dans la source. Il y est presque
toujours, énoncé sans être nommé : « Risk is what all risk averters hate », « Curvature of
u captures attitude toward outcome risk », une section intitulée « Hedging ». Le principe
prend alors `statut: source` avec la référence de la phrase qui le porte, ou `ajout` si
rien ne l'énonce. Dans les deux cas il est **déclaré au rapport** comme la décision de
structure de la session, parce qu'il engage tout un pan de l'arbre. Ce qui reste interdit :
inventer un principe pour faire tenir une abstraction dont les membres ne sont pas là.

**A5 — Règle des frères. [E]**
Pour toute $y$ abstraite : $|A^{-1}(y)| \geq 2$, ou bien $y$ est elle-même l'un d'au moins
deux enfants de son parent. *Empêche* : les abstractions décoratives. Une abstraction
pressentie sans second membre n'entre pas dans le graphe ; elle va dans le rapport.

**A6 — Paramètre générateur. [E]**
Toute abstraite $y$ porte `parametre`. Tout membre $x$ d'une abstraite porte `valeur`. Les
valeurs des membres d'une même abstraite sont deux à deux distinctes. *Empêche* : deux
membres qui sont le même cas ; les abstractions qui décrivent sans engendrer.

**A7 — Disjonction. [E]**
$D \cap A^{+} = \varnothing$ : une notion ne liste jamais un de ses ancêtres d'abstraction
dans `construite_a_partir_de`. *Empêche* : l'explosion de navigation (remonter les deux
relations à la fois).

**A8 — Réduction transitive. [W, corrigé]**
Si $(x, y) \in D$, il n'existe pas de chemin de longueur $\geq 2$ de $x$ à $y$ dans $D$.
Le validateur signale et propose la suppression ; le protocole d'ingestion l'applique.
*Empêche* : les dépendances redondantes qui gonflent les socles.

**A9 — Inverses dérivés. [E]**
Aucune fiche ne contient : une section « Sert ensuite à », « Membres », « Socle »,
« Niveau », « Le paramètre qui les distingue ». Ces objets sont calculés au build :
$D^{-1}$, $A^{-1}$, $D^{+}$ (socle), $\ell(n)$ = longueur du plus long chemin de $n$ vers une
source de $D$. *Empêche* : la désynchronisation. **C'est l'axiome qui autorise
l'incrémental** : ajouter une notion avec ses seules arêtes sortantes ne peut invalider
aucune notion existante, sauf A5 et A8 qui sont recalculés.

**A10 — Acyclicité entre cours. [E]**
Les arêtes de $D$ entre cours sont autorisées (id préfixé, p. ex. `cs/lemme-ito`). Le graphe
quotient sur $\mathcal C$ induit par $D$ est acyclique. Les arêtes de $A$ entre cours sont
interdites : une abstraction appartient à un cours. *Empêche* : deux cours qui se
présupposent.

## 4. Les axiomes de fidélité à la source

Ils ne sont pas des propriétés du graphe ; ils sont relatifs au document du professeur.

**A11 — Traçabilité et projection stricte. [E]**
Toute assertion porte un marqueur (§2.3). Une notion de statut `source` ne liste jamais
dans `construite_a_partir_de` une notion de statut `ajout`. Conséquence : la projection
« cours strict », obtenue en effaçant toute notion `ajout` et tout paragraphe `[ajout]`,
satisfait encore A1–A10. *Empêche* : la confusion entre le cours et son interprétation ;
garantit qu'un bouton « masquer les ajouts » donne toujours un objet cohérent et
opposable à l'examen.

**A12 — Registre de notations. [E]**
`courses/<code>/notation.yml` liste chaque symbole que le cours définit : symbole, notion
associée, référence de première occurrence, sens en une ligne. Règles :
- une fiche n'emploie, pour un objet nommé par le cours, que le symbole du registre ;
- un symbole introduit par l'opérateur est marqué `ajout: true` dans le registre et ne
  peut pas coïncider avec un symbole `source` du même cours ;
- deux cours peuvent donner deux sens au même symbole ; la collision est déclarée dans
  `notation.yml` (clé `collisions`) et le site affiche le contexte de cours.
Le validateur vérifie que le champ `symbole` de chaque fiche est dans le registre du cours
(source ou ajout déclaré). *Empêche* : le renommage silencieux qui fait perdre l'étudiant
entre la fiche et son poly.

**A13 — Couverture. [E]**
`courses/<code>/inventaire.yml` liste tout élément indexable de la source : chaque
définition, théorème, proposition, lemme, corollaire, exemple numéroté, équation
numérotée, et chaque titre de section. Chaque élément a exactement une image :
- `notion: <id>` — c'est une notion à part entière ;
- `absorbe: <id>` — son contenu est dans le corps de cette notion ;
- `exclu: "<raison>"` — volontairement hors base ;
- `a_venir: "<date prévue>"` — pas encore traité (dette, **W**).
Le validateur refuse un élément sans image et un id d'image qui n'existe pas. *Empêche* :
les oublis silencieux.

**Limite d'A13, à connaître.** A13 garantit que rien d'inventorié n'est perdu. Il ne peut
pas garantir que l'inventaire est complet. Une définition que l'opérateur n'a pas vue en
lisant la source est perdue sans bruit, et A12 ne détectera pas une notation qu'il n'a pas
vue. C'est le seul point où la machine ne peut pas se vérifier elle-même. Conséquence :
**l'utilisateur audite l'inventaire, pas les fiches.** Une liste par semaine.

## 5. Le critère de grain

Un élément de la source est une notion à part entière si l'une des trois conditions tient :

1. il porte un nom ou un symbole réutilisé ailleurs dans la source ;
2. il apparaît, ou apparaîtra, dans une arête $D$ ou $A$ d'une autre notion ;
3. il possède sa propre limite de validité (une rubrique 8 qui lui est propre).

Sinon il est absorbé dans la notion la plus proche, et l'inventaire le dit. Exemple : les
grecques — delta, gamma, véga, thêta, rhô — ont chacune un nom et une limite propre :
cinq fiches sous une abstraite `sensibilite`, dont le paramètre est « la variable dérivée ».

## 6. Ce que les axiomes garantissent

- Le socle de toute notion est fini, calculable, et son ordre de lecture (par niveau
  croissant) est bien défini. (A3, A8)
- **Le socle est clos** : si $y$ est dans le socle de $x$, tout le socle de $y$ y est déjà.
  Lire le socle d'une fiche suffit donc, et ne renvoie jamais à une notion extérieure.
  C'est la fermeture transitive, la propriété est vraie par construction. (A3)
- **Le niveau est le plus long chemin, pas le seul.** Une notion de niveau $n$ peut dépendre
  directement d'une notion de niveau $n-3$ : les niveaux ne forment pas une chaîne. Ce qui
  reste vrai, et qui est l'usage recherché : lire par niveaux croissants ne fait jamais
  rencontrer une notion qu'on n'a pas déjà vue. (A3)
- Toute notion a un unique chemin d'abstraction jusqu'à un principe. (A4)
- Toute navigation termine. (A3, A7)
- Ajouter une notion avec ses seules arêtes sortantes ne peut invalider aucune notion
  existante ; seuls A5 et A8 sont recalculés. (A9)
- Effacer les ajouts laisse un graphe valide. (A11)

## 7. Fichiers annexes d'un cours

`course.yml`
```yaml
code: fpp
titre: Financial Products and Introduction to Pricing
enseignant: Nicolas Gaussel
annee: 2025-2026
sources:
  - id: poly
    fichier: sources/financial_products_lecture_notes.pdf
    type: notes de cours
refs_pattern: '^(§\d+(\.\d+)*|Déf\. \d+|Prop\. \d+|Th\. \d+|Ex\. \d+|éq\. \d+|p\. \d+|Rem\. \d+|slide \d+)$'
depend_de: [cs]          # cours prérequis (A10) ; vide si aucun
```

`notation.yml`
```yaml
symboles:
  - symbole: "$P(t,T)$"
    notion: fpp/facteur-actualisation
    ref: "Déf. 3"
    sens: prix en t d'un flux de 1 payé en T
  - symbole: "$\\Phi$"
    notion: fpp/portage
    ajout: true
    sens: facteur de portage du sous-jacent
collisions:
  - symbole: "$P$"
    ici: zéro-coupon
    ailleurs: { cs: probabilité historique }
```

`inventaire.yml`
```yaml
elements:
  - ref: "Déf. 3"
    intitule: Zero Coupon Bond
    notion: fpp/facteur-actualisation
  - ref: "§1.3"
    intitule: Joint dynamics of Assets, Equity and Debts
    a_venir: "2026-10"
  - ref: "Ex. 2"
    intitule: Flat rate curve
    absorbe: fpp/taux-forward
```

`a-venir.yml`
```yaml
- id: fpp/option-europeenne
  raison: section 6 non encore traitée
  depuis: 2026-09-20
```
