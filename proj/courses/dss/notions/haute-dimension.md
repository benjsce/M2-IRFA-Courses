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

Les moindres carrés n'y ont plus leur place : trop souples, ils surajustent. Les méthodes utilisables sont la sélection ascendante, ridge, le lasso et la régression sur composantes principales. [slide 91]

La colinéarité y est extrême, au sens fort : toute variable du modèle peut s'écrire comme combinaison linéaire des autres. [slide 94]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/moindres-carres-ordinaires. [ajout]

Le régime se définit contre eux : ce qui le caractérise est l'endroit exact où l'inégalité $n\gg p$ se retourne. Sans l'estimateur de référence, il n'y aurait rien à opposer. [ajout]

## Exemple minimal
Un jeu de 4 718 gènes mesurés sur 349 patients est en haute dimension : $p$ vaut plus de treize fois $n$. [slide 117]

## Geste de calcul type
Ne jamais rapporter en haute dimension une RSS, une p-value ou un $R^2$ calculés sur les données d'apprentissage : le cours l'interdit explicitement, et demande un jeu de test indépendant ou une erreur de validation croisée. [slide 94]

## Cesse d'être valide quand
Ce n'est pas une méthode mais un régime : il dit quelles méthodes tombent, pas laquelle choisir. [ajout]
