---
id: fpp/formule-de-black
nom: Formule de Black
symbole: $F$
type: notion
statut: source
construite_a_partir_de:
- fpp/formule-black-scholes
- fpp/prix-a-terme
alias:
- Black formula
- option sur future
- option sur forward
- option de change
- Garman-Kohlhagen
refs:
- éq. 11
- éq. 12
- éq. 13
- éq. 14
- §6.5
- exos éq. 1.2
- exos éq. 1.3
- exo. 7
- exo. 9
- exo. 13
- exo. 14
---

## Ce que c'est
La formule de Black et Scholes réécrite avec le prix forward et le zéro-coupon, qui s'applique telle quelle à tout sous-jacent dont on connaît le prix à terme. [éq. 11, §6.5]

## Forme
$$C=P(0,T)\big(F\,N(d_1)-K\,N(d_2)\big),\qquad P=P(0,T)\big(K\,N(-d_2)-F\,N(-d_1)\big)$$ [éq. 11, éq. 12]

$$d_1=\frac{\ln(F/K)+\frac{\sigma^2T}{2}}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T$$ [éq. 13, éq. 14]

## Ce que les symboles modélisent
$F$ est le prix à terme du sous-jacent pour la maturité de l'option, $F(0,T)$ ; c'est lui, et non le prix comptant, qui entre dans la formule. $P(0,T)$ actualise ; ici le $P$ de gauche est le prix du put, celui de droite le zéro-coupon. [éq. 11]

## Retrouver la formule
Dans la formule de Black et Scholes, écrivons le prix comptant comme le prix forward actualisé : $S_0=F\,P(0,T)$, et $K\,e^{-rT}=K\,P(0,T)$. Le zéro-coupon se met en facteur. [ajout]

Dans $d_1$, le taux disparaît : $\ln(S_0/K)+rT=\ln(F/K)$. Avec l'action à 100 et 4 % à un an, $F=104{,}08$, $\ln(104{,}08/100)=0{,}04$ : c'est bien le même $d_1=0{,}30$. [exos éq. 1.3, ajout]

Le taux et les dividendes ne sont plus visibles : ils sont passés dans $F$. [ajout]

$$C=P(0,T)\big(F\,N(d_1)-K\,N(d_2)\big)$$ [éq. 11]

## Ce qui la définit
Ce qui est **connu** : le prix à terme, le zéro-coupon, le strike et la volatilité. Le reste est déjà dans $F$ : le taux, les dividendes, le taux étranger d'une devise, le coût de portage d'une matière première. [§6.5, ajout]

Le livre d'exercices l'applique à une option sur future de pétrole, à une option de change, où le taux étranger joue le rôle du dividende, et en tire la parité écrite sur le forward : $K+\mathrm{Call}(F,K,T,0)=F+\mathrm{Put}(F,K,T,0)$ en valeur à l'échéance. [exo. 7, exo. 9, exo. 13, exo. 14]

## Le chemin jusqu'ici
fpp/formule-black-scholes est la formule de départ ; fpp/prix-a-terme dit que tout sous-jacent a un prix à terme, calculé par le même geste, et c'est lui qu'on met à la place du prix comptant. [ajout]

Le reste du socle est celui de la formule. fpp/option et fpp/payoff décrivent le paiement ; fpp/modele-black-scholes sa loi, que fpp/probabilite-risque-neutre et fpp/tendance-risque-neutre centrent sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne en fixent la forme. [ajout]

L'actualisation passe par fpp/valeur-actuelle-nette et fpp/zero-coupon, en convention de fpp/capitalisation ; le prix forward vient de fpp/cash-and-carry sous fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
$F=104{,}08$, $P(0,T)=0{,}9608$, un strike de 100, $\sigma=20\,\%$, un an : le call vaut 9,93, comme par la formule de Black et Scholes. [ajout]

## Geste de calcul type
Le livre d'exercices : un future de pétrole à 25, un strike de 23, quatre mois, une volatilité de 25 % et un taux de 9 % donnent un call de 2,53. [exo. 7]

## Cesse d'être valide quand
$F$ doit être le prix à terme pour la maturité de l'option. Un prix future ne le remplace que si les taux sont déterministes. [éq. 11, Prop. 4]
