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
Reproduire un contrat à terme en achetant le sous-jacent à crédit aujourd'hui, en le gardant et en le livrant à l'échéance, sans aucun geste entre-temps. [§3.1]

## Forme
$$(S_T-K)-\left(S_T-\dfrac{S_t}{P(t,T)}\right)=\dfrac{S_t}{P(t,T)}-K$$ [§3.1]

## Ce que les symboles modélisent
La Forme est la position d'un acheteur à terme qui fait, en face, le montage inverse. $(S_T-K)$ est ce que lui rapporte le contrat : recevoir l'action, qui vaut $S_T$, contre $K$. $\left(S_T-S_t/P(t,T)\right)$ est ce que rapporte l'action achetée à crédit, qui vaut $S_T$ et laisse une dette de $S_t/P(t,T)$ ; le signe moins dit qu'il en tient l'opposé. Leur différence ne contient plus $S_T$. [§3.1, ajout]

$t$ est la date où l'on monte l'opération et $T$ l'échéance. $S_t$, le prix de l'action aujourd'hui, est connu ; $S_T$, son prix en $T$, est aléatoire vu de $t$. $K$ est le prix de livraison inscrit dans le contrat : c'est lui qu'on cherche. [§3.1, ajout]

$P(t,T)$ est le prix en $t$ du zéro-coupon qui paie une unité en $T$ ; diviser par lui, c'est capitaliser, et $S_t/P(t,T)$ est ce qu'on rembourse en $T$ pour avoir emprunté $S_t$. Ce n'est pas le prix d'un put. [§3.1, ajout]

## Retrouver la formule
![Le montage du vendeur à terme, celui qui livre. En $t$, il emprunte $S_t$ et achète l'action avec : solde nul. En $T$, il livre l'action contre $K$, le seul montant cherché, et rembourse $S_t/P(t,T)$, connu dès $t$. Entre les deux, aucun geste. Un flux reçu monte, un flux payé descend.](figures/replication-statique.svg) [ajout]

On se place du côté du **vendeur à terme**, celui qui devra livrer l'action en $T$ contre $K$ ; son solde est l'opposé de celui de la Forme. **Connus aujourd'hui** : le prix de l'action $S_t$ et celui du zéro-coupon $P(t,T)$. **Cherché** : $K$. [ajout]

En $t$, le vendeur emprunte $S_t$ et achète l'action avec : le montage ne lui coûte rien. [§3.1]

En $T$, il livre l'action contre $K$ et rembourse son emprunt. Chaque unité due en $T$ ne lui a rapporté que $P(t,T)$ en $t$ : pour avoir emprunté $S_t$, il doit donc $S_t/P(t,T)$. [ajout]

Son solde en $T$, $K-S_t/P(t,T)$, ne dépend pas de ce que vaut alors l'action : il est connu dès $t$. [§3.1]

Un solde certain, obtenu sans rien débourser, ne peut être que nul. Positif, ce serait un gain sans risque ni mise ; négatif, le montage inverse (vendre l'action à découvert, placer le produit, acheter à terme) en serait un. [§3.1]

$$K=\dfrac{S_t}{P(t,T)}$$ [§3.1]

## Ce qui la définit
Tout se décide en $t$ et rien ne se touche ensuite : c'est ce qui rend le solde de l'échéance connu dès aujourd'hui, et ce que dit le mot « statique ». [ajout]

## Exemple minimal
Action à 100, $P(t,t+1)=0{,}9608$ : le vendeur emprunte 100, achète l'action et la livre dans un an contre $K=104{,}08$, exactement ce qu'il rembourse. [ajout]

## Geste de calcul type
Écrire le montage, en compter le solde à l'échéance, l'égaler à zéro : emprunter 100 pour acheter l'action et la livrer donne $K=100/0{,}9608=104{,}08$. [§3.1]

## Cesse d'être valide quand
Exige un payoff linéaire *et* un refinancement connu dès $t$. La première condition tombe avec les options, la seconde avec les futures. [§3.1, §4.2.2]

## Origine
- exercice fpp/ex-06 : emprunter, changer, porter, livrer — le seul cas du cours où l'écart résiduel se mesure et se rattache à l'arrondi du prix affiché [exo. 6]
- exercice fpp/ex-12 : la réplication ne demande aucun geste entre-temps, donc aucune hypothèse de modèle : l'arbitrage tient sans Black et Scholes [ajout]
- exercice fpp/ex-20 : quatre montages sur le Nikkei en 2013, trois identiques au dollar près ; l'identité se vérifie numériquement sur un cas historique [exo. 20]
