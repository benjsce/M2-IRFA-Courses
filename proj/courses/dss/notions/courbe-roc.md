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
Le tracé du taux de vrais positifs contre le taux de faux positifs quand le seuil de décision balaie toutes ses valeurs. [slide 12, ajout]

## Forme
$$\text{GINI} = 2\times\mathrm{AUC} - 1$$ [slide 12]

## Ce que les symboles modélisent
Le taux de vrais positifs, $\mathrm{TP}/\mathrm{P}$, est la part des défauts que le modèle détecte ; le taux de faux positifs, $\mathrm{FP}/\mathrm{N}=1-$ spécificité, la part des bons clients qu'il refuse. [slide 10, slide 12]

AUC, l'aire sous la courbe, résume toute la courbe en un nombre entre zéro et un, qui ne dépend d'aucun seuil. Ce n'est pas une proportion de bonnes réponses. [slide 12, ajout]

## Ce qui la définit
Le modèle note chaque dossier d'un score, et annonce un défaut au-delà d'un seuil. **Ce qui est connu** : le score et l'étiquette de chaque dossier passé. **Ce qu'on ignore** : le seuil que la banque choisira. Chaque seuil donne une matrice de confusion, donc un point de la courbe ; en baissant le seuil, on refuse davantage et l'on monte le long de la courbe. La tracer pour tous les seuils évite d'en choisir un : ce qui reste mesure la capacité du score à ranger les défauts avant les autres. [ajout]

Le classifieur aléatoire est la diagonale, d'aire un demi ; le classifieur parfait est le coin supérieur gauche, d'aire un. Le GINI réétale l'aire sur $[-1,1]$ pour qu'un tirage au hasard vaille zéro. [slide 12, ajout]

![Une courbe d'AUC 0,75, l'exemple, entre la diagonale du hasard et le coin du classifieur parfait. Trois seuils y sont marqués : chacun est une matrice de confusion, donc un point, et baisser le seuil fait monter le long de la courbe. L'aire grisée sous elle est l'AUC, et le GINI vaut $2\times0{,}75-1=0{,}50$. La forme de la courbe, celle de deux scores gaussiens de même écart type, est choisie pour le dessin.](figures/courbe-roc.svg) [ajout]

## Le chemin jusqu'ici
dss/apprentissage-supervise fournit l'étiquette de chaque dossier, et dss/matrice-de-confusion les quatre comptes qu'on en tire à un seuil donné. [ajout]

La courbe n'ajoute aucun ingrédient : elle refait la matrice pour chaque seuil et empile les résultats. C'est le balayage qui est nouveau, pas le contenu. [ajout]

## Exemple minimal
Une AUC de 0,75 donne un GINI de 0,50. [ajout]

## Geste de calcul type
Lire l'AUC, la doubler, retirer un : c'est le GINI, l'unité dans laquelle le cours compare ses modèles de crédit. Une AUC de 0,7568 donne 0,5136, que le tableau du cours écrit 51,36. [slide 12, slide 17]

## Cesse d'être valide quand
L'AUC ne dit rien du coût relatif d'un faux positif et d'un faux négatif : deux courbes de même aire peuvent être très inégales dans la zone qui intéresse le métier. [ajout]
