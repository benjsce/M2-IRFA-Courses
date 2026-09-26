---
id: pfo/kurtosis
nom: Kurtosis
symbole: '$K$, $K_{\mathrm{ex}}$, $K_F$'
type: notion
statut: source
cas_de: pfo/moment-standardise
valeur: '4'
construite_a_partir_de:
- fpp/volatilite
alias:
- coefficient d'aplatissement
- excès de kurtosis
- excess kurtosis
- kurtosis de Pearson
- kurtosis de Fisher
- convention de Fisher
refs:
- §2.1.2
- éq. 2.2
- éq. 2.4
- éq. 2.5
- éq. 2.6
- éq. 2.7
---

## Ce que c'est
Le moment centré réduit d'ordre 4 des rendements, qui mesure le poids des observations éloignées de la moyenne, c'est-à-dire l'épaisseur des queues. [éq. 2.2, p. 22]

## Forme
$$K = E\!\left[\left(\dfrac{r-\mu}{\sigma}\right)^{4}\right] = \dfrac{E\big[(r-\mu)^4\big]}{\sigma^4}, \qquad K_F = K_{\mathrm{ex}} = K - 3$$ [éq. 2.2, éq. 2.5, éq. 2.6]

## Ce que les symboles modélisent
$K$ est la kurtosis de Pearson : elle vaut 3 pour toute loi normale, quelle que soit sa variance. $K_{\mathrm{ex}}$ et $K_F$ désignent le même nombre, l'excès sur la loi normale : 0 pour une loi normale, positif pour des queues plus épaisses, négatif pour des queues plus minces. [éq. 2.2, éq. 2.6, éq. 2.7, p. 23]

Le cours emploie aussi $K$ seul pour désigner l'excès, dans le test de Jarque-Bera et dans le développement de Cornish-Fisher : dans ces deux formules, $K$ vaut 0 pour une loi normale, et non 3. [§2.3, éq. 2.26]

## Ce qui la définit
La quatrième puissance donne un poids considérable aux observations lointaines : un écart de 4 à la moyenne compte 16 fois plus qu'un écart de 1 au carré, et 256 fois plus à la puissance quatre. [éq. 2.4]

## Le chemin jusqu'ici
fpp/volatilite fournit le $\sigma$ dont la quatrième puissance sert de dénominateur. C'est ce qui rend la kurtosis indépendante de l'échelle : elle compare l'épaisseur des queues de lois de même variance, et non leur dispersion. [ajout]

## Exemple minimal
Une loi normale a $K = 3$ et $K_{\mathrm{ex}} = 0$ ; une loi de Laplace, à queues plus épaisses, a $K = 6$ et $K_{\mathrm{ex}} = 3$. [ajout]

## Geste de calcul type
Fixer la convention avant de brancher le chiffre dans une formule : scipy rend $K_F$ par défaut, que Jarque-Bera et Cornish-Fisher attendent tel quel ; comparer le résultat à 3 n'a de sens qu'avec `fisher=False`. [p. 23, §2.3, éq. 2.26]

## Ce qui reste libre
| convention | valeur pour une loi normale | appel scipy |
|---|---|---|
| Pearson | 3 | `stats.kurtosis(x, fisher=False)` |
| Fisher, ou excès | 0 | `stats.kurtosis(x, fisher=True)` |
[éq. 2.5, éq. 2.6, p. 23]

## Cesse d'être valide quand
Sur un petit échantillon, elle ne reflète pas les queues : la série {−10 %, −1 %, 0 %, 1 %, 12 %}, que le cours donne en exemple de valeurs extrêmes qui font monter la kurtosis, a un excès empirique de −0,52. [p. 23, ajout]
