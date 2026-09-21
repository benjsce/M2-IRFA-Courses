---
id: dss/courbe-roc
nom: Courbe ROC
symbole: AUC
type: notion
statut: source
construite_a_partir_de:
- dss/matrice-de-confusion
alias:
- ROC curve
- AUC
- Gini coefficient
refs:
- slide 12
---

## Ce que c'est
Le tracé du taux de vrais positifs contre le taux de faux positifs quand le seuil de décision balaie toutes ses valeurs. [slide 12]

## Forme
$$\text{GINI} = 2\times\mathrm{AUC} - 1$$ [slide 12]

## Ce que les symboles modélisent
AUC résume toute la courbe en un nombre entre zéro et un, et ce nombre ne dépend d'aucun seuil : c'est là son intérêt. Un demi est le tirage au sort, un est la séparation parfaite. Ce n'est pas une proportion de bonnes réponses. [slide 12]

## Ce qui la définit
Faire varier le seuil retire du jugement le choix du seuil : ce qui reste mesure la capacité du score à ordonner, pas à trancher. [ajout]

Le classifieur aléatoire est la diagonale, le classifieur parfait est le coin supérieur gauche. L'aire sous la courbe résume la position entre les deux, et le GINI la réétale sur $[-1,1]$ pour qu'un tirage au hasard vaille zéro. [slide 12]


## Le chemin jusqu'ici
dss/apprentissage-supervise donne l'étiquette, dss/matrice-de-confusion les quatre nombres. [ajout]

La courbe n'ajoute aucun ingrédient : elle refait la matrice pour chaque seuil et empile les résultats. C'est le balayage qui est nouveau, pas le contenu. [ajout]

## Exemple minimal
Une AUC de 0,75 donne un GINI de 0,50. [ajout]

## Geste de calcul type
Lire l'AUC, la doubler, retirer un : c'est le GINI, l'unité dans laquelle le cours compare tous ses modèles de crédit. Une AUC de 0,7568 donne 51,36. [slide 12, slide 17]

## Cesse d'être valide quand
L'AUC ne dit rien du coût relatif d'un faux positif et d'un faux négatif : deux courbes de même aire peuvent être très inégales dans la zone qui intéresse le métier. [ajout]
