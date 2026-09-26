---
id: fpp/produit-a-capital-garanti
nom: Produit à capital garanti
symbole: '$V_0$, $C_0$, $k$'
type: notion
statut: source
construite_a_partir_de:
- fpp/parite-call-put
- fpp/formule-black-scholes
alias:
- principal protected product
- capital garanti
- produit structuré
- structured product
- coussin
- taux de participation
refs:
- §9.2
- exos §2.2
- exo. 17
- exo. 18
---

## Ce que c'est
Un placement qui rend au moins le capital à l'échéance, construit avec un zéro-coupon et des calls, ou avec le sous-jacent et un put. [§9.2]

## Forme
$$C_0=V_0\big(1-e^{-rT}\big),\qquad k=\frac{C_0}{V_0\,\mathrm{Call}(S_0=1,K=1)},\qquad \text{paiement : }V_0+k\,V_0\Big(\frac{S_T}{S_0}-1\Big)^+$$ [exo. 17]

## Ce que les symboles modélisent
$V_0$ est le montant investi et garanti. $C_0$, le coussin, est ce qui reste une fois acheté le zéro-coupon qui rendra $V_0$ ; ce n'est pas le prix d'un call. $k$ est la participation : la part de la hausse de l'action que le placement reverse. [exo. 17]

## Retrouver la formule
![Un zéro-coupon qui rend V₀ en T, plus des calls, égale un paiement qui ne descend jamais sous V₀ et reverse une part k de la hausse. Le zéro-coupon coûte V₀ e^(−rT) ; le coussin qui reste, C₀ = V₀ (1 − e^(−rT)), achète les calls, d'où k = C₀ / (V₀ Call(S₀ = 1, K = 1)).](figures/produit-a-capital-garanti.svg) [§9.2, ajout]

On investit 100 pour un an, avec un taux de 4 %. Rendre 100 dans un an coûte un zéro-coupon de 96,08 : le coussin vaut 3,92. [exo. 17, ajout]

Un call à la monnaie sur l'action à 100 coûte 9,93. Le coussin en achète $3{,}92/9{,}93=0{,}395$ : la participation vaut 39,5 %. [exo. 17, ajout]

En lettres, le coussin est $V_0(1-e^{-rT})$ et un call ramené à un placement de 1 coûte $\mathrm{Call}(S_0=1,K=1)$ : [exo. 17]

$$k=\frac{C_0}{V_0\,\mathrm{Call}(S_0=1,K=1)}$$ [exo. 17]

## Ce qui la définit
Ce qui est **connu** : le montant, le taux, la maturité et le prix des calls. Ce qu'on **cherche** : la participation à la hausse. Elle croît avec le taux, qui grossit le coussin, et baisse avec la volatilité, qui renchérit les calls. [exo. 17, ajout]

Le poly donne deux constructions, zéro-coupon plus call, ou action plus put ; par la parité call-put, elles paient la même chose. Le livre d'exercices montre, avec quatre ans à 4 %, une volatilité de 15 % et un dividende de 1,88 %, une participation proche de 100 % ; ce n'est pas un arbitrage, car le produit renonce aux dividendes. La même construction, un actif plus un put, protège une entreprise qui attend des dollars contre leur baisse. [§9.2, exo. 17, exo. 18]

## Le chemin jusqu'ici
fpp/parite-call-put montre que les deux constructions du poly sont la même ; fpp/formule-black-scholes donne le prix des calls, donc la participation. [ajout]

Derrière elles : fpp/option et fpp/payoff pour le paiement ; fpp/modele-black-scholes pour sa loi, avec fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre autour de fpp/prix-forward, le fpp/taux-de-dividende et les fpp/dividendes-intermediaires auxquels le produit renonce, fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne. [ajout]

Le zéro-coupon de la garantie vient de fpp/zero-coupon, actualisé comme dans fpp/valeur-actuelle-nette et selon fpp/capitalisation ; fpp/cash-and-carry et fpp/absence-d-arbitrage fixent le prix forward qui entre dans les calls. [ajout]

## Exemple minimal
100 investis pour un an, à 4 %, avec une volatilité de 20 % : le capital est garanti et la participation vaut 39,5 %. [ajout]

## Geste de calcul type
Le livre d'exercices : à 4 % sur quatre ans, le coussin vaut $1-e^{-0,16}=14{,}79\,\%$ du montant investi. [exo. 17]

## Cesse d'être valide quand
La garantie ne vaut que ce que vaut l'émetteur du zéro-coupon ; et la participation fond quand les taux baissent, parce que le coussin fond avec eux. [ajout]
