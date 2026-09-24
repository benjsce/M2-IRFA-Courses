---
id: pfo/rendement-logarithmique
nom: Rendement logarithmique
symbole: '$r_t$, $r_{0\to T}$'
type: notion
statut: source
cas_de: pfo/passage-aux-rendements
construite_a_partir_de: []
alias:
- log-return
- log return
- logarithmic return
- rendement log
refs:
- §1.2.1
- éq. 1.5
- éq. 1.6
---

## Ce que c'est
Le logarithme du rapport de deux prix successifs. [éq. 1.5]

## Forme
$$r_t = \ln\!\left(\dfrac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1}), \qquad r_{0\to T} = \ln\!\left(\dfrac{P_T}{P_0}\right) = \sum_{t=1}^{T} r_t$$ [éq. 1.5, éq. 1.6]

## Ce que les symboles modélisent
$r_t$ mesure la variation du prix sur une période en échelle logarithmique. Il se lit comme un rendement et reste proche du rendement arithmétique pour de petites variations — 0,995 % pour une hausse de 1 % — mais s'en écarte quand la variation grandit : 9,53 % pour une hausse de 10 %. [ajout]

$r_{0\to T}$ est le rendement logarithmique de la période entière, et il vaut exactement la somme des rendements des sous-périodes. [éq. 1.6]

## Ce qui la définit
Sa propriété est l'additivité dans le temps : la somme des logarithmes de rapports successifs est télescopique et se réduit au logarithme du rapport entre le dernier et le premier prix. [§1.2.1, éq. 1.6]

C'est le rendement que le cours calcule ensuite dans chaque listing, sur les prix de clôture ajustés : filtrage, EWMA, covariances, tests de normalité et mesures de risque. [p. 11, Listing 1.1, Listing 2.1, Listing 2.2]

## Exemple minimal
Un prix qui passe de 100 à 110 puis à 99 fait +9,53 %, puis −10,54 %, et −1,01 % sur l'ensemble, qui est bien la somme des deux. [ajout]

## Geste de calcul type
Sommer, puis revenir à l'échelle arithmétique si besoin : $0{,}0953 - 0{,}1054 = -0{,}0101$, et $e^{-0{,}0101} - 1 = -1\,\%$, le rendement arithmétique de la période. En Python, `np.log(prices / prices.shift(1)).dropna()`. [ajout]

## Cesse d'être valide quand
Il cesse de s'agréger entre actifs : le rendement logarithmique d'un portefeuille n'est pas la moyenne pondérée de ceux de ses composantes. C'est le piège d'agrégation. [§1.2.2, éq. 1.8]
