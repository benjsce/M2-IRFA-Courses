---
id: dss/cp-de-mallows
nom: Cp de Mallows
symbole: $C_p$
type: notion
statut: source
cas_de: dss/critere-penalise
valeur: $2d\hat\sigma^2$ ajouté à la RSS
construite_a_partir_de:
- dss/moindres-carres-ordinaires
alias:
- Mallow's Cp
refs:
- slide 39
- slide 41
- slide 42
---

## Ce que c'est
L'estimation de l'erreur quadratique de test d'un modèle des moindres carrés à $d$ prédicteurs. [slide 41]

## Forme
$$C_p=\frac{1}{n}\big(\mathrm{RSS}+2d\hat\sigma^2\big)$$ [slide 41]

## Ce que les symboles modélisent
$d$ compte les prédicteurs du modèle qu'on évalue. $\hat\sigma^2$ estime la variance du bruit, et vient d'un modèle **complet** — pas de celui qu'on est en train de juger, sans quoi le critère se mordrait la queue. $C_p$ combine les deux pour estimer une erreur de test à partir d'une erreur d'apprentissage. [slide 41]

## Ce qui la définit
La pénalité $2d\hat\sigma^2$ corrige exactement ce que l'erreur d'apprentissage sous-estime : plus le modèle porte de variables, plus la correction est forte. [slide 41]

$\hat\sigma^2$ estime la variance de l'erreur associée à chaque mesure de la réponse ; il faut donc un modèle de référence pour l'obtenir. [slide 41]


## Le chemin jusqu'ici
dss/apprentissage-supervise fixe le cadre, dss/moindres-carres-ordinaires fournit la RSS que le critère corrige. [ajout]

La correction porte sur une quantité issue de l'ajustement lui-même, ce qui explique qu'aucun autre ingrédient ne soit nécessaire. [ajout]

## Exemple minimal
Sur les 20 clients, avec $\hat\sigma^2=1{,}40$ estimé sur le modèle complet, $C_p$ vaut 1,40 pour le modèle à deux prédicteurs et 1,68 pour le modèle complet ; il est minimal au premier. [ajout]

![Pour chaque taille de modèle sur les 20 clients, la barre grise est $\mathrm{RSS}/n$, qui baisse toujours, et la barre posée dessus la pénalité $2d\hat\sigma^2/n$, qui monte toujours. Leur somme est $C_p$ : 1,40 à deux prédicteurs, le minimum, et 1,68 pour le modèle complet.](figures/cp-de-mallows.svg) [ajout]

## Geste de calcul type
Calculer $C_p$ pour chaque taille de modèle et retenir le plus petit : une petite valeur indique une erreur faible. [slide 40]

Pour le modèle à deux prédicteurs : $C_p=(22{,}43+2\times2\times1{,}40)/20=(22{,}43+5{,}60)/20=1{,}40$. [ajout]

## Cesse d'être valide quand
Sous modèle linéaire à erreurs gaussiennes, il est équivalent à l'AIC — le cours le dit explicitement. Ce n'est donc pas un critère de plus. [slide 42]
