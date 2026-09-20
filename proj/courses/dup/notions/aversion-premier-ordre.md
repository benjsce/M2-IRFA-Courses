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
---

## Ce que c'est
La prime d’un petit pari de moyenne nulle proportionnelle à l’écart type lui-même, et non à son carré. [L2 slide 21]

## Forme
$$r(\sigma)=\dfrac{\lambda^{\frac{1}{1-\gamma}}-1}{\lambda^{\frac{1}{1-\gamma}}+1}\,\sigma=k\sigma$$ [L3 slide 41]

## Ce qui la définit
Elle apparaît dès que la fonction de valeur présente un coude en zéro, ou que les probabilités sont déformées : la prime ne s’évanouit plus au second ordre quand le pari rétrécit. [L3 slide 41, L2 slide 21]

C’est ce qui permet d’expliquer le refus de petits paris favorables, que l’utilité espérée dérivable interdit. [L2 slide 21]

## Exemple minimal
Avec $\lambda=2$ et $\gamma=0$ : $k=1/3$, donc un pari de $\pm10$ coûte une prime de $3{,}33$, contre $0{,}5$ au second ordre. [ajout]

## Geste de calcul type
Chercher si la prime tend vers zéro comme $\sigma$ ou comme $\sigma^2$ : c’est le test qui sépare les deux régimes, et il décide de la capacité du modèle à rendre compte des petits risques. [L3 slide 40, L3 slide 41]

## Cesse d'être valide quand
Un coude en zéro exige un point de référence : le modèle doit dire où il se trouve, et la théorie des perspectives le prend comme donné. [L3 slide 20]
