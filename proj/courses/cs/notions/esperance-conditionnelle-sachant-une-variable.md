---
id: cs/esperance-conditionnelle-sachant-une-variable
nom: Espérance conditionnelle sachant une variable
symbole: '$E[X|Y]$, $\sigma(Y)$'
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle
alias:
- E[X|Y]
- conditional expectation given a random variable
refs:
- Déf. 0.4.2
- Rem. 0.4.3
---

## Ce que c'est
Conditionner par une variable $Y$, c'est conditionner par l'information qu'elle apporte, la tribu $\sigma(Y)$ ; le résultat est alors une fonction de $Y$. [Déf. 0.4.2, Rem. 0.4.3]

## Forme
$$E[X|Y]=E[X|\sigma(Y)]$$ [Déf. 0.4.2]

$$\text{i) } E[X|Y] \text{ est } \sigma(Y)\text{-mesurable}\qquad\text{ii) } E[Xg(Y)]=E\big[E[X|Y]\,g(Y)\big]\ \text{ pour toute } g \text{ borélienne bornée}$$ [Rem. 0.4.3]

## Ce que les symboles modélisent
$\sigma(Y)$ est la tribu engendrée par $Y$ : les événements de la forme $\{Y\in B\}$, ceux dont on sait s'ils se sont produits dès qu'on connaît la valeur de $Y$. $E[X|Y]$ est une variable aléatoire, que la condition i) oblige à ne dépendre que de $Y$ ; les fonctions $g(Y)$ de ii) sont les paris qu'on peut écrire en ne regardant que $Y$. [Déf. 0.4.2, Rem. 0.4.3, ajout]

## Ce qui la définit
La définition générale demandait de tester $X$ contre toute variable $U$ mesurable par rapport à l'information ; quand l'information est celle de $Y$, ces variables sont exactement les $g(Y)$, et la condition se réécrit avec elles. [Rem. 0.4.3]

Être $\sigma(Y)$-mesurable, c'est s'écrire $h(Y)$ pour une fonction borélienne $h$ : $E[X|Y]=h(Y)$, et $h(y)$ se lit comme la prévision de $X$ quand $Y$ vaut $y$. [ajout]

## Le chemin jusqu'ici
cs/esperance-conditionnelle définit la prévision sachant une tribu quelconque ; il suffit de prendre pour tribu l'information que porte $Y$. La condition sur les variables $U$ devient une condition sur les fonctions de $Y$, plus facile à manier. [Déf. 0.4.1, Rem. 0.4.3]

## Exemple minimal
Deux lancers, $X$ le nombre de piles, $Y$ égal à $1$ si le premier lancer donne pile et $0$ sinon : $E[X|Y]=\tfrac12+Y$, soit $h(y)=\tfrac12+y$. [ajout]

## Geste de calcul type
Quand $Y$ prend un nombre fini de valeurs, calculer $h(y)=E[X\,1_{\{Y=y\}}]/P(Y=y)$ pour chacune, puis écrire $E[X|Y]=h(Y)$. Ici $h(1)=\tfrac34/\tfrac12=1{,}5$ et $h(0)=\tfrac14/\tfrac12=0{,}5$. [ajout]

## Cesse d'être valide quand
$X$ n'est pas intégrable, comme pour toute espérance conditionnelle. La fonction $h$ n'est fixée que sur les valeurs que $Y$ prend vraiment, à un ensemble de probabilité nulle près. [Déf. 0.4.2, ajout]
