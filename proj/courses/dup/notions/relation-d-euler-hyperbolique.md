---
id: dup/relation-d-euler-hyperbolique
nom: Relation d'Euler hyperbolique forte
symbole: '$c(w)$, $y_t$, $W(w)$'
type: notion
statut: source
construite_a_partir_de:
- dup/euler-sans-engagement
alias:
- strong hyperbolic Euler relation
- Euler hyperbolique
refs:
- L5 slide 37
- L5 slide 38
- L5 slide 39
- L5 slide 40
---

## Ce que c'est
La même équation d'Euler sans engagement, à horizon infini et avec un revenu aléatoire, quand tous les moi suivent une même règle de consommation. [L5 slide 40]

## Forme
$$u'\big(c(w_t)\big)=\mathbb{E}_t\Big[\big(c'(w_{t+1})\,\beta\delta+(1-c'(w_{t+1}))\,\delta\big)\,R\,u'\big(c(w_{t+1})\big)\Big]$$ [L5 slide 40]

## Ce que les symboles modélisent
$y_t$ est le revenu du travail de la période $t$, aléatoire et indépendant d'une période à l'autre ; la richesse évolue par $w_{t+1}=R(w_t-c_t)+y_{t+1}$. $c(w)$ est la règle de consommation, la même pour tous les moi : elle ne dépend que de la richesse, pas de la date. [L5 slide 37]

La valeur $V(w_{t+1})=u(c(w_{t+1}))+\delta\,\mathbb{E}_{t+1}V(\dots)$ est celle du moi $t$ : il n'applique $\beta$ qu'une fois, en tête. Ce que le moi $t+1$ attribue lui-même à sa richesse est une autre fonction, notée $W(w)$ : $W(w_{t+1})$ diffère de $V(w_{t+1})$ parce que le moi $t+1$ applique $\beta$ à ses propres suivants. [L5 slide 38]

## Ce qui la définit
La dérivation est celle des trois périodes, avec une espérance : la condition du premier ordre du moi $t$, puis la dérivée de $V$ où la part épargnée pèse $1/\beta$, puis la combinaison des deux. Le crochet reste le facteur d'actualisation effectif, désormais aléatoire parce que $c'(w_{t+1})$ l'est. [L5 slide 39]

Avec une contrainte d'emprunt, l'égalité devient $\ge$, et elle vaut égalité quand $c_t<w_t$. Les auteurs obtiennent l'existence de $V$ et une règle $c(w)$ continue en bornant l'aversion au risque et l'incertitude du revenu, et en prenant $\beta$ proche de 1. [L5 slide 37, L5 slide 40]

## Le chemin jusqu'ici
dup/euler-sans-engagement établissait le facteur effectif sur trois périodes, en résolvant à rebours les moi successifs. À horizon infini, il n'y a plus de dernière période d'où partir : la règle stationnaire remplace la récurrence, et le crochet est le même. [L5 slide 37, L5 slide 39]

Chaque moi y reste celui de dup/engagement-complet, avec les poids de dup/actualisation-quasi-hyperbolique, et chacun prévoit les suivants comme le veut dup/sophistication. Leur désaccord vient de ce que dup/coherence-dynamique tombe sous dup/biais-pour-le-present, les choix de dup/inversion-des-preferences-dans-le-temps violant dup/stationnarite mais pas dup/invariance-temporelle ; ce sont eux qui écartaient dup/actualisation-exponentielle au profit d'une dup/utilite-actualisee plus souple, sur les utilités de dup/fonction-utilite. [L5 slide 22, ajout]

## Exemple minimal
Si le moi suivant consomme un dixième de tout euro de plus, avec $\beta=\tfrac12$ et $\delta=1$, le facteur effectif vaut $0{,}1\times0{,}5+0{,}9\times1=0{,}95$ : l'agent actualise presque sans biais. [ajout]

## Geste de calcul type
Supposer une règle $c(w)$, calculer sa pente à la richesse de demain, et vérifier le crochet sur chaque revenu possible. [ajout]

## Cesse d'être valide quand
L'existence de $V$ et la dérivabilité de $c(w)$ sont supposées ; les établir est la principale contribution de l'article, et elles peuvent échouer, comme à trois périodes. [L5 slide 37]
