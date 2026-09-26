---
id: dss/choix-du-parametre-de-reglage
nom: Choix du paramètre de réglage
type: notion
statut: source
construite_a_partir_de:
- dss/regularisation
- dss/validation-croisee
alias:
- selecting the tuning parameter
refs:
- slide 68
- slide 69
- slide 70
---

## Ce que c'est
Retenir la valeur de la pénalité qui minimise l'erreur estimée sur des données non vues. [slide 68]

## Ce qui la définit
On connaît, pour chaque valeur de $\lambda$ d'une grille, une erreur de test estimée par validation croisée ; on cherche $\lambda$. On retient la valeur où cette erreur estimée est la plus basse. [slide 68]

Un dernier pas est explicitement demandé, et il est facile à oublier : une fois $\lambda$ retenu, le modèle est réajusté sur toutes les observations. [slide 68]

Le problème est le même que pour la sélection de sous-ensemble : il faut départager une famille de modèles. Ce qui change est que la famille est indexée par un réel et non par un entier. [slide 68]

## Le chemin jusqu'ici
dss/regularisation fournit une famille de modèles indexée par $\lambda$ : la somme des carrés des erreurs de dss/moindres-carres-ordinaires, qui ajuste les couples observés de dss/apprentissage-supervise, plus une pénalité dont dss/compromis-biais-variance dit qu'elle peut payer. Elle ne fournit pas son propre réglage. [ajout]

dss/validation-croisee fournit le moyen de trancher : elle estime, sans clients nouveaux, l'erreur que définit dss/erreur-de-test, pour chaque valeur de $\lambda$ comme pour chaque modèle. C'est pourquoi cette fiche existe séparément de ridge et du lasso. [ajout]

## Exemple minimal
Sur les 20 clients, avec ridge et les cinq blocs de 4 clients, l'erreur estimée vaut 2,22 à $\lambda=0$, 2,13 au plus bas, à $\lambda=5$ sur la grille $0, 1, \dots, 10$, et 2,46 à $\lambda=100$ : la courbe est presque plate, et $\lambda=5$ est retenu. [ajout]

![Ridge sur les 20 clients. En trait plein, ce qui est connu : pour chaque $\lambda$, l'erreur estimée par validation croisée sur cinq blocs de 4 clients. On retient le $\lambda$ où elle est la plus basse, voisin de 5. En pointillés, ce qu'elle cherche à estimer et que la banque ne voit pas : l'erreur sur 20 000 clients nouveaux, la plus basse, elle, à $\lambda$ presque nul.](figures/choix-du-parametre-de-reglage.svg) [ajout]

Le cours montre la même allure sur des données de crédit : une courbe presque plate, un creux à peine marqué, et un $\lambda$ retenu petit, qui change peu les coefficients des moindres carrés. [slide 69]

## Geste de calcul type
Étendre la grille jusqu'à voir l'erreur remonter des deux côtés : si le minimum est au bord, la grille est trop étroite et la valeur retenue ne veut rien dire. [ajout]

## Cesse d'être valide quand
La valeur retenue dépend du découpage en blocs : sur un petit jeu, deux exécutions de la validation croisée peuvent donner deux $\lambda$ différents. [ajout]

Et l'erreur estimée sur un petit jeu est elle-même bruitée. Sur les 20 clients, elle réclame $\lambda=5$, et ce choix fait monter l'erreur mesurée sur 20 000 clients nouveaux de 1,83, à $\lambda=0$, à 2,43. [ajout]
