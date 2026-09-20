---
id: dup/utilite-quadratique
nom: Utilité quadratique
type: notion
statut: source
cas_de: dup/famille-hara
valeur: une aversion absolue croissante, $A(z)=(c-z)^{-1}$
construite_a_partir_de:
- dup/fonction-utilite
- dup/moyenne-variance
alias:
- quadratic utility
refs:
- L1 slide 14
- L1 slide 15
---

## Ce que c'est
La seule forme d’utilité pour laquelle l’utilité espérée ne dépend que de la moyenne et de la variance. [L1 slide 14]

## Forme
$$U(x)=\alpha x+\beta x^2\ \implies\ \mathbb{E}[U(\tilde x)]=\alpha\mu+\beta(\mu^2+\sigma^2)$$ [L1 slide 14]

## Ce qui la définit
Sur des distributions non restreintes, un agent à utilité espérée classe tous les risques par leur seule moyenne et leur seule variance si et seulement si son utilité est quadratique. [L1 slide 14]

## Exemple minimal
Avec $\alpha=1$ et $\beta=-0{,}005$, le pari $(0,\tfrac12;100,\tfrac12)$ vaut $25$. [ajout]

## Geste de calcul type
Substituer $\mathbb{E}[U]=\alpha\mu+\beta(\mu^2+\sigma^2)$ : deux moments suffisent. Vérifier ensuite que la richesse reste sous le point de satiation $-\alpha/2\beta$, sans quoi l’utilité décroît. [L1 slide 14, L1 slide 15]

## Cesse d'être valide quand
Avec $\beta<0$ l’utilité est concave mais $U'(x)=\alpha+2\beta x$ finit par devenir négative : au-delà du point de satiété, plus de richesse fait baisser l’utilité, et l’aversion absolue croît avec la richesse. [L1 slide 15]
