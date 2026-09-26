---
id: pfo/annualisation
nom: Annualisation des statistiques
symbole: '$\mu_d$, $\sigma_d$, $\mu_{\mathrm{annuel}}$, $\sigma_{\mathrm{annuel}}$'
type: notion
statut: source
construite_a_partir_de:
- pfo/rendement-logarithmique
- fpp/echelonnement-de-la-variance
alias:
- annualization
- annualiser
- règle de la racine du temps
refs:
- §3.0.7
- §3.0.8
---

## Ce que c'est
Passer des statistiques journalières des rendements à leurs valeurs annuelles : l'espérance et la variance se multiplient par 252, l'écart type par la racine de 252. [§3.0.7]

## Forme
$$\mu_{\mathrm{annuel}}=252\times\mu_d,\qquad \sigma_{\mathrm{annuel}}^2=252\times\sigma_d^2,\qquad \sigma_{\mathrm{annuel}}=\sigma_d\sqrt{252},\qquad \boldsymbol{\Sigma}_{\mathrm{annuel}}=252\times\boldsymbol{\Sigma}_{\mathrm{journalière}}$$ [§3.0.7]

## Ce que les symboles modélisent
$\mu_d$ est le rendement logarithmique espéré d'une seule séance, et $\sigma_d$ son écart type. $\mu_{\mathrm{annuel}}$ et $\sigma_{\mathrm{annuel}}$ sont les mêmes grandeurs pour une année de bourse ; les indices sont en français dans le poly anglais. [§3.0.7]

## Ce qui la définit
Les données de marché arrivent à fréquence journalière, alors que les performances, les mandats de gestion et les comparaisons d'actifs s'expriment sur un an. Une année de bourse compte environ 252 séances, hors week-ends et jours fériés. [§3.0.7]

Le rendement logarithmique annuel est la somme des rendements journaliers ; sous stationnarité, son espérance vaut donc 252 fois l'espérance journalière, par linéarité. Sous l'hypothèse de rendements indépendants et de même loi, la variance d'une somme est la somme des variances, et l'écart type suit la règle de la racine du temps. [§3.0.7]

En Python, multiplier par 252 la matrice `returns.cov()` annualise d'un coup toutes les variances et toutes les covariances ; le script du cours annualise de même `returns.mean()`. [§3.0.7, §3.0.8]

## Le chemin jusqu'ici
L'espérance s'annualise par simple multiplication parce que pfo/rendement-logarithmique est additif dans le temps : le rendement de l'année est la somme de ceux des séances. [ajout]

La variance demande une hypothèse de plus, celle de fpp/echelonnement-de-la-variance : des accroissements indépendants et de même loi, dont les variances s'additionnent. Appliquée à l'écart type de fpp/volatilite, elle donne la racine du temps. [ajout]

## Exemple minimal
Un rendement espéré journalier de 0,04 % et une volatilité journalière de 1 % deviennent 10,08 % et 15,87 % par an. [ajout]

![Sur $n$ séances, la moyenne de l'exemple croît comme $n$ et l'écart type comme $\sqrt n$ : à 252 séances, 10,08 % et 15,87 %. Multiplier l'écart type par 252 au lieu de sa racine le porterait à 252 %, hors du cadre.](figures/annualisation.svg) [ajout]

## Geste de calcul type
$\mu_{\mathrm{annuel}}=252\times0{,}04\,\%=10{,}08\,\%$ ; $\sigma_{\mathrm{annuel}}=1\,\%\times\sqrt{252}=1\,\%\times15{,}87=15{,}87\,\%$. Multiplier l'écart type par 252 au lieu de sa racine le gonflerait près de seize fois. [ajout]

## Ce qui reste libre
| fréquence des rendements | facteur pour l'espérance et la variance | facteur pour l'écart type |
|---|---|---|
| journalière | 252 | $\sqrt{252}$ |
| hebdomadaire | 52 | $\sqrt{52}$ |
[§3.0.7, Listing 1.4]

## Cesse d'être valide quand
Au §3.0.7, le poly note $R_t$ le rendement logarithmique journalier, alors que le chapitre 1 réserve $R_t$ au rendement arithmétique et $r_t$ au logarithmique. La multiplication de l'espérance par 252 ne vaut exactement que pour le second. [§3.0.7, §1.2.1]

Le facteur 252 suppose 252 lignes par an : sur un actif coté tous les jours, comme une cryptomonnaie, il en faut environ 365. [ajout]

La variance ne s'additionne que sans autocorrélation des rendements journaliers ; le poly relie cette hypothèse à l'efficience faible des marchés. [§3.0.7]
