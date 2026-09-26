---
id: fpp/cash-and-carry
nom: Arbitrage cash-and-carry
symbole: $S_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/zero-coupon
- fpp/absence-d-arbitrage
alias:
- cash and carry
- cash and carry arbitrage
- portage de l'action
refs:
- §3.1
- exo. 13
---

## Ce que c'est
Acheter l'action aujourd'hui avec de l'argent emprunté et la garder jusqu'en T, pour pouvoir la livrer à terme à un coût connu dès aujourd'hui. [§3.1]

## Forme
$$\underbrace{(S_T-K)}_{\text{achat à terme}}-\underbrace{\Big(S_T-\frac{S_t}{P(t,T)}\Big)}_{\text{action portée à crédit}}=\frac{S_t}{P(t,T)}-K$$ [§3.1]

## Ce que les symboles modélisent
$S_t$ est le prix comptant de l'action aujourd'hui, connu ; $S_T$ son prix à l'échéance, inconnu. $K$ est le prix de livraison écrit dans le contrat à terme. $S_t/P(t,T)$ est ce qu'il faudra rembourser en $T$ pour avoir emprunté $S_t$ aujourd'hui. [§3.1]

## Ce qui la définit
Le poly compare deux positions : acheter l'action à terme au prix $K$, et la porter soi-même, achetée comptant avec de l'argent emprunté. Les deux finissent avec une action en $T$ ; leur écart ne dépend plus de $S_T$. [§3.1]

Ce résultat est **certain**, et on l'obtient sans rien débourser aujourd'hui. S'il n'était pas nul, on le répéterait à volonté : il est donc nul, et $K=S_t/P(t,T)$. Celui qui vend l'action à terme fait exactement ce montage : il livre en $T$ l'action qu'il a achetée et portée. [§3.1, ajout]

![Le portage vu du vendeur à terme. Aujourd'hui, il emprunte 100 et achète l'action : rien ne sort de sa poche. Dans un an, il livre l'action, reçoit K et rembourse 104,08 ; son résultat, K − 104,08, est connu dès aujourd'hui.](figures/cash-and-carry.svg) [ajout]

## Le chemin jusqu'ici
fpp/zero-coupon donne le coût de l'emprunt : emprunter $S_t$ jusqu'en $T$, c'est vendre $S_t/P(t,T)$ zéro-coupons, donc rembourser $S_t/P(t,T)$. fpp/absence-d-arbitrage interdit qu'un résultat certain obtenu sans mise soit autre chose que nul, et fixe ainsi $K$. fpp/capitalisation rappelle ce que coûte le temps qui passe entre l'achat et la livraison. [ajout]

## Exemple minimal
L'action vaut 100 et le zéro-coupon à un an 0,9608 : la porter un an coûte 104,08 remboursés dans un an. [ajout]

## Geste de calcul type
Si un contrat à terme cote 106, vendre à terme, emprunter 100 et acheter l'action : dans un an, on livre l'action, on reçoit 106, on rembourse 104,08 et on garde 1,92. [ajout]

## Cesse d'être valide quand
Les dividendes versés pendant le portage reviennent à celui qui porte l'action et abaissent son coût. Le montage inverse, pour un contrat trop bon marché, demande de vendre l'action à découvert et de prêter au même taux. Le livre d'exercices l'applique aussi aux devises : emprunter en devise locale, changer, placer en devise étrangère. [§3.2, exo. 13, ajout]
