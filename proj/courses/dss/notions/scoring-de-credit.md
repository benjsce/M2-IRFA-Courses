---
id: dss/scoring-de-credit
nom: Scoring de crédit
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- credit scoring
refs:
- slide 17
- slide 204
- slide 205
---

## Ce que c'est
Prédire si une contrepartie fera défaut à partir de ses caractéristiques, pour décider d'un octroi, d'un suivi ou d'un recouvrement. [slide 17, slide 205]

## Ce qui la définit
**Ce qui est connu** : les caractéristiques de chaque entreprise et, pour les anciennes, si elles ont fait défaut. **Ce qu'on cherche** : si celle qui demande un crédit fera défaut. L'étiquette est donc un binaire, défaut ou non, et les variables explicatives décrivent l'entreprise. [slide 205, ajout]

Dans l'article du cours : 12 544 entreprises du périmètre européen, 343 variables de chiffre d'affaires, de marge et autres, un facteur binaire de défaut. [slide 205]

La mesure d'usage n'est pas l'exactitude mais le GINI : il note la capacité du score à ranger les défauts avant les autres, de 0 pour un tirage au hasard à 1 pour une séparation parfaite, et le tableau du cours l'écrit en points, sur 100. [slide 12, slide 17, ajout]

Il ne dépend d'aucun seuil de décision, ce qui permet de comparer des modèles sans en fixer un. [ajout]

## Le chemin jusqu'ici
Tout repose sur dss/apprentissage-supervise : pour les anciens emprunteurs, l'étiquette de défaut est connue, et c'est ce qui rend le problème traitable. [ajout]

## Exemple minimal
Dans le tableau comparatif du cours, la régression logistique obtient un GINI de 51,36 points, soit 0,5136, et la forêt aléatoire 57,84. [slide 17]

## Cesse d'être valide quand
Un score figé ne tient pas : le cours conclut que seuls des cadres dynamiques sont viables, et que les modèles avancés n'ont de sens que si de nouveaux flux de données sont captés. [slide 214]
