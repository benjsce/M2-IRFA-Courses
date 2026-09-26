---
id: dss/validation-croisee
nom: Validation croisée
type: notion
statut: source
construite_a_partir_de:
- dss/erreur-de-test
alias:
- cross-validation
- CV
refs:
- slide 38
- slide 45
---

## Ce que c'est
Estimer directement l'erreur de test en réservant tour à tour une part des données. [slide 45]

## Ce qui la définit
**Ce qu'on connaît** : les seules observations dont on dispose. **Ce qu'on cherche** : l'erreur sur des observations qu'on n'a pas. On en fabrique : on coupe les données en blocs, on ajuste le modèle sur tous les blocs sauf un, on mesure l'erreur sur le bloc mis de côté, et l'on recommence jusqu'à ce que chaque bloc ait servi une fois. L'estimation est la moyenne des erreurs mesurées. [slide 182]

![Les 20 clients en 5 blocs de 4, pour le modèle à l'endettement et au revenu : à chaque tour, il est ajusté sur les 16 clients gris et évalué sur les 4 du bloc coloré. À droite, l'erreur mesurée sur le bloc caché ; chaque client sert une fois, et une seule, à l'évaluation. L'estimation de l'erreur de test est la moyenne des cinq, 1,66.](figures/validation-croisee.svg) [ajout]

Pour choisir un modèle, on calcule cette erreur pour chacun des modèles candidats — la suite indexée par la taille $k$ que renvoie une procédure de sélection — et l'on retient le $k$ dont l'erreur estimée est la plus faible. [slide 45]

Contrairement aux critères pénalisés, elle ne suppose rien sur la forme du modèle : elle s'applique à un choix de modèle beaucoup plus large. [slide 45]


## Le chemin jusqu'ici
dss/erreur-de-test est la quantité à estimer, et dss/apprentissage-supervise ce qui rend l'estimation possible : chaque exemple mis de côté porte sa réponse, à laquelle on compare la prédiction. C'est la voie directe : elle ne corrige pas l'erreur d'apprentissage, elle fabrique des données non vues en découpant celles dont on dispose. [ajout]

## Exemple minimal
Sur les 20 clients coupés en 5 blocs de 4, l'erreur moyenne vaut 1,66 pour le modèle à l'endettement et au revenu et 2,22 pour le modèle complet. Sur 20 000 clients nouveaux, les vraies erreurs de test sont 1,16 et 1,83 : la validation croisée range les deux modèles dans le bon ordre, mais surestime leur erreur, en partie parce que chaque ajustement ne voit que 16 clients. [ajout]

## Geste de calcul type
Tracer l'erreur estimée contre la taille du modèle, puis lire le minimum — et, si la courbe est plate, appliquer la règle de l'écart type : retenir le modèle le plus simple dont l'erreur reste à un écart type du minimum. [slide 45, ajout]

## Cesse d'être valide quand
Elle coûte un ajustement par bloc et par modèle candidat, ce que le cours oppose aux critères pénalisés, qui ne demandent qu'un ajustement. [ajout]
