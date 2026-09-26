---
id: pfo/var-de-cornish-fisher
nom: VaR de Cornish-Fisher
symbole: '$q_\alpha^{CF}$, $z_{CF}$'
type: notion
statut: source
cas_de: pfo/modele-de-risque
valeur: la loi normale corrigée de l'asymétrie et de l'excès de kurtosis
construite_a_partir_de:
- pfo/var-gaussienne
- pfo/developpement-de-cornish-fisher
alias:
- Cornish-Fisher VaR
- CVaR de Cornish-Fisher
- VaR modifiée
- modified VaR
refs:
- §2.5.1
- éq. 2.29
- éq. 2.30
- éq. 2.35
- éq. 2.36
- Listing 2.2
---

## Ce que c'est
La VaR et la CVaR gaussiennes dans lesquelles le quantile normal est remplacé par le quantile corrigé de Cornish-Fisher. [Listing 2.2, §2.5.1]

## Forme
$$\mathrm{VaR}_\alpha^{CF} \approx -q_\alpha^{CF}\times\text{capital}, \qquad \mathrm{CVaR}_\alpha^{CF} \approx -\left(\dfrac{1}{\alpha}\int_0^{\alpha} q_u^{CF}\,du\right)\times\text{capital}, \qquad q_{u}^{CF} = \mu + \sigma\, z_{CF}(u)$$ [éq. 2.29, éq. 2.30, éq. 2.35, Listing 2.2]

## Ce que les symboles modélisent
$z_{CF}$ est le quantile centré réduit corrigé ; au niveau $u$, $z_{CF}(u)$ est le $q_u$ que rend pfo/developpement-de-cornish-fisher, sous le nom que le poly lui donne ici. $q_u^{CF}=\mu+\sigma\,z_{CF}(u)$ le ramène en rendement, et $q_\alpha^{CF}$ est ce rendement au seuil $\alpha$. Le premier se compare à $z_\alpha$, le second à un rendement observé. [éq. 2.29, éq. 2.35, ajout]

Le poly écrit la VaR et la CVaR en rendement ; le listing les multiplie par le capital, comme la Forme ci-dessus. [éq. 2.29, éq. 2.30, Listing 2.2]

## Ce qui la définit
**Connu** : la moyenne $\mu$, l'écart type $\sigma$ et, à chaque niveau $u$, le quantile corrigé $z_{CF}(u)$. **Cherché** : la VaR, qui n'est qu'un de ces quantiles, celui du seuil $\alpha$ ; et la CVaR, qui est leur moyenne sur toute la queue, de 0 à $\alpha$. [§2.5.1, éq. 2.32, éq. 2.33]

Pourquoi une moyenne de quantiles : tirer un rendement dans la queue revient à tirer un niveau $u$ uniformément entre 0 et $\alpha$, puis à lire le quantile $q_u$. La moyenne de la queue est donc la moyenne des quantiles, $\tfrac1\alpha\int_0^\alpha q_u\,du$. Le développement fournissant des quantiles et non une moyenne, il faut les intégrer. [ajout]

En Python, on construit une grille de probabilités $u_1, \dots, u_M$ sur $[0, \alpha]$, on calcule le quantile corrigé en chaque point, et l'on intègre par la méthode des trapèzes : `np.trapezoid(q_cf_values, u_values) / alpha`. [éq. 2.34, éq. 2.35, éq. 2.36, Listing 2.2]

## Le chemin jusqu'ici
pfo/var-gaussienne fournit le calcul, pfo/developpement-de-cornish-fisher le quantile à y substituer : la VaR de Cornish-Fisher est la VaR gaussienne dans laquelle $z_\alpha$ a été corrigé. Ce quantile ne sait de la loi réelle que deux nombres, pfo/coefficient-d-asymetrie et pfo/kurtosis, tous deux réduits par l'écart type de fpp/volatilite. [ajout]

Pour la CVaR, la substitution ne suffit plus. pfo/valeur-a-risque-conditionnelle est une moyenne de queue dont pfo/valeur-a-risque ne fixe que la borne : il faut corriger chaque quantile de la queue, puis les moyenner. [ajout]

## Exemple minimal
Avec $\mu = 0{,}05\,\%$, $\sigma = 2\,\%$, une asymétrie de −0,5, un excès de kurtosis de 3 et un capital de 1 000 000, la VaR à 95 % passe de 32 397 en gaussien à 33 935 avec Cornish-Fisher, et la CVaR de 40 754 à 53 511. [ajout]

![Les quantiles de la queue, de $u=0{,}0001$ à $u=0{,}05$, gaussiens et corrigés, pour les paramètres de l'exemple. La VaR se lit au bout de chaque courbe et bouge à peine. La CVaR est la moyenne de toute la courbe. Au-delà de 1,73 écart type, soit sous $u=4{,}2\,\%$, le terme de kurtosis change de signe et pousse vers les pertes : la correction écarte surtout l'extrême queue, d'où le passage de $-4{,}08\,\%$ à $-5{,}35\,\%$.](figures/var-de-cornish-fisher.svg) [ajout]

## Geste de calcul type
$z_{CF} = -1{,}7217$ au seuil de 5 %, donc $\mathrm{VaR} = -(0{,}0005 - 1{,}7217 \times 0{,}02) \times 10^6 = 33\,935$. La CVaR s'obtient en intégrant $q_u^{CF}$ sur la grille du listing, 1 000 points entre 0,0001 et 0,05. [ajout]

## Cesse d'être valide quand
Elle hérite des limites du développement : pour une asymétrie ou une kurtosis fortes, les quantiles corrigés de l'extrême queue perdent leur ordre, et l'intégrale de la CVaR moyenne des valeurs qui ne sont plus des quantiles. [ajout]

La grille du listing commence à 0,0001 et non à 0, le quantile normal de 0 étant infini : l'intégrale néglige la toute première portion de la queue. [ajout]
