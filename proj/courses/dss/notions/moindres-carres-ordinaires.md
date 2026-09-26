---
id: dss/moindres-carres-ordinaires
nom: Moindres carrés ordinaires
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-supervise
alias:
- OLS
- ordinary least squares
refs:
- slide 25
- slide 26
- slide 48
- slide 56
- slide 91
---

## Ce que c'est
Choisir les coefficients d'un modèle linéaire qui rendent la somme des carrés des erreurs, la RSS, la plus petite possible. [slide 48]

## Forme
$$\hat\beta=\arg\min_{\beta}\ \mathrm{RSS}(\beta),\qquad \mathrm{RSS}(\beta)=\sum_{i=1}^{n}\Big(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\Big)^2$$ [slide 48]

## Ce que les symboles modélisent
$y_i$ est la réponse observée de l'observation $i$, ici la perte d'un client en milliers d'euros, et $x_{ij}$ la valeur de son prédicteur $j$ ; $n$ compte les observations, $p$ les prédicteurs. [slide 26, slide 48]

$\beta_j$ est le coefficient du prédicteur $j$ : de combien la prédiction bouge quand ce prédicteur augmente d'une unité, les autres restant fixes ; $\beta_0$ est la constante. $\hat\beta$, avec son chapeau, est le vecteur des coefficients retenus, qu'on distingue des vrais coefficients, inconnus. [ajout]

RSS, la somme des carrés des résidus, est une fonction des $\beta$ : les données sont fixées, et chaque choix de coefficients laisse sa propre somme. C'est un montant d'erreur, pas un taux. [slide 48, ajout]

$X$ est la matrice des données, une ligne par observation, une colonne de 1 pour la constante puis une colonne par prédicteur ; $y$ est le vecteur des réponses. [ajout]

## Retrouver la formule
![Les 20 clients, chacun un point : son endettement et sa perte, connus. On cherche la droite, c'est-à-dire deux coefficients. Chaque trait vertical est l'écart d'un client à la droite des moindres carrés, et la RSS est la somme de leurs carrés. La droite plate, à la perte moyenne, laisse une RSS de 44,0 ; inclinée autour du client moyen, cerclé, jusqu'à la droite des moindres carrés, elle tombe à 34,8, et aucune autre droite ne fait moins.](figures/moindres-carres-ordinaires.svg) [ajout]

Pour tenir dans un plan, ne gardons que l'endettement $x_1$. **Ce qui est connu** : les 20 clients, chacun un point, son endettement et sa perte. **Ce qu'on cherche** : la droite $\hat y=\beta_0+\beta_1x_1$, c'est-à-dire deux nombres. [ajout]

Toute droite laisse, pour chaque client, un écart vertical $e_i=y_i-\hat y_i$ entre sa perte et la perte prédite. On l'élève au carré, pour que les écarts en dessous de la droite ne compensent pas ceux au-dessus, et l'on somme : c'est la RSS. La droite plate, à la perte moyenne de 3,60, laisse 44,0. [ajout]

Inclinée, la droite suit mieux les points et la somme baisse : avec une constante de 1,92 et une pente de 0,046, elle tombe à 34,8, et aucune autre droite ne fait moins. Ce sont les coefficients des moindres carrés. [ajout]

Pourquoi un fond, et où ? Les $\beta$ entrent au premier degré dans chaque écart, donc au second dans la RSS : en chaque coefficient, la RSS est une parabole tournée vers le haut, et son fond est là où sa pente est nulle. [ajout]

La pente nulle en $\beta_0$ dit que les écarts se compensent, $\sum_ie_i=0$ : la droite passe par le client moyen, d'endettement 36,7 et de perte 3,60, là où les deux droites de la figure se croisent. La pente nulle en $\beta_1$ dit que les écarts ne suivent plus l'endettement, $\sum_ix_{i1}e_i=0$. [ajout]

Avec $p$ prédicteurs, il y a une pente nulle par coefficient, donc $p+1$ équations à $p+1$ inconnues. Rangées en matrice, elles s'écrivent $X^T(y-X\beta)=0$ : ce sont les équations normales, qu'on résout quand $X^TX$ est inversible. [ajout]

$$X^TX\,\hat\beta=X^Ty\quad\Longleftrightarrow\quad\hat\beta=(X^TX)^{-1}X^Ty$$ [ajout]

## Ce qui la définit
L'erreur ne se mesure que sur la réponse, verticalement, et elle est élevée au carré : un grand écart pèse beaucoup plus que deux petits, et un client très mal prédit tire la droite vers lui. [ajout]

Les coefficients retenus sont ceux qui ajustent le mieux ces données-là, pas les vrais. Le cours en fait l'ajustement de référence, que la suite cherche à remplacer pour gagner en précision de prédiction et en interprétabilité. [slide 25, ajout]

## Le chemin jusqu'ici
dss/apprentissage-supervise fournit ce que l'ajustement consomme : pour chaque client, des prédicteurs et une réponse connue, les points de la figure. [ajout]

## Exemple minimal
Sur les 20 clients, avec l'endettement $x_1$, en %, et le revenu $x_2$, en milliers d'euros : $\hat y=3{,}30+0{,}076\,x_1-0{,}060\,x_2$, pour une RSS de 22,43. Un point d'endettement de plus ajoute 76 € à la perte prédite. [ajout]

La règle qui a servi à simuler les données, $y=2+0{,}10\,x_1-0{,}05\,x_2$ plus un bruit, laisse sur ces clients une RSS plus grande, 26,61 : les moindres carrés prennent la plus petite sur ces 20 clients-là, et la vraie règle n'y est qu'une candidate parmi d'autres. [ajout]

## Geste de calcul type
Former $X$, 20 lignes et 3 colonnes : la constante, l'endettement, le revenu. Calculer $X^TX$, un tableau 3 × 3, et $X^Ty$, puis résoudre le système plutôt que d'inverser : on retrouve $(3{,}30\,;0{,}076\,;-0{,}060)$, les coefficients de l'exemple. [ajout]

Contrôle immédiat, par la première équation : le plan passe par le client moyen, $3{,}304+0{,}0759\times36{,}72-0{,}0604\times41{,}18\approx3{,}60$, la perte moyenne. [ajout]

## Cesse d'être valide quand
Les moindres carrés ne sont sûrs que si la relation est à peu près linéaire et que les observations sont beaucoup plus nombreuses que les prédicteurs, $n\gg p$ ; sinon l'ajustement devient très variable. Dès que les coefficients, constante comprise, sont aussi nombreux que les observations, par exemple 19 prédicteurs pour les 20 clients, le modèle passe exactement par tous les points, avec une RSS nulle, et ne dit plus rien ; dès $p\ge n$, $X^TX$ n'est plus inversible et les solutions sont une infinité. Le cours dit de ne pas les employer dès que $p$ atteint $n$. [slide 26, slide 56, slide 91, ajout]
