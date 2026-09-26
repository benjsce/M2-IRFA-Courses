---
id: fpp/amelioration-de-rendement
nom: Amélioration de rendement
type: notion
statut: source
cas_de: fpp/strategie-optionnelle
valeur: on vend l’optionalité
construite_a_partir_de:
- fpp/call
- fpp/put
alias:
- return enhancement
- covered call
refs:
- §9.3
---

## Ce que c'est
Vendre des calls ou des puts pour encaisser la prime, en échange d’un profil de gain tronqué. [§9.3]

## Ce qui la définit
**Ce qu'on reçoit est connu aujourd'hui** : la prime. **Ce qu'on cède est inconnu** : toute la hausse au-delà du strike. Le rendement amélioré est celui du portefeuille qu'on détient déjà : la prime s'y ajoute, tant que le sous-jacent ne monte pas trop. [§9.3, ajout]

![Deux gains à l'échéance pour une action achetée 100 : l'action seule, et l'action avec le call de strike 100 vendu, prime comprise sans ses intérêts. En dessous de 100, la seconde fait mieux de 9,93, la prime connue aujourd'hui ; elle ne perd qu'en dessous de 90,07. Au-dessus, elle plafonne à 9,93 et cède la hausse : l'action seule fait mieux à partir de 109,93.](figures/amelioration-de-rendement.svg) [ajout]

C'est le sens inverse du produit à capital protégé : on vend l'optionalité au lieu de l'acheter, et l'on porte donc le risque que l'acheteur a cédé. Vendre un call contre l'action détenue ou vendre un put contre un zéro-coupon donne le même profil, par la même parité : $\text{Spot}-\text{Call}=\text{ZC}-\text{Put}$. C'est pourquoi le poly range sous ce nom la vente de calls comme la vente de puts. [§9.3, Prop. 7, ajout]

## Le chemin jusqu'ici
fpp/payoff donne la forme générale d'un contrat, et fpp/call comme fpp/put en sont les deux briques élémentaires. [ajout]

L'amélioration de rendement est la première stratégie du cours où l'on est *vendeur* : on encaisse la prime et on accepte de tronquer le gain. Le socle s'arrête aux payoffs parce que le profil se dessine sans prix ; la prime de l'exemple, 9,93, est simplement le prix du call à la monnaie de l'exemple courant. [ajout]

## Exemple minimal
L'action vaut 100 ; le call de strike 100 à un an (taux 4 %, volatilité 20 %) vaut 9,93. Détenir l'action et vendre ce call rapporte 9,93 de plus aujourd'hui, près de 10 % de la mise, au prix de toute la hausse au-delà de 100. [ajout]

## Geste de calcul type
Retrancher le payoff vendu du portefeuille existant et ajouter la prime, sans les intérêts : $\min(S_T,100)-100+9{,}93$. Achetée 100, l'action avec le call vendu ne perd qu'en dessous de $100-9{,}93=90{,}07$ et gagne au plus 9,93 ; l'action seule ne la dépasse qu'au-delà de $100+9{,}93=109{,}93$. [ajout]

## Cesse d'être valide quand
Sous $\mathbb{Q}$, la prime vaut exactement ce qu'on cède : le gain moyen risque-neutre est nul. Le rendement supplémentaire n'est pas un repas gratuit ; c'est le prix de la hausse abandonnée. [ajout]
