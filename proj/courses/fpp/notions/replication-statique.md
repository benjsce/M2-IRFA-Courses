---
id: fpp/replication-statique
nom: Réplication statique
type: notion
statut: source
cas_de: fpp/replication
valeur: aucun rééquilibrage
construite_a_partir_de: []
alias:
- cash and carry
- cash & carry
refs:
- §3.1
---

## Ce que c'est
Acheter le sous-jacent, le porter, le livrer. Aucun geste entre-temps. [§3.1]

## Forme
$$(S_T-K)-\left(S_T-\dfrac{S_t}{P(t,T)}\right)=\dfrac{S_t}{P(t,T)}-K$$ [§3.1]

## Ce qui la définit
Le P&L est non aléatoire et le portefeuille coûte zéro : il vaut donc zéro, ce qui détermine $K$. [§3.1]

## Exemple minimal
Action à 100, $P(0,1)=0{,}9608$ : acheter l’action à crédit et la livrer dans un an donne $K=104{,}08$. [ajout]

## Geste de calcul type
Écrire le portefeuille qui reproduit le payoff, en compter le coût, l’égaler à zéro : acheter l’action à 100 en s’endettant et la livrer donne $K=100/0{,}9608=104{,}08$. [§3.1]

## Cesse d'être valide quand
Exige un payoff linéaire *et* un refinancement connu dès $t$. La première condition tombe avec les options, la seconde avec les futures. [§3.1, §4.2.2]
