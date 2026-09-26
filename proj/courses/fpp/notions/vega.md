---
id: fpp/vega
nom: Vega
symbole: $\mathcal{V}$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: la volatilité
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- vega de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand la volatilité bouge. [§8.2]

## Forme
$$\mathcal{V}=\dfrac{\partial P}{\partial\sigma}=S\,n(d_1)\sqrt{\tau}$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\mathcal{V}$ dérive le prix par rapport à la volatilité, c'est-à-dire par rapport à un **paramètre du modèle** et non à une grandeur cotée sur le marché. C'est ce qui la sépare du rho : le taux, lui aussi supposé constant par le modèle, se lit sur le marché ; la volatilité, non. [§8.2, ajout]

$P$ est le prix de l'option, call ou put : les deux ont le même vega. $n$ est la densité de la loi normale centrée réduite, et non sa fonction de répartition $N$ ; $\tau=T-t$ est le temps qui reste jusqu'à l'échéance. [§8.2, ajout]

## Ce qui la définit
Positif pour le call comme pour le put : plus d’incertitude vaut plus cher des deux côtés, parce que le payoff est convexe. [§8.2]

![Le payoff du call de strike 100 et deux paires d'issues également probables, choisies pour le dessin. 90 ou 110 paient 0 ou 10, en moyenne 5 ; écartées à 80 ou 120, elles paient 0 ou 20, en moyenne 10. L'issue basse tombe sur le plancher et n'y perd rien ; l'issue haute gagne tout l'écart.](figures/vega.svg) [ajout]

Deux issues également probables, 90 ou 110 : le call de strike 100 paie 0 ou 10, en moyenne 5. Écartées à 80 ou 120, elles paient 0 ou 20, en moyenne 10. Le plancher coupe la perte, pas le gain : écarter les issues ne peut qu'ajouter. [ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le véga est la dérivée par rapport à la **volatilité**, un paramètre que le marché ne cote pas. [ajout]

## Exemple minimal
Le call de l'exemple courant : action à 100, strike 100, taux 4 %, un an. Passer la volatilité de 20 % à 21 % le fait passer de 9,93 à 10,31 : le vega vaut 0,38 par point de volatilité. [ajout]

## Geste de calcul type
La formule donne $S\,n(d_1)\sqrt{\tau}=100\times0{,}3814\times1=38{,}14$ par unité de volatilité, c'est-à-dire pour 100 points : soit 0,38 par point, le chiffre de l'exemple. On lit une position en volatilité en multipliant le vega par la variation de volatilité exprimée en points. [§8.2, ajout]

La table du §8.2 écrit $SN(d_1)\sqrt{\tau}$, avec la fonction de répartition, ce qui donnerait 61,79 : c'est la densité $n$ qu'il faut. [§8.2, ajout]

## Cesse d'être valide quand
Le paramètre dérivé est justement celui que le modèle suppose constant : dériver par rapport à lui, c’est déjà sortir du modèle. [ajout]

## Origine
- exercice fpp/ex-15 : pour choisir une stratégie de volatilité, on ne regarde pas le profil de gain mais le signe du véga — le profil ne distingue pas l'achat de straddle de la vente de butterfly [ajout]
