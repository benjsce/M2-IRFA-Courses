---
id: dup/aversion-premier-ordre
nom: Aversion au risque du premier ordre
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-second-ordre
alias:
- first-order risk aversion
refs:
- L2 slide 21
- L3 slide 41
- L4 slide 25
---

## Ce que c'est
La prime d’un petit pari de moyenne nulle proportionnelle à l’écart type lui-même, et non à son carré. [L2 slide 21]

## Forme
$$r(\sigma)=\dfrac{\lambda^{\frac{1}{1-\gamma}}-1}{\lambda^{\frac{1}{1-\gamma}}+1}\,\sigma=k\sigma$$ [L3 slide 41]

## Ce qui la définit
Elle apparaît dès que la fonction de valeur présente un coude en zéro, ou que les probabilités sont déformées : la prime ne s’évanouit plus au second ordre quand le pari rétrécit. [L3 slide 41, L2 slide 21]

C’est ce qui permet d’expliquer le refus de petits paris favorables, que l’utilité espérée dérivable interdit. [L2 slide 21]

Le quatrième cours en donne la dérivation par la seule déformation des probabilités, sans coude dans l’utilité. Pour un pari symétrique de $\pm\sigma$ autour de la richesse, en posant $a=\varphi(1/2)$, le développement limité de la compensation donne un terme d’ordre un qui ne s’annule que si $a$ vaut un demi — c’est-à-dire sous utilité espérée. [L4 slide 25]

$$r(\sigma)=(2a-1)\,\sigma+O(\sigma^2)$$ [L4 slide 25]

La conséquence porte sur la participation, et pas seulement sur la prime. Pour une petite position longue d’excédent de rendement $\mu$, la dérivée de la valeur en zéro vaut $u'(w)\big[\mu-(2a-1)\sigma\big]$ : une prime objectivement positive peut rester trop faible pour faire entrer l’agent sur le marché. [L4 slide 25]

## Le chemin jusqu'ici
Le socle est celui du paradoxe de Rabin, et pour cause : cette fiche en est la sortie. La courbure de dup/fonction-utilite se mesure par dup/aversion-absolue-arrow-pratt ; dup/loterie, évaluée par cette utilité, porte dup/utilite-esperee, puis dup/equivalent-certain et dup/prime-de-risque ; dup/approximation-arrow-pratt réunit les deux branches et permet de nommer dup/aversion-second-ordre. [ajout]

Le premier ordre se définit **par contraste** : une prime proportionnelle à l'écart type et non à la variance. Il faut donc avoir établi le second ordre, sans quoi « premier ordre » ne désigne rien. Et pour l'obtenir, il faut quitter l'utilité espérée dérivable. [ajout]

## Exemple minimal
Avec $\lambda=2$ et $\gamma=0$ : $k=1/3$, donc un pari de $\pm10$ coûte une prime de $3{,}33$, contre $0{,}5$ au second ordre. [ajout]

![Les deux régimes sur le même repère. Ce qui se joue est près de zéro : la droite part avec une pente, la parabole part à plat, et c'est pourquoi seule la première explique qu'on refuse un petit pari favorable. La parabole est celle qui passe par $0{,}5$ en $\sigma=10$, seul point que la fiche en donne.](figures/aversion-premier-ordre.svg) [ajout]

## Geste de calcul type
Chercher si la prime tend vers zéro comme $\sigma$ ou comme $\sigma^2$ : c’est le test qui sépare les deux régimes, et il décide de la capacité du modèle à rendre compte des petits risques. [L3 slide 40, L3 slide 41]

## Cesse d'être valide quand
Un coude en zéro exige un point de référence : le modèle doit dire où il se trouve, et la théorie des perspectives le prend comme donné. [L3 slide 20]
