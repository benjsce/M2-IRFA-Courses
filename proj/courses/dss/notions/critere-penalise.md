---
id: dss/critere-penalise
nom: Critère pénalisé
type: principe
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/erreur-de-test
refs:
- slide 38
- slide 39
- slide 40
---

## Ce que c'est
Estimer l'erreur de test en corrigeant l'erreur d'apprentissage d'une pénalité qui croît avec le nombre de variables. [slide 39]

## Ce qui la définit
Tous ajoutent une pénalité à la RSS pour la taille du modèle, et tous servent au même usage : comparer des modèles qui n'ont pas le même nombre de variables. [slide 39]

Un critère ne calcule pas les coefficients : dans chaque modèle comparé, ce sont toujours ceux des moindres carrés, qui minimisent la RSS. La pénalité ne dépend que du nombre de variables, pas de la valeur des coefficients ; elle ne départage donc que des modèles déjà ajustés. [ajout]

C'est la voie indirecte. Elle ne demande qu'un ajustement, là où la validation croisée en demande un par bloc — mais elle suppose une forme de modèle, ce que la validation croisée ne suppose pas. [slide 38]

Trois d'entre eux se lisent dans le sens « plus petit vaut mieux » ; le $R^2$ ajusté se lit dans l'autre sens. [slide 40]


## Le chemin jusqu'ici
dss/apprentissage-supervise donne le cadre, dss/moindres-carres-ordinaires la RSS, dss/erreur-de-test la quantité qu'on cherche à estimer. [ajout]

Le critère est le pont entre les deux dernières : il corrige l'une pour approcher l'autre. Sans la distinction entre erreur d'apprentissage et erreur de test, la pénalité n'aurait pas d'objet. [ajout]

## Exemple minimal
Sur les 20 clients, passer du modèle à deux prédicteurs au modèle complet fait baisser l'erreur d'apprentissage de 0,14 et monter la pénalité du $C_p$ de 0,42 : leur somme est plus basse pour le petit modèle, le bon. [ajout]

## Cesse d'être valide quand
Ces critères estiment l'erreur de test, ils ne la mesurent pas : leur pénalité repose sur une hypothèse de modèle, et $\hat\sigma^2$ doit lui-même être estimé. [ajout]
