---
id: pfo/ratio-de-sharpe
nom: Ratio de Sharpe
symbole: '$R_f$, $SR(W)$'
type: notion
statut: source
construite_a_partir_de:
- pfo/moments-du-portefeuille
alias:
- Sharpe ratio
- SR
- rendement excédentaire par unité de risque
refs:
- §3.0.3
- p. 40
---

## Ce que c'est
Le rendement d'un portefeuille au-delà de celui de l'actif sans risque, divisé par sa volatilité : ce que rapporte chaque unité de risque prise. [§3.0.3]

## Forme
$$SR(W)=\frac{W^T\mu-R_f}{\sqrt{W^T\boldsymbol{\Sigma}W}}$$ [§3.0.3]

## Ce que les symboles modélisent
$R_f$ est le rendement certain de l'actif sans risque, celui qu'on obtient sans rien risquer ; c'est le point de comparaison de tout le reste. $SR(W)$ est un nombre sans unité, puisqu'il divise un rendement par un écart type de rendement : il ne dit pas combien un portefeuille rapporte, mais combien il rapporte par unité de volatilité. [§3.0.3]

## Ce qui la définit
Dès qu'un actif sans risque existe, le ratio permet de comparer des portefeuilles risqués en tenant compte à la fois de leur rendement et de leur risque. [§3.0.3]

Il a une lecture géométrique : l'actif sans risque, de volatilité nulle, est le point $(0,R_f)$ du plan risque-rendement, et la pente de la droite qui le relie à un portefeuille $(\sigma_P,\mu_P)$ vaut $(\mu_P-R_f)/\sigma_P$. Le ratio de Sharpe d'un portefeuille est la pente de cette droite. [p. 40]

![La lecture géométrique sur l'exemple : chaque ratio est la pente de la droite qui relie l'actif sans risque, au point (0 ; 2 %), au portefeuille. Les deux actifs sont sur la même droite, de pente 0,40 ; leur mélange à parts égales est sur une droite plus raide, de pente 0,54.](figures/ratio-de-sharpe.svg) [ajout]

## Le chemin jusqu'ici
Le numérateur et le dénominateur sont les deux nombres de pfo/moments-du-portefeuille : le rendement espéré, dont l'écart à $R_f$ mesure ce qu'on gagne à prendre du risque, et la volatilité, qui mesure ce risque. [ajout]

Ces deux nombres viennent d'une chaîne déjà faite. pfo/rendement-arithmetique s'agrège entre actifs, comme le rappelle pfo/piege-d-agregation, qui met en garde contre pfo/rendement-logarithmique ; pfo/matrice-de-covariance, annualisée par fpp/echelonnement-de-la-variance, porte le carré de fpp/volatilite sur sa diagonale. dup/moyenne-variance résumait déjà chaque dup/loterie par ces deux nombres, et dup/diversification montrait qu'un mélange peut réduire le second sans ruiner le premier. [ajout]

## Exemple minimal
Avec un taux sans risque de 2 %, deux actifs de rendements 6 % et 10 % et de volatilités 10 % et 20 % ont chacun un ratio de 0,40 ; leur mélange à parts égales, s'ils ne sont pas corrélés, atteint 0,54. [ajout]

## Geste de calcul type
Pour le mélange à parts égales : $W^T\mu-R_f=8\,\%-2\,\%=6\,\%$ et $\sigma_p=11{,}18\,\%$, donc $SR=0{,}06/0{,}1118=0{,}54$. Pour chaque actif seul : $(6-2)/10=0{,}40$ et $(10-2)/20=0{,}40$. [ajout]

## Cesse d'être valide quand
Le script du cours pose $R_f=0$ : le ratio y devient le simple rapport du rendement à la volatilité. [§3.0.8]

Comme la variance, le ratio ne voit que deux moments : deux portefeuilles de même ratio peuvent avoir des queues de pertes très différentes, ce que le chapitre 2 mesure par la VaR et la CVaR. [ajout]
