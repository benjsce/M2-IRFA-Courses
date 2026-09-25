---
id: pfo/ligne-de-marche-des-capitaux
nom: Ligne de marché des capitaux
symbole: '$\alpha$, $\mu_C$, $\sigma_C$'
type: notion
statut: source
construite_a_partir_de:
- pfo/portefeuille-tangent
- dup/frontiere-actif-sans-risque
alias:
- Capital Market Line
- CML
- droite de marché des capitaux
refs:
- p. 40
- p. 41
- Fig. 3.2
---

## Ce que c'est
La droite qui relie l'actif sans risque au portefeuille tangent : tous les placements qui mélangent ces deux-là s'y trouvent, et sa pente est le ratio de Sharpe maximal. [p. 40, p. 41]

## Forme
$$\mu_C=(1-\alpha)R_f+\alpha\,\mu_{W^*}=R_f+\alpha\,(\mu_{W^*}-R_f),\qquad \sigma_C=\alpha\,\sigma_{W^*}$$ [p. 41]

## Ce que les symboles modélisent
$\alpha$ est la part du capital placée dans le portefeuille tangent, le reste $1-\alpha$ allant à l'actif sans risque ; le cours la prend entre zéro et un. $\mu_C$ et $\sigma_C$ sont le rendement espéré et l'écart type du placement combiné. [p. 41]

Au chapitre 2, $\alpha$ désignait tour à tour le lissage EWMA, le niveau d'un test et le seuil de la VaR ; ici, c'est une part de capital. [ajout]

## Ce qui la définit
Une fois le portefeuille tangent déterminé, l'investisseur peut le combiner avec l'actif sans risque. Le rendement espéré et le risque du mélange sont tous deux linéaires en $\alpha$ : les combinaisons décrivent une droite dans le plan risque-rendement, la ligne de marché des capitaux. [p. 41]

Sa pente est le ratio de Sharpe du portefeuille tangent, $SR(W^*)=\max_W SR(W)$. [p. 40, Fig. 3.2]

## Le chemin jusqu'ici
dup/frontiere-actif-sans-risque établissait déjà la géométrie : mélanger un actif sans risque et un actif risqué trace une droite, parce qu'un actif de variance nulle ne peut pas courber le mélange. Il restait à choisir l'actif risqué ; pfo/portefeuille-tangent est celui qui rend cette droite la plus pentue. [ajout]

Ce choix se fait sur pfo/frontiere-efficiente par le critère de pfo/ratio-de-sharpe, et tous deux lisent les deux nombres de pfo/moments-du-portefeuille. L'espérance y est linéaire comme pfo/piege-d-agregation le montre pour pfo/rendement-arithmetique, et non pour pfo/rendement-logarithmique ; le risque vient de pfo/matrice-de-covariance, annualisée par fpp/echelonnement-de-la-variance, avec le carré de fpp/volatilite sur la diagonale. [ajout]

En amont, le décor est celui de la décision en incertain : dup/loterie, résumée par dup/moyenne-variance, et dup/diversification, sans laquelle la frontière serait une droite et il n'y aurait pas de tangente à chercher. [ajout]

## Exemple minimal
Avec un taux sans risque de 2 % et le portefeuille tangent de l'exemple, de rendement 7,33 % et de volatilité 9,43 %, placer la moitié du capital dans chacun donne un rendement de 4,67 % pour une volatilité de 4,71 %. [ajout]

## Geste de calcul type
$\mu_C=2\,\%+0{,}5\times(7{,}33\,\%-2\,\%)=4{,}67\,\%$ et $\sigma_C=0{,}5\times9{,}43\,\%=4{,}71\,\%$. Le ratio du mélange, $(4{,}67-2)/4{,}71=0{,}566$, est celui du portefeuille tangent : toute la droite a la même pente. [ajout]

## Cesse d'être valide quand
Le cours limite $\alpha$ à l'intervalle entre zéro et un. [p. 41]

Avec $\alpha>1$, l'investisseur emprunte au taux sans risque pour investir davantage dans le portefeuille tangent, et la droite se prolonge au-delà de lui ; cela suppose qu'on puisse emprunter au même taux qu'on prête. [ajout]
