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
La procédure est fixée : choisir une grille de valeurs, estimer par validation croisée l'erreur de test pour chacune, retenir la plus faible. [slide 68]

Un dernier pas est explicitement demandé, et il est facile à oublier : une fois $\lambda$ retenu, le modèle est réajusté sur toutes les observations. [slide 68]

Le problème est le même que pour la sélection de sous-ensemble : il faut départager une famille de modèles. Ce qui change est que la famille est indexée par un réel et non par un entier. [slide 68]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise, dss/moindres-carres-ordinaires, dss/erreur-de-test et dss/compromis-biais-variance donnent dss/regularisation, la famille indexée par $\lambda$ ; dss/validation-croisee donne le moyen de trancher. [ajout]

La méthode ne fournit pas son propre réglage, et c'est pourquoi il faut les deux — et pourquoi cette fiche existe séparément de ridge et du lasso. [ajout]

## Exemple minimal
Sur les données Credit, la courbe d'erreur de validation croisée tracée contre $\lambda$ présente un minimum net, et c'est ce minimum qui fixe la valeur retenue. [slide 69]

## Geste de calcul type
Étendre la grille jusqu'à voir l'erreur remonter des deux côtés : si le minimum est au bord, la grille est trop étroite et la valeur retenue ne veut rien dire. [ajout]

## Cesse d'être valide quand
La valeur retenue dépend du découpage en blocs : sur un petit jeu, deux exécutions de la validation croisée peuvent donner deux $\lambda$ différents. [ajout]
