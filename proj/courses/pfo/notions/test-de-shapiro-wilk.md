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
$$W = \dfrac{\left(\sum_{i=1}^{n} a_i X_{(i)}\right)^2}{\sum_{i=1}^{n} \left(X_i - \bar X\right)^2}$$ [p. 27]

## Ce que les symboles modélisent
$X_1,\dots,X_n$ sont les $n$ observations dans leur ordre d'arrivée, $\bar X$ leur moyenne, et $X_{(i)}$ la $i$-ème plus petite : les $X_{(i)}$ sont l'échantillon trié, ses statistiques d'ordre. [p. 27]

$m_i$ est la position qu'aurait en moyenne la $i$-ème plus petite de $n$ observations normales centrées réduites, et $V$ la matrice de covariance de ces statistiques d'ordre, qui ne sont pas indépendantes. [p. 28]

$a_i$ est le poids donné à $X_{(i)}$ ; le cours le tire de $m$ et de $V$, $a = m^{\top}V^{-1}/\sqrt{m^{\top}V^{-1}V^{-1}m}$, et personne ne le calcule à la main. [p. 28, p. 29]

$W$ est en général compris entre 0 et 1, et proche de 1 quand l'échantillon ressemble à un échantillon normal. [p. 27, p. 29]

## Ce qui la définit
Le test range l'échantillon et place chaque observation face à la position $m_i$ qu'elle aurait sous une loi normale : si l'échantillon est normal, les points s'alignent à peu près sur une droite. [p. 27, p. 28, ajout]

![L'échantillon de l'exemple, rangé, face aux positions qu'occuperaient en moyenne cinq observations rangées d'une loi normale centrée réduite : $\pm1{,}163$, $\pm0{,}495$ et 0. Les points sont presque alignés, et $W=0{,}951$. La droite pointillée est celle des moindres carrés, tracée pour guider l'œil.](figures/test-de-shapiro-wilk.svg) [ajout]

$W$ mesure, à peu près, cet alignement : proche de 1 quand les points sont sur une droite, plus petit quand ils s'en écartent. [ajout]

La décision se prend sur la p-valeur, probabilité sous l'hypothèse nulle d'obtenir une valeur de $W$ au moins aussi petite que celle observée. Le sens de l'inégalité compte : ce sont les petites valeurs de $W$ qui écartent de la normalité. [p. 28]

La loi de $W$ sous l'hypothèse nulle dépend de la taille de l'échantillon et n'a pas de forme analytique simple : la p-valeur s'obtient par approximation numérique. [p. 28, p. 29]

## Le chemin jusqu'ici
Le test tient tout entier dans pfo/p-valeur une fois sa statistique définie. Ce qu'il y apporte est une statistique dont la loi n'est connue que numériquement, si bien que la p-valeur vient du logiciel et non d'une table. [ajout]

## Exemple minimal
L'échantillon {3 %, −1 %, 2 %, 5 %, −2 %} a pour statistiques d'ordre $X_{(1)} = -2\,\%$, $X_{(2)} = -1\,\%$, $X_{(3)} = 2\,\%$, $X_{(4)} = 3\,\%$ et $X_{(5)} = 5\,\%$ [p. 27]. Il donne $W = 0{,}951$ et une p-valeur de 0,74 : on ne rejette pas la normalité. [ajout]

## Geste de calcul type
`W, p_value = scipy.stats.shapiro(x)` rend la statistique et la p-valeur ; sur l'échantillon de l'exemple, 0,951 et 0,74. Sur les dix rendements du listing du cours, il rend 0,948 et 0,65 : on ne rejette pas non plus. [p. 29, p. 30, ajout]

## Cesse d'être valide quand
Il rejette pour toute forme d'écart à la normale sans dire laquelle, et sur de longues séries financières il rejette presque toujours. [ajout]

Au-delà de 5 000 observations, scipy avertit que la statistique reste exacte mais que la p-valeur peut ne plus l'être. [ajout]
