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
Chaque procédure de sélection renvoie une suite de modèles indexée par la taille $k$ ; la validation croisée calcule une erreur pour chacun et retient le $k$ dont l'erreur estimée est la plus faible. [slide 45]

Contrairement aux critères pénalisés, elle ne suppose rien sur la forme du modèle : elle s'applique à un choix de modèle beaucoup plus large. [slide 45]

Le cours mentionne aussi la règle de l'écart type, qui retient le modèle le plus simple dont l'erreur reste à un écart type du minimum. [slide 45]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/erreur-de-test, qu'il s'agit d'estimer. [ajout]

C'est la voie directe : elle ne corrige pas l'erreur d'apprentissage, elle fabrique des données non vues en découpant celles dont on dispose. [ajout]

## Exemple minimal
Avec dix blocs, le modèle est ajusté dix fois sur 90 % des données et évalué sur les 10 % restants ; l'erreur retenue est la moyenne des dix. [slide 182]

## Geste de calcul type
Tracer l'erreur estimée contre la taille du modèle, puis lire le minimum — et, si la courbe est plate, appliquer la règle de l'écart type plutôt que de prendre le point le plus bas. [slide 45]

## Cesse d'être valide quand
Elle coûte un ajustement par bloc et par valeur du paramètre, ce que le cours oppose aux critères pénalisés, qui ne demandent qu'un ajustement. [ajout]
