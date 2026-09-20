# Rapport d'ingestion — spec-ingestion — 2026-09-20

Deuxième session du jour, après `2026-09-20-site.md`. Aucune fiche n'a été touchée.
Objet : intégrer la révision de `SPEC-INGESTION.md` fournie par l'utilisateur et la
répercuter sur le site.

Le nom du fichier s'écarte de la convention `AAAA-MM-JJ-<code>.md` : la session ne porte
sur aucun cours. Même écart, même raison que `2026-09-20-site.md`.

## Matériau traité
`~/Downloads/SPEC-INGESTION.md`, version du 2026-09-20 16:21. Diff contre la version du
dépôt : **une seule modification**, étape 3, puce « Exemple minimal ».

```diff
-- **« Exemple minimal »** : une instance chiffrée, une ligne, sans calcul.
+- **« Exemple minimal »** : une instance chiffrée, une ligne, sans calcul. Elle ne dépend
+  d'aucun exercice et s'écrit dès la création de la fiche ; la laisser en dette est une
+  faute de protocole.
```

Installée à l'identique dans les deux copies du dépôt (`SPEC-INGESTION.md` à la racine et
`proj/SPEC-INGESTION.md`), fins de ligne LF vérifiées, les deux copies restent identiques.

## Ce que cette phrase change

Elle ne change pas le modèle, elle change une **classification**. Quinze rubriques
« Exemple minimal » portent `à venir [ajout]` depuis l'amorçage. Elles étaient comptées en
dette ; elles ne le sont plus : ce sont des fautes de protocole.

La lecture est confirmée par le plan de rapport de l'étape 6, qui n'a jamais listé les
exemples dans la section « Dette » : seulement « liens a-venir · gestes à venir · éléments
d'inventaire a_venir ». Et par SPEC-MODELE §2.1, où la tolérance `à venir` n'est écrite
que pour la rubrique 6, « Geste de calcul type », jamais pour la rubrique 5.

Autrement dit, le validateur est aujourd'hui plus laxiste que les trois documents de loi :
il traite les deux rubriques de la même façon, en **W**. Voir la question 1.

## Inventaire ajouté (à auditer par l'utilisateur)
Aucun.

## Notations ajoutées ou en collision
Aucune.

## Fiches créées
Aucune.

## Fiches modifiées
**Aucune.** Les quinze fiches concernées n'ont pas été touchées : écrire leurs exemples
minimaux demande la source et relève d'une session d'ingestion. Voir la question 2.

## Abstractions créées / insérées
Aucune.

## Abstractions en attente
Inchangé : `sensibilite` (membre unique `duration`) ; `swap` sous `contrat-prime-nulle`.

## Générateur — ce qui a été repris dans `tools/build.py`

Aucune modification de `courses/`, de `validate.py` ni du test de disposition.

| endroit | avant | après |
|---|---|---|
| carte du cours | « exemples minimaux à venir : 15 » dans le bandeau Dette | bandeau distinct « Faute de protocole », au-dessus de la Dette, citant l'étape 3 |
| bandeau Dette | liens · exemples · gestes · inventaire | liens · gestes · inventaire, exactement le plan de l'étape 6 |
| fiche | rubrique « Exemple minimal » neutre | rubrique bordée, intitulé en ambre, mention « faute de protocole », et la phrase de l'étape 3 citée sous le « à venir » |
| accueil | dette : inventaire, gestes, liens | idem, plus « 15 exemples minimaux manquants (faute de protocole) » |
| `build.py` | — | avertissement sur `stderr` à chaque build tant qu'il en reste |

La couleur de la faute (`--faute`) est distincte de celle de « Cesse d'être valide quand »
(`--lim`) : une limite de validité est une information du cours, une faute de protocole est
une dette envers le protocole. Les confondre visuellement serait une erreur.

## Dette

Après reclassement, et à contenu inchangé :

| poste | avant | après |
|---|---|---|
| liens à venir | 0 | 0 |
| gestes de calcul à venir | 15 | 15 |
| éléments d'inventaire à venir | 55 | 55 |
| *exemples minimaux à venir* | *15, comptés en dette* | *15, hors dette : fautes de protocole* |

Le validateur continue de les compter dans sa ligne `dette` ; le site et le build les en
sortent. C'est précisément la divergence de la question 1.

## Contradictions source
Aucune nouvelle.

## Questions pour l'utilisateur

1. **Faut-il promouvoir « Exemple minimal à venir » de W en E dans `validate.py` ?**
   C'est ce que disent maintenant les trois documents lus ensemble. Conséquence immédiate :
   15 erreurs, graphe invalide, `build.py` refuse de construire jusqu'à ce que les quinze
   exemples soient écrits. Je ne l'ai pas fait : CLAUDE.md interdit de toucher au validateur
   pour contourner un axiome, et l'inverse — le durcir au point de bloquer le dépôt — est
   une décision de modèle, pas d'opérateur. Recommandation : écrire d'abord les quinze
   exemples (question 2), promouvoir en E ensuite, dans le même mouvement. Sinon le dépôt
   reste bloqué entre les deux.
2. **Voulez-vous que j'écrive les quinze exemples minimaux ?** C'est une vraie session
   d'ingestion sur `sources/financial_products_lecture_notes.pdf` : quinze fiches
   existantes modifiées, donc quinze entrées « Fiches modifiées » au rapport, ancien texte
   → nouveau. Les fiches concernées sont listées sur `site/fpp/index.html`. À faire avant
   ou après l'audit des références de l'amorçage (point 4 du README) ; je recommande après,
   pour ne pas écrire un exemple sur une référence qui se révélerait fausse.
3. Les questions 1 à 4 de `2026-09-20-site.md` restent ouvertes (README à jour, MathJax
   CDN/offline, `site/` à commiter, pliage de « Cesse d'être valide quand »).

## Validation
```
25 notions · 0 erreur · 88 avertissement(s)
dette (validateur) : Exemple minimal à venir = 15, Geste de calcul type à venir = 15,
                     inventaire à venir = 55
dette (site, après reclassement) : gestes 15, inventaire 55, liens 0
                                   + 15 fautes de protocole hors dette
test_layout : ok fpp (complet) 19 nœuds · ok fpp (ajouts masqués) 13 nœuds
site : 36 fichiers, la plus lourde 27 ko
```
