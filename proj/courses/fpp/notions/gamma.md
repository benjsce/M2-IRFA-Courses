---
id: fpp/gamma
nom: Gamma
symbole: $\gamma$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le sous-jacent, au second ordre
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- gamma de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le delta bouge quand le sous-jacent bouge. [§8.2]

## Forme
$$\gamma=\dfrac{\partial^2P}{\partial S^2}=\dfrac{n(d_1)}{S\,\sigma\sqrt{\tau}}$$ [§8.2, ajout]

## Ce que les symboles modélisent
$\gamma$ est la dérivée du delta, donc la dérivée seconde du prix : elle dit de combien la couverture doit être réajustée quand le sous-jacent bouge. Une couverture qui ne regarde que le delta suppose le gamma petit. $P$ est le prix de l'option, call ou put : les deux ont le même gamma. [§8.2, ajout]

$n$ est la densité de la loi normale centrée réduite, $n(x)=e^{-x^2/2}/\sqrt{2\pi}$, et non sa fonction de répartition $N$ ; $\tau=T-t$ est le temps qui reste jusqu'à l'échéance. La table du §8.2 n'écrit que $n(d_1)$, le facteur qui dépend de $d_1$. [§8.2, ajout]

## Ce qui la définit
**On connaît** le delta d'aujourd'hui : 0,618 action à vendre par call acheté. **On cherche** celui d'après le mouvement, c'est-à-dire de combien réajuster la couverture. Le gamma donne l'ajustement : il mesure la courbure du prix, donc la vitesse à laquelle la couverture en delta se périme et la fréquence à laquelle il faut la refaire, surtout près de la monnaie et près de l'échéance. [§8.2, ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le gamma est la dérivée **seconde** par rapport au comptant. [ajout]

## Exemple minimal
Le call de l'exemple courant : action à 100, strike 100, taux 4 %, volatilité 20 %, un an. Passer l'action de 100 à 101 fait passer son delta de 0,618 à 0,637 : le gamma vaut environ 0,019. [ajout]

![Le delta du call de l'exemple selon le sous-jacent, à un an et à un mois de l'échéance, cet horizon étant choisi pour le dessin. Le gamma est la pente de ces courbes : 0,019 en 100 à un an, bien plus fort près du strike à un mois.](figures/gamma.svg) [ajout]

## Geste de calcul type
Le gamma se lit dans la formule : $n(0{,}3)/(100\times0{,}2\times1)=0{,}3814/20=0{,}019$, le même 0,019 que l'exemple. [ajout]

Il sert à prévoir le delta d'après le mouvement, $\delta(S+\Delta S)\approx\delta+\gamma\,\Delta S$ : à 101, $0{,}618+0{,}019=0{,}637$, soit 0,019 action de plus à vendre ; à 98, $0{,}618-2\times0{,}019=0{,}580$, soit 0,038 action à racheter. [ajout]

## Cesse d'être valide quand
Calculé dans le modèle de Black et Scholes : une volatilité non constante le déplace. [ajout]
