---
id: fpp/prix-forward
nom: Prix forward
symbole: $F(t,T)$
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: une action
construite_a_partir_de:
- fpp/cash-and-carry
alias:
- forward price
- valeur forward
- forward value
refs:
- Déf. 8
- §3.1
---

## Ce que c'est
Le prix, fixé aujourd'hui, auquel une action sera livrée en T : son prix comptant capitalisé jusqu'à T. [Déf. 8, §3.1]

## Forme
$$F(t,T)=\frac{S_t}{P(t,T)}=S_t\,e^{R(t,T)(T-t)}$$ [§3.1, Déf. 8]

## Ce que les symboles modélisent
$F(t,T)$ prend deux dates, celle où l'on fixe le prix et celle de la livraison ; c'est un prix, en euros. Le poly l'écrit $F(S,T)$ dans sa définition 8, une coquille pour $F(t,T)$. L'écart $F(t,T)-S_t$ s'appelle la **base**. [Déf. 8, ajout]

## Retrouver la formule
![Deux façons d'avoir l'action en T, qui ne coûtent rien aujourd'hui. ① L'acheter à terme : rien en t, et en T on paie F et on reçoit l'action. ② L'acheter aujourd'hui à crédit : on emprunte S_t et on achète l'action ; la dette grandit jusqu'à S_t / P(t,T), remboursés en T. ③ Même action à l'arrivée, même coût au départ : même paiement en T, F(t,T) = S_t / P(t,T).](figures/prix-forward.svg) [ajout]

L'action vaut 100 aujourd'hui, et le zéro-coupon à un an 0,9608. [ajout]

① Acheter l'action à terme ne coûte rien aujourd'hui ; dans un an, on paie $F$ et on reçoit l'action. [§3.1]

② L'acheter aujourd'hui à crédit ne coûte rien non plus : on emprunte 100 et on les donne pour l'action. Emprunter 100 jusqu'à l'échéance, c'est rembourser $100/P(t,T)=100/0{,}9608=104{,}08$ ; dans un an, on rembourse 104,08 et on garde l'action. [§3.1]

③ Les deux montages finissent avec la même action et n'ont rien coûté au départ : ils doivent demander le même paiement à l'arrivée, sinon on achèterait par le moins cher en vendant par l'autre, sans risque. Donc $F=104{,}08$, et en lettres : [§3.1, ajout]

$$F(t,T)=\frac{S_t}{P(t,T)}$$ [§3.1, Déf. 8]

## Ce qui la définit
Ce qui est **connu** : le prix comptant et le zéro-coupon. Ce qu'on **cherche** : le prix de livraison qui rend le contrat gratuit. C'est ce que coûte l'action livrée par portage, achetée aujourd'hui et financée jusqu'à l'échéance. [§3.1]

La base est le coût de ce portage ; elle se referme à l'échéance, où le prix forward et le prix comptant se confondent. Le poly en déduit que le prix forward varie comme l'action moins le zéro-coupon, $dF_t/F_t=dS_t/S_t-dP_t/P_t$, soit en moyenne $(\mu-r)\,dt$. [Déf. 8, §3.1]

## Le chemin jusqu'ici
fpp/cash-and-carry produit ce prix : c'est le coût certain d'une action livrée par portage. Ce coût est un emprunt remboursé en $T$, évalué par fpp/zero-coupon ; fpp/absence-d-arbitrage en fait le seul prix possible ; fpp/capitalisation l'écrit en taux continu, $S_t\,e^{R(t,T)(T-t)}$. [ajout]

## Exemple minimal
L'action vaut 100, le taux à un an 4 % : le prix forward à un an vaut 104,08 et la base 4,08. [ajout]

## Geste de calcul type
Diviser le prix comptant par le zéro-coupon de l'échéance : à deux ans, $100/0{,}9048=110{,}52$. [§3.1]

## Cesse d'être valide quand
Si l'action verse un dividende avant l'échéance, le prix forward est plus bas. L'écriture $S_t\,e^{r(T-t)}$, que le poly donne aussi, n'est qu'une approximation par un taux constant. [§3.2, §3.1]
