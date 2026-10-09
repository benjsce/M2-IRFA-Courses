---
id: pfo/modele-factoriel-statistique
nom: Modèle factoriel statistique
symbole: '$\beta_{ik}$, $\varepsilon_{i,t}$'
type: notion
statut: source
cas_de: pfo/modele-factoriel
construite_a_partir_de:
- pfo/facteur-statistique
- dss/moindres-carres-ordinaires
alias:
- statistical factor model
- régression sur les facteurs de l'ACP
- PCA factor model
refs:
- p. 62
- p. 88
---

## Ce que c'est
La régression du rendement d'un actif sur les premiers facteurs statistiques, pour mesurer son exposition à chacun. [p. 62]

## Forme
$$R_{i,t}=\alpha_i+\beta_{i1}\,PC_{1,t}+\beta_{i2}\,PC_{2,t}+\beta_{i3}\,PC_{3,t}+\varepsilon_{i,t}$$ [p. 62]

## Ce que les symboles modélisent
$\beta_{ik}$ est l'exposition de l'actif $i$ au facteur $k$ : de combien son rendement bouge quand $PC_{k,t}$ bouge d'une unité. $\varepsilon_{i,t}$ est ce que les facteurs gardés n'expliquent pas. Ce n'est pas le loading $v_{ik}$, qui dit comment l'actif entre dans le facteur ; $\beta_{ik}$ dit comment le facteur entre dans l'actif. [p. 62, p. 65]

## Ce qui la définit
**Connus** : les séries des facteurs, que l'analyse en composantes principales a construites, et celle de l'actif. **Cherchées** : les expositions. L'analyse a répondu à « quels sont les facteurs communs ? » ; la régression répond à « comment chaque actif y est-il exposé ? ». [p. 62]

Le modèle a la forme du MEDAF et de Fama-French, mais ses facteurs ne viennent d'aucune théorie : ils sont extraits des rendements. [p. 62]

## Le chemin jusqu'ici
Les variables explicatives sont des séries de pfo/facteur-statistique, fabriquées par pfo/analyse-en-composantes-principales à partir de pfo/matrice-de-covariance. Celle-ci est faite, dans l'exemple, de pfo/rendement-logarithmique, avec le carré de fpp/volatilite sur la diagonale et l'annualisation de fpp/echelonnement-de-la-variance. [ajout]

L'estimation est celle de dss/moindres-carres-ordinaires, la même que pour le MEDAF : des couples d'une variable expliquée et de variables explicatives, comme dans dss/apprentissage-supervise, et la somme des carrés des résidus rendue minimale. [ajout]

## Exemple minimal
Régressé sur le seul premier facteur de l'exemple, le second actif a une exposition de 0,96 et un $R^2$ de 98,5 % ; le premier, une exposition de 0,29 et un $R^2$ de 36 %. [ajout]

## Geste de calcul type
Les facteurs étant non corrélés et de variance $\lambda_k$, l'exposition de l'actif $i$ au facteur $k$ vaut $\mathrm{Cov}(R_i,PC_k)/\lambda_k=\lambda_k v_{ik}/\lambda_k=v_{ik}$ : sur la population, l'exposition est le loading. La part expliquée est $v_{i1}^2\lambda_1/\Sigma_{ii}$ : $0{,}957^2\times0{,}1084/0{,}1008=0{,}985$ pour le second actif, $0{,}290^2\times0{,}1084/0{,}0252=0{,}36$ pour le premier. [ajout]

## Cesse d'être valide quand
Si l'actif fait partie du panier qui a servi à construire les facteurs, il est en partie régressé sur lui-même ; avec autant de facteurs que d'actifs, la régression est exacte et ne dit plus rien. [ajout]

Le signe d'une exposition dépend du signe arbitraire du vecteur propre : il ne se lit qu'avec les loadings de la même estimation. [ajout]

## Origine
- exercice pfo/ex-09 : exposition de AAPL aux trois premiers facteurs de huit actions [p. 88]
