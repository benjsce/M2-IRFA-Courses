---
id: dup/utilite-implicite
nom: Utilité implicite
type: notion
statut: source
cas_de: dup/famille-chew-dekel
valeur: une probabilité compensatrice $\rho(R)$ qui dépend de la loterie commune
construite_a_partir_de:
- dup/utilite-ponderee
alias:
- implicit utility
- implicit weighted utility
- Dekel
refs:
- L3 slide 7
- L3 slide 8
---

## Ce que c'est
La compensation autorisée dépend maintenant de la loterie commune avec laquelle on mélange. [L3 slide 7]

## Forme
$$V(P)=\dfrac{\sum_i p_i w\big(x_i,V(P)\big)u(x_i)}{\sum_i p_i w\big(x_i,V(P)\big)}$$ [L3 slide 8]

## Ce qui la définit
La table du cours range les trois degrés : $\rho=\lambda$ pour l’indépendance, $\rho$ indépendant de $R$ pour l’utilité pondérée, $\rho=\rho(R)$ ici. [L3 slide 7]

Le même résultat peut recevoir un poids différent dans une bonne et dans une mauvaise loterie ; il faut résoudre la valeur conjointement avec les poids, ce qui exige des conditions assurant qu’elle est bien définie. [L3 slide 8]

## Exemple minimal
Des poids indépendants de $V$ redonnent l’utilité pondérée ; $\Gamma(x,v)=u(x)$ redonne l’utilité espérée. [L3 slide 8, L3 slide 4]

## Geste de calcul type
Résoudre l’équation de point fixe en $V$ : poser $V$ inconnue, écrire la somme pondérée, et chercher la valeur qui se reproduit elle-même. [L3 slide 8]

## Cesse d'être valide quand
L’intermédiarité est conservée : droites d’indifférence non parallèles, mais aucune attirance pour la randomisation. [L3 slide 8]
