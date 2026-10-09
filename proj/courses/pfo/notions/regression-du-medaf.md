---
id: pfo/regression-du-medaf
nom: Régression du MEDAF
symbole: '$R_{i,t}$, $R_{f,t}$, $R_{m,t}$, $\epsilon_{i,t}$, $Y_t$, $\hat Y_t$, $\epsilon_t$'
type: notion
statut: source
cas_de: pfo/modele-factoriel
construite_a_partir_de:
- pfo/medaf
- dss/moindres-carres-ordinaires
alias:
- CAPM regression
- modèle de marché
- market model
- décomposition de la performance
- performance decomposition
- risque spécifique
- idiosyncratic risk
refs:
- p. 59
- §4.3.1
- p. 62
- p. 63
- §4.3.2
---

## Ce que c'est
L'estimation du MEDAF sur données historiques, en régressant par moindres carrés le rendement d'un actif au-delà du taux sans risque sur celui du marché. [p. 59]

## Forme
$$R_{i,t}-R_{f,t}=\alpha_i+\beta_i\,(R_{m,t}-R_{f,t})+\epsilon_{i,t}$$ [p. 59]

$$\min_{\alpha_i,\beta_i}\ \sum_{t=1}^{T}\epsilon_t^2,\qquad \epsilon_t=Y_t-\hat Y_t$$ [p. 62]

## Ce que les symboles modélisent
$R_{i,t}$, $R_{m,t}$ et $R_{f,t}$ sont les rendements observés à la date $t$ de l'actif, du marché et de l'actif sans risque ; une observation par date, sur $T$ dates. $\beta_i$ est la pente, l'exposition au marché ; $\alpha_i$ la constante, ce que l'actif rapporte en moyenne au-delà de ce que son exposition lui vaut. [p. 59]

$\epsilon_{i,t}$ est le terme d'erreur, le risque propre à l'entreprise, un scandale ou un succès technologique qui ne concerne qu'elle ; le modèle suppose son espérance nulle. Dans l'écriture générale des moindres carrés, $Y_t$ est la variable expliquée, $\hat Y_t$ sa valeur prédite par la droite et $\epsilon_t$ leur écart, le résidu. [p. 59, p. 62]

## Ce qui la définit
**Connus** : une série de rendements de l'actif et du marché, et le taux sans risque. **Cherchés** : la pente $\beta_i$ et la constante $\alpha_i$ de la droite qui passe au plus près des points, au sens des moindres carrés. [p. 59, p. 62]

![Soixante mois simulés dans le monde du chapitre 3 : chaque point est un mois, le marché au-delà du taux sans risque en abscisse, le second actif en ordonnée. La droite des moindres carrés a pour pente β̂ = 1,56 et coupe l'axe vertical en α̂ = 0,59 % ; le trait vertical est le résidu ε d'un mois. Dessous, la Forme : R_2,t − R_f,t = α_2 + β_2 (R_m,t − R_f,t) + ε_2,t.](figures/regression-du-medaf.svg) [ajout]

La régression décompose le risque de l'actif en deux parts : celle qui suit le marché, $\beta_i(R_{m,t}-R_{f,t})$, le risque systématique, que la diversification n'élimine pas ; et $\epsilon_{i,t}$, le risque spécifique, qu'elle élimine. [§4.1, p. 59]

En Python, `sm.OLS(Y, X).fit()` estime les deux coefficients, à condition d'avoir ajouté une colonne de 1 à $X$ par `sm.add_constant(X)` : sans elle, la droite est forcée de passer par l'origine, $\alpha_i$ vaut zéro, et toute la performance résiduelle de l'actif se reporte sur la pente. [p. 62, p. 63]

## Le chemin jusqu'ici
La régression met à l'épreuve pfo/medaf : si le modèle est juste, la constante est nulle et la pente est pfo/beta. Ce bêta mesure l'exposition à pfo/portefeuille-de-marche, référence que le MEDAF tient pour égale à pfo/portefeuille-tangent, le point de pfo/frontiere-efficiente où pfo/ratio-de-sharpe culmine. [ajout]

L'outil d'estimation vient d'un autre cours : dss/moindres-carres-ordinaires choisit les coefficients qui rendent la somme des carrés des résidus minimale, sur des couples d'une variable expliquée et d'une variable explicative, le cadre de dss/apprentissage-supervise. Ici, le couple est le rendement de l'actif et celui du marché, à la même date. [ajout]

Ces rendements entrent dans pfo/matrice-de-covariance et pfo/moments-du-portefeuille, avec le carré de fpp/volatilite sur la diagonale et fpp/echelonnement-de-la-variance pour passer d'une fréquence à l'autre. Le rendement du marché est une moyenne pondérée, exacte en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique, comme le dit pfo/piege-d-agregation. Enfin, dup/moyenne-variance réduit chaque dup/loterie à deux nombres, et dup/diversification explique pourquoi le résidu, propre à l'actif, s'efface dans un mélange. [ajout]

## Exemple minimal
Sur 60 mois simulés pour le second actif, de vrai bêta 1,5 et de vrai alpha nul, la régression donne $\hat\beta_2=1{,}56$ et $\hat\alpha_2=0{,}59\,\%$ par mois. [ajout]

## Geste de calcul type
Former $Y$, le rendement mensuel du second actif moins le taux sans risque mensuel, $2\,\%/12$, et $X$, celui du marché moins le même taux ; ajouter la constante, puis ajuster : `sm.OLS(Y, sm.add_constant(X)).fit()`. On lit $\hat\alpha_2=0{,}59\,\%$ et $\hat\beta_2=1{,}556$ dans `params`. [p. 63, ajout]

Contrôle : sans la constante, la pente monte à 1,571, parce qu'elle absorbe la performance moyenne que la constante portait. [p. 62, ajout]

## Ce qui reste libre
| choix | dans le cours | effet |
|---|---|---|
| taux sans risque | $R_f=0$ dans le script du §4.3.2 | le modèle régresse alors les rendements bruts |
| fréquence | journalière (§4.3.2), mensuelle (exercice 1) | l'alpha s'annualise par 252 ou par 12 |
| marché | le S&P 500, `^GSPC` | un indice tient lieu du portefeuille de marché |
[§4.3.2, p. 67, p. 73]

## Cesse d'être valide quand
Les coefficients sont des estimations, propres à l'échantillon : soixante mois tirés d'un monde où le vrai bêta vaut 1,5 en donnent 1,56, et une constante de 0,59 % par mois alors que la vraie est nulle. Il faut juger chacun par sa statistique t. [p. 63, ajout]

La droite ne vaut que si la relation est à peu près linéaire et stable sur la période ; sur une fenêtre où le bêta de l'actif change, elle en donne une moyenne. [ajout]

## Origine
- exercice pfo/ex-05 : sur 60 mois simulés, de vrai bêta 1,3 et de vrai alpha 0,16 % par mois, la régression retrouve 1,34 et 0,157 % [p. 73]
- exercice pfo/ex-07 : trois régressions sur cinq ans de rendements journaliers [p. 75]
