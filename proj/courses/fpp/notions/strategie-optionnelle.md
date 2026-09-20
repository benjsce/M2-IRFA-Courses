---
id: fpp/strategie-optionnelle
nom: Stratégie optionnelle
type: abstraite
statut: ajout
cas_de: fpp/contrat-a-prime
valeur: une combinaison de payoffs élémentaires
parametre: le sens de la position optionnelle
construite_a_partir_de:
- fpp/payoff
alias:
- options use cases
refs:
- §9
- §9.1
---

## Ce que c'est
Assembler des options élémentaires pour obtenir un profil de gain qu’aucune ne donne seule. [§9.1]

## Ce que les membres partagent
Toutes se construisent par somme et différence de calls, de puts et de zéro-coupons ; toutes se valorisent donc par simple addition de prix, par linéarité de l’opérateur de prix. [§9.1, ajout]

## Pourquoi ce niveau existe
Le §9 présente deux usages qui ne diffèrent que par le sens de la position : on achète l’optionalité pour se protéger, on la vend pour encaisser la prime. Les séparer sans les réunir ferait manquer que c’est la même mécanique lue à l’envers. [ajout]

## Cesse d'être valide quand
L’addition de prix suppose qu’on peut traiter chaque jambe séparément, sans coût de transaction ni contrainte de marge. [ajout]

## Origine
- exercice fpp/ex-11 : « acheter le call, vendre le put » n'est pas une stratégie optionnelle — c'est un forward déguisé, le profil n'est pas coudé [ajout]
- exercice fpp/ex-15 : le butterfly est écarté non parce qu'il a le mauvais signe, mais parce que son véga change de signe selon l'endroit où se trouve le sous-jacent [ajout]
