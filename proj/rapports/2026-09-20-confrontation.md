# Rapport d'ingestion — confrontation à l'existant — 2026-09-20

*Session hors cours : elle porte sur le protocole, le validateur et un outil nouveau.
Le nom du fichier suit la convention des sessions sans cours (SPEC-INGESTION, étape 6).*

## Matériau traité

Aucune source nouvelle. La question posée était : *quand un cours nouveau arrive, ou la
suite d'un cours, qu'est-ce qui permet de reconnaître de façon fiable ce qui est déjà
écrit ?* L'étape 2 de SPEC-INGESTION prescrit cette confrontation depuis le début. Rien
ne la calculait, et deux des règles qu'elle énonce étaient fausses.

Fichiers touchés : les quatre documents de loi (deux copies chacun), `tools/validate.py`,
`tools/confronter.py` (nouveau), `tools/tests/test_garde_fous.py` (nouveau), et les trois
`notation.yml`. **Aucune fiche n'a été modifiée.**

## Ce que la mesure a montré avant d'agir

| question | mesure |
|---|---|
| noms ou alias partagés par deux fiches | 1 paire, `dup/prime-de-risque` ↔ `fpp/prime-de-risque`, sur le nom **et** sur l'alias `risk premium` |
| dans un même cours | aucune |
| symboles présents dans deux registres ou plus | 10 |
| … dont la collision était déclarée | 5 |
| lettres grecques employées dans une fiche mais absentes du registre du cours | 10 |

La première ligne condamne la règle telle qu'elle était écrite : « prime de risque »
désigne, dans `dup`, ce que l'agent abandonne sur la moyenne pour se débarrasser du risque
[L1 slide 9], et dans `fpp`, le rendement d'un actif au-delà de son coût de financement
[Déf. 2]. Les deux cours emploient en plus la même lettre $\pi$. Ce n'est pas une faute à
interdire, c'est un fait à déclarer.

## Les trous, un par un

### 1. Le nom et l'alias — règle énoncée, jamais vérifiée

SPEC-INGESTION étape 2 disait : « Interdit : créer une fiche dont le nom ou un alias
coïncide avec une fiche existante. **Le validateur le refuse** ». Il ne le refusait pas :
`validate.py` ne portait qu'un seul contrôle touchant au nom, `nom manquant`.

Corrigé en deux temps. Dans un même cours, la coïncidence devient une **erreur** — un
cours ne nomme pas deux notions de la même façon. Entre deux cours, elle devient un
**avertissement** levé par une déclaration `homonymes` dans `notation.yml`. La seule
homonymie du dépôt est déclarée dans `courses/dup/notation.yml`.

### 2. La collision de symbole entre cours — idem

A12 dit : « deux cours peuvent donner deux sens au même symbole ; la collision est
déclarée dans `notation.yml` ». Le validateur vérifiait seulement que le `symbole` d'une
fiche figure au registre de son propre cours. Cinq collisions sur dix n'étaient pas
déclarées : $\gamma$, $\mu$, $\pi$, $\sigma$ entre `dup` et `fpp`, et $\rho$ entre les
trois cours.

Le contrôle exige qu'**une** entrée nomme **tous** les cours concernés, pas un morceau par
cours : le lecteur doit trouver l'histoire entière au même endroit. Les cinq manquantes
sont écrites.

### 3. Le socle qui grandit sous une fiche déjà écrite — ce trou était déjà bouché

SPEC-INGESTION affirmait : « Le validateur ne voit pas ce cas. Il est à vérifier à la
main ». C'était vrai jusqu'au commit `0ba82d7`, qui a rendu obligatoire que « Le chemin
jusqu'ici » nomme chaque notion de son socle. Depuis, le cas se signale tout seul.

Vérifié plutôt qu'affirmé : une notion témoin insérée sous `dss/regression-ridge` dans une
copie du dépôt produit

```
W A1 dss/regression-ridge     : « Le chemin jusqu'ici » ne nomme pas 1 notion(s) de son socle
W A1 dss/lasso                : idem
W A1 dss/comparaison-de-modeles : idem
W A1 dss/biais-societal       : idem
```

— la fiche *et* toute sa descendance par $D^{-1}$, c'est-à-dire exactement la liste que la
spec demandait d'établir à la main. La phrase a été corrigée au lieu d'ajouter un contrôle
qui aurait fait double emploi, et les deux cas sont passés en test de non-régression.

### 4. Le cours fantôme `cs` avait survécu à cinq endroits

Ma vérification de la session précédente cherchait `cs/` avec une barre oblique. Les
occurrences restantes s'écrivaient `cs:`, comme clé de table. Elles sont retirées ici.

