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

- Un ensemble de cours $\mathcal C$. Un cours a un code court en minuscules (`fpp`,
  `dup`, `dss`), un dossier `courses/<code>/`, un fichier `course.yml`.
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

Un cours porte aussi des **parcours** (§8). Ce ne sont pas des notions et ils n'ajoutent
aucune relation : ils ordonnent un récit à travers les notions existantes, et le validateur
vérifie que ce récit ne contredit jamais $D$.

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

## Ce que les symboles modélisent
$\Phi$ est le portage : ce que rapporte ou coûte la détention du sous-jacent jusqu'à
l'échéance, exprimé en facteur et non en montant. [Déf. 5]

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
| 3 | Ce que les symboles modélisent | tous | **obligatoire dès que le registre attribue un symbole à la fiche, ou que la fiche porte une Forme** ; elle nomme tous les symboles du registre |
| 3 bis | Retrouver la formule | tous | facultatif ; la figure d'abord s'il y en a une, puis le raisonnement ; **finit sur la formule retrouvée**, en `$$…$$` |
| 4 | Ce qui la définit / Ce que les membres partagent | tous | obligatoire |
| 5 | Pourquoi ce niveau existe | abstraite | obligatoire |
| 6 | Le chemin jusqu'ici | tous | **obligatoire dès que le socle n'est pas vide** ; interdite s'il l'est |
| 7 | Exemple minimal | tous | obligatoire si Forme ; une instance concrète chiffrée, sans calcul |
| 8 | Geste de calcul type | tous | obligatoire si Forme ; peut être `à venir [ajout]` → dette |
| 9 | Ce qui reste libre | tous | facultatif ; table |
| 10 | Cesse d'être valide quand | tous | obligatoire ; peut être « rien dans le périmètre du cours [réf] » |
| 11 | Origine | tous | facultatif ; liste d'exercices |

Une rubrique absente qui n'est pas obligatoire est simplement omise. Une rubrique hors de
cette liste est une erreur. L'ordre est une erreur s'il n'est pas respecté.

**« Ce que les symboles modélisent », en détail.** Une notation n'est pas son nom. Le
registre dit que $\varphi$ est la « fonction de distorsion des probabilités » : cela nomme
l'objet et ne dit pas ce qu'il modélise — ce qu'il prend en entrée, ce qu'il rend, et ce
qu'il n'est pas. La rubrique le dit en français, pour les symboles que la fiche possède.

**Elle nomme chaque symbole que le registre lui attribue, sans exception**, et le validateur
compte ceux qu'elle oublie, comme il le fait pour les notions du socle. Expliquer deux
symboles sur trois laisse le lecteur devant la question même que la rubrique existe pour
éviter. Pour chacun, elle dit :

- **ce qu'il prend et ce qu'il rend**, quand c'est une fonction. L'argument de $\varphi$ est
  une probabilité cumulée et non un montant, et toute la notion tient dans cette
  différence-là ;
- **ce qu'il modélise**, en une phrase de français et sans formule ;
- **ce qu'il n'est pas**, quand la confusion est probable : une croyance, une utilité,
  l'homonyme d'un autre cours.

Ce qu'elle ne fait pas : redire la formule, qui est en « Forme » ; redire ce qu'est la
notion, qui est en « Ce que c'est » ; recopier le `sens` du registre, qui tient en une ligne
parce qu'il sert à **retrouver** un symbole et non à le comprendre.

**Dès qu'il y a une formule, la rubrique est due**, même si le registre n'attribue aucun
symbole à la fiche. Une formule emploie des lettres que la fiche n'a pas toujours
définies — les arguments d'une fonction, un paramètre, une variable muette —, et c'est là
que le lecteur se perd : dans `fpp/duration`, $P(t,r)$ prend une durée et un taux, alors
que $P(t,T)$ prenait deux dates. La rubrique dit alors ce que modélise chaque symbole de
la Forme qui n'est pas déjà dit en français par « Ce que c'est ». *Demandé par
l'utilisateur le 2026-09-26 : « ça devrait être une règle pour tous les cours, la rubrique
"Ce que les symboles modélisent", quand c'est nécessaire ».*

