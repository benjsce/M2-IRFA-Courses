---
id: dup/independance-de-certitude
nom: Indépendance de certitude
type: notion
statut: source
cas_de: dup/independance-restreinte
valeur: le mélange n’est imposé qu’avec une loterie constante
construite_a_partir_de:
- dup/cadre-anscombe-aumann
alias:
- certainty independence
- axiome 5
refs:
- L4 slide 45
---

## Ce que c'est
L’indépendance n’est exigée que pour un mélange avec une loterie constante, et non avec un acte quelconque. [L4 slide 45]

## Forme
$$f\succsim g\iff \alpha f+(1-\alpha)\ell\succsim\alpha g+(1-\alpha)\ell,\qquad \ell\in\Delta(X),\ \alpha\in(0,1)$$ [L4 slide 45]

## Ce que les symboles modélisent
$f$ et $g$ sont des actes quelconques, et $\ell$ une loterie constante : elle donne la même loterie dans tous les états, ce qui la distingue d'un acte ordinaire. $\Delta(X)$ est l'ensemble des loteries sur les conséquences, et $\alpha$ le poids du mélange. [L4 slide 45, ajout]

## Ce qui la définit
L’indépendance pleine remplacerait la loterie constante $\ell$ par un acte $h$ quelconque, et c’est elle qui, avec les quatre premiers axiomes, force la croyance à être une probabilité unique. La restreindre aux loteries constantes laisse la place à l’aversion à l’ambiguïté : mélanger avec un acte constant ne change pas la position de l’agent face aux états, mélanger avec un acte ordinaire, si. [L4 slide 45, L4 slide 46]

Un axiome supplémentaire complète la liste. L’aversion à l’ambiguïté dit que si $f$ et $g$ sont indifférents, tout mélange des deux est au moins aussi bon qu’eux. Mélanger des actes indifférents peut en effet couvrir l’ambiguïté, et l’indépendance pleine exigerait précisément l’indifférence à tout mélange de ce genre. [L4 slide 45]

## Le chemin jusqu'ici
dup/acte et dup/loterie s’emboîtent dans dup/cadre-anscombe-aumann, qui fournit l’opération de mélange entre actes et la notion d’acte constant. [ajout]

Sans cette opération, l’axiome ne pourrait même pas s’écrire : il porte sur une égalité entre deux préférences, dont l’une compare des mélanges. Et c’est dans le cadre seul que « loterie constante » se distingue d’« acte quelconque », distinction qui fait tout le contenu de l’affaiblissement. [ajout]

## Exemple minimal
Sur l’urne du cours, parier sur bleu et parier sur vert valent zéro chacun, tandis que leur mélange à parts égales paie 50 dans les deux états et vaut $100/3$. [L4 slide 42]

## Geste de calcul type
Pour savoir si un modèle admet l’ambiguïté, remplacer la loterie constante par un acte dans l’axiome : si la préférence y résiste, la croyance est nécessairement un point. [L4 slide 46]

## Cesse d'être valide quand
Même affaibli, l’axiome reste exigeant : il impose à la valeur une invariance d’échelle et de translation, que des modèles comme les préférences variationnelles abandonnent. [L4 slide 49, L4 slide 50, L4 slide 37]
