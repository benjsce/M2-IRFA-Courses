---
id: fpp/edp-black-scholes
nom: Équation de Black et Scholes
symbole: $V$
type: notion
statut: source
cas_de: fpp/couverture
construite_a_partir_de:
- fpp/formule-d-ito
alias:
- Black and Scholes equation
- Black-Scholes PDE
- EDP de Black et Scholes
refs:
- §7.1
- éq. 16
---

## Ce que c'est
L'équation aux dérivées partielles que vérifie le prix de toute option européenne, obtenue en couvrant l'option par des actions jusqu'à ne plus porter de risque. [§7.1]

## Forme
$$\frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2C}{\partial S^2}=rC,\qquad C(T,x)=(x-K)^+$$ [éq. 16]

## Ce que les symboles modélisent
$C(t,S)$ est le prix de l'option, inconnu, cherché à toute date et pour tout prix de l'action ; la condition en $T$ est son payoff. $V$ est la valeur du portefeuille fait d'une option et de $\delta$ actions qui sert à l'obtenir. $\mu$ n'apparaît nulle part. [§7.1]

## Retrouver la formule
La formule d'Itô donne la variation de l'option : une dérive, et un bruit $\sigma S\,\frac{\partial C}{\partial S}\,dW_t$. Ajoutons $\delta$ actions ; leur bruit vaut $\delta\,\sigma S\,dW_t$. [§7.1]

Choisissons $\delta=-\frac{\partial C}{\partial S}$ : les deux bruits s'annulent. Pour le call de l'exemple, cela veut dire vendre 0,618 action par call détenu. Entre $t$ et $t+dt$, le portefeuille ne porte plus de risque. [§7.1]

Un portefeuille sans risque doit rapporter le taux sans risque, sinon il y aurait arbitrage : $dV=rV\,dt$. En écrivant les deux dérives et en simplifiant, les termes en $\mu$ disparaissent : [§7.1]

$$\frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2C}{\partial S^2}=rC$$ [éq. 16]

## Ce qui la définit
Ce qui est **connu** : le payoff à l'échéance, la volatilité et le taux. Ce qu'on **cherche** : le prix de l'option à chaque date. L'équation relie ses dérivées en tout point ; la condition finale la fixe. [§7.1]

La tendance réelle de l'action a disparu : deux investisseurs en désaccord sur elle s'accordent sur le prix, parce que le prix vient de la couverture, pas des anticipations. [§7.1]

## Le chemin jusqu'ici
fpp/formule-d-ito donne la variation de l'option ; c'est elle qui fait apparaître un bruit que l'on peut annuler avec des actions. Elle s'appuie sur fpp/modele-black-scholes, dont la dynamique log-normale combine fpp/volatilite, fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne. [ajout]

L'argument final, un portefeuille sans risque rapporte le taux sans risque, est fpp/absence-d-arbitrage ; le reste du socle, fpp/tendance-risque-neutre, fpp/probabilite-risque-neutre, fpp/prix-forward, fpp/taux-de-dividende, fpp/dividendes-intermediaires, fpp/cash-and-carry, fpp/valeur-actuelle-nette, fpp/zero-coupon et fpp/capitalisation, vient du modèle, mais l'équation n'en retient que le taux. [ajout]

## Exemple minimal
Pour le call de strike 100 à un an, l'action à 100 : $-5{,}89+0{,}04\times100\times0{,}618+\tfrac12\times0{,}04\times100^2\times0{,}019=0{,}40$, et $rC=0{,}04\times9{,}93=0{,}40$. [ajout]

## Geste de calcul type
Vérifier qu'un prix candidat résout l'équation, en calculant ses dérivées ; ou la résoudre, par des méthodes numériques, par transformée de Fourier, ou en la ramenant à une espérance. [§7.2]

## Cesse d'être valide quand
La couverture est supposée ajustée en continu, sans coût ; la volatilité et le taux sont constants, l'action ne verse pas de dividende. [§7.1]