L'obligation est un **W** compté en dette, et non un **E**. Le jour où elle est écrite, elle
porte sur 87 fiches ; les rendre toutes conformes d'un coup serait la réécriture en masse
que le protocole tient pour le danger principal du dépôt. *Ouverte le 2026-09-21, sur cette
remarque de l'utilisateur : « parfois il est nécessaire à la compréhension de comprendre ce
que modélise une fonction / une notation en français ».*

**« Retrouver la formule », en détail.** La démonstration qui permet de reconstruire la
formule sans l'avoir apprise : pour un prix à terme, chaque jambe du contrat ramenée en $t$,
puis l'égalité qui dit que le contrat ne coûte rien. Elle s'ouvre sur la figure quand la
fiche en a une — le dessin d'abord, parce que c'est lui qu'on refait de tête —, avance par
paragraphes courts, un pas par paragraphe, chacun avec son marqueur, et **se termine sur la
formule** en équation centrée : une démonstration qui s'arrête avant sa conclusion laisse
au lecteur la dernière ligne, la seule qu'il cherchait. Le validateur vérifie les deux
règles, figure en tête et formule à la fin, en **E**. La rubrique est facultative : elle
n'a de sens que là où la formule se déduit d'un raisonnement du cours, pas là où elle est
une définition. *Demandée par l'utilisateur le 2026-09-25 : « pour retrouver les formules
comme le prix forward, celui de l'exchange, je voudrais les graphiques puis le raisonnement
(démo) pour retrouver la formule ».*

**« Le chemin jusqu'ici », en détail.** Deux à quatre paragraphes courts qui disent *en quoi
les notions du socle mènent à celle-ci*. Le socle donne l'ordre de lecture ; ce paragraphe
donne la raison. Il nomme les notions par leur identifiant, ce qui les rend cliquables et
vérifiables. Il se rend en tête de la rubrique générée « Socle complet », pas à sa place
dans le fichier : c'est là que la question se pose.

**Il nomme chaque notion du socle, sans exception.** Le validateur compte celles qu'il
oublie et les signale. La règle a un coût — sur un socle de quatorze notions, il faut les
faire tenir dans un récit — mais l'alternative est pire : nommer trois notions sur quatre
laisse le lecteur devant la question même que la rubrique existe pour éviter. *Constaté le
2026-09-20 par l'utilisateur, sur `dup/assurance-probabiliste`, qui n'en nommait qu'une sur
quatre ; 35 fiches sur 97 étaient dans ce cas et ont été réécrites.*

Ce qu'il ne fait pas :

- **il ne recopie pas la liste.** Les nommer toutes n'est pas les énumérer : une liste dans
  l'ordre des niveaux n'apprend rien que la liste générée ne montre déjà. Il faut une ligne
  narrative — le socle de `fpp/delta` a une seule histoire, en trois temps ;
- **il n'emploie aucun raccourci qui ne se comprenne pas sur cette page seule.** « Le socle
  commun », « toute la chaîne de Savage », « même socle que X » : ces formules économisent
  l'écriture et coûtent la lecture. Elles sont apparues sur 21 fiches et ont été retirées ;
- **il n'écrit aucun nombre dérivé en dur.** « Treize notions » devient faux la semaine où
  une dépendance change, et rien ne le signale. Le nombre est déjà affiché par le
  générateur, à côté du titre de la rubrique ;
- **il ne nomme aucune notion absente du socle.** Le validateur le refuse ;
- **il n'écrit pas une arête du graphe à la place d'une phrase.** « X et Y donnent Z » n'est
  pas du français : « donner » y sert de flèche, pas de verbe. Une notion *fournit* un objet,
  *évalue*, *se combine en*, *se déduit de*. La liste des dépendances est déjà affichée sous
  le paragraphe ; celui-ci doit dire ce qu'aucune flèche ne dit. *Relevé le 2026-09-20 :
  « donne » ou « donnent » servait de verbe d'arête 109 fois dans 97 chemins* ;
