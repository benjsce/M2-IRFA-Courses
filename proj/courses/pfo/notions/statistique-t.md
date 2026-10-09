---
id: pfo/statistique-t
nom: Statistique t
symbole: '$t$, $\hat\theta$, $SE(\hat\theta)$'
type: notion
statut: source
construite_a_partir_de:
- pfo/regression-du-medaf
- pfo/p-valeur
alias:
- t-statistic
- t-stat
- t de Student
- significativité d'un coefficient
refs:
- p. 63
---

## Ce que c'est
Le coefficient estimé divisé par son erreur type : le nombre d'erreurs types qui le séparent de zéro. [p. 63]

## Forme
$$t=\frac{\hat\theta}{SE(\hat\theta)}$$ [p. 63]

## Ce que les symboles modélisent
$\hat\theta$ est un coefficient estimé, par exemple $\hat\alpha_i$ ou $\hat\beta_i$ ; $SE(\hat\theta)$ est son erreur type, l'écart type qu'aurait cette estimation si l'on refaisait l'expérience sur d'autres échantillons : l'incertitude de l'estimation, dans l'unité du coefficient. $t$ est sans unité. Ce n'est pas la date $t$ des rendements, que le cours note de la même lettre. [p. 63, ajout]

## Ce qui la définit
**Connus** : le coefficient estimé et son erreur type, que la régression fournit. **Cherché** : si le coefficient est loin de zéro au regard de l'incertitude avec laquelle on l'estime. Le cours en donne un exemple : $\hat\beta=1{,}20$ et $SE(\hat\beta)=0{,}10$ donnent $t=12$. [p. 63]

![Chaque coefficient estimé de la régression du second actif, posé sur une règle graduée dans sa propre erreur type. α̂ = 0,59 % tient en moins d'une graduation de 0,61 %, t = 0,97 : on ne le distingue pas de zéro. β̂ = 1,56 est à plus de sept graduations de 0,21, t = 7,45. La bande grise marque |t| < 2. Dessous, la Forme : t = θ̂ / SE(θ̂).](figures/statistique-t.svg) [ajout]

Une grande valeur absolue de $t$ dit que le coefficient est loin de zéro par rapport à son incertitude. La p-valeur associée sert à tester l'hypothèse $H_0:\beta=0$, ou $H_0:\alpha=0$ ; `statsmodels` affiche les deux dans `model.summary()`. [p. 63]

## Le chemin jusqu'ici
La statistique t juge un coefficient de pfo/regression-du-medaf, l'ajustement par dss/moindres-carres-ordinaires d'une variable expliquée sur une variable explicative, comme dans dss/apprentissage-supervise. Ce test la ramène à pfo/p-valeur : sous l'hypothèse d'un coefficient nul, quelle chance d'en trouver un aussi loin de zéro ? [ajout]

Les coefficients jugés sont ceux de pfo/medaf. La pente estime pfo/beta, l'exposition à pfo/portefeuille-de-marche, que le modèle identifie à pfo/portefeuille-tangent, le point de pfo/frontiere-efficiente où pfo/ratio-de-sharpe culmine. Tout se calcule avec pfo/moments-du-portefeuille et pfo/matrice-de-covariance, dont fpp/volatilite fait la diagonale et que fpp/echelonnement-de-la-variance porte d'une fréquence à l'autre. [ajout]

Les rendements du marché sont des moyennes pondérées, ce que pfo/piege-d-agregation autorise en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique. dup/moyenne-variance, qui réduit chaque dup/loterie à deux nombres, et dup/diversification, qui efface le risque propre, sont le décor où une constante non nulle aurait un sens économique. [ajout]

## Exemple minimal
Sur les 60 mois simulés du second actif, $\hat\beta_2=1{,}556$ d'erreur type 0,209 donne $t=7{,}45$, et $\hat\alpha_2=0{,}59\,\%$ d'erreur type 0,61 % donne $t=0{,}97$. [ajout]

## Geste de calcul type
Lire `model.tvalues` ou diviser `model.params` par `model.bse`. Avec 58 degrés de liberté, le seuil d'un test bilatéral à 5 % est d'environ 2,00 : la pente est significative, la constante ne l'est pas, et `model.pvalues` le confirme. [p. 63, ajout]

## Cesse d'être valide quand
L'erreur type et la p-valeur que calcule `sm.OLS` supposent des résidus indépendants et de même variance ; des rendements financiers, dont la volatilité se regroupe, s'en écartent. [ajout]

Un $t$ faible ne prouve pas que le coefficient est nul : il dit que l'échantillon ne permet pas de le distinguer de zéro. Dans l'exemple, le vrai alpha est nul ; dans l'exercice 1, il vaut 0,16 % par mois, et le test ne le voit pas davantage. [p. 76, ajout]

## Origine
- exercice pfo/ex-05 : la p-valeur de l'alpha, 0,52, ne permet pas de rejeter un alpha nul ; celle du bêta est infime [p. 73, ajout]
