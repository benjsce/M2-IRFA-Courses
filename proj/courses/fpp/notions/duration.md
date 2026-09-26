---
id: fpp/duration
nom: Sensibilité, duration
type: notion
statut: source
cas_de: fpp/sensibilite
valeur: le taux, sur un zéro-coupon
construite_a_partir_de:
- fpp/valeur-actuelle-nette
refs:
- Déf. 5
---

## Ce que c'est
Ce que perd un zéro-coupon, en pour cent, quand le taux monte d'un point : à peu près autant de pour cent qu'il lui reste d'années avant d'être payé. [Déf. 5]

## Forme
$$\dfrac{\partial P(t,r)}{P(t,r)\,\partial r}=-t$$ [Déf. 5]

## Ce que les symboles modélisent
$P(t,r)$ est le prix d'un zéro-coupon, écrit autrement qu'avec deux dates : ses arguments sont une durée et un taux. $t$ est la maturité, le nombre d'années qui restent jusqu'au paiement ; $r$ est le taux continu, le même pour toutes les maturités. Donc $P(t,r)=e^{-rt}$ : le même objet que le zéro-coupon $P(t,T)$ du cours, mais écrit pour qu'on puisse faire bouger le taux. [Déf. 5, ajout]

$\mathcal{D}$, lettre ajoutée par le dépôt, est la duration d'un titre qui paie plusieurs flux : une durée moyenne jusqu'à ses paiements, qui joue pour lui le rôle que la maturité $t$ joue pour un zéro-coupon. [ajout]

## Retrouver la formule
![Un zéro-coupon qui paie 1 dans cinq ans revient en $t$ année par année. Le taux passe de 4 % à 5 % : chacune des cinq années d'actualisation coûte environ 1 % de valeur de plus, et le prix perd environ 5 %, exactement 4,9 %, de 0,8187 à 0,7788.](figures/duration.svg) [ajout]

Un zéro-coupon paie 1 dans cinq ans. **Connu** : au taux continu de 4 %, il vaut aujourd'hui $e^{-0{,}04\times5}=0{,}8187$. **Cherché** : ce qu'il perd si le taux monte d'un point, à 5 %. [ajout]

Pour ramener le 1 en $t$, on l'actualise année par année : chaque année multiplie sa valeur par $e^{-0{,}04}$. À 5 %, chaque année la multiplie par $e^{-0{,}05}$, soit $e^{-0{,}01}\approx0{,}99$ fois plus : chaque année d'attente coûte environ 1 % de valeur de plus. [ajout]

Il y a cinq années d'attente, donc le point de taux se paie cinq fois : le prix perd environ $5\times1\,\%=5\,\%$. Le calcul exact donne $e^{-0{,}05}-1=-4{,}9\,\%$. C'est ce que dit le poly : une variation du taux agit sur toute la vie du titre, et plus elle est longue, plus le prix bouge. [Déf. 5]

En lettres : relever le taux de $\Delta r$ multiplie $e^{-rt}$ par $e^{-t\,\Delta r}\approx1-t\,\Delta r$. Le prix perd la fraction $t\,\Delta r$, la maturité fois la variation du taux ; rapportée à $\Delta r$ petit, c'est la dérivée. [ajout]

$$\dfrac{\partial P(t,r)}{P(t,r)\,\partial r}=-t$$ [Déf. 5]

## Ce qui la définit
La perte relative ne dépend que de la maturité, pas du niveau du taux : un point coûte environ 5 % à un zéro-coupon à cinq ans, que le taux soit à 4 % ou à 8 %. [ajout]

Le poly intitule la définition « Duration » mais n'écrit que cette sensibilité. Pour un titre qui paie plusieurs flux, la même dérivée fait sortir la moyenne des maturités de ses flux, chacune pondérée par la part de la valeur actualisée qui y tombe : c'est sa duration $\mathcal{D}$, et pour un zéro-coupon elle vaut la maturité. [ajout]

## Le chemin jusqu'ici
fpp/convention-capitalisation fixe la capitalisation continue, où un taux $r$ tenu pendant $t$ années fait d'un euro $e^{rt}$. fpp/facteur-actualisation en tire le prix aujourd'hui d'un euro payé dans $t$ années, $e^{-rt}$, et fpp/valeur-actuelle-nette additionne ces prix sur tout un échéancier. [ajout]

Une fois ce prix écrit comme une fonction du taux, sa sensibilité n'est qu'une dérivée : c'est la première fois du cours qu'on dérive un prix. [ajout]

## Exemple minimal
Au taux de 4 %, un zéro-coupon qui paie 1 dans cinq ans vaut 0,8187 ; si le taux monte d'un point, il perd environ 5 % de sa valeur. [ajout]

## Geste de calcul type
Perte relative ≈ maturité × hausse du taux : $5\times1\,\%=5\,\%$. Au premier ordre seulement : le calcul exact, $e^{-5\times0{,}01}-1=-4{,}88\,\%$, est un peu plus petit. [ajout]

## Cesse d'être valide quand
La variation du taux est grande : la règle est un premier ordre, et elle surestime la perte, 5 % au lieu de 4,88 % pour un point sur cinq ans. Elle suppose aussi que tous les taux montent du même point, la courbe se déplaçant parallèlement. [ajout]

Le taux n'est plus continu : en taux actuariel, un zéro-coupon $(1+r)^{-t}$ perd $t/(1+r)$ pour cent par point, un peu moins que $t$. [ajout]