- **il ne reprend pas l'ouverture d'une autre fiche**, sauf si les deux fiches ont
  exactement le même socle — c'est le cas des grecques, qui partagent celui de la formule.
  Une phrase identique sur deux socles différents signale une rédaction au gabarit, pas une
  parenté. Le validateur compare les ouvertures et les socles, et compte les récidives.
  *Relevé le 2026-09-20 : douze fiches ouvraient sur la même phrase au mot près.*

**Pourquoi cette rubrique est écrite et non dérivée.** Le socle, lui, est calculé (A9). La
raison pour laquelle ces notions-là y figurent ne l'est pas : c'est du contenu. Le risque,
assumé, est que les deux divergent — le validateur exige donc la rubrique dès que le socle
existe et refuse toute notion citée hors du socle, mais il ne peut pas voir qu'un socle a
grandi sans que la prose suive. C'est la même limite qu'A13 : la machine ne se vérifie pas
entièrement elle-même, et c'est le rapport hebdomadaire qui l'attrape.

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

**Plusieurs sources dans un même cours.** Si `course.yml` déclare plus d'une source,
**toute référence dont la forme existe dans plus d'une source** est préfixée de
l'identifiant de la source, sans quoi `slide 12` est ambigu. Le numéro retenu est celui
que l'étudiant lit sur le document — le numéro imprimé sur la slide, pas la page du PDF,
les deux divergeant dès qu'une slide est en plusieurs temps.

`courses/dup/` préfixe tout : ses trois sources sont trois jeux de slides, donc toutes
leurs formes se recouvrent — `L1 slide 12`, `L2 éq. 1`.

`courses/fpp/` ne préfixe que ce qui se recouvre. Ses deux sources sont un poly et un
livre d'exercices ; la seule forme commune est `§x`. Une référence à une section du livre
s'écrit donc `exos §2.1`, un exercice `exo. 5`, et les formes propres au poly
(`§3.2`, `Déf. 8`, `Prop. 2`, `Th. 1`, `Rem. 1`, `Ex. 2`, `éq. 16`) restent nues.

Le choix se mesure : préfixer les 300 références déjà écrites au poly aurait touché
presque chaque fiche pour lever une ambiguïté qui n'existe sur aucune d'elles, et le
protocole tient la réécriture en masse pour le danger principal du dépôt. La règle porte
donc sur la forme, pas sur le nombre de sources. Elle a une conséquence à accepter : le
jour où une troisième source emploie `exo. n`, il faudra préfixer — et cela se verra,
parce que `refs_pattern` refusera la forme nue.

### 2.4 Les figures

Une rubrique porte une figure chaque fois qu'un dessin montre en une fois ce que la prose
dit en trois phrases. Elle s'écrit comme un bloc à part, avec sa légende et son marqueur :

```markdown
![La corde passe sous la courbe : c'est toute l'inégalité.](figures/aversion-au-risque.svg) [ajout]
```

Quatre règles, et elles ne se négocient pas.

1. **La figure ne montre que ce que sa fiche dit.** Elle illustre, elle n'ajoute pas. Une
   figure qui introduit un objet dont la fiche ne parle pas appartient à une autre fiche.
2. **Elle porte un marqueur comme n'importe quel bloc** (A11). Tracée par l'opérateur à
   partir de l'exemple du cours, c'est `[ajout]` ; reproduite d'un schéma de la source,
   c'est la référence de ce schéma.
3. **Le dessin est calculé, pas dessiné.** `courses/<code>/figures/<slug>.py` est un
   script sans dépendance qui imprime le SVG sur la sortie standard ; `<slug>.svg` est sa
   sortie, déposée à côté. Le validateur rejoue le script et compare : une figure qu'on ne
   sait plus refaire est une figure qui dérivera de ce qu'elle montre, comme une prose qui
   décrit un socle calculé.
4. **Aucune couleur en dur.** Les traits nomment les variables CSS du site — `var(--fg)`,
   `var(--mut)`, `var(--acc)`. Le fond reste vide. C'est ce qui fait qu'une figure suit le
   thème clair ou sombre au lieu de disparaître dans l'un des deux ; une image matricielle,
   même à fond transparent, garderait son encre noire.

`tools/figure.py` porte les primitives de tracé — repère, courbe, point, mesure d'un écart,
axes — et n'a besoin de rien d'autre que la bibliothèque standard.

