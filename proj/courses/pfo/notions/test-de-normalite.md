---
id: pfo/test-de-normalite
nom: Test de normalité
symbole: '$H_0$, $H_1$'
type: abstraite
statut: source
cas_de: pfo/marches-non-gaussiens
parametre: l'information de l'échantillon que résume la statistique du test
construite_a_partir_de:
- pfo/p-valeur
alias:
- normality test
- test d'adéquation à la loi normale
refs:
- éq. 2.13
- éq. 2.14
- Table 2.1
- p. 31
---

## Ce que c'est
Un test statistique dont l'hypothèse nulle est que les données, ici des rendements, suivent une loi normale. [éq. 2.13, éq. 2.14, Table 2.1]

## Forme
$$H_0 : X \sim \mathcal{N}(\mu, \sigma^2) \qquad\text{contre}\qquad H_1 : X \text{ ne suit pas une loi normale}$$ [éq. 2.13, éq. 2.14, p. 27]

## Ce que les symboles modélisent
$H_0$ est l'hypothèse de normalité, la seule que le test puisse rejeter ; $H_1$ est sa négation, qui ne désigne aucune loi particulière. Le test ne dit donc jamais quelle loi suivent les rendements, seulement si la loi normale reste tenable. [éq. 2.13, éq. 2.14]

## Ce que les membres partagent
Même hypothèse nulle, même décision : une statistique, une p-valeur comparée à 5 %, et le rejet de la normalité si elle est inférieure. [Table 2.1, p. 30]

Ils diffèrent par l'information qu'ils regardent : Jarque-Bera ne voit que l'asymétrie et la kurtosis, Shapiro-Wilk la structure entière de l'échantillon ordonné. [p. 31]

## Pourquoi ce niveau existe
La table 2.1 compare les deux tests terme à terme sur une même grille, et ce niveau est cette grille. Il porte aussi la règle de lecture conjointe : si les deux p-valeurs dépassent 5 %, aucun test ne rejette ; si les deux sont inférieures, l'écart à la normale est établi. [Table 2.1, p. 31]

Si un seul des deux rejette, ce n'est pas une contradiction : les deux tests n'utilisent pas la même information. Le cours cite comme causes possibles d'un tel désaccord une asymétrie marquée, des queues plus épaisses que la normale, des valeurs extrêmes, ou une autre forme d'écart, et conclut que les deux tests sont complémentaires plutôt que concurrents. [p. 31]

## Le chemin jusqu'ici
pfo/p-valeur fournit la règle de décision commune ; ce qui fait un test de normalité, c'est l'hypothèse nulle à laquelle on l'applique. [ajout]

La p-valeur ne dit pas quelle statistique calculer : chaque membre en apporte une, et c'est la loi de cette statistique sous l'hypothèse nulle qui la rend calculable. [ajout]

## Exemple minimal
Un titre peu échangé ne bouge que d'un cran : sur trente jours, cinq baisses de 1 %, vingt jours sans changement, cinq hausses de 1 %. Son asymétrie est nulle et sa kurtosis vaut exactement 3 : Jarque-Bera rend une p-valeur de 1 et ne rejette pas la normalité ; Shapiro-Wilk, qui voit trois paliers là où une loi normale mettrait une pente régulière, rend une p-valeur de l'ordre de 0,00001 et la rejette. [ajout]

## Geste de calcul type
Lancer les deux tests sur la même série et lire les deux p-valeurs ensemble : `stats.jarque_bera(r)` et `stats.shapiro(r)` rendent chacun une statistique et une p-valeur. [Listing 2.1, p. 30]

## Cesse d'être valide quand
Ne pas rejeter la normalité ne la prouve pas. [p. 29]

Sur un petit échantillon, les deux tests ont peu de puissance : un écart réel à la loi normale peut ne pas être rejeté, d'autant que la loi de Jarque-Bera n'est qu'asymptotique. [p. 26, ajout]
