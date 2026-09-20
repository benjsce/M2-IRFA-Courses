---
id: dup/critique-de-borch
nom: Critique de Borch
type: notion
statut: source
construite_a_partir_de:
- dup/moyenne-variance
- dup/dominance-stochastique-ordre-1
alias:
- Borch's critique
refs:
- L1 slide 16
---

## Ce que c'est
Un classement fondé sur le seul couple moyenne-écart type peut déclarer indifférentes deux distributions dont l’une domine l’autre au premier ordre. [L1 slide 16]

## Ce qui la définit
La moyenne et l’écart type jettent de l’information distributionnelle que tout agent monotone à utilité espérée, lui, valorise. [L1 slide 16]

## Le chemin jusqu'ici
Deux fils y mènent. Le premier réduit dup/loterie à dup/moyenne-variance : c'est le critère attaqué. Le second l'évalue par dup/fonction-utilite et dup/utilite-esperee, d'où sort dup/dominance-stochastique-ordre-1 : c'est l'arme de l'attaque. [ajout]

La critique consiste exactement à faire se heurter les deux : une paire de distributions que moyenne-variance déclare indifférentes alors que l'une domine l'autre au premier ordre. Il fallait donc les deux critères au socle — une critique a besoin de deux règles qui se contredisent. [ajout]

## Cesse d'être valide quand
La critique ne mord ni sous utilité quadratique, ni sur les familles de distributions où deux moments suffisent. [L1 slide 14]