**Choisir la forme.** Les quatre règles disent ce qu'une figure a le droit de montrer ; elles
ne disent pas laquelle dessiner. La forme se choisit sur ce que la figure doit faire voir,
écrit d'abord en une phrase, et c'est la forme qui le montre le plus directement qui
l'emporte, même si elle n'a encore servi nulle part. Quelques formes déjà éprouvées :

- l'**échéancier** — un axe du temps, des flux qui montent quand on les reçoit et
  descendent quand on les paie, une flèche courbe qui les ramène en $t$ — pour tout ce qui
  s'actualise, se capitalise ou se réplique (`fpp/facteur-actualisation`) ;
- la **planche** — deux ou trois cadres côte à côte reliés par « + », « − », « = » ou « → »
  — pour une identité ou un avant/après, là où un cadre unique superposerait les traits
  (`fpp/parite-call-put`) ;
- l'**aire** — une intégrale ou une somme pondérée lue comme une surface
  (`dup/integrale-de-choquet`) ;
- la **corde et la courbe** pour une inégalité de Jensen, la **tangente** pour une
  sensibilité, la **répartition** pour un ordre stochastique.

Une courbe ou des barres ne s'imposent pas par défaut : elles se choisissent quand ce
qu'elles montrent est ce qu'il faut voir. *Demandé par l'utilisateur le 2026-09-26, après
les figures de dup et de pfo : « pas n'importe quel graphique ; il faut faire un graphique
qui met en évidence au mieux ce que l'on cherche à montrer ».*

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
Les arêtes de $D$ entre cours sont autorisées (id préfixé : une fiche de `fpp` pourrait
dépendre de `dup/loterie`). Le graphe
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
  `notation.yml` (clé `collisions`) et le site affiche le contexte de cours. Une entrée
  `collisions` nomme **tous** les cours concernés, pas seulement l'un d'eux : le lecteur
  doit trouver l'histoire entière au même endroit. Les clés de `ailleurs` sont des codes
  de cours existants ;
- deux cours peuvent aussi donner le même *nom*, ou le même alias, à deux notions
  distinctes. C'est une homonymie, déclarée dans `notation.yml` (clé `homonymes`), avec
  les identifiants concernés sous `entre`. **Dans un même cours, c'est une faute** : un
  cours ne nomme pas deux notions de la même façon.
Le validateur vérifie que le champ `symbole` de chaque fiche est dans le registre du cours
(source ou ajout déclaré), que toute collision entre registres est déclarée (**W**), et
que toute homonymie entre cours l'est aussi (**W**) — dans un même cours, **E**.
*Empêche* : le renommage silencieux qui fait perdre l'étudiant entre la fiche et son poly,
et la notion réécrite sous un autre code parce qu'on ne l'a pas reconnue.

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
- **Lire les parcours d'un cours dans l'ordre ne fait jamais rencontrer une fiche avant ce
  qu'elle suppose** : chaque prérequis a été raconté plus tôt, ou présenté « à savoir
  avant » avec son rôle. (A3, A14, A15)
- **Ce qui a été lu reste lisible dans le même ordre** : le récit d'une semaine est
  contenu dans celui de la suivante, sauf refonte déclarée. (A17)

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
depend_de: []            # cours prérequis (A10) ; vide si aucun
hors_parcours:           # fiches sans place dans aucun récit, avec leur raison (A16)
  fpp/exemple: digression de la section 4, qui couperait le fil des options
refonte_du_recit:        # refontes voulues du récit, datées et motivées (A17)
  - date: '2026-11-02'
    raison: le chapitre 5 réorganise les options ; le parcours 3 est refait
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
    ailleurs: { dup: une loterie }
homonymes:
  - nom: Prime de risque
    entre: [dup/prime-de-risque, fpp/prime-de-risque]
    note: deux grandeurs distinctes sous le même mot, et sous le même $\pi$
