---
id: pfo/alpha-de-jensen
nom: Alpha de Jensen
symbole: '$\alpha_i$'
type: notion
statut: source
construite_a_partir_de:
- pfo/regression-du-medaf
alias:
- Jensen's alpha
- alpha
- rendement anormal
- abnormal excess return
refs:
- p. 59
- p. 69
- p. 76
---

## Ce que c'est
La constante de la régression du MEDAF : ce qu'un actif a rapporté en moyenne au-delà de ce que son exposition au marché lui vaut. [p. 59, p. 76]

## Forme
$$\hat\alpha_i=\overline{R_{i}-R_{f}}-\hat\beta_i\ \overline{R_{m}-R_{f}}$$ [ajout]

## Ce que les symboles modélisent
$\alpha_i$ est la constante de la régression du MEDAF ; $\hat\alpha_i$, avec son chapeau, est sa valeur estimée sur l'échantillon, qu'on distingue de la vraie, inconnue. Les barres désignent des moyennes sur les dates de l'échantillon : $\overline{R_i-R_f}$ est le rendement moyen de l'actif au-delà du taux sans risque, $\overline{R_m-R_f}$ celui du marché, et $\hat\beta_i$ la pente estimée. L'alpha est un rendement, à la fréquence des données : journalier, mensuel. [p. 59, ajout]

Ce n'est aucun des $\alpha$ des chapitres précédents, ni le lissage EWMA, ni le niveau d'un test, ni le seuil de la VaR, ni la part placée dans le portefeuille tangent. [ajout]

## Ce qui la définit
**Connus** : le rendement moyen de l'actif et celui du marché, au-delà du taux sans risque, et le bêta estimé. **Cherché** : ce que l'actif a gagné de plus, ou de moins, que ce que le marché seul explique. La droite des moindres carrés passe par le point moyen ; sa hauteur en zéro est donc la moyenne de l'actif moins le bêta fois la moyenne du marché. [p. 59, ajout]

![Dans le plan bêta – rendement moyen au-delà du taux sans risque, la droite issue de zéro qui passe par le marché, au bêta 1 et à 0,22 % par mois, donne ce que chaque bêta explique. Le second actif, au bêta estimé 1,56, aurait dû faire 0,35 % ; il a fait 0,94 %. L'écart vertical est α̂ = 0,59 % par mois. Dessous, la Forme : α̂_2 = moyenne de R_2,t − R_f,t, moins β̂_2 fois moyenne de R_m,t − R_f,t.](figures/alpha-de-jensen.svg) [ajout]

Le cours le lit comme une performance anormale : un alpha positif et statistiquement significatif signale un gérant habile ou une anomalie de marché exploitable. Si le MEDAF est juste, l'alpha est nul. [p. 59]

## Le chemin jusqu'ici
L'alpha n'existe qu'à travers pfo/regression-du-medaf, qui ajuste par dss/moindres-carres-ordinaires une droite à des couples de rendements, à la manière de dss/apprentissage-supervise : il en est la constante. La pente, elle, estime pfo/beta, et la droite que dessine la figure, celle d'un alpha nul, est la prédiction de pfo/medaf. [ajout]

Cette prédiction prend pour référence pfo/portefeuille-de-marche, que le MEDAF identifie à pfo/portefeuille-tangent, choisi sur pfo/frontiere-efficiente par pfo/ratio-de-sharpe. Les moyennes et les risques qu'on y compare viennent de pfo/moments-du-portefeuille et de pfo/matrice-de-covariance, où fpp/volatilite fournit la diagonale et fpp/echelonnement-de-la-variance le passage d'une fréquence à l'autre. [ajout]

Les rendements de portefeuille s'y agrègent comme pfo/piege-d-agregation le permet en pfo/rendement-arithmetique et non en pfo/rendement-logarithmique. Et si l'alpha compte, c'est que dup/diversification efface le risque propre d'un actif : dup/moyenne-variance, en réduisant chaque dup/loterie à deux nombres, laisse alors le rendement moyen comme seule chose à comparer à son risque de marché. [ajout]

## Exemple minimal
Sur les 60 mois simulés du second actif, le marché a fait en moyenne 0,22 % par mois au-delà du taux sans risque et l'actif 0,94 % ; avec $\hat\beta_2=1{,}56$, l'alpha vaut 0,59 % par mois, environ 7,1 % par an. [ajout]

## Geste de calcul type
$\hat\alpha_2=0{,}938-1{,}556\times0{,}224=0{,}938-0{,}349=0{,}59\,\%$ par mois. L'annualisation du cours est linéaire : $0{,}59\times12\approx7{,}1\,\%$ ; sur des données journalières, le script multiplie par 252. [p. 69, ajout]

## Cesse d'être valide quand
Un alpha non nul dans l'échantillon n'est pas pour autant différent de zéro : ici, le vrai alpha est nul, et le hasard de soixante mois en fait 7 % par an. Il ne se lit qu'avec sa statistique t, et le cours exige qu'il soit statistiquement significatif. [p. 76, p. 59, ajout]

L'alpha est mesuré contre un modèle : celui du MEDAF n'est pas celui de Fama et French. Un actif peut avoir un alpha dans le premier et aucun dans le second, si ses autres expositions expliquent ce que le marché seul n'expliquait pas. [§4.2.2, ajout]

## Origine
- exercice pfo/ex-05 : un vrai alpha de 0,16 % par mois, estimé à 0,157 %, ne se distingue pas de zéro sur 60 mois, avec une p-valeur de 0,52 [p. 73, ajout]
