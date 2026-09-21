---
id: dss/r2-ajuste
nom: R2 ajusté
type: notion
statut: source
cas_de: dss/critere-penalise
valeur: un degré de liberté retiré au numérateur et au dénominateur
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- adjusted R2
refs:
- slide 39
- slide 44
---

## Ce que c'est
Le $R^2$ corrigé du nombre de variables, et le seul critère du groupe qui se lit à la hausse. [slide 44]

## Forme
$$R^2_{\text{ajusté}}=1-\frac{\mathrm{RSS}/(n-d-1)}{\mathrm{TSS}/(n-1)}$$ [slide 44]

## Ce que les symboles modélisent
TSS est la dispersion totale de la variable à expliquer : l'erreur qu'on ferait en ne prédisant jamais que la moyenne. C'est l'étalon de la comparaison — le $R^2$ rapporte l'erreur du modèle à celle-là, et non à zéro. [slide 44]

## Ce qui la définit
La correction porte sur les degrés de liberté : ajouter une variable fait baisser la RSS mais aussi $n-d-1$, et le rapport ne diminue que si la baisse de RSS est assez forte. [slide 44]

C'est ce qui lui fait payer un prix pour l'inclusion de variables inutiles, là où le $R^2$ ordinaire monte toujours. [slide 44]


## Le chemin jusqu'ici
Comme les autres critères du groupe, il part de dss/apprentissage-supervise puis de dss/moindres-carres-ordinaires. [ajout]

Ce qu'il corrige n'est pas la RSS seule mais son rapport à la somme totale des carrés : la correction porte sur les degrés de liberté, et c'est pourquoi il se lit à la hausse quand les trois autres se lisent à la baisse. [ajout]

## Exemple minimal
Ajouter une variable qui ne fait pas baisser la RSS fait baisser le $R^2$ ajusté, alors que le $R^2$ ordinaire reste au même niveau. [ajout]

## Geste de calcul type
Retenir la plus grande valeur, à l'inverse des trois autres critères. C'est la seule inversion de lecture du groupe. [slide 40, slide 44]

## Cesse d'être valide quand
Sa justification est plus faible que celle du $C_p$ ou du BIC : c'est un ajustement de degrés de liberté, pas une estimation de l'erreur de test. [ajout]
