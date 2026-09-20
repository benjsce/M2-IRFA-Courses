---
id: dup/assurance-probabiliste
nom: Assurance probabiliste
type: notion
statut: source
cas_de: dup/violation-de-l-independance
valeur: une couverture qui ne joue qu’une fois sur deux
construite_a_partir_de:
- dup/aversion-au-risque
alias:
- probabilistic insurance
refs:
- L2 slide 10
- L2 slide 12
- L2 slide 13
---

## Ce que c'est
Une assurance à demi-prime qui ne couvre qu’une fois sur deux, refusée par 80 % des sujets alors que la théorie la recommande. [L2 slide 10]

## Forme
$$\begin{pmatrix}w-L&\pi/2\\ w-y&\pi/2\\ w-y/2&1-\pi\end{pmatrix}\ \succ\ \big(w-y\big)$$ [L2 slide 12]

## Ce qui la définit
La démonstration est en deux temps. L’indépendance donne l’indifférence entre le mélange et l’assurance complète ; puis la branche risquée du mélange est remplacée par sa moyenne, ce qui est une contraction préservant la moyenne, donc préférée par tout agent averse. [L2 slide 12, L2 slide 13]

$$\mathbb{E}[u(P)]-\mathbb{E}[u(M)]=(1-\pi)\Big[u\Big(w-\tfrac{y}{2}\Big)-\tfrac{u(w-y)+u(w)}{2}\Big]\ \ge\ 0$$ [L2 slide 13]

## Le chemin jusqu'ici
Le socle commun mène à dup/aversion-au-risque. [ajout]

L'expérience oppose une prédiction et une observation, et les deux ont besoin de l'aversion au risque : la théorie prédit qu'un agent averse accepte la demi-couverture à demi-prix, 80 % des sujets la refusent. Sans la prédiction chiffrée, il n'y aurait qu'une curiosité ; avec elle, c'est une réfutation. [ajout]

## Exemple minimal
Un assuré indifférent entre payer la prime $y$ et rester exposé devrait préférer strictement payer $y/2$ pour une couverture une fois sur deux. [L2 slide 12]

## Geste de calcul type
Écrire les deux loteries, repérer les branches communes, les annuler, puis appliquer Jensen à ce qui reste. Le signe suit immédiatement de la concavité. [L2 slide 13]

## Cesse d'être valide quand
Le résultat est strict si $u$ est strictement concave, $y>0$ et $\pi<1$. Le risque de non-paiement est un cas voisin mais distinct, qui ne contredit pas directement l’utilité espérée. [L2 slide 13, L2 slide 14]
