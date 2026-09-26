---
id: dss/haute-dimension
nom: Haute dimension
type: notion
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- high-dimensional setting
refs:
- slide 91
- slide 94
---

## Ce que c'est
Le régime où le nombre de variables est du même ordre que le nombre d'observations, ou plus grand. [slide 91]

## Ce qui la définit
Le nombre de variables peut être énorme là où le nombre d'observations reste borné par le coût ou la disponibilité des échantillons. C'est une asymétrie de fait, pas un choix. [slide 91]

Les moindres carrés n'y ont plus leur place : trop souples, ils surajustent. Dès qu'il y a autant de coefficients que d'observations, ils passent exactement par tous les points : la RSS est nulle et le $R^2$ vaut 1, quelles que soient les données, et l'ajustement ne dit plus rien. [slide 91, ajout]

Si la banque décrivait ses 20 clients par 19 prédicteurs, les 20 coefficients, constante comprise, passeraient ainsi par les 20 points, même si aucun prédicteur n'avait de lien avec la perte. C'est le même fait qui rend la colinéarité extrême : toute variable du modèle peut s'écrire comme combinaison linéaire des autres. [slide 94, ajout]

Les méthodes encore utilisables sont la sélection ascendante, ridge, le lasso et la régression sur composantes principales. [slide 91]


## Le chemin jusqu'ici
Le régime se définit contre dss/moindres-carres-ordinaires : il commence là où ils cessent de fonctionner, quand le nombre de prédicteurs mesurés sur chaque observation de dss/apprentissage-supervise rattrape le nombre d'observations, et que l'inégalité $n\gg p$ se retourne. [ajout]

## Exemple minimal
Un jeu de 4 718 gènes mesurés sur 349 patients est en haute dimension : $p$ vaut plus de treize fois $n$. [slide 117]

## Geste de calcul type
Ne jamais rapporter en haute dimension une RSS, une p-value ou un $R^2$ calculés sur les données d'apprentissage : le cours l'interdit explicitement, et demande un jeu de test indépendant ou une erreur de validation croisée. [slide 94]

## Cesse d'être valide quand
Ce n'est pas une méthode mais un régime : il dit quelles méthodes tombent, pas laquelle choisir. [ajout]
