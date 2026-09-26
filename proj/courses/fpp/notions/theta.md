---
id: fpp/theta
nom: Theta
symbole: $\Theta$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le temps qui passe
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- theta de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand le temps passe. [§8.2]

## Forme
$$\Theta=\dfrac{\partial P}{\partial t}$$ [§8.2]

## Ce que les symboles modélisent
$\Theta$ mesure ce que le seul passage du temps fait au prix, tout le reste étant tenu fixe : $t$ est la date, et non le temps qui reste. C'est la seule des sensibilités dont la variable avance à coup sûr, et toujours dans le même sens. [§8.2, ajout]

## Ce qui la définit
Négatif pour un call ; pour un put, le plus souvent, mais pas toujours. À l'approche de l'échéance, le prix fond : pas seulement la valeur temps, mais aussi, à cours tenu fixe, la valeur intrinsèque au sens du cours, $S-Ke^{-r\tau}$, qui tend vers $S-K$. [§8.2, Déf. 12, ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le thêta est la dérivée par rapport au **temps** : ce que coûte l'attente. Il est le pendant du gamma, l'équation de Black et Scholes les liant terme à terme. [ajout]

## Exemple minimal
Le call de l'exemple courant : action à 100, strike 100, taux 4 %, volatilité 20 %, un an ; il vaut 9,93. Sa valeur intrinsèque au sens du cours est $S-Ke^{-r\tau}=100-96{,}08=3{,}92$, et sa valeur temps 6,00. Si l'action reste à 100, les deux tombent à zéro à l'échéance : le theta vaut −5,89 par an au départ, soit −0,016 par jour. [Déf. 12, Déf. 13, ajout]

![Le call à la monnaie de l'exemple, sous-jacent tenu à 100, à mesure que le temps passe. Tout le prix fond, de 9,93 à zéro : la valeur temps, 6,00, mais aussi la valeur intrinsèque, de 3,92 à zéro. La pente de la courbe du prix est le theta, −5,89 par an au départ, et de plus en plus raide à la fin.](figures/theta.svg) [ajout]

## Geste de calcul type
Pour un call, $\Theta=-\tfrac12\sigma^2S^2\gamma-rKe^{-r\tau}N(d_2)$. Sur l'exemple : $-\tfrac12\times0{,}04\times100^2\times0{,}019\,07=-3{,}81$, plus $-0{,}04\times96{,}08\times0{,}540=-2{,}07$, soit $-5{,}89$ par an. [ajout]

La première part est le loyer du gamma : ce que l'acheteur perd, jour après jour, pour détenir de la convexité, qui lui rapporte quand l'action bouge. La seconde est le financement du strike. [ajout]

## Cesse d'être valide quand
La table marque ce signe d’un astérisque, « presque toujours vrai » : les exceptions existent, notamment pour un put très en dedans. [§8.2]
