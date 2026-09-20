---
id: fpp/contrat-derive
nom: Contrat dérivé
type: abstraite
statut: ajout
cas_de: fpp/absence-arbitrage
parametre: le flux échangé à la signature
construite_a_partir_de:
- fpp/mesure-risque-neutre
refs:
- Prop. 6
---

## Ce que c'est
Un engagement dont la valeur dépend d’un sous-jacent. [ajout]

## Ce que les membres partagent
Le même moteur de valorisation : espérance du payoff sous $\mathbb{Q}$, actualisée. Ce qui change en dessous n’est pas le moteur, c’est l’inconnue qu’on y cherche. [ajout]

## Pourquoi ce niveau existe
C’est le niveau qui répond à la question « $\mathrm{NPV}=0$, est-ce propre au forward ? ». Non : c’est l’invariant d’une des deux branches, et il n’existe que parce que l’autre existe. [ajout]

## Le chemin jusqu'ici
Toute la chaîne du prix : fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (sur fpp/convention-capitalisation) donnent fpp/prix-a-terme, qui donne fpp/mesure-risque-neutre. [ajout]

La définition d'un contrat dérivé ne vient qu'après, et c'est volontaire : on ne sait dire « un engagement dont la valeur dépend d'un sous-jacent » que lorsqu'on sait ce qu'est *la valeur* d'un tel engagement. Nommer d'abord et évaluer ensuite aurait inversé la dépendance. [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]
