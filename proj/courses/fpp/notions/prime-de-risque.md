---
id: fpp/prime-de-risque
nom: Prime de risque
symbole: '$\tilde\pi_A$, $\tilde\pi_E$, $\pi_A$, $\pi_E$'
type: notion
statut: source
construite_a_partir_de:
- fpp/bilan
alias:
- risk premium
- prime de risque espérée
- expected risk premium
- rendement excédentaire espéré
- expected excess return
refs:
- Déf. 2
- §1.3
- Rem. 1
---

## Ce que c'est
Ce qu'un actif rapporte au-delà du coût de son financement ; sa moyenne attendue s'appelle la prime de risque espérée. [Déf. 2]

## Forme
$$\tilde\pi_A = \frac{\Delta A_t}{A_t} - \frac{\Delta D_t}{D_t},\qquad \pi_A = E(\tilde\pi_A)$$ [§1.3, Déf. 2]

## Ce que les symboles modélisent
$\tilde\pi_A$, avec le tilde, est la prime réalisée sur une période : une variable aléatoire, le rendement des actifs moins celui de la dette. $\pi_A$, sans tilde, en est la moyenne attendue, tournée vers l'avenir. $\tilde\pi_E$ et $\pi_E$ sont les mêmes objets pour les capitaux propres, dont le rendement remplace celui des actifs. [§1.3, Déf. 2]

Ce sont des taux, exprimés par unité de temps, par an sauf mention contraire. Ce n'est pas la prime de risque du cours dup, qui est un montant qu'un agent abandonne pour ne plus courir un risque. [Rem. 1, ajout]

## Ce qui la définit
On connaît le rendement de l'actif et le coût de la dette qui le finance ; la prime est leur écart. Elle est négative quand l'actif rapporte moins que la dette. [§1.3]

Le poly traite ces primes comme des variables aléatoires stationnaires : c'est ce qui donne un sens à leur moyenne. [§1.3]

L'unité de temps compte. Un taux de 5 % sous-entend 5 % par an, et une journée vaut $1/256$ ou $1/365$ d'année selon la convention retenue. [Rem. 1]

## Le chemin jusqu'ici
fpp/bilan dit comment les actifs sont financés : par des capitaux propres et par une dette. Le rendement de cette dette est le coût du financement, et c'est à lui que la prime compare le rendement de l'actif. [ajout]

## Exemple minimal
Des actifs qui rapportent 6 % sur l'année, financés par une dette qui coûte 4 % : la prime réalisée des actifs vaut 2 %. [ajout]

## Geste de calcul type
Mettre le rendement de l'actif et celui de la dette sur la même période et dans la même unité de temps, puis soustraire : 0,5 % par mois d'un côté contre 4 % par an de l'autre ne se comparent pas tels quels. [Rem. 1, ajout]

## Cesse d'être valide quand
La moyenne $\pi_A$ n'a de sens que si les primes sont stationnaires, hypothèse que pose le poly ; si la loi du rendement change d'une période à l'autre, il n'y a plus une prime espérée mais une par période. [§1.3]
