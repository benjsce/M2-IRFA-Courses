---
id: fpp/edp-black-scholes
nom: Équation de Black et Scholes
type: notion
statut: source
construite_a_partir_de:
- fpp/modele-black-scholes
- fpp/replication-dynamique
alias:
- B&S PDE
- équation aux dérivées partielles des options
refs:
- §7.1
- éq. 16
---

## Ce que c'est
L’équation que satisfait tout prix d’option quand on peut couvrir le risque en continu. [§7.1]

## Forme
$$\dfrac{\partial C}{\partial t}+rS\dfrac{\partial C}{\partial S}+\tfrac12\sigma^2S^2\dfrac{\partial^2C}{\partial S^2}=rC,\qquad C(T,x)=(x-K)^+$$ [éq. 16]

## Ce que les symboles modélisent
$C$ est une fonction de deux variables : elle prend une date $t$ et un niveau $S$ du sous-jacent, et rend le prix de l'option à cette date si le sous-jacent vaut $S$. Ici $S$ est une variable, un point de l'axe des prix, et non la trajectoire aléatoire $S_t$ ; $\partial C/\partial t$ dérive à $S$ fixé, par rapport à la date et non à la durée restante. [§7.1, ajout]

$r$ est le taux sans risque, constant, et $\sigma$ la volatilité du sous-jacent. $T$ est l'échéance de l'option et $K$ son strike ; $x$ est une variable muette, la valeur du sous-jacent à l'échéance. Seule la condition terminale dit de quelle option il s'agit : $(x-K)^+$ est le payoff du call, et la même équation, avec $(K-x)^+$, porte sur le put. [§7.1, ajout]

## Retrouver la formule
Le sous-jacent suit $dS_t=S_t(\mu\,dt+\sigma\,dW_t)$ : une dérive $\mu$, sa tendance moyenne, et un choc brownien $dW_t$, imprévisible. Le prix $C(t,S_t)$ de l'option en dépend ; la formule d'Itô écrit sa variation, avec un terme en $dt$ et un terme en $dW_t$ : [§7.1]

$$dC=\Big(\dfrac{\partial C}{\partial t}+\mu S\dfrac{\partial C}{\partial S}+\tfrac12\sigma^2S^2\dfrac{\partial^2C}{\partial S^2}\Big)dt+\sigma S\dfrac{\partial C}{\partial S}\,dW_t$$ [§7.1]

On forme un portefeuille d'une option et de $\delta$ actions ; $\delta$ est ici la quantité *détenue*. Sa valeur $V=C+\delta S$ varie de $dV=dC+\delta\,dS$, et le choc y apparaît deux fois : $\sigma S\,\partial C/\partial S\,dW_t$ par l'option, $\delta\,\sigma S\,dW_t$ par les actions. [§7.1]

On choisit $\delta=-\partial C/\partial S$ : les deux chocs s'annulent, et le terme en $\mu$ disparaît avec eux, puisqu'il vient lui aussi de $dS$. Sur $[t,t+dt]$, le portefeuille ne porte plus de risque : $dV=\big(\partial C/\partial t+\tfrac12\sigma^2S^2\,\partial^2C/\partial S^2\big)dt$. [§7.1]

Un placement sans risque doit rapporter le taux sans risque, sinon il y a arbitrage : $dV=rV\,dt=r\big(C-S\,\partial C/\partial S\big)\,dt$. On égale les deux expressions de $dV$ et l'on range les termes ; au bout, le prix à l'échéance est le payoff. [§7.1]

$$\dfrac{\partial C}{\partial t}+rS\dfrac{\partial C}{\partial S}+\tfrac12\sigma^2S^2\dfrac{\partial^2C}{\partial S^2}=rC,\qquad C(T,x)=(x-K)^+$$ [éq. 16]

## Ce qui la définit
Un portefeuille sans risque doit rapporter le taux sans risque : l'équation n'est rien d'autre que cette phrase, écrite en différentiel. [§7.1]

**On connaît** le payoff à l'échéance et la façon dont le sous-jacent bouge. **On cherche** le prix $C(t,S)$ à toute date antérieure. L'équation bouche ce trou un pas de temps à la fois, en remontant depuis l'échéance. [ajout]

La dérive $\mu$ disparaît de l’équation : le prix ne dépend pas de ce qu'on anticipe pour le sous-jacent. C'est le résultat central du chapitre. [§7.1]

## Le chemin jusqu'ici
Le chemin est celui du modèle, plus une brique. [ajout]

**Le modèle.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre ; fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**La couverture.** fpp/compte-capitalise ouvre fpp/replication-dynamique : on peut rééquilibrer à chaque pas. [ajout]

Cette addition est toute l'idée : le modèle dit comment le sous-jacent bouge, la réplication dynamique dit qu'on peut annuler ce mouvement. [ajout]

## Exemple minimal
Pour $C(t,S)=S$, l’équation se réduit à $rS=rS$ : une action est bien son propre prix. [ajout]

## Geste de calcul type
Pour vérifier qu’une formule candidate est un prix : la dériver une fois en $t$, deux fois en $S$, reporter dans l’équation, puis contrôler la condition terminale. [éq. 16]

Sur le call de l'exemple courant (action 100, strike 100, taux 4 %, volatilité 20 %, un an ; prix 9,925), les trois dérivées sont le theta, $-5{,}889$ par an, le delta, $0{,}618$, et le gamma, $0{,}019\,07$. Alors $-5{,}889+0{,}04\times100\times0{,}618+\tfrac12\times0{,}04\times100^2\times0{,}019\,07=-5{,}889+2{,}472+3{,}814=0{,}397$, et $rC=0{,}04\times9{,}925=0{,}397$. [ajout]

## Cesse d'être valide quand
Exige un rééquilibrage continu et sans friction, une volatilité constante et un taux déterministe. Le rééquilibrage continu est l’hypothèse la plus fragile de tout l’édifice : on ne réajuste qu'à intervalles, et chaque intervalle laisse un risque. [ajout]