```

`figures/<slug>.py` et `figures/<slug>.svg` — le script d'une figure et sa sortie (§2.4).
Le second se régénère depuis le premier ; le validateur vérifie qu'ils s'accordent.

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

## 8. Les parcours

### 8.1 Pourquoi

Le découpage en fiches perd le récit du cours. Une fiche dit ce qu'est une notion et ce
qu'il faut savoir avant ; elle ne dit pas pourquoi la notion arrive, ni quelle question elle
résout. « Le chemin jusqu'ici » raconte l'amont d'une fiche, pas le cours. Un **parcours**
raconte une partie du cours : il traverse des fiches dans un ordre choisi et dit, à chaque
étape, la question qui mène à la suivante. Les fiches restent le dictionnaire ; les
parcours sont le cours qu'on lit. *Essayé sur dup et retenu par l'utilisateur le
2026-09-24 : « à chaque étape, ce qu'il y a dans le socle, ce sont des choses qu'on a soit
vues précédemment, soit qui faisaient partie de ce qu'il faut savoir avant de commencer ».*

### 8.2 Le format

Un fichier `courses/<code>/parcours/<slug>.md`, identifiant `<code>/parcours-<slug>`
(définitif, A1).

```markdown
---
id: dup/parcours-ambiguite
ordre: 6                                  # la place du parcours dans le cours
titre: Quand on ne connaît même pas les probabilités
source: L1 slides 59–64, L4 slides 35–62  # indicatif
---

## Point de départ
Une situation concrète, prise au monde numérique du cours, qui pose la question. [L1 slide 62]

## À savoir avant
- dup/acte : le rôle que cette fiche joue dans cette histoire-ci. [L1 slide 2]

## Étapes
1. dup/separation-gouts-croyances
   La question qui mène à cette fiche. [ajout]
   Histoire : « mots du point de départ » — ce que la fiche en fait. [ajout]

2. dup/utilite-esperee-subjective
   … [L1 slide 59]
   Suite : ce que l'histoire ajoute ici, et la question que cela pose. [ajout]
   Histoire : « la question que cela pose » — comment la fiche y répond. [ajout]

