---
id: pfo/test-de-shapiro-wilk
nom: Test de Shapiro-Wilk
symbole: '$W$, $X_{(i)}$, $a_i$, $m_i$, $V$'
type: notion
statut: source
cas_de: pfo/test-de-normalite
valeur: l'échantillon ordonné entier, comparé aux positions attendues sous la loi normale
construite_a_partir_de:
- pfo/p-valeur
alias:
- Shapiro-Wilk test
- Shapiro–Wilk
- statistique d'ordre
- order statistics
refs:
- §2.4
- p. 27
- p. 28
- p. 29
---

## Ce que c'est
Un test de normalité qui compare l'échantillon rangé par ordre croissant aux positions qu'occuperaient en moyenne les observations d'une loi normale. [§2.4, p. 27]

## Forme
$$W = \dfrac{\left(\sum_{i=1}^{n} a_i X_{(i)}\right)^2}{\sum_{i=1}^{n} \left(X_i - \bar X\right)^2}, \qquad a = \dfrac{m^{\top} V^{-1}}{\sqrt{m^{\top} V^{-1} V^{-1} m}}$$ [p. 27, p. 29]

## Ce que les symboles modélisent
$X_{(i)}$ est la $i$-ème plus petite observation : les $X_{(i)}$ sont les statistiques d'ordre, l'échantillon trié. $m_i$ est la position moyenne qu'aurait la $i$-ème plus petite de $n$ observations normales centrées réduites, et $V$ la matrice de covariance de ces statistiques d'ordre, qui ne sont pas indépendantes. [p. 27, p. 28]

$a_i$ est le poids donné à la $i$-ème observation ordonnée, construit à partir de $m$ et de $V$ pour que la comparaison avec la loi normale soit la plus efficace possible ; personne ne le calcule à la main. [p. 28, p. 29]

$W$ se lit comme le rapport entre la structure compatible avec la normalité et la variabilité totale. Il est en général compris entre 0 et 1, et proche de 1 quand l'échantillon ressemble à un échantillon normal. [p. 27, p. 29]

## Ce qui la définit
La décision se prend sur la p-valeur, probabilité sous l'hypothèse nulle d'obtenir une valeur de $W$ au moins aussi petite que celle observée. Le sens de l'inégalité compte : ce sont les petites valeurs de $W$ qui écartent de la normalité. [p. 28]

La loi de $W$ sous l'hypothèse nulle dépend de la taille de l'échantillon et n'a pas de forme analytique simple : la p-valeur s'obtient par approximation numérique, et `scipy.stats.shapiro(x)` rend $W$ et la p-valeur. [p. 28, p. 29]

## Le chemin jusqu'ici
Le test tient tout entier dans pfo/p-valeur une fois sa statistique définie. Ce qu'il y apporte est une statistique dont la loi n'est connue que numériquement, si bien que la p-valeur vient du logiciel et non d'une table. [ajout]

## Exemple minimal
L'échantillon {3 %, −1 %, 2 %, 5 %, −2 %} a pour statistiques d'ordre $X_{(1)} = -2\,\%$, $X_{(2)} = -1\,\%$, $X_{(3)} = 2\,\%$, $X_{(4)} = 3\,\%$ et $X_{(5)} = 5\,\%$. [p. 27]

## Geste de calcul type
`W, p_value = shapiro(returns)` sur les dix rendements du listing du cours rend $W = 0{,}948$ et une p-valeur de 0,65 : on ne rejette pas la normalité au niveau de 5 %. [ajout]

## Cesse d'être valide quand
Il rejette pour toute forme d'écart à la normale sans dire laquelle, et sur de longues séries financières il rejette presque toujours. [ajout]

Au-delà de 5 000 observations, scipy avertit que la statistique reste exacte mais que la p-valeur peut ne plus l'être. [ajout]
