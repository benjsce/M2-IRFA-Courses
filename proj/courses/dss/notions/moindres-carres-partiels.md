---
id: dss/moindres-carres-partiels
nom: Moindres carrés partiels
type: notion
statut: source
cas_de: dss/reduction-de-dimension
valeur: 'oui : chaque direction est pondérée par sa liaison à la réponse'
construite_a_partir_de:
- dss/regression-composantes-principales
alias:
- PLS
- partial least squares
refs:
- slide 86
- slide 87
- slide 88
- slide 89
- slide 90
---

## Ce que c'est
La réduction de dimension où la réponse sert à choisir les directions. [slide 87]

## Forme
$$\hat\varphi_{mj}=\langle \mathbf{x}_j^{(m-1)},\mathbf{y}\rangle,\qquad \mathbf{z}_m=\sum_{j=1}^{p}\hat\varphi_{mj}\mathbf{x}_j^{(m-1)}$$ [slide 90]

## Ce qui la définit
Le poids de chaque prédicteur dans la première direction est son produit scalaire avec la réponse : la méthode place donc le poids le plus fort sur les variables les plus liées à ce qu'on veut prédire. [slide 89, slide 90]

Les directions suivantes s'obtiennent en orthogonalisant les prédicteurs par rapport à celles déjà construites, puis en recommençant sur les résidus. [slide 89, slide 90]

La réduction supervisée peut baisser le biais, mais elle a aussi le pouvoir d'augmenter la variance — le cours le dit, sans trancher. [slide 89]


## Le chemin jusqu'ici
La chaîne est celle de la version non supervisée : dss/apprentissage-supervise, dss/moindres-carres-ordinaires, dss/decomposition-en-valeurs-singulieres, dss/composante-principale, puis dss/regression-composantes-principales. [ajout]

La dernière dépendance est tout le contenu de la fiche : les moindres carrés partiels se définissent en changeant une seule chose à la régression sur composantes principales, l'usage de la réponse pour choisir les directions. [ajout]

## Exemple minimal
Un prédicteur orthogonal à la réponse reçoit un poids nul dans la première direction, alors que la régression sur composantes principales pourrait lui en donner un grand s'il est très dispersé. [ajout]

## Geste de calcul type
Standardiser, calculer les produits scalaires avec $\mathbf{y}$ pour la première direction, orthogonaliser, recommencer ; $M$ se choisit par validation croisée comme pour les composantes principales. [slide 89, slide 90]

## Cesse d'être valide quand
L'avantage sur la version non supervisée n'est pas garanti : le cours signale le risque d'augmentation de variance, sans donner de critère pour choisir entre les deux. [slide 89]
