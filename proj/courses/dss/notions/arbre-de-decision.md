---
id: dss/arbre-de-decision
nom: Arbre de décision
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- decision tree
- arbre de régression
- regression tree
- arbre de classification
refs:
- slide 97
- slide 98
- slide 104
- slide 115
- slide 125
---

## Ce que c'est
Un modèle qui prédit par une suite de questions à seuil sur les prédicteurs : chaque question coupe les exemples en deux groupes, et l'on prédit, dans le groupe où l'on tombe, la moyenne des réponses. [slide 115, slide 125, ajout]

## Forme
$$\text{question : } x_j\le s\ ?\qquad\text{choisie pour rendre minimale}\qquad\sum_{x_{ij}\le s}\big(y_i-\bar y_{\text{oui}}\big)^2+\sum_{x_{ij}>s}\big(y_i-\bar y_{\text{non}}\big)^2$$ [slide 104, slide 115, ajout]

$$\text{prédiction pour un nouveau client : }\ \bar y_{\text{oui}}\ \text{ou}\ \bar y_{\text{non}},\ \text{la moyenne de son groupe}$$ [ajout]

## Ce que les symboles modélisent
$x_j$ est l'un des prédicteurs, et $s$ le seuil de la question ; $x_{ij}$ est la valeur de ce prédicteur pour l'ancien client $i$, et $y_i$ sa perte. $\bar y_{\text{oui}}$ et $\bar y_{\text{non}}$ sont les pertes moyennes des anciens clients qui ont répondu oui et non. La somme à rendre minimale est la RSS des deux groupes, ce que le cours appelle leur impureté. [slide 104, ajout]

## Ce qui la définit
**On connaît** les anciens clients, leurs prédicteurs et leur perte. **On cherche** la question qui sépare le mieux les pertes fortes des pertes faibles : on essaie chaque prédicteur et chaque seuil, et l'on garde celui qui laisse les deux groupes les plus homogènes. Puis on recommence dans chaque groupe, question après question, jusqu'à une taille minimale de groupe. [slide 115]

![Les 20 clients de la banque, la perte en fonction de x₃, une variable sans lien avec la perte. La meilleure première question est x₃ ≤ 0,22 : 8 clients répondent oui, de perte moyenne 2,43, et 12 non, de perte moyenne 4,39. Les deux paliers bleus sont les prédictions ; les traits gris, les écarts à la moyenne de chaque groupe, dont la somme des carrés passe de 44,03 à 25,60.](figures/arbre-de-decision.svg) [ajout]

Un groupe final s'appelle une feuille, ou nœud terminal ; un arbre à $d$ coupures a $d+1$ feuilles. En classification, la feuille prédit la classe majoritaire, et l'impureté se mesure par l'indice de Gini. [slide 104, slide 125, ajout]

## Le chemin jusqu'ici
dss/apprentissage-supervise fournit les couples dont l'arbre a besoin : des anciens clients dont on connaît la perte. Toutes les questions de l'arbre sont choisies pour reproduire ces pertes, et chaque prédiction est une moyenne de pertes déjà observées. [slide 7, ajout]

## Exemple minimal
Sur les 20 clients, la première question est $x_3\le0{,}22$ : un nouveau client de $x_3=0{,}5$ répond non, et l'arbre à une question lui prédit une perte de 4,39. [ajout]

## Geste de calcul type
Pour chaque prédicteur et chaque seuil entre deux valeurs observées, calculer la somme des carrés des écarts dans les deux groupes, puis garder le minimum. Sur les 20 clients, une seule moyenne, 3,60, laisse 44,03 ; la question $x_3\le0{,}22$ fait descendre la somme à 25,60, mieux que toute question sur l'endettement. [ajout]

## Cesse d'être valide quand
L'arbre est instable : ses questions dépendent de quelques clients. Sur les 190 façons de retirer deux clients parmi les 20, la première question cesse de porter sur $x_3$ dans 42 cas, et passe alors le plus souvent à l'endettement, au seuil 42. Découper les données autrement donne un autre arbre : c'est la forte variance que le cours lui reproche. [slide 97, slide 98, ajout]

Il coupe aussi sur le bruit : ici, sa première question porte sur une variable sans lien avec la perte, qu'une coïncidence de l'échantillon a liée à elle. Poussé jusqu'à des groupes d'un seul client, il apprend les pertes par cœur. [ajout]
