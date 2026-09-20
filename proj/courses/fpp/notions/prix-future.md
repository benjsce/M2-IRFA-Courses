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

## Le chemin jusqu'ici
fpp/convention-capitalisation et fpp/facteur-actualisation donnent le prix du temps ; fpp/compte-capitalise donne celui de l'argent réinvesti au jour le jour ; fpp/replication-dynamique dit comment le répliquer. [ajout]

Le future se distingue du forward par une seule chose : les appels de marge quotidiens, donc un réglage à chaque pas. C'est pourquoi son socle passe par le compte capitalisé alors que celui du forward n'en a pas besoin. Les deux prix coïncident quand les taux sont déterministes — et le socle montre exactement où cette hypothèse entre. [ajout]

## Exemple minimal
Sous-jacent à 100, taux déterministes, $B(0,1)=P(0,1)=0{,}9608$ : $H_0=104{,}08$, égal au forward. [ajout]

## Geste de calcul type
Vérifier d’abord si les taux sont déterministes : si oui, $B=P$ et le future vaut le forward, 104,08. Sinon il n’y a pas de forme fermée et il faut un modèle de taux. [Prop. 4]

## Cesse d'être valide quand
Pas de forme fermée : $H$ ne s’exprime pas en quantités observables en $t$, il faut un modèle de taux. [§4.2, §4.2.2]

Égale le forward si les taux sont déterministes. [Prop. 4]

## Origine
- exercice fpp/ex-07 : une option sur future se price avec la formule du cours en posant $q=r$, sans rien redémontrer [exo. 7]
- exercice fpp/ex-14 : le prix forward est une martingale sous $\mathbb{Q}$ — c'est pourquoi la formule de Black n'a pas de terme de dérive [exo. 14]
- exercice fpp/ex-20 : à taux nuls, future = comptant, et deux stratégies distinctes deviennent indiscernables (Prop. 4 sur un cas réel) [exo. 20]
