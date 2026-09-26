---
id: fpp/feynman-kac
nom: Équivalence de Feynman-Kac
symbole: $\mathcal{L}$
type: notion
statut: source
construite_a_partir_de:
- fpp/edp-black-scholes
alias:
- Feynman-Kac
refs:
- §7.2.1
- éq. 18
- éq. 19
---

## Ce que c'est
La valeur en $t$ d'un paiement futur se calcule de deux façons, par la moyenne des paiements ou par une équation qui remonte de l'échéance, et les deux donnent la même fonction. [§7.2.1]

## Forme
$$\begin{cases}\mathcal{L}f=0\\ f(T,x)=F(x)\end{cases}\quad\Longleftrightarrow\quad f(t,X_t)=\mathbb{E}\big(F(X_T)\mid\mathcal{F}_t\big)$$ [§7.2.1, éq. 19]

$$\text{où}\quad\mathcal{L}f=\dfrac{\partial f}{\partial t}+\mu(t,x)\dfrac{\partial f}{\partial x}+\tfrac12\sigma^2(t,x)\dfrac{\partial^2f}{\partial x^2}$$ [éq. 18]

## Ce que les symboles modélisent
$X_t$ est la quantité aléatoire dont dépend le paiement, par exemple le cours d'une action ; elle bouge selon $dX_t=\mu(t,X_t)\,dt+\sigma(t,X_t)\,dW_t$, où $W_t$ est le mouvement brownien, la source du hasard. Ce n'est pas ici le taux de change $X_t$. [éq. 17, ajout]

$\mu(t,x)$ et $\sigma(t,x)$ sont des fonctions de la date et du niveau, et non des constantes : $\mu$ est la tendance de $X$, $\sigma$ l'amplitude de ses chocs, là où il se trouve. Pour l'action sous $\mathbb{Q}$, dans le modèle de Black et Scholes, $\mu(t,x)=rx$ et $\sigma(t,x)=\sigma x$, avec $r$ le taux sans risque et $\sigma$ la volatilité, constante. [éq. 17, ajout]

$F$ prend la valeur de $X$ à l'échéance et rend le montant payé ; ce n'est pas ici le prix forward $F$. $f(t,x)$ est l'inconnue : la valeur en $t$ du paiement quand $X_t=x$ ; ce n'est pas le taux forward instantané $f(t,T)$. $\mathcal{F}_t$ est ce qu'on sait en $t$, l'histoire de $X$ jusque-là ; ici, seul $X_t$ en compte. [§7.2.1, ajout]

$\mathcal{L}$ n'est pas un nombre mais un opérateur : il prend une fonction $f(t,x)$ et rend la tendance de $f(t,X_t)$, ce dont elle dérive en moyenne par unité de temps. [éq. 18, ajout]

## Retrouver la formule
![À gauche, par l'espérance : des trajectoires d'un mouvement brownien partent de 0 en t ; chacune finit sur la parabole des paiements x², connue, et la moyenne de ces paiements vaut 1. À droite, par l'équation : partie du paiement x² en T, la solution de $\mathcal{L}f=0$ remonte le temps en montant d'autant, x² + 0,5 à mi-chemin, x² + 1 en t. Les deux donnent f(t, 0) = 1.](figures/feynman-kac.svg) [ajout]

On connaît le paiement à l'échéance, $F(X_T)$, et la façon dont $X$ bouge. On cherche sa valeur en $t$ quand $X_t=x$ : c'est le trou, $f(t,x)$. Deux façons de le boucher : la moyenne des paiements sur les trajectoires issues de $x$, ou une équation résolue en partant de l'échéance. [§7.2.1, ajout]

En chiffres : $X$ est un mouvement brownien, $\mu=0$ et $\sigma=1$, le paiement est $F(x)=x^2$, l'échéance dans un an. Parti de 0, $X_T$ est une normale de moyenne 0 et de variance 1 : la moyenne de $X_T^2$ est cette variance, et $f(t,0)=1$. Parti de $x$, $X_T$ vaut $x$ plus un écart de variance $T-t$, et $f(t,x)=x^2+(T-t)$. [ajout]

Cette fonction résout l'équation : $\partial f/\partial t=-1$ et $\tfrac12\,\partial^2f/\partial x^2=1$, leur somme $\mathcal{L}f$ est nulle ; et $f(T,x)=x^2$, le paiement. La moyenne est bien la solution. [ajout]

Pourquoi en général. $f(t,X_t)=\mathbb{E}\big(F(X_T)\mid\mathcal{F}_t\big)$ est une martingale : la moyenne, aujourd'hui, de ce qu'on prévoira demain est ce qu'on prévoit aujourd'hui. [§7.2.1]

La formule d'Itô sépare sa variation en une tendance et un aléa, $df(t,X_t)=\mathcal{L}f\,dt+\sigma\,\dfrac{\partial f}{\partial x}\,dW_t$. Une martingale n'a pas de tendance : $\mathcal{L}f$ doit être nul, quelle que soit la valeur de $X_t$, et à l'échéance $f(T,x)=F(x)$. [§7.2.1]

Réciproquement, si $\mathcal{L}f=0$, il ne reste que l'aléa : $f(t,X_t)$ est une martingale qui vaut $F(X_T)$ en $T$, donc la moyenne de $F(X_T)$ sachant ce qu'on sait en $t$. [§7.2.1]

$$\begin{cases}\mathcal{L}f=0\\ f(T,x)=F(x)\end{cases}\quad\Longleftrightarrow\quad f(t,X_t)=\mathbb{E}\big(F(X_T)\mid\mathcal{F}_t\big)$$ [§7.2.1, éq. 19]

## Ce qui la définit
C'est ce qui réconcilie les deux voies du cours : valoriser par une espérance sous $\mathbb{Q}$, ou en résolvant une équation. Le poly appelle le système de gauche un problème de Dirichlet, $P(\mathcal{L},F)$. [§7.2, §7.2.1]

## Le chemin jusqu'ici
Deux routes mènent au prix, et elles sont toutes les deux dans le socle. [ajout]

**Par l'espérance.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre. [ajout]

**Par l'équation.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes ; fpp/compte-capitalise ouvre fpp/replication-dynamique, qui avec le modèle produit fpp/edp-black-scholes. [ajout]

Feynman-Kac est le théorème qui dit que les deux routes arrivent au même prix. [ajout]

## Exemple minimal
Mouvement brownien parti de 0, paiement $X_T^2$ dans un an : la moyenne des paiements et la solution de l'équation valent toutes deux 1. [ajout]

## Geste de calcul type
Identifier $\mu$ et $\sigma$, écrire $\mathcal{L}$, puis vérifier qu'une fonction candidate annule $\mathcal{L}f$ et vaut le paiement à l'échéance. Pour un brownien et $f=x^2+(T-t)$ : $-1+\tfrac12\times2=0$, et $f(T,x)=x^2$. [§7.2.1, ajout]

## Cesse d'être valide quand
Exige que $\mu$ et $\sigma$ satisfassent une condition de Lipschitz, pour que l'équation différentielle stochastique admette une solution forte unique. [éq. 17]

Ne s'applique pas tel quel à une équation qui contient un terme en $f$ lui-même, comme le $rC$ de l'équation de Black et Scholes : il faut d'abord le retirer. [§7.2.2]
