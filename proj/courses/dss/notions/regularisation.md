---
id: dss/regularisation
nom: Régularisation
type: abstraite
statut: source
cas_de: dss/selection-de-variables
valeur: contraindre tous les coefficients au lieu d'en retirer
parametre: la norme des coefficients que l'on pénalise
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/compromis-biais-variance
alias:
- shrinkage
- regularization
refs:
- slide 46
- slide 47
---

## Ce que c'est
Ajuster un modèle contenant tous les prédicteurs, avec une contrainte qui rétrécit les coefficients vers zéro. [slide 46]

## Ce que les membres partagent
Tous ajoutent à la RSS un terme de pénalité gouverné par un paramètre $\lambda\ge 0$ : à $\lambda=0$ on retrouve exactement les moindres carrés, à $\lambda$ grand tous les coefficients tendent vers zéro, et le modèle vers le modèle nul. [slide 50]

Tous échangent du biais contre de la variance, et tous demandent que les prédicteurs soient standardisés au préalable, puisque la pénalité porte sur l'échelle des coefficients. [slide 52, slide 53]

Le cours présente la régularisation comme sa première arme contre le surapprentissage : elle contraint l'algorithme pour améliorer l'erreur hors échantillon, surtout en présence de bruit. [slide 47]

## Pourquoi ce niveau existe
Le cours construit le lasso entièrement contre la régression ridge, en ne changeant qu'une chose : la norme pénalisée. Le paramètre est donc explicitement isolé par la source, sur la slide qui superpose les deux régions de contrainte, le losange de la norme $\ell_1$ et le disque de la norme $\ell_2$. [slide 62, slide 66]


## Le chemin jusqu'ici
La famille naît de la rencontre de deux choses : dss/apprentissage-supervise puis dss/moindres-carres-ordinaires d'un côté, dss/erreur-de-test puis dss/compromis-biais-variance de l'autre. [ajout]

On contraint l'ajustement, ce qui le dégrade sur les données d'apprentissage, et l'on y gagne sur des données non vues. Tout le contenu de la famille tient dans cet échange. [ajout]

## Cesse d'être valide quand
Le réglage de $\lambda$ n'est pas donné par la méthode : il faut une procédure extérieure, et le cours renvoie à la validation croisée. [slide 50, slide 68]
