---
id: fpp/modele-black-scholes
nom: Modèle de Black et Scholes
symbole: $W_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/tendance-risque-neutre
- fpp/echelonnement-de-la-variance
- fpp/transformee-de-laplace-gaussienne
alias:
- Black and Scholes model
- modèle log-normal
- diffusion log-normale
- mouvement brownien géométrique
refs:
- §5.4
- §5.3
- éq. 15
---

## Ce que c'est
Le modèle où le prix de l'action est une diffusion log-normale et où le taux d'intérêt est constant. [§5.4]

## Forme
$$dS_t=S_t\big(\mu\,dt+\sigma\,dW_t^{\mathbb P}\big)=S_t\big(r\,dt+\sigma\,dW_t^{\mathbb Q}\big),\qquad S_t=S_0\,e^{\left(\mu-\frac{\sigma^2}{2}\right)t+\sigma W_t^{\mathbb P}}$$ [§5.4, éq. 15]

## Ce que les symboles modélisent
$W_t$ est un mouvement brownien : un bruit dont les accroissements sont gaussiens, indépendants, de variance égale à leur durée ; $W_t^{\mathbb P}$ et $W_t^{\mathbb Q}$ sont ce bruit décrit sous chacune des deux probabilités. $\mu$ est la tendance réelle, $\sigma$ la volatilité, $r$ le taux constant. [§5.4]

## Ce qui la définit
Ce qui est **connu** : le prix d'aujourd'hui, la volatilité et le taux. Le modèle donne alors toute la loi du prix futur : sous $\mathbb Q$, son logarithme suit $Y(T)\sim\mathcal N\big(rT-\tfrac12\sigma^2T,\ \sigma^2T\big)$. [§5.4]

Changer de probabilité change la tendance, $\mu$ sous $\mathbb P$, $r$ sous $\mathbb Q$, et pas la volatilité : $E^{\mathbb P}(S_t)=S_0\,e^{\mu t}$, $E^{\mathbb Q}(S_t)=S_0\,e^{rt}$. [§5.4]

![La loi de S_T sous la probabilité risque-neutre dans le modèle de Black et Scholes : log-normale, étirée vers le haut ; la médiane vaut S₀ e^((r − σ²/2)T) et la moyenne S₀ e^(rT), le prix forward.](figures/modele-black-scholes.svg) [ajout]

## Le chemin jusqu'ici
Chaque ingrédient du modèle vient d'une fiche. fpp/tendance-risque-neutre fixe la tendance sous $\mathbb Q$ au taux sans risque, diminué du fpp/taux-de-dividende quand l'action en verse ; cette tendance sortait de fpp/probabilite-risque-neutre, qui fait de l'espérance le prix de fpp/prix-forward. [ajout]

fpp/echelonnement-de-la-variance, appliqué à fpp/volatilite, donne la variance $\sigma^2T$ du log-prix ; fpp/transformee-de-laplace-gaussienne dit pourquoi sa moyenne doit être $rT-\sigma^2T/2$ pour que l'espérance du prix soit bien $S_0\,e^{rT}$. [ajout]

En amont restent le portage de fpp/cash-and-carry, les fpp/dividendes-intermediaires dont le taux continu est la limite, et l'actualisation de fpp/valeur-actuelle-nette par fpp/zero-coupon dans la convention de fpp/capitalisation, sous la contrainte de fpp/absence-d-arbitrage. [ajout]

## Exemple minimal
L'action à 100, une volatilité de 20 %, un taux de 4 % : sous $\mathbb Q$, le prix dans un an a pour médiane 102,02 et pour moyenne 104,08. [ajout]

## Geste de calcul type
Écrire le prix futur comme $S_T=S_0\,e^{(r-\sigma^2/2)T+\sigma\sqrt T\,Z}$ avec $Z$ gaussienne centrée réduite, puis calculer l'espérance d'un paiement sur cette loi. [§5.4, ajout]

## Cesse d'être valide quand
La volatilité et le taux sont supposés constants, et le prix sans saut ; les rendements réels ont des queues plus épaisses que la loi normale. Le poly s'arrête sur un « à suivre ». [§5.4, ajout]