### 5. Les quatre documents de loi existaient en double sans garde-fou

Signalé cinq fois au rapport sans être vérifié. `validate.py` compare désormais les deux
copies octet par octet et refuse une divergence.

## Outil nouveau — `tools/confronter.py`

Il n'écrit rien, ne décide rien et retourne toujours 0. Il imprime une liste de travail.
Quatre modes, un par question de l'étape 2 :

| appel | ce qu'il répond | exactitude |
|---|---|---|
| `--refs <code> refs.txt` | la suite d'un cours ouvert : que connaît déjà l'inventaire ? | **exact** (A13 rend l'inventaire exhaustif, la clé est la référence de source) |
| `--noms "<candidat>" …` | ces noms existent-ils ailleurs, avant qu'aucune fiche ne soit écrite ? | approché |
| `--cours <code>` | ce cours recouvre-t-il un autre ? nom, alias, et symboles partagés | approché |
| `--aval <id> …` | quels chemins déjà écrits vais-je périmer en insérant sous ces notions ? | **exact** |

Le rapprochement approché combine deux mesures : mots communs, et similarité de chaîne.
La seconde ne compte que si les deux chaînes partagent une racine de cinq caractères.
Sans ce filtre, la similarité de caractères rapproche n'importe quels noms français de
même longueur — « arbre de décision » et « invariance de description » sortaient à 0,67.

| seuil 0,45, paires inter-cours signalées | sans le filtre | avec |
|---|---|---|
| | 1610 | 71 |

et aucun rapprochement vrai n'est perdu : les six contrôles (`Régression ridge`,
`Prime de risque`, `Bootstrap`, `Validation croisée`, `Forêt aléatoire`,
`Régularisation`) ressortent tous à 1,00 sur leur fiche.

Ce que l'outil ne fait pas : la confrontation « par le sens ». Deux cours peuvent nommer
autrement la même chose, et aucune mesure de chaînes ne le verra. L'outil réduit la
surface à lire, il ne la supprime pas — c'est écrit dans son en-tête et dans la spec.

## Tests

`tools/tests/test_garde_fous.py` fabrique un corpus minuscule en dossier temporaire, y
injecte une faute à la fois, et vérifie que le validateur la voit — et se tait quand elle
est déclarée. Onze cas, tous verts. Un contrôle qu'on n'a jamais vu échouer n'est pas un
contrôle. Le test est entré au déroulé de session dans `CLAUDE.md`.

## Fiches créées

Aucune.

## Fiches modifiées

**Aucune.** Le graphe des notions est inchangé : 199 fiches, mêmes identifiants, mêmes
arêtes, mêmes proses.

## Registres modifiés

| fichier | ancien | nouveau | raison |
|---|---|---|---|
| `courses/fpp/notation.yml` | collision `$P$` · `ailleurs: { cs: probabilité historique }` | `note:` en texte libre, sans clé de cours | `cs` n'est pas un cours de la base ; le fait reste utile à l'étudiant |
| `courses/fpp/notation.yml` | collision `$F$` · `ailleurs: { cs: filtration F_t }` | idem | idem |
| `courses/dup/notation.yml` | — | entrée `$\rho$` · `dup/aversion-second-ordre` · L3 slide 40 · « aversion absolue au risque, $-u''(x)/u'(x)$ » | le symbole est employé dans la formule de la fiche et manquait au registre (A12) |
| `courses/dup/notation.yml` | collision `$\pi$`, `ailleurs` ne nommait que `dup` | `ailleurs` nomme aussi `fpp` | collision inter-cours non déclarée |
| `courses/dup/notation.yml` | — | collisions `$\mu$`, `$\sigma$`, `$\gamma$` avec `fpp` | idem |
| `courses/dup/notation.yml` | — | bloc `homonymes` : « Prime de risque » entre `dup/prime-de-risque` et `fpp/prime-de-risque` | seule homonymie du dépôt |
| `courses/dss/notation.yml` | bloc `collisions` au format `ou:` / `sens:` (9 entrées) | même contenu au format `ici:` / `ailleurs:` / `note:` (8 entrées) | le format de `schema/notation.template.yml` est `ici` / `ailleurs` ; celui que j'avais employé pour `dss` la semaine passée n'était lisible par aucun contrôle. Les deux entrées `$\lambda$` fusionnent en une, qui nomme les quatre emplois |
| `courses/dss/notation.yml` | collision `$\rho$` · `ou: dss · dup/aversion-second-ordre` | `ailleurs: { dup: …, fpp: … }` | la déclaration omettait `fpp/rho`, qui emploie la même lettre |

## Documents de loi modifiés