## Point d'arrivée
Ce que le récit a établi, en une ou deux phrases. [ajout]
```

Quatre rubriques, dans cet ordre, et rien d'autre ; « À savoir avant » est omise si aucune
étape ne suppose de fiche extérieure au parcours. Chaque phrase porte un marqueur (A11),
dans la grammaire du cours.

Sous chaque étape, après la transition, deux lignes qui ne sont pas des rubriques :
**`Suite :`**, facultative, ce que l'histoire ajoute à cette étape ; **`Histoire :`**,
obligatoire, les mots de l'histoire que la fiche traite, cités entre « », puis, après un
tiret, la phrase qui dit ce que la fiche en fait. Sans citation, la phrase seule. Leurs
règles sont A18 et §8.5.

### 8.3 Les axiomes du récit

**A14 — Ordre du récit. [E]**
Dans un parcours, aucune étape n'arrive avant l'un de ses prérequis, directs ou non. Entre
les parcours d'un cours, lus par `ordre` croissant, aucun ne suppose — par une étape, son
socle, ou « à savoir avant » — une fiche qu'un parcours d'ordre supérieur est le premier à
raconter. Les `ordre` d'un cours sont distincts ; une étape appartient au cours du parcours
et n'y figure qu'une fois. *Empêche* : un récit qui demande de lire une fiche avant ce
qu'elle suppose, dans un parcours ou d'un parcours au suivant.

**A15 — Rattachement. [E]**
Tout prérequis **direct** d'une étape, que le parcours ne raconte pas, figure « à savoir
avant » avec une phrase qui dit **le rôle qu'il joue dans cette histoire** ; et rien d'autre
n'y figure. *Empêche* : arriver sur une fiche de base sans savoir ce qu'elle fait dans le
récit. Seuls les prérequis directs : exiger aussi leur socle demandait plus de quinze rôles
à un parcours de dup, pour des fiches sans rapport avec son histoire ; chaque fiche garde
son socle complet sur sa propre page.

**A16 — Couverture du récit. [W, dette]**
Toute fiche d'un cours est l'étape d'un parcours, ou figure « à savoir avant » dans l'un
d'eux, ou est déclarée dans `course.yml` sous `hors_parcours` avec sa raison. Un cours
qui a des fiches et aucun parcours est compté en dette. *Empêche* : les notions que rien
ne raconte et que rien n'explique, ce qu'A13 empêche pour la source.

**A17 — Le fil ne se perd pas. [E]**
`build.py` scelle, dans `courses/<code>/parcours/fil.yml`, la suite de toutes les étapes
du cours dans l'ordre de lecture — les parcours par `ordre`, les étapes dans leur ordre.
La suite actuelle doit **contenir** le fil scellé, dans le même ordre : on peut insérer une
étape, prolonger un parcours, en ajouter un, ou découper un parcours en parcours
consécutifs ; on ne peut ni retirer une étape du récit, ni en réordonner deux. Une refonte
voulue se déclare dans `course.yml`, sous `refonte_du_recit`, avec sa date et sa raison :
l'erreur devient alors un avertissement, et le fil est scellé à nouveau. *Empêche* : qu'un
lecteur qui a suivi le récit une semaine ne le retrouve plus la suivante. *Demandé par
l'utilisateur le 2026-09-24 : « que l'histoire précédente soit toujours contenue, et
qu'après on passe à d'autres histoires ».*

**A18 — Ancrage dans l'histoire. [E pour la forme, W dette pour la couverture]**
Chaque étape porte une ligne « Histoire : ». Toute citation y est prise **mot pour mot**
dans le point de départ ou dans une suite racontée à cette étape ou avant — jamais dans
une suite à venir — et ne coupe aucune formule. Une étape porte au plus une ligne
« Suite : » et une ligne « Histoire : », et celle-ci a une phrase après ses citations.
Une étape sans ligne « Histoire : » est un avertissement compté en dette (« étape sans
lien à l'histoire »). *Empêche* : que le lecteur fasse de tête, par des allers-retours
vers la page du parcours, le lien entre la fiche et la question qu'elle résout ; et qu'un
mot mis en gras ne se trouve pas dans l'histoire qu'il a sous les yeux. *Demandé par
l'utilisateur le 2026-09-26 : « j'essaye moi-même de ramener les fiches à l'histoire ;
j'aimerais que ce soit fait automatiquement ».*

### 8.4 Écrire un parcours

- **Combien de parcours : autant que le cours pose de questions, pas plus.** Un cours
  court, ou qui commence, tient en **un seul** parcours ; on découpe quand le cours pose
  plusieurs questions distinctes, ou quand un fil dépasse une vingtaine d'étapes — le
  validateur avertit au-delà de vingt. *Constaté sur pfo : trois parcours annoncés, cinq
  écrits, parce que les fondre donnait des fils de plus de quinze étapes.*
- **Un fil, pas un chapitre.** Un parcours suit une question du début à sa réponse ; il
  peut traverser plusieurs supports (le parcours sur l'ambiguïté va de L1 à L4) et un
  support peut nourrir plusieurs parcours. Une bifurcation se raconte en ligne : on
  l'annonce, on suit la première branche, puis la seconde, puis on dit où elles se
  rejoignent.
- **La transition pose la question, pas la réponse.** La page affiche la définition de la
  fiche juste après la transition ; la redire est la faute la plus fréquente. Le
  validateur compte les mots pleins de « Ce que c'est » repris par la transition : au-delà
  de la moitié, avertissement compté en dette. *Mesuré le 2026-09-24 : les transitions qui
  fonctionnent en reprennent au plus 36 %, les paraphrases 56 % et plus ; le contrôle en a
  attrapé 15 sur les 84 de dup, toutes réécrites.*
- **Le rôle dit ce que la fiche fait ici**, pas ce qu'elle est. « Elle porte l'aversion au
  risque. Ici elle ne change jamais : toute l'histoire se joue du côté de la croyance »,
  et non « la fonction qui traduit un résultat en utilité ».
- **Le point de départ est une instance concrète**, prise au monde numérique du cours
  (SPEC-INGESTION étape 3), et le point d'arrivée dit ce que le récit a établi. Le
  validateur avertit quand le départ ne porte aucun chiffre, les numéros de référence
  mis à part ; il ne peut pas vérifier que les chiffres viennent du bon monde. *Mesuré le
  2026-09-25 : 15 départs sur 27 n'en portaient aucun, les 7 de dss compris.*
- **Des phrases, pas des étiquettes** ; aucun nombre que le générateur calcule (le nombre
  d'étapes est affiché) ; aucune arête transcrite en prose (« X et Y donnent Z »).
- **Faire grandir le récit sans perdre le fil.** Quand le cours avance, dans cet ordre de
  préférence : la matière nouvelle **prolonge** le dernier parcours, ou **ouvre** un
  parcours d'ordre supérieur, ou **s'insère** dans un parcours existant à l'endroit où sa
  question se pose. Quand un parcours devient trop long, on le **découpe** en parcours
  consécutifs dont la suite reproduit exactement ses étapes : le premier garde
  l'identifiant (A1), les suivants prennent les ordres qui suivent, et les `ordre` des
  parcours d'après se décalent sans changer d'ordre relatif. Un seul parcours du premier
  chapitre devient ainsi, au fil des semaines, le premier d'une série. Ce qui est interdit
  est ce qui perd le lecteur : retirer une étape, déplacer une étape avant une autre qui
  la précédait, réordonner les parcours (A17).
- **Viser la couverture, pas l'exhaustivité forcée.** Une digression qui couperait le fil
  se déclare `hors_parcours` avec sa raison ; elle n'a pas à entrer dans un récit.

### 8.5 L'histoire qui avance

Le point de départ pose l'histoire ; il ne la contient pas toute. Chaque fiche du parcours
la rappelle en tête — le départ, les suites déjà racontées, puis celle de l'étape — avec en
gras les mots qu'elle traite (SPEC-SITE §3.1). Ce que le lecteur voit sur une fiche est donc
l'histoire telle qu'elle est arrivée jusqu'à lui. *Essayé sur `dup/parcours-risque` le
2026-09-26, en trois versions ; la dernière, retenue : « c'est absolument parfait ».*

- **Le point de départ ne suppose que la première étape.** Aucun terme, aucun calcul
  qu'une étape suivante introduit. *Constaté le 2026-09-26 : un départ complété pour
  couvrir toutes les étapes — second agent, richesse, primes calculées — a été rejeté :
  « dès le point de départ, l'histoire implique déjà des calculs, des termes qu'on n'a
  pas encore abordés ».*
- **L'histoire avance par des suites, là où le récit en a besoin.** Quand le lien d'une
  étape devrait introduire un objet absent de l'histoire — un second agent, une richesse,
  un pari plus petit, une économie —, c'est une ligne « Suite : » à cette étape qui
  l'introduit, jamais le départ. La suite reste dans le monde numérique du cours et ses
  chiffres sont recalculés avant d'être écrits.
- **Une suite pose une seule question : celle que la fiche de son étape résout.** Une
  question qui appartient à l'étape suivante va dans la suite de celle-ci. *Constaté le
  2026-09-26 : la suite de l'aversion absolue demandait « lequel craint le plus le risque,
  et comment le prévoir sans refaire le calcul ? » ; la seconde question est celle de
  l'approximation d'Arrow-Pratt, l'étape d'après.*
- **Le gras tombe sur les mots de la question, pas sur un détail.** À l'aversion absolue,
  « Lequel des deux craint le plus le risque », et non « un second agent, d'utilité
  $\ln x$ ». Une étape sans citation dit pourquoi dans sa phrase — une règle de cohérence,
  comme l'axiome d'indépendance, n'est pas un fait de l'histoire.
- **L'histoire parle la langue du cours dès qu'elle l'a apprise.** Une notion racontée à
  une étape antérieure se nomme : « la prime de risque du premier n'est plus que de 4,3 »,
  et non « il n'abandonne plus que 4,3 », que ne comprend pas qui ne connaît pas le cours.
  Une notion à venir ne se nomme pas.
- **La phrase de lien relie la fiche aux données de l'histoire.** Quand la fiche pose une
  formule, le lien dit pourquoi cette forme-là et l'évalue sur les nombres de l'histoire :
  $A(x)=-U''(x)/U'(x)$, parce que $U''$ seule change quand on double $U$ ; $1/200$ et
  $1/100$ pour les deux agents à 100. Le lien ne redit pas la transition : celle-ci vient
  de l'étape précédente, le lien vient de l'histoire.
- **Deux passes.** On écrit le départ et un lien par étape ; puis on relit les liens un à
  un et, pour chacun qui introduit un objet absent, on écrit la suite à l'étape concernée.
  *Mesuré le 2026-09-26 : au premier jet, 10 étapes sur 17 de `dup/parcours-risque`
  introduisaient dans leur lien un objet que l'histoire ne contenait pas.*
- **Mêmes symboles que la fiche** (A12) : le lien écrit la formule avec les lettres de la
  « Forme » de sa fiche.

### 8.6 L'histoire d'abord, les fiches ensuite

Un parcours n'est pas une liste de fiches qu'on relie après coup : c'est une histoire à
laquelle on accroche des fiches. Écrit dans l'autre sens — les fiches dans l'ordre du
support, une transition qui résume chacune, une histoire ajoutée par-dessus —, il se lit
comme une suite d'arrêts. *Constaté le 2026-09-26 sur fpp, dont les parcours avaient été
découpés pour couvrir les 55 fiches dans l'ordre du poly, puis dotés d'histoires :
« rien n'est logique », alors que ceux de dup, écrits d'emblée comme des récits, « tout
s'agence bien ». Deux relectures phrase à phrase n'y avaient rien changé.*

- **Écrire l'histoire d'abord, d'un seul tenant.** Avant de toucher au fichier, écrire en
  prose continue l'histoire du parcours : un départ, puis la question que chaque réponse
  fait naître, jusqu'à l'arrivée. Ensuite seulement, repérer à quel moment chaque fiche
  sert, et découper. Si une fiche ne trouve pas de moment, elle va dans un autre parcours
  ou `hors_parcours` (A16) — l'histoire ne se tord pas pour la faire passer.
- **L'ordre des étapes est celui de l'histoire, pas celui du support.** Le support est une
  référence, pas un plan. Quand les deux divergent, l'histoire gagne, dans la limite
  d'A14 ; réordonner un fil déjà scellé se déclare comme refonte (A17).
- **La question avant la réponse.** Une fiche qui dit *ce qu'on cherche* vient avant celle
  qui le calcule. *Constaté : le prix à terme était calculé à l'étape 3 de
  `fpp/parcours-terme`, et l'étape 5 expliquait seulement ensuite que l'inconnue était le
  prix inscrit dans le contrat.*
- **Chaque étape fait avancer.** Chaque réponse apporte quelque chose que les étapes
  précédentes n'avaient pas, et ouvre la question de l'étape suivante. Trois étapes qui
  répondent chacune un peu à la même question sont une seule étape de l'histoire : les
  fiches en trop vont ailleurs, ou deviennent « à savoir avant ».
- **Un seul point de vue.** L'histoire suit un personnage — l'acheteur, l'épargnant, la
  banque — et le garde. Si une fiche est écrite d'un autre point de vue (le vendeur
  quand l'histoire suit l'acheteur), la transition le dit : « le vendeur, lui, fait le
  même montage ». *Constaté : la réplication statique « livre » l'action, du côté du
  vendeur, dans une histoire où l'on veut l'acheter ; le lecteur ne savait pas d'où
  venait la livraison.*
- **Une seule voix.** La transition parle comme l'histoire : la question que le lecteur se
  pose à cet instant, avec les objets de l'histoire, et non un résumé abstrait de la fiche
  (« la réplication donne la réponse d'un coup, pour une famille entière de contrats »).
- **Le test de lecture.** `python tools/recit.py <code> [<parcours>]` imprime le parcours
  comme l'étudiant le lit : départ, transitions, suites, réponses, arrivée, sans
  marqueurs. On le lit d'une traite, sans ouvrir aucune fiche. Chaque endroit où l'on
  s'arrête — un mot inconnu, un nombre dont on ne voit pas l'origine, une question déjà
  posée, un changement de personnage, une réponse qui arrive avant sa question — est à
  reprendre. Aucun contrôle automatique ne remplace ce test : les mesures essayées
  (citations répétées, étapes qui reviennent au départ) ne distinguaient pas fpp de dup.
  Le rapport dit, parcours par parcours, que le test a été fait et ce qu'il a trouvé.
