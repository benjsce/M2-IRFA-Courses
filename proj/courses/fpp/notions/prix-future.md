---
id: fpp/prix-future
nom: Prix future
type: notion
statut: source
construite_a_partir_de:
- fpp/contrat-future
- fpp/compte-capitalise
alias:
- future price
- futures price
- prix du future
refs:
- Prop. 3
- Prop. 2
- Prop. 4
- §4.2.1
- §4.2.2
---

## Ce que c'est
Le prix aujourd'hui d'un titre qui paierait en T la valeur de l'action divisée par le compte capitalisé, là où le prix forward la divise par le zéro-coupon. [Prop. 3, Prop. 2]

## Forme
$$H(t)=\text{prix en }t\text{ de }\frac{S(T)}{B(t,T)}\qquad\text{et}\qquad F(t,T)=\text{prix en }t\text{ de }\frac{S(T)}{P(t,T)}$$ [Prop. 3, Prop. 2]

## Ce que les symboles modélisent
$H(t)$ est le prix future, $F(t,T)$ le prix forward, $S(T)$ le prix de l'action à l'échéance. Les deux titres paient la même action, amplifiée par un coût de portage : connu dès aujourd'hui pour le forward, $1/P(t,T)$, découvert au fil du temps pour le future, $1/B(t,T)$. [§4.2.2]

## Retrouver la formule
![La stratégie du future jour après jour. À chaque date, elle détient 1/B(t₀,tᵢ) contrats et place H(tᵢ)/B(t₀,tᵢ) ; sa valeur passe de H(t₀) au départ à S(T)/B(t₀,T) à l'échéance.](figures/prix-future.svg) [§4.2.2, ajout]

D'abord le forward. Acheter $1/P(t,T)$ contrats forward et placer $F(t,T)$ en zéro-coupon coûte $F(t,T)$ aujourd'hui. En $T$, le placement rend $F(t,T)/P(t,T)$ et les contrats $\big(S(T)-F(t,T)\big)/P(t,T)$ : au total $S(T)/P(t,T)$. [§4.2.1]

Même idée pour le future, une période à la fois. En $t_0$, acheter $1/P(t_0,t_1)$ contrats et placer $H(t_0)$ jusqu'en $t_1$ : en $t_1$, la richesse vaut $H(t_1)/P(t_0,t_1)$, car les flux de marge et le placement s'additionnent comme pour le forward. [§4.2.2]

On recommence en $t_1$ avec cette richesse : en $t_i$, détenir $1/B(t_0,t_i)$ contrats et placer $H(t_i)/B(t_0,t_i)$ ; en $t_{i+1}$, la richesse vaut $H(t_{i+1})/B(t_0,t_{i+1})$. [§4.2.2]

À l'échéance, $H(T)=S(T)$ : la stratégie coûte $H(t_0)$ et rend $S(T)/B(t_0,T)$. Par la loi du prix unique : [§4.2.2]

$$H(t)=\text{prix en }t\text{ de }\frac{S(T)}{B(t,T)}$$ [Prop. 3]

## Ce qui la définit
Ce qui est **connu** : le prix de l'action et le zéro-coupon, qui suffisent au forward. Ce qui manque au future : les zéro-coupons courts à venir, que $B(t,T)$ contient. Forward et future sont tous deux le prix comptant amplifié par le coût du portage ; seul le premier connaît ce coût d'avance. [§4.2.2]

Quand les taux sont déterministes, $B(t,T)=P(t,T)$ et les deux prix sont égaux. Aller plus loin demande un modèle de taux, que le cours ne construit pas. [Prop. 4, §4.2.2]

## Le chemin jusqu'ici
fpp/contrat-future fournit les flux quotidiens que la stratégie encaisse, fpp/compte-capitalise le facteur par lequel elle les replace. La démonstration reprend pas à pas celle de fpp/prix-forward, qui tenait en une seule période : le prix que produit fpp/cash-and-carry avec un emprunt valorisé par fpp/zero-coupon, dans la convention de fpp/capitalisation. fpp/absence-d-arbitrage, sous le nom de loi du prix unique, conclut dans les deux cas. [ajout]

## Exemple minimal
Si le taux reste à 4 % quoi qu'il arrive, le prix future à un an de l'action à 100 vaut 104,08, comme le prix forward. [Prop. 4, ajout]

## Geste de calcul type
Dans le cours, où les taux sont déterministes, traiter un prix future comme un prix forward : c'est ce que fait le livre d'exercices pour évaluer une option sur future de pétrole par la formule de Black. [Prop. 4, exo. 7]

## Cesse d'être valide quand
Si les taux sont aléatoires et liés au prix de l'action, $B(t,T)$ et $S(T)$ ne sont plus indépendants et le prix future s'écarte du prix forward ; le poly renvoie à un modèle de taux. [§4.2.2]
