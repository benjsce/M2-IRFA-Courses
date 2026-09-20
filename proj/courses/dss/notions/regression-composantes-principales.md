---
id: dss/regression-composantes-principales
nom: Régression sur composantes principales
type: notion
statut: source
cas_de: dss/reduction-de-dimension
valeur: 'non : les directions ne dépendent que des prédicteurs'
construite_a_partir_de:
- dss/composante-principale
alias:
- PCR
- principal components regression
refs:
- slide 75
- slide 76
- slide 77
- slide 78
- slide 85
---

## Ce que c'est
Construire les $M$ premières composantes principales, puis les utiliser comme prédicteurs d'une régression par moindres carrés. [slide 75]

## Forme
$$\hat{\mathbf{y}}^{\text{pcr}}_{(M)}=\bar y\mathbf{1}+\sum_{m=1}^{M}\hat\theta_m\mathbf{z}_m,\qquad \hat\theta_m=\frac{\langle \mathbf{z}_m,\mathbf{y}\rangle}{\langle \mathbf{z}_m,\mathbf{z}_m\rangle}$$ [slide 76]

## Ce qui la définit
Les composantes étant orthogonales, la régression se réduit à une somme de régressions univariées : chaque coefficient se calcule indépendamment des autres. [slide 76]

L'hypothèse de fond est explicite et n'est pas garantie : on suppose que les directions où les prédicteurs varient le plus sont celles qui sont liées à la réponse. [slide 75]

La parenté avec ridge est étroite, et la différence tient en un mot. Ridge rétrécit toutes les directions et n'en annule aucune ; la régression sur composantes principales, elle, ne rétrécit pas du tout ou annule complètement. [slide 77, slide 78]


## Le chemin jusqu'ici
La chaîne est droite : dss/apprentissage-supervise, dss/moindres-carres-ordinaires, dss/decomposition-en-valeurs-singulieres, puis dss/composante-principale. [ajout]

Chaque étape est un changement de base, jamais un changement de méthode : à l'arrivée on fait toujours des moindres carrés, mais sur les composantes au lieu des prédicteurs. [ajout]

## Exemple minimal
Sur les données Credit, l'erreur de validation croisée ne chute franchement qu'à partir de la dixième composante. [slide 84]

## Geste de calcul type
Standardiser, construire les composantes, faire varier $M$ et lire la courbe d'erreur de validation croisée : le biais baisse et la variance monte avec $M$. [slide 85]

## Cesse d'être valide quand
Ce n'est pas une méthode de sélection de variables, le cours insiste. Et rien ne garantit que les premières composantes aient à voir avec la réponse. [slide 85, slide 86]
