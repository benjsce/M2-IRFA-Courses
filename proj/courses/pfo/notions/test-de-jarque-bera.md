---
id: pfo/test-de-jarque-bera
nom: Test de Jarque-Bera
symbole: '$JB$, $T$, $\chi^2(2)$'
type: notion
statut: source
cas_de: pfo/test-de-normalite
valeur: l'asymétrie et l'excès de kurtosis de l'échantillon
construite_a_partir_de:
- pfo/coefficient-d-asymetrie
- pfo/kurtosis
- pfo/p-valeur
alias:
- Jarque-Bera test
- Jarque-Bera
refs:
- §2.3
- p. 26
- Listing 2.1
---

## Ce que c'est
Un test de normalité dont la statistique combine l'écart de l'asymétrie à zéro et l'écart de l'excès de kurtosis à zéro. [§2.3]

## Forme
$$JB = \dfrac{T}{6}\left(S^2 + \dfrac{K_{\mathrm{ex}}^2}{4}\right) \;\overset{a}{\sim}\; \chi^2(2), \qquad p = 1 - F_{\chi^2_2}(JB_{\mathrm{obs}})$$ [§2.3, p. 26]

## Ce que les symboles modélisent
$JB$ est une somme de deux carrés, donc toujours positive, et nulle seulement si l'échantillon a exactement l'asymétrie et la kurtosis d'une loi normale. $T$ est le nombre d'observations : à écarts de moments égaux, la statistique croît avec la taille de l'échantillon. [§2.3]

$\chi^2(2)$ est la loi du khi-deux à deux degrés de liberté, que suit asymptotiquement $JB$ sous l'hypothèse de normalité ; c'est d'elle que vient la p-valeur. [p. 26]

Ce $T$ n'est pas l'échéance du cours fpp, et au chapitre 1 la même lettre compte des sous-périodes. [ajout]

## Ce qui la définit
Pour une loi normale, $S = 0$ et $K_{\mathrm{ex}} = 0$, donc $JB = 0$ ; toute déviation de l'un ou l'autre moment fait grandir la statistique. La p-valeur est la probabilité, sous la loi $\chi^2(2)$, d'observer une statistique au moins aussi grande que celle de l'échantillon. [§2.3, p. 26]

En Python, `stats.jarque_bera(x)` rend la statistique et la p-valeur ; le cours l'applique aux rendements du Bitcoin. [§2.3, Listing 2.1]

## Le chemin jusqu'ici
pfo/coefficient-d-asymetrie et pfo/kurtosis fournissent les deux moments que le test confronte à ceux de la loi normale, 0 et 0 une fois la kurtosis prise en excès. Tous deux sont réduits par l'écart type de fpp/volatilite, ce qui rend la statistique indépendante de l'échelle des rendements. [ajout]

pfo/p-valeur ferme le raisonnement : la statistique n'a de sens que rapportée à sa loi sous l'hypothèse nulle, et c'est la p-valeur qui tranche. [ajout]

## Exemple minimal
Sur 1 000 rendements d'asymétrie −0,5 et d'excès de kurtosis 3, $JB = 416{,}7$, très au-delà du seuil de 5,99 qui correspond au niveau de 5 %. [ajout]

![Pour 1 000 rendements, les couples d'asymétrie et d'excès de kurtosis qui passent le test au niveau de 5 % forment la petite ellipse centrée sur la loi normale, où $JB<5{,}99$. L'exemple, $S=-0{,}5$ et $K_{\mathrm{ex}}=3$, est très loin dehors.](figures/test-de-jarque-bera.svg) [ajout]

## Geste de calcul type
$JB = \dfrac{1000}{6}\left(0{,}25 + \dfrac{9}{4}\right) = 166{,}7 \times 2{,}5 = 416{,}7$. Pour une loi $\chi^2(2)$, la p-valeur vaut exactement $e^{-JB/2}$, ici de l'ordre de $10^{-91}$ : la normalité est rejetée. [ajout]

## Cesse d'être valide quand
La loi $\chi^2(2)$ n'est qu'asymptotique : sur un petit échantillon, la p-valeur est approximative. [p. 26]

Il ne voit que deux moments : une loi non normale qui aurait l'asymétrie et la kurtosis d'une loi normale passerait le test, là où Shapiro-Wilk peut la détecter. [p. 31]

La table 2.1 écrit « $S = 0$, $K = 3$ sous normalité », en kurtosis de Pearson, alors que la formule attend l'excès. [Table 2.1, §2.3]

Brancher la kurtosis de Pearson dans la formule ferait valoir la statistique au moins $3T/8$ pour un échantillon parfaitement normal, et rejeter la normalité à tout coup. [ajout]
