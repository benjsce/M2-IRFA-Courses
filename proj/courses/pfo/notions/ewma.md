---
id: pfo/ewma
nom: Variance EWMA
symbole: '$\sigma_t^2$, $\lambda$, $\alpha$, $\widehat\sigma_t$'
type: notion
statut: source
construite_a_partir_de:
- pfo/rendement-logarithmique
- pfo/regroupement-de-volatilite
- fpp/echelonnement-de-la-variance
alias:
- EWMA
- exponentially weighted moving average
- moyenne mobile à pondération exponentielle
- RiskMetrics
- volatilité EWMA
refs:
- §1.4
- éq. 1.10
- §1.4.1
- Listing 1.2
- p. 16
---

## Ce que c'est
Une estimation récursive de la variance, où chaque date mélange la variance de la veille et le carré du dernier rendement, avec des poids qui décroissent exponentiellement dans le passé. [§1.4, éq. 1.10]

## Forme
$$\sigma_t^2 = \lambda\,\sigma_{t-1}^2 + (1-\lambda)\,r_{t-1}^2 = \alpha\, r_{t-1}^2 + \alpha(1-\alpha)\, r_{t-2}^2 + \alpha(1-\alpha)^2 r_{t-3}^2 + \cdots, \qquad \alpha = 1-\lambda$$ [éq. 1.10, p. 16]

## Ce que les symboles modélisent
$\sigma_t^2$ est la variance du rendement de la date $t$, estimée avec les rendements connus jusqu'à la veille ; $\widehat\sigma_t$, sa racine carrée, est la volatilité EWMA, journalière tant qu'on ne l'a pas annualisée. [éq. 1.10, p. 16]

$\lambda$ est la persistance, la part de l'estimation de la veille que l'on garde. $\alpha = 1-\lambda$ est le lissage, le poids du rendement le plus récent : plus $\alpha$ est grand, plus les observations récentes pèsent, et plus l'estimateur réagit vite. [éq. 1.10, p. 14, p. 16]

Ce $\alpha$ n'a rien à voir avec le niveau d'un test ni avec le seuil de la VaR, que le cours note de la même lettre au chapitre 2. [ajout]

## Ce qui la définit
Hier soir, on **connaît** la variance estimée pour hier, $\sigma_{t-1}^2$, et le rendement d'hier, $r_{t-1}$. On **cherche** la variance d'aujourd'hui, $\sigma_t^2$ : on garde 94 % de l'ancienne estimation et l'on ajoute 6 % du dernier rendement au carré. [éq. 1.10, ajout]

Le cours l'introduit pour capturer le regroupement de volatilité ; c'est le modèle de RiskMetrics, avec $\lambda = 0{,}94$ pour des données journalières. [§1.4]

En Python, `.pow(2).ewm(alpha=alpha_param, adjust=False).mean()` applique la même récurrence, avec `adjust=False` pour la formule récursive stricte, sans renormaliser les premiers poids ; la volatilité annualisée est ensuite `np.sqrt(ewma_variance * 252)`. [§1.4.1, Listing 1.2]

À un détail près : la ligne $t$ de pandas inclut déjà $r_t^2$, le rendement du jour même. C'est donc la variance prévue pour le lendemain, le $\sigma_{t+1}^2$ de la Forme : un décalage d'un jour que le poly ne signale pas. [p. 16, ajout]

![Le poids de chaque rendement passé dans la variance du jour, $\alpha(1-\alpha)^{k-1}$ avec $\lambda=0{,}94$. Le rendement de la veille pèse 6 %, le poids diminue de moitié environ tous les onze jours, et les vingt derniers jours portent ensemble 71 % du total.](figures/ewma.svg) [ajout]

## Le chemin jusqu'ici
pfo/regroupement-de-volatilite pose le problème : la volatilité change dans le temps, alors que fpp/volatilite la traite comme un nombre fixe. L'EWMA y répond en réestimant la variance chaque jour à partir des carrés de pfo/rendement-logarithmique, qui mesurent la dispersion autour de zéro. [ajout]

L'annualisation par $\sqrt{252}$ vient de fpp/echelonnement-de-la-variance : si les rendements journaliers étaient indépendants et de même loi, la variance annuelle vaudrait 252 fois la variance journalière. [ajout]

## Exemple minimal
Avec $\lambda = 0{,}94$, une variance de la veille de 0,0001 — une volatilité journalière de 1 % — et un rendement de la veille de 2 %, la variance du jour vaut 0,000118. [ajout]

## Geste de calcul type
$\sigma_t^2 = 0{,}94 \times 0{,}0001 + 0{,}06 \times 0{,}02^2 = 0{,}000094 + 0{,}000024 = 0{,}000118$, d'où $\widehat\sigma_t = 1{,}09\,\%$ par jour et $\sqrt{252 \times 0{,}000118} = 17{,}2\,\%$ par an. [ajout]

## Ce qui reste libre
| paramètre | valeur du cours |
|---|---|
| persistance $\lambda$ | 0,94 pour des données journalières |
| facteur d'annualisation | 252 |
[§1.4, Listing 1.2]

## Cesse d'être valide quand
L'annualisation par $\sqrt{252}$ suppose la variance constante sur un an, alors que l'estimateur existe précisément parce qu'elle ne l'est pas : le chiffre annualisé est une conversion d'unité, pas une prévision à un an. [ajout]

La persistance est fixée et non estimée : 0,94 est la valeur de RiskMetrics pour des données journalières, et rien ne garantit qu'elle convienne aussi bien au Bitcoin qu'à Apple. [ajout]

Les premières valeurs dépendent du point de départ de la récurrence, le premier rendement au carré avec `adjust=False`, et ne s'interprètent pas. [ajout]
