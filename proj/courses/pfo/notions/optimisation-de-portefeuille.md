---
id: pfo/optimisation-de-portefeuille
nom: Optimisation de portefeuille
type: abstraite
statut: source
cas_de: pfo/paradigme-de-markowitz
parametre: l'objectif optimisé, et ce qui est tenu fixe
construite_a_partir_de:
- pfo/moments-du-portefeuille
alias:
- portfolio optimization
- problème de Markowitz
- formulations du problème de portefeuille
refs:
- p. 38
- §3.0.5
---

## Ce que c'est
Choisir les poids d'un portefeuille en résolvant un problème d'optimisation sous contraintes, qui arbitre entre son rendement espéré et son risque. [p. 38]

## Ce que les membres partagent
Toutes les formulations cherchent un vecteur de poids $W$, sous les mêmes contraintes : poids de somme un, et positifs ou nuls. Toutes jugent un portefeuille sur les mêmes deux nombres, $W^T\mu$ et $\sqrt{W^T\boldsymbol{\Sigma}W}$. [p. 38, §3.0.2, §3.0.3]

Elles diffèrent par ce qu'elles optimisent : la première fixe un rendement cible et minimise le risque, la seconde maximise le rendement excédentaire par unité de risque. [p. 38]

## Pourquoi ce niveau existe
Le cours pose les formulations ensemble, comme deux approches « étroitement liées » d'un même problème, et consacre une section entière à les relier : la première construit la frontière efficiente, la seconde choisit un point sur elle. [p. 38, §3.0.4, §3.0.5]

Séparées, elles cacheraient ce qui les unit : le portefeuille de ratio de Sharpe maximal est lui-même un portefeuille efficient, celui où la fonction qui associe à chaque rendement cible le ratio de Sharpe du portefeuille efficient atteint son maximum. [§3.0.4]

## Le chemin jusqu'ici
Tout le problème s'écrit dans les deux moments de pfo/moments-du-portefeuille : le rendement espéré, linéaire en les poids comme le veut pfo/piege-d-agregation pour pfo/rendement-arithmetique, et la variance, lue dans pfo/matrice-de-covariance. [ajout]

Cette matrice est estimée sur pfo/rendement-logarithmique, annualisée par fpp/echelonnement-de-la-variance, et sa diagonale porte le carré de fpp/volatilite. Le décor vient de la décision : dup/loterie résumée par dup/moyenne-variance, et dup/diversification, qui montrait qu'un mélange peut être moins risqué que ses parties. Optimiser, c'est chercher le meilleur de ces mélanges. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| objectif | frontière efficiente | minimiser $\tfrac12W^T\boldsymbol{\Sigma}W$ sous $W^T\mu=\mu_0$ |
| objectif | portefeuille tangent | maximiser $(W^T\mu-R_f)/\sqrt{W^T\boldsymbol{\Sigma}W}$ |
[§3.0.2, §3.0.3]

L'exercice 1 du cours en ajoute un troisième cas, sans cible de rendement : minimiser la seule variance, ce qui donne le portefeuille de variance minimale globale. [p. 52]

## Cesse d'être valide quand
Les formulations supposent un investisseur qui juge un portefeuille sur sa seule moyenne et sa seule variance, sur une seule période. Tout ce que le chapitre 2 a mesuré au-delà — asymétrie, queues épaisses — leur échappe. [ajout]
