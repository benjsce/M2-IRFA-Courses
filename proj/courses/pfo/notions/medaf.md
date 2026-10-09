---
id: pfo/medaf
nom: MEDAF
symbole: '$E(R_i)$, $E(R_m)$, $w^M$, $w^T$'
type: notion
statut: source
construite_a_partir_de:
- pfo/beta
- pfo/portefeuille-tangent
alias:
- CAPM
- Capital Asset Pricing Model
- modèle d'évaluation des actifs financiers
- prime de risque du marché
- market risk premium
refs:
- §4.1
- p. 58
- §4.2.1
- p. 59
---

## Ce que c'est
Le modèle selon lequel le rendement espéré d'un actif risqué ne dépend que de son exposition au risque de marché, mesurée par son bêta. [§4.2.1]

## Forme
$$E(R_i)=R_f+\beta_i\,\big(E(R_m)-R_f\big)$$ [§4.2.1]

## Ce que les symboles modélisent
$E(R_i)$ est le rendement espéré de l'actif $i$, celui que le modèle juge justifié par son risque ; $E(R_m)$ est celui du portefeuille de marché, par exemple le S&P 500 ou le CAC 40. L'écart $E(R_m)-R_f$ est la prime de risque du marché : ce que le marché rapporte en moyenne au-delà du taux sans risque $R_f$. [§4.2.1, p. 59]

$w^M$ et $w^T$ sont les vecteurs de poids du portefeuille de marché et du portefeuille tangent. [p. 58]

## Ce qui la définit
**Connus** : le taux sans risque, la prime de risque du marché et le bêta de l'actif. **Cherché** : le rendement que l'actif doit rapporter pour que son risque soit rémunéré, ni plus ni moins. Au taux sans risque s'ajoute la prime du marché, prise autant de fois que le bêta. [§4.1, §4.2.1]

![Les trois barres du marché de l'exemple. Sur le socle commun R_f = 2 % s'empile la prime du marché, E(R_m) − R_f = 5,33 points, prise β fois : trois quarts de bloc pour le premier actif, 6 % ; un bloc pour le marché, 7,33 % ; un bloc et demi pour le second actif, 10 %. Dessous, la Forme : E(R_i) = R_f + β_i (E(R_m) − R_f).](figures/medaf.svg) [ajout]

La part du risque d'un actif qui ne bouge pas avec le marché n'est pas rémunérée : elle disparaît dans un portefeuille diversifié, et personne n'a à être payé pour la porter. [§4.1, p. 59]

Pourquoi le portefeuille de marché sert de référence : sous les hypothèses du MEDAF, il coïncide avec le portefeuille tangent, $w^M=w^T$. Tous les investisseurs détiennent alors le même portefeuille risqué, le marché, et ne diffèrent que par la part qu'ils placent sans risque. En général, et sur des données historiques, les deux ne coïncident pas : c'est un résultat de la théorie, qui repose sur ses hypothèses. [p. 58]

## Le chemin jusqu'ici
Le MEDAF réunit deux constructions. D'un côté pfo/portefeuille-tangent, le mélange risqué que la droite issue du taux sans risque touche sur pfo/frontiere-efficiente, là où pfo/ratio-de-sharpe est le plus élevé ; de l'autre pfo/portefeuille-de-marche, pondéré par les capitalisations. Le modèle pose qu'ils sont le même portefeuille, et c'est ce qui fait du marché la référence de tout actif. [ajout]

pfo/beta mesure alors l'exposition de chaque actif à cette référence. Il se lit dans pfo/matrice-de-covariance, dont la diagonale porte le carré de fpp/volatilite et que fpp/echelonnement-de-la-variance annualise ; c'est la même matrice qui, avec pfo/moments-du-portefeuille, chiffre le rendement et le risque de tout mélange. [ajout]

Ces rendements de portefeuille sont des moyennes pondérées, exactes en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique, comme le rappelle pfo/piege-d-agregation. En amont, dup/moyenne-variance résume chaque dup/loterie par sa moyenne et son écart type, et dup/diversification montre pourquoi le risque propre d'un actif peut se dissoudre dans un mélange : c'est lui que le MEDAF ne paie pas. [ajout]

## Exemple minimal
Sur le marché de l'exemple, $R_f=2\,\%$ et $E(R_m)=7{,}33\,\%$ : le second actif, de bêta 1,5, doit rapporter $2+1{,}5\times5{,}33=10\,\%$, exactement son rendement espéré. [ajout]

## Geste de calcul type
Le marché pèse deux tiers et un tiers des deux actifs, de rendements espérés 6 % et 10 % : $E(R_m)=\tfrac23\times6+\tfrac13\times10=7{,}33\,\%$, et la prime du marché vaut $7{,}33-2=5{,}33$ points. Pour le premier actif, de bêta 0,75 : $2+0{,}75\times5{,}33=6\,\%$. [ajout]

Les poids de capitalisation, deux tiers et un tiers, sont aussi ceux du portefeuille tangent du chapitre 3, proportionnels à $(6-2)/0{,}01=400$ et $(10-2)/0{,}04=200$ : sur ce marché, $w^M=w^T$, et c'est pourquoi chaque actif retombe exactement sur son rendement. [ajout]

## Cesse d'être valide quand
L'égalité $w^M=w^T$ et la formule reposent sur les hypothèses du modèle ; le portefeuille tangent calculé sur des données historiques ne coïncide pas, en pratique, avec le marché observé. [p. 58]

Le vrai portefeuille de marché n'est pas observable ; on le remplace par un indice d'actions. [p. 59, p. 67]

Le cours rappelle les limites empiriques d'un modèle à un seul facteur : c'est la raison du modèle de Fama et French, qui en ajoute deux. [§4.2.2]
