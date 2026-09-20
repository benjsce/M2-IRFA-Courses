---
id: dup/theorie-du-regret
nom: Théorie du regret
type: notion
statut: source
cas_de: dup/axiome-independance
valeur: la comparaison état par état avec l’option abandonnée
construite_a_partir_de:
- dup/acte
alias:
- regret theory
refs:
- L1 slide 58
---

## Ce que c'est
La valeur d’un résultat dépend de ce qu’on aurait obtenu en choisissant autrement. [L1 slide 58]

## Forme
$$v(x,y)\quad\text{où }y\text{ est le résultat de l’option abandonnée dans le même état}$$ [L1 slide 58]

## Ce qui la définit
Regret quand le résultat choisi est le moins bon, satisfaction quand il est le meilleur. Le choix dépend donc de la comparaison état par état, et non de la seule distribution marginale de chaque acte. [L1 slide 58]

## Exemple minimal
Deux loteries statistiquement identiques peuvent être évaluées différemment selon l’option à laquelle on les oppose. [L1 slide 58]

## Geste de calcul type
Ne pas réduire chaque acte à sa distribution : écrire la table état par état, et comparer ligne à ligne. [L1 slide 58]

## Cesse d'être valide quand
Le modèle abandonne la transitivité dans ses versions les plus simples : c’est le prix payé pour la dépendance au contexte. [ajout]
