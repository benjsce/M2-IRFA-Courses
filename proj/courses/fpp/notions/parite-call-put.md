---
id: fpp/parite-call-put
nom: Parité call-put
type: notion
statut: source
construite_a_partir_de:
- fpp/call
- fpp/put
- fpp/facteur-actualisation
alias:
- call put parity
- parité
refs:
- Prop. 7
---

## Ce que c'est
La différence entre un call et un put de mêmes strike et maturité est un forward. [Prop. 7]

## Forme
$$(S_T-K)^+-(K-S_T)^+=S_T-K\ \implies\ C(S_0,K,T)-P(S_0,K,T)=S_0-KP(0,T)$$ [Prop. 7]

## Ce qui la définit
C’est une identité de payoff, vraie état par état, donc une identité de prix par absence d’arbitrage. Aucun modèle n’y entre : ni volatilité, ni loi du sous-jacent. [Prop. 7]

## Exemple minimal
Avec $S_0=100$, $K=100$, $P(0,1)=0{,}9608$ : $C-P=100-96{,}08=3{,}92$. [ajout]

## Geste de calcul type
Connaissant l’un des deux prix, en déduire l’autre sans modèle. Si les deux sont cotés et que la parité n’est pas respectée, l’écart est un arbitrage. [Prop. 7]

## Cesse d'être valide quand
Énoncée sans dividende dans la source. Avec un dividende, $S_0$ est remplacé par $S_0\Phi$, et l’identité de payoff reste mais l’identité de prix change. [ajout]
