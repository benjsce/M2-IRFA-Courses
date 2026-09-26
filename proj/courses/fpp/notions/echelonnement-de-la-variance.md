---
id: fpp/echelonnement-de-la-variance
nom: Échelonnement de la variance
symbole: '$\sigma(T)$, $Y(T)$'
type: notion
statut: source
construite_a_partir_de:
- fpp/volatilite
alias:
- scaling of variance
- racine du temps
- square root of time
refs:
- §5.3
- Rem. 1
- exo. 18
---

## Ce que c'est
Quand les accroissements du log-prix sont indépendants et de même loi, la variance croît comme le temps et l'écart type comme sa racine. [§5.3]

## Forme
$$\sigma^2(T)=\sigma^2\,T,\qquad \sigma(T)=\sigma\sqrt T$$ [§5.3]

## Ce que les symboles modélisent
$Y(T)$ est le log-rendement cumulé de 0 à $T$, tel que $\tilde S_T=e^{Y(T)}$ ; $\sigma(T)$ est son écart type sur toute la durée $T$ ; $\sigma$ la volatilité sur une unité de temps, l'année, et $T$ la durée comptée en années. [§5.3]

## Retrouver la formule
![L'enveloppe d'un écart type autour du log-prix, pour une volatilité de 20 % par an : elle s'ouvre comme la racine du temps. Au quart de l'année, elle ne vaut pas le quart de 20 % mais la moitié, 10 %.](figures/echelonnement-de-la-variance.svg) [ajout]

Découpons l'année en quatre trimestres. Le log-rendement de l'année est la somme des quatre log-rendements trimestriels : $Y(T)=\sum_i\Delta Y_i$. [§5.3]

Première hypothèse : les quatre accroissements ont la même loi, donc la même variance. Seconde hypothèse : ils sont indépendants, donc leurs variances s'additionnent, ce que ne font pas leurs écarts types. [§5.3]

La variance de l'année, $0{,}2^2=0{,}04$, est donc la somme de quatre variances égales de $0{,}01$ ; l'écart type d'un trimestre vaut $\sqrt{0{,}01}=10\,\%$, la moitié de celui de l'année. [ajout]

En général, $\sigma^2(t_1+t_2)=\sigma^2(t_1)+\sigma^2(t_2)$ : la variance est proportionnelle à la durée. [§5.3]

$$\sigma^2(T)=\sigma^2T,\qquad\sigma(T)=\sigma\sqrt T$$ [§5.3]

## Ce qui la définit
Ce qui est **connu** : la volatilité sur une unité de temps. Ce qu'on **cherche** : la dispersion sur une autre durée. Les écarts types ne s'additionnent pas, les variances si ; le livre d'exercices l'applique à une exposition de change sur trois mois, dont la volatilité est la moitié de la volatilité annuelle, 5 % pour 10 %. [§5.3, exo. 18]

La convention de jours compte : une année de 256 jours donne une volatilité journalière de $\sigma/16$, une année de 365 jours $\sigma/\sqrt{365}$. [Rem. 1, ajout]

## Le chemin jusqu'ici
fpp/volatilite donne l'écart type du rendement sur une période ; l'échelonnement dit comment ce nombre change quand la période change, pourvu que les périodes successives se ressemblent et ne s'influencent pas. [ajout]

## Exemple minimal
Une volatilité de 20 % par an donne 10 % sur trois mois et 1,25 % par jour, sur une année de 256 jours. [ajout]

## Geste de calcul type
Annualiser une volatilité journalière en la multipliant par la racine du nombre de jours : $1{,}25\,\%\times\sqrt{256}=20\,\%$. [Rem. 1, ajout]

## Cesse d'être valide quand
Si les accroissements se corrèlent d'une période à l'autre, ou si leur volatilité change, les variances ne s'additionnent plus simplement et la racine du temps se trompe. La moyenne, elle, croît comme le temps et non comme sa racine. [§5.3, ajout]