| fichier | ancien | nouveau | raison |
|---|---|---|---|
| `SPEC-MODELE.md` §1 | codes d'exemple `` `fpp`, `cs`, `dup`, `ml` `` | `` `fpp`, `dup`, `dss` `` | deux des quatre cours cités n'existent pas |
| `SPEC-MODELE.md` §7 | `depend_de: [cs]` | `depend_de: []` | idem |
| `SPEC-MODELE.md` §7 | `ailleurs: { cs: probabilité historique }` | `ailleurs: { dup: une loterie }`, plus un exemple de bloc `homonymes` | idem, et le nouveau bloc doit figurer à l'exemple |
| `SPEC-MODELE.md` A12 | « la collision est déclarée dans `notation.yml` » + « le validateur vérifie que le champ `symbole` … est dans le registre » | même texte, plus : une entrée nomme tous les cours concernés ; les clés de `ailleurs` sont des codes existants ; l'homonymie de nom se déclare sous `homonymes` ; ce que le validateur vérifie exactement, avec **E** ou **W** | l'axiome énonçait une déclaration que rien ne vérifiait, et ne disait rien du nom |
| `SPEC-INGESTION.md` étape 2 | « Le validateur ne voit pas ce cas. Il est à vérifier à la main … » | le contrôle des chemins le signale, sur la fiche et sa descendance ; `--aval` donne la liste avant l'arête. Plus les quatre appels de `confronter.py` et ce que chacun vaut | la phrase décrivait un angle mort fermé depuis `0ba82d7`, et l'étape n'avait aucun outil |
| `SPEC-INGESTION.md` étape 2 | « Interdit : créer une fiche dont le nom ou un alias coïncide … Le validateur le refuse » | interdit dans un même cours ; permis et déclaré entre deux cours, avec l'exemple de la prime de risque | la règle était fausse dans un sens et trop forte dans l'autre |
| `CLAUDE.md` déroulé | 5 = build, 6 = rapport, 7 = commit | 5 = `test_garde_fous.py`, 6 = build, 7 = rapport, 8 = commit | un contrôle qu'on ne voit jamais échouer n'est pas un contrôle |

Les deux copies de chaque document ont reçu la même édition, et le validateur le vérifie
désormais.

## Abstractions créées / insérées

Aucune.

## Abstractions en attente

Inchangé depuis le rapport `2026-09-20-dss.md`.

## Dette

Inchangée : 1 (l'élément d'inventaire `fpp` `exos §2.1`, échéance 2026-09-27). Les cinq
collisions et l'homonymie découvertes en cours de session ont été déclarées dans la
session même ; elles ne passent pas en dette.

## Contradictions source

Aucune nouvelle.

## Questions pour l'utilisateur

- **Dix lettres grecques sont employées dans des formules de fiches sans figurer au
  registre de leur cours** (`dss` : $\Delta$, $\beta$, $\delta$ ; `dup` : $\epsilon$,
  $\phi$, $\theta$, $\zeta$ ; `fpp` : $\Delta$, $\Pi$, $\lambda$), et le comptage ne porte
  que sur les grecques. A12 exige le registre pour « chaque symbole que le cours
  définit » : certaines de ces lettres sont des variables muettes ($\epsilon$ petit,
  $\delta$ incrément) et n'ont rien à y faire, d'autres sont de vrais objets. *Recommandé :
  les trier une fois, cours par cours, plutôt que d'étendre le contrôle A12 aux formules —
  il produirait surtout du bruit.*
- **`build.py` charge le bloc `collisions` dans son modèle et ne l'affiche nulle part.**
  A12 dit « le site affiche le contexte de cours » ; c'est vrai au sens de l'en-tête de
  fiche, qui porte le cours, mais la table des collisions, elle, n'est lue par personne.
  *Recommandé : une page « notations » par cours, symboles et collisions ; SPEC-SITE ne la
  prévoit pas, donc c'est un ajout à décider, pas un trou à boucher.*
- **`fpp/feynman-kac` porte toujours la dépendance redondante `fpp/mesure-risque-neutre`**
  (A8, avertissement présent depuis plusieurs sessions). *Recommandé : la retirer ; le
  socle est inchangé par construction.*

## Validation

```
199 notions · 0 erreur(s) · 2 avertissement(s)
dette : inventaire à venir = 1
```

Les deux avertissements sont antérieurs à cette session (`fpp/feynman-kac`, A8 ;
`fpp` inventaire `exos §2.1`, A13). `tools/tests/test_garde_fous.py` : 11 cas, tous verts.
`tools/tests/test_layout.py` : tous verts. `tools/build.py` : 251 fichiers.
