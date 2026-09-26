---
id: fpp/feynman-kac
nom: Feynman-Kac
symbole: '$\mathcal{L}$, $X(t)$, $Z_t$'
type: notion
statut: source
construite_a_partir_de:
- fpp/edp-black-scholes
alias:
- formule de Feynman-Kac
- équivalence de Feynman-Kac
- équation de la chaleur
- heat equation
- problème de Dirichlet
refs:
- §7.2
- §7.2.1
- §7.2.2
- éq. 17
- éq. 18
- éq. 19
- éq. 20
- éq. 21
---

## Ce que c'est
L'équivalence entre résoudre une équation aux dérivées partielles linéaire et calculer une espérance, qui relie l'équation de Black et Scholes au prix donné par la probabilité risque-neutre. [§7.2]

## Forme
$$\mathcal Lf=\frac{\partial f}{\partial t}+\mu(t,x)\frac{\partial f}{\partial x}+\frac12\sigma^2(t,x)\frac{\partial^2f}{\partial x^2},\qquad \begin{cases}\mathcal Lf=0\\ f(T,x)=F(x)\end{cases}\iff f(t,X_t)=E\big(F(X_T)\mid\mathcal F_t\big)$$ [éq. 18, éq. 19, §7.2.1]

## Ce que les symboles modélisent
$X(t)$ est une diffusion, $dX=\mu(t,X)\,dt+\sigma(t,X)\,dW_t$, qui n'a rien d'un taux de change. $\mathcal{L}$, son générateur, prend une fonction et rend la dérive de $f(t,X_t)$. $Z_t$, égal à $f(t,X_t)$, est l'espérance, vue en $t$, du paiement final $F(X_T)$ ; ici $F$ est une fonction, pas un prix forward. $\mathcal F_t$ est l'information disponible en $t$. [éq. 17, éq. 18, éq. 19]

## Retrouver la formule
![Le prix du call en fonction du prix de l'action, à un an, six mois et trois mois de l'échéance, puis à l'échéance, où il devient le payoff coudé : en remontant le temps, l'équation lisse le coude, comme la chaleur lisse une température.](figures/feynman-kac.svg) [ajout]

Par la formule d'Itô, $df(t,X)=\mathcal Lf\,dt+\frac{\partial f}{\partial x}\sigma\,dW_t$. [§7.2.1]

Si $Z_t=E(F(X_T)\mid\mathcal F_t)$, la propriété de la tour donne $Z_t=E(Z_u\mid\mathcal F_t)$ pour tout $u>t$ : $Z$ est une martingale, sans dérive. Il faut donc $\mathcal Lf=0$, avec $f(T,x)=F(x)$. Réciproquement, une solution de ce problème de Dirichlet donne une martingale de valeur finale $F(X_T)$. [§7.2.1]

L'équation de Black et Scholes n'est pas de cette forme à cause du terme $rC$. Le poly passe au prix forward de l'option, $e^{r(T-t)}C$ : les dérivées en espace ne changent que d'un facteur, la dérivée en temps perd $rC$, et l'on obtient $\mathcal L^{BS}f=0$ avec $\mu(x)=rx$ et $\sigma^2(x)=\sigma^2x^2$. [§7.2.2]

C'est la dynamique de l'action sous la probabilité risque-neutre : le prix forward de l'option est l'espérance risque-neutre de son payoff, et le call de l'exemple vaut $e^{-0,04}\times E^{\mathbb Q}\big((S_1-100)^+\big)=9{,}93$. [§7.2.2, ajout]

$$C(t,x)=e^{-r(T-t)}\,E^{\mathbb Q}\big((S_T-K)^+\mid S_t=x\big)$$ [§7.2.2, ajout]

## Ce qui la définit
Ce qui est **connu** : une équation aux dérivées partielles et sa condition finale. Ce qu'on **cherche** : sa solution. Feynman-Kac la donne comme une espérance, et relie ainsi les deux approches du cours : le prix par couverture du chapitre 7 et le prix par espérance actualisée du chapitre 6. [§7.2]

Deux changements de variables de plus, le prix forward de l'action et son logarithme, ramènent l'équation de Black et Scholes à l'équation de la chaleur, $\frac{\partial C}{\partial t}+\frac12\sigma^2\frac{\partial^2C}{\partial x^2}=0$ avec $C(T,x)=(e^x-K)^+$. [§7.2.2, éq. 20, éq. 21]

## Le chemin jusqu'ici
fpp/edp-black-scholes fournit l'équation à résoudre, et fpp/formule-d-ito l'outil qui montre que la solution, lue le long du prix, n'a pas de dérive. [ajout]

Le prix retrouvé est celui de fpp/probabilite-risque-neutre : la dynamique $\mu(x)=rx$ est celle de fpp/modele-black-scholes sous la tendance de fpp/tendance-risque-neutre, qui centre le prix sur fpp/prix-forward, net du fpp/taux-de-dividende et des fpp/dividendes-intermediaires ; fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne fixent sa loi. [ajout]

L'actualisation par $e^{-r(T-t)}$ est celle de fpp/valeur-actuelle-nette et de fpp/zero-coupon, dans la convention de fpp/capitalisation ; fpp/cash-and-carry et fpp/absence-d-arbitrage sont à l'origine du prix forward. [ajout]

## Exemple minimal
Le call de strike 100 : la solution de l'équation vaut 9,93 à un an de l'échéance, 6,63 à six mois, 4,49 à trois mois, l'action restant à 100. [ajout]

## Geste de calcul type
Pour résoudre une équation de prix : l'écrire sur le prix forward pour faire disparaître le terme d'actualisation, lire dans $\mathcal L$ la dynamique du sous-jacent, et calculer l'espérance du payoff sous cette dynamique. [§7.2.2]

## Cesse d'être valide quand
Les coefficients doivent être assez réguliers, lipschitziens dans le poly, pour que la diffusion ait une solution unique. Et les changements de variables qui mènent à l'équation de la chaleur supposent le taux et la volatilité constants. [§7.2.1, §7.2.2]
