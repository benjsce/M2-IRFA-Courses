---
id: pfo/coefficient-d-asymetrie
nom: Coefficient d'asymétrie
symbole: '$S$'
type: notion
statut: source
cas_de: pfo/moment-standardise
valeur: '3'
construite_a_partir_de:
- fpp/volatilite
alias:
- skewness
- asymétrie
- Fisher's skewness coefficient
- coefficient d'asymétrie de Fisher
refs:
- §2.1.2
- éq. 2.1
- p. 21
- éq. 2.3
---

## Ce que c'est
Le moment centré réduit d'ordre 3 des rendements, qui mesure le sens et la force de l'asymétrie de leur loi. [§2.1.2, éq. 2.1]

## Forme
$$S = E\!\left[\left(\dfrac{r-\mu}{\sigma}\right)^{3}\right]$$ [éq. 2.1]

## Ce que les symboles modélisent
$S$ est un nombre sans unité : nul pour une loi symétrique, positif quand la queue droite domine, négatif quand c'est la queue gauche. Il ne mesure pas la dispersion, que porte l'écart type, mais la façon dont elle se répartit de part et d'autre de la moyenne. [éq. 2.1, p. 21]

Ce $S$ n'est pas la fourchette $S_t$ du chapitre 1, ni l'espace des états du cours dup. [ajout]

## Ce qui la définit
Le cube garde le signe de l'écart à la moyenne : une observation au-dessus contribue positivement, une observation en dessous négativement, et le cube amplifie les observations lointaines. Quelques rendements très négatifs suffisent donc à rendre le coefficient nettement négatif. [p. 21]

En Python, `stats.skew(array)` en calcule la version empirique ; une valeur négative signale une queue gauche étirée, donc davantage de pertes extrêmes latentes. [§2.2.1]

## Le chemin jusqu'ici
fpp/volatilite fournit l'écart type par lequel on réduit l'écart à la moyenne. Sans cette réduction, le moment d'ordre 3 aurait l'unité d'un rendement au cube et changerait avec l'échelle ; réduit, il ne décrit plus que la forme. [ajout]

## Exemple minimal
La série de rendements {−2 %, −1 %, 0 %, 1 %, 2 %, −10 %} du cours a un coefficient d'asymétrie de −1,37 ; sans la perte de −10 %, elle est symétrique et son coefficient est nul. [ajout]

![La contribution de chaque observation de l'exemple, le cube de son écart réduit. Cinq observations restent près de zéro ; celle de $-10\,\%$ vaut $-9{,}4$ à elle seule, et la moyenne des six, $-1{,}37$, est le coefficient.](figures/coefficient-d-asymetrie.svg) [ajout]

## Geste de calcul type
`stats.skew([-0.02, -0.01, 0, 0.01, 0.02, -0.10])` rend −1,37 : une seule observation lointaine, élevée au cube, emporte le signe de toute la série. [ajout]

## Cesse d'être valide quand
Le coefficient empirique de scipy est la version biaisée, sans correction de petit échantillon, et il est dominé par les quelques observations extrêmes : il faut de longues séries pour qu'il soit stable. [ajout]
