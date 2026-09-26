---
id: fpp/volatilite
nom: Volatilité
symbole: '$\sigma$, $\sigma_A$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- volatility
refs:
- Déf. 2
---

## Ce que c'est
L’écart type du rendement d’un actif : de combien ce rendement s’écarte d’ordinaire de sa moyenne. [Déf. 2, ajout]

## Forme
$$\sigma=\mathrm{stdev}(\text{rendement})$$ [Déf. 2]

## Ce que les symboles modélisent
$\sigma$ est l'écart type d'un rendement, pas d'un prix : un pourcentage, donné d'ordinaire pour un an, qui ne dit rien du niveau du prix. Il mesure la dispersion autour de la moyenne, pas la moyenne elle-même : un titre peut être très volatil et rapporter peu. [Déf. 2, Rem. 1, ajout]

$\sigma_A$ est la volatilité de l'actif d'une entreprise, c'est-à-dire du rendement de tout ce qu'elle possède. L'indice dit de quel rendement on parle : celle des capitaux propres de la même entreprise n'est pas la même. [§1.3]

## Ce qui la définit
Elle mesure le risque par la dispersion du rendement, sans regarder le sens des écarts : un écart à la hausse compte autant qu'un écart à la baisse. [Déf. 2, ajout]

![Deux titres qui rapportent en moyenne 5 % par an. Chaque année, le premier rapporte 5 % plus ou moins 10 points, le second 5 % plus ou moins 20 points, à parts égales. Même moyenne, écarts différents : leurs volatilités sont 10 % et 20 %.](figures/volatilite.svg) [ajout]

Elle se donne par an ; sur une durée plus courte, elle ne se réduit pas en proportion de la durée, mais comme sa racine carrée. [§5.3]

## Exemple minimal
Deux titres rapportent en moyenne 5 % par an ; l'un s'écarte d'ordinaire de 10 points de cette moyenne, l'autre de 20 : leurs volatilités sont 10 % et 20 %. [ajout]

## Geste de calcul type
Le second titre rapporte $+25\,\%$ ou $-15\,\%$, à parts égales. Moyenne : $5\,\%$. Écarts à la moyenne : $+20$ et $-20$ points. Écart type : la racine de la moyenne des carrés des écarts, $\sqrt{(20^2+20^2)/2}=20\,\%$. [ajout]

## Cesse d'être valide quand
Elle ne décrit complètement le risque que si le rendement est gaussien ; sinon elle ignore l’asymétrie et les queues. [ajout]
