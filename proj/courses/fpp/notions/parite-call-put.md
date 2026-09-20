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

## Le chemin jusqu'ici
Deux fils se rejoignent ici. Le premier part de fpp/payoff, dont fpp/call et fpp/put sont deux cas ; le second part de fpp/convention-capitalisation et aboutit à fpp/facteur-actualisation. [ajout]

La parité se démontre en deux temps, et le socle le montre : d'abord une identité entre payoffs, vraie état par état ; ensuite seulement l'actualisation, pour passer des payoffs aux prix. C'est pourquoi elle ne demande aucun modèle — elle tient là où Black et Scholes ne tient plus. [ajout]

## Exemple minimal
Avec $S_0=100$, $K=100$, $P(0,1)=0{,}9608$ : $C-P=100-96{,}08=3{,}92$. [ajout]

## Geste de calcul type
Connaissant l’un des deux prix, en déduire l’autre sans modèle. Si les deux sont cotés et que la parité n’est pas respectée, l’écart est un arbitrage. [Prop. 7]

## Cesse d'être valide quand
Énoncée sans dividende dans la source. Avec un dividende, $S_0$ est remplacé par $S_0\Phi$, et l’identité de payoff reste mais l’identité de prix change. [ajout]

## Origine
- exercice fpp/ex-10 : quatre inconnues, une équation ; on l'emploie dans les quatre sens, ici pour extraire le strike [ajout]
- exercice fpp/ex-12 : elle ne sert pas qu'à calculer un prix manquant, elle sert à **tester une table de prix** — trois strikes, trois valeurs de $C-P+K$ [exo. 12]
- exercice fpp/ex-14 : la démonstration ne demande ni modèle ni Black et Scholes, seulement une identité de payoff, la loi du prix unique et la linéarité [exo. 14]
- exercice fpp/ex-16 : emploi le plus inattendu — séparer la dette risquée en dette sans risque **moins un put** vendu aux actionnaires [exo. 16]
