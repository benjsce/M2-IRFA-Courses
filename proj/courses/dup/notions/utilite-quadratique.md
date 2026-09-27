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

## Ce que les symboles modélisent
$\alpha$ et $\beta$ sont les deux coefficients d'une parabole, et non des degrés d'aversion : c'est leur rapport qui fixe le sommet, au-delà duquel l'utilité se met à décroître. $\beta$ porte le terme carré, donc toute la courbure. [L1 slide 14]

## Ce qui la définit
Sur des distributions non restreintes, un agent à utilité espérée classe tous les risques par leur seule moyenne et leur seule variance si et seulement si son utilité est quadratique. [L1 slide 14]

## Le chemin jusqu'ici
Deux fils y mènent. dup/fonction-utilite fournit la forme ; dup/loterie, réduite par dup/moyenne-variance, fournit le résumé à deux nombres. [ajout]

Cette fiche est le point où les deux se rencontrent exactement : l'utilité quadratique est la **seule** forme pour laquelle l'utilité espérée ne dépend que de la moyenne et de la variance. Le socle dit donc pourquoi la fiche existe — c'est une justification de l'analyse moyenne-variance, et la seule que le cours donne dans le cadre de l'utilité espérée. [ajout]

## Exemple minimal
Avec $\alpha=1$ et $\beta=-0{,}005$, le pari $(0,\tfrac12;100,\tfrac12)$ vaut $25$. [ajout]

![La parabole $U(x)=x-0{,}005\,x^2$ monte jusqu'au point de satiété $-\alpha/2\beta=100$, puis redescend, en pointillé. Le pari du cours, 0 ou 100, a pour moyenne $\mu=50$ et pour variance $\sigma^2=2\,500$. À la verticale de μ, la courbe vaut $U(\mu)=\alpha\mu+\beta\mu^2=37{,}5$ ; le milieu de la corde, l'utilité espérée, est plus bas de $\beta\sigma^2=-12{,}5$ : $\mathbb{E}(U)=U(\mu)+\beta\sigma^2=\alpha\mu+\beta(\mu^2+\sigma^2)=25$.](figures/utilite-quadratique.svg) [ajout]

## Geste de calcul type
Substituer $\mathbb{E}[U]=\alpha\mu+\beta(\mu^2+\sigma^2)$ : deux moments suffisent. Vérifier ensuite que la richesse reste sous le point de satiation $-\alpha/2\beta$, sans quoi l’utilité décroît. [L1 slide 14, L1 slide 15]

## Cesse d'être valide quand
Avec $\beta<0$ l’utilité est concave mais $U'(x)=\alpha+2\beta x$ finit par devenir négative : au-delà du point de satiété, plus de richesse fait baisser l’utilité, et l’aversion absolue croît avec la richesse. [L1 slide 15]
