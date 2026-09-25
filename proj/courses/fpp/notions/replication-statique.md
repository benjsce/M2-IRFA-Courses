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
Acheter le sous-jacent, le porter et le livrer, sans aucun geste entre-temps. [§3.1]

## Forme
$$(S_T-K)-\left(S_T-\dfrac{S_t}{P(t,T)}\right)=\dfrac{S_t}{P(t,T)}-K$$ [§3.1]

## Retrouver la formule
![Les quatre flux du montage. En $t$, l'emprunt paie l'action et le solde est nul ; en $T$, on livre l'action contre $K$ et on rembourse $S_t/P(t,T)$. Entre les deux, aucun geste. Un flux reçu monte, un flux payé descend.](figures/replication-statique.svg) [ajout]

En $t$ : emprunter $S_t$ et acheter l'action avec. Le montage ne coûte rien. [ajout]

En $T$ : livrer l'action contre $K$, rembourser $S_t/P(t,T)$. Le solde, $K-S_t/P(t,T)$, est connu dès $t$ : il ne dépend pas de $S_T$. C'est le montage du vendeur à terme ; l'acheteur a le solde opposé, celui de la forme. [ajout]

Le P&L est non aléatoire et le portefeuille coûte zéro : il vaut donc zéro, ce qui détermine $K$. [§3.1]

$$K=\dfrac{S_t}{P(t,T)}$$ [§3.1]

## Ce qui la définit
Le P&L est non aléatoire et le portefeuille coûte zéro : il vaut donc zéro, ce qui détermine $K$. [§3.1]

## Exemple minimal
Action à 100, $P(0,1)=0{,}9608$ : acheter l’action à crédit et la livrer dans un an donne $K=104{,}08$. [ajout]

## Geste de calcul type
Écrire le portefeuille qui reproduit le payoff, en compter le coût, l’égaler à zéro : acheter l’action à 100 en s’endettant et la livrer donne $K=100/0{,}9608=104{,}08$. [§3.1]

## Cesse d'être valide quand
Exige un payoff linéaire *et* un refinancement connu dès $t$. La première condition tombe avec les options, la seconde avec les futures. [§3.1, §4.2.2]

## Origine
- exercice fpp/ex-06 : emprunter, changer, porter, livrer — le seul cas du cours où l'écart résiduel se mesure et se rattache à l'arrondi du prix affiché [exo. 6]
- exercice fpp/ex-12 : la réplication ne demande aucun geste entre-temps, donc aucune hypothèse de modèle : l'arbitrage tient sans Black et Scholes [ajout]
- exercice fpp/ex-20 : quatre montages sur le Nikkei en 2013, trois identiques au dollar près ; l'identité se vérifie numériquement sur un cas historique [exo. 20]
