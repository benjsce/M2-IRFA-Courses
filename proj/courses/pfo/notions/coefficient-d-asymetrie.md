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
Le cube garde le signe de l'écart à la moyenne : une observation au-dessus de la moyenne contribue positivement, une observation en dessous négativement, et le cube amplifie les observations lointaines. Quelques rendements très négatifs suffisent donc à rendre le coefficient nettement négatif. [p. 21]

## Le chemin jusqu'ici
fpp/volatilite fournit l'écart type par lequel on réduit l'écart à la moyenne. Sans cette réduction, le moment d'ordre 3 aurait l'unité d'un rendement au cube et changerait avec l'échelle ; réduit, il ne décrit plus que la forme. [ajout]

## Exemple minimal
La série de rendements {−2 %, −1 %, 0 %, 1 %, 2 %, −10 %} du cours a une moyenne de −1,67 %, un écart type de 3,94 % et un coefficient d'asymétrie de −1,37 ; sans la perte de −10 %, elle est symétrique et son coefficient est nul. [éq. 2.3, ajout]

![La contribution de chaque observation de l'exemple, le cube de son écart réduit. Les écarts se comptent depuis la moyenne de la série, −1,67 % : −2 % est presque dessus, −1 % et au-delà sont au-dessus et contribuent positivement. Celle de −10 % vaut −9,43 à elle seule, et la moyenne des six, −1,37, est le coefficient.](figures/coefficient-d-asymetrie.svg) [ajout]

## Geste de calcul type
La moyenne vaut −1,67 % et l'écart type 3,94 %. L'écart réduit de −10 % est $(-10+1{,}67)/3{,}94=-2{,}11$, et son cube $-9{,}43$ ; les cinq autres cubes vont de 0 à 0,80 et totalisent 1,19. La moyenne des six cubes, $(-9{,}43+1{,}19)/6$, vaut $-1{,}37$. En Python, `stats.skew(array)` fait ce calcul et rend le même $-1{,}37$. [§2.2.1, ajout]

## Cesse d'être valide quand
Le coefficient empirique de scipy est la version biaisée, sans correction de petit échantillon. Sur l'exemple, la seule perte de −10 % en fournit plus que la totalité, $-9{,}43/6=-1{,}57$ sur $-1{,}37$ : une observation de plus ou de moins change le résultat du tout au tout. [ajout]
