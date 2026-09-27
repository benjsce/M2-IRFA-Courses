# LECTURE.md — lire le dépôt sans tout relire

La base grandit chaque semaine, et une session a un budget de lecture fini. Relire tout le
dépôt à chaque session finira par le dépasser, et bien avant cela par noyer ce qui compte.
Ce document dit **ce qui se lit toujours, ce qui se lit selon le travail, et ce qui ne se
lit jamais**. Il ne remplace aucune règle : il dit comment les appliquer en lisant peu.

*Demandé par l'utilisateur le 2026-09-24 : « tu n'es pas obligé de relire tous les autres
cours ; mais sans eux on ne pourrait pas faire les liens entre pfo et fpp ».* Les deux
exigences tiennent ensemble parce qu'un lien se **reconnaît** sur une ligne et ne se
**vérifie** que sur une fiche : la carte donne la ligne de toutes les fiches, et on n'ouvre
que celles qu'elle désigne.

## Ce que coûte chaque partie

Mesuré le 2026-09-24, à quatre caractères par token. Les chiffres vieillissent ;
l'ordre de grandeur, moins.

| partie | tokens |
|---|---|
| CLAUDE.md et les trois SPEC | ≈ 18 k |
| fiches d'un cours | ≈ 20 à 47 k |
| fichiers d'un cours hors fiches (inventaire, registre, parcours, exercices) | ≈ 6 à 20 k |
| tous les rapports | ≈ 86 k |
| tous les scripts de `tools/` | ≈ 53 k |
| un poly de 35 pages lu en images | de loin le plus cher |
| `python tools/carte.py` | ≈ 0,2 k |
| `python tools/carte.py <code> --seul` | ≈ 1 k |
| `python tools/carte.py <code>` (avec une ligne par fiche des autres cours) | ≈ 11 k |

Les cours ne sont pas le poste le plus lourd : les rapports et les scripts le sont.

## Toujours, à chaque session

1. **CLAUDE.md, LECTURE.md, SPEC-MODELE, SPEC-INGESTION, SPEC-SITE, en entier.** Dans
   `proj/` seulement : les copies de la racine sont identiques, et le validateur le vérifie.
2. **`python tools/validate.py`**, dont on lit le résumé et les lignes du cours travaillé.
   Pour filtrer : `python tools/validate.py | grep <code>`.
3. **`python tools/carte.py`** : les cours, leurs tailles, leurs parcours, le dernier
   rapport de chacun, les arêtes entre cours.

## Selon le travail

**Travailler sur un cours** (ingestion, parcours, correction) :

- `python tools/carte.py <code>` : le graphe du cours en une ligne par fiche, ses
  parcours, son inventaire, et une ligne par fiche de **tous les autres cours**. C'est cette
  dernière partie qui permet les liens entre cours sans relire ces cours.
- `python tools/recit.py <code> [<parcours>]` : un parcours tel que l'étudiant le lit, d'un seul
  tenant et sans marqueurs ; c'est le texte du test de lecture (SPEC-MODELE §8.6), à passer sur
  tout parcours écrit ou modifié. Avec `--questions`, chaque étape en une ligne, « mots en gras »
  ? → titre de la fiche : la réponse doit être la notion (SPEC-MODELE §8.5).
- **Deux rapports seulement** : le dernier du cours, et ceux du dernier jour (la carte les
  nomme). Les questions ouvertes, la dette et les abstractions en attente y sont
  recopiées d'un rapport à l'autre ; les rapports plus anciens ne se relisent pas.
- **Les fiches du cours qu'on va toucher, en entier**, et leurs voisines : celles dont
  elles dépendent, celles qui en dépendent (`python tools/confronter.py --aval <id>`), et
  les étapes qui les entourent dans leur parcours. Les autres fiches du cours se lisent
  par la carte.
- **Une fiche d'un autre cours seulement si la carte ou `confronter.py` la désigne** :
  même objet (la volatilité), homonyme, symbole partagé. On la lit alors en entier avant
  d'y poser une arête.

**Lire une source** : seulement le matériau nouveau, et par tranches de pages. Les
chapitres déjà traités ne se relisent pas : l'inventaire les a recensés élément par élément
(A13) et les fiches en portent le contenu. Pour vérifier un point ancien, relire la page
citée par la référence, pas le document.

**Toucher un script** : `grep -n` pour trouver la fonction, puis `sed -n` sur la plage
utile. `build.py` dépasse deux mille lignes ; il ne se lit jamais d'un bloc.

**Relire un cours entier** (écrire tous ses parcours, auditer un cours ancien) : le
confier à des sous-agents, un par tranche du cours, qui rendent des notes compactes —
pour chaque fiche, ce qu'elle résout et ce qui y mène. Les notes servent à construire le
plan ; toute phrase qui sera **écrite dans la base** se vérifie ensuite sur la fiche
elle-même, jamais sur la note d'un sous-agent.

## Jamais

- `site/` : il est généré. Pour vérifier une page, l'ouvrir dans le navigateur ou y
  chercher une chaîne précise.
- Les SVG des figures : ils sont la sortie d'un script, et le validateur vérifie qu'ils
  s'accordent. De même `parcours/fil.yml`, que `build.py` écrit et que le validateur lit.
- Les copies de synchronisation `* 2.md`, `* 2.html` : des doublons que le validateur
  signale et ignore.
- Une sortie longue en entier : `tail`, `head`, `grep`, ou un compte.

## Ce qui rend l'économie possible : le rapport

Si les anciens rapports ne se relisent pas, le dernier doit suffire. Chaque rapport
**recopie** donc ce qui reste ouvert — dette, abstractions en attente, questions sans
réponse, contradictions non tranchées — au lieu de renvoyer à un rapport antérieur. Un
rapport qui écrit « voir le rapport du 20 » oblige la session suivante à le relire.

## Quand ce document ne suffit plus

Si la carte elle-même devient trop longue — plusieurs dizaines de milliers de tokens pour
les autres cours —, la restreindre aux cours listés dans `depend_de` et à ceux qui
partagent un symbole ou un nom avec le cours travaillé, et le dire au rapport. Ce seuil
n'est pas atteint le jour où ce document est écrit.
