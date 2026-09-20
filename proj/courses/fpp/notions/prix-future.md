---
id: fpp/prix-future
nom: Prix future
symbole: $H_t$
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: $D=B(t,T)$, aléatoire
construite_a_partir_de:
- fpp/replication-dynamique
alias:
- futures
- contrat à terme margé
refs:
- §4.2
- Prop. 3
- Prop. 4
---

## Ce que c'est
Le prix d’un contrat à terme réglé par appels de marge quotidiens. [§4.2, Prop. 3, Prop. 4]

## Forme
$$H_t=\Pi_t\!\left[\dfrac{S_T}{B(t,T)}\right]$$ [§4.2, Prop. 3, Prop. 4]

## Ce qui la définit
Chaque variation est encaissée le jour même et doit être replacée à un taux inconnu : le facteur d’actualisation devient $B(t,T)$. [§4.2, Prop. 3, Prop. 4]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Pas de forme fermée : $H$ ne s’exprime pas en quantités observables en $t$, il faut un modèle de taux. Égale le forward si les taux sont déterministes. [Prop. 4]
