---
id: fpp/echelonnement-de-la-variance
nom: Échelonnement de la variance
type: notion
statut: source
construite_a_partir_de:
- fpp/volatilite
alias:
- scaling of variance
- racine du temps
refs:
- §5.3
---

## Ce que c'est
Sur des accroissements indépendants et stationnaires, la variance croît comme le temps et l’écart type comme sa racine. [§5.3]

## Forme
$$\sigma^2(t_1+t_2)=\sigma^2(t_1)+\sigma^2(t_2)\ \implies\ \sigma^2(T)=\sigma^2T,\qquad \sigma(T)=\sigma\sqrt{T}$$ [§5.3]

## Ce qui la définit
Deux hypothèses seulement : les accroissements sont tirés de la même loi, et ils sont indépendants. L’additivité de la variance suit, et la racine du temps avec elle. [§5.3]

## Exemple minimal
Une volatilité annuelle de 20 % donne $20\sqrt{0{,}25}=10\,\%$ à trois mois. [ajout]

## Geste de calcul type
Pour changer d’horizon, multiplier la volatilité par la racine du rapport des durées — jamais par le rapport lui-même. [§5.3]

## Cesse d'être valide quand
L’indépendance est l’hypothèse fragile : avec un retour à la moyenne ou de l’autocorrélation, l’écart type croît moins vite que $\sqrt{T}$. [ajout]

## Origine
- exercice fpp/ex-18 : passer d'une volatilité annuelle de 10 % à une volatilité trimestrielle de 5 % en divisant par deux, et l'employer aussitôt pour chiffrer une exposition — la fiche donnait $\sigma\sqrt T$ sans l'usage [exo. 18]
