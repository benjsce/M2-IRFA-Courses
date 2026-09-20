---
id: fpp/feynman-kac
nom: Équivalence de Feynman-Kac
symbole: $\mathcal{L}$
type: notion
statut: source
construite_a_partir_de:
- fpp/edp-black-scholes
- fpp/mesure-risque-neutre
alias:
- Feynman-Kac
refs:
- §7.2.1
- éq. 18
- éq. 19
---

## Ce que c'est
Le pont entre l’équation aux dérivées partielles et l’espérance : une solution de l’une est une martingale de l’autre. [§7.2.1]

## Forme
$$\mathcal{L}f(t,x)=\dfrac{\partial f}{\partial t}+\mu(t,x)\dfrac{\partial f}{\partial x}+\tfrac12\sigma^2(t,x)\dfrac{\partial^2f}{\partial x^2},\qquad Z_t=f(t,X_t)\equiv\mathbb{E}\big(F(X_T)\mid\mathcal{F}_t\big)$$ [éq. 18, éq. 19]

## Ce qui la définit
Pour que $f(t,X_t)$ soit une martingale, sa partie à variation finie doit être nulle, donc $\mathcal{L}f=0$. Réciproquement, toute solution du problème de Dirichlet $\mathcal{L}f=0$ avec $f(T,x)=F(x)$ définit une martingale de valeur terminale $F(X_T)$. [§7.2.1]

C’est ce qui réconcilie les deux voies du cours : valoriser par espérance sous $\mathbb{Q}$, ou valoriser en résolvant une équation. [§7.2]

## Le chemin jusqu'ici
Deux routes mènent au prix, et elles sont toutes les deux dans le socle. [ajout]

**Par l'espérance.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre. [ajout]

**Par l'équation.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes ; fpp/compte-capitalise donne fpp/replication-dynamique, et avec le modèle, fpp/edp-black-scholes. [ajout]

Feynman-Kac est le théorème qui dit que ce sont les mêmes. Son socle contient nécessairement les deux routes : on ne peut pas énoncer l'équivalence de deux choses avant de disposer des deux. [ajout]

## Exemple minimal
Pour une diffusion sans dérive et $F(x)=x$, la fonction $f(t,x)=x$ résout $\mathcal{L}f=0$ : le prix d’un actif sans dérive est sa valeur courante. [ajout]

## Geste de calcul type
Identifier $\mu$ et $\sigma$ de la diffusion, écrire $\mathcal{L}$, poser la condition terminale, puis lire le prix comme l’espérance conditionnelle correspondante. [§7.2.1]

## Cesse d'être valide quand
Exige que $\mu$ et $\sigma$ satisfassent une condition de Lipschitz, pour que l’équation différentielle stochastique admette une solution forte unique. [éq. 17]
