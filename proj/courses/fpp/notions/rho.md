---
id: fpp/rho
nom: Rho
symbole: $\rho$
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le taux d’intérêt
construite_a_partir_de:
- fpp/formule-black-scholes
alias:
- rho de Black et Scholes
refs:
- §8.2
---

## Ce que c'est
De combien le prix bouge quand le taux d’intérêt bouge. [§8.2]

## Forme
$$\rho=\dfrac{\partial P}{\partial r}$$ [§8.2]

## Ce que les symboles modélisent
$\rho$ dérive le prix par rapport à un taux : c'est donc un montant par point de taux, et non un nombre sans unité comme le delta. Deux sensibilités ne se comparent pas sans regarder ce qu'elles dérivent. [§8.2]

## Ce qui la définit
Positif pour un call, négatif pour un put : monter le taux abaisse la valeur actualisée du strike, donc renchérit le droit d’acheter à ce strike et déprécie le droit de vendre à ce strike. [§8.2, ajout]

## Le chemin jusqu'ici
Le socle est celui de fpp/formule-black-scholes, la formule elle-même en plus : tout y sert à l'écrire, et cette fiche ne fait que la dériver. Trois fils y mènent. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : à ce stade, un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue, et les trois se nouent dans fpp/formule-black-scholes. [ajout]

Ce qui distingue les grecques entre elles, c'est la variable dérivée, pas le chemin — celui-ci est le même pour toutes et ne vaut la peine d'être lu qu'une fois. Le rhô est la dérivée par rapport au **taux**, qui entre dans la formule par l'actualisation du strike, pas par l'aléa. [ajout]

## Exemple minimal
Le call de l'exemple courant : action à 100, strike 100, volatilité 20 %, un an. Si le taux tombe de 4 % à 3 %, le strike actualisé passe de 96,08 à 97,04 ; le call passe de 9,93 à 9,41 et le put de 6,00 à 6,46. [ajout]

## Geste de calcul type
Dériver la seule actualisation du strike, $N(d_2)$ tenu fixe : $\rho=KTe^{-rT}N(d_2)=100\times1\times0{,}9608\times0{,}540=51{,}9$ par unité de taux, soit 0,52 par point. Ce n'est pas une approximation : les effets du taux sur $d_1$ et sur $d_2$ s'annulent exactement. Le call de l'exemple perd 0,51 pour un point de baisse, l'écart venant de la courbure. [§8.2, ajout]

## Cesse d'être valide quand
Le modèle suppose le taux déterministe : comme pour le vega, on dérive par rapport à ce qu’on a supposé fixe. [ajout]
