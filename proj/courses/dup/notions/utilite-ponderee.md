---
id: dup/utilite-ponderee
nom: Utilité pondérée
type: notion
statut: source
cas_de: dup/famille-chew-dekel
valeur: une probabilité compensatrice $\rho$ indépendante de la loterie commune
construite_a_partir_de:
- dup/utilite-esperee
alias:
- weighted EU
- Chew et MacCrimmon
refs:
- L3 slide 5
- L3 slide 6
---

## Ce que c'est
Chaque résultat porte un poids propre, qui déforme la probabilité avec laquelle il compte. [L3 slide 5]

## Forme
$$V(P)=\dfrac{\sum_i p_i w(x_i)u(x_i)}{\sum_i p_i w(x_i)},\qquad w(x_i)>0$$ [L3 slide 5]

## Ce qui la définit
L’axiome affaibli est l’indépendance faible : si $P\sim Q$, il existe pour chaque $\lambda$ une probabilité compensatrice $\rho$, qui peut différer de $\lambda$ mais doit être **la même pour toute** loterie commune $R$. [L3 slide 5]

La probabilité effective d’un résultat devient $p_i^w=p_iw(x_i)/\sum_j p_jw(x_j)$ : un prix est conservé avec probabilité $w(x_i)$, sinon la loterie est retirée. [L3 slide 6]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite donnent dup/utilite-esperee — les notions que presque tout ce cours suppose acquises. [ajout]

Un poids propre attaché à chaque résultat : c'est la déformation la plus simple qu'on puisse faire subir à la formule de l'utilité espérée, en gardant sa structure de moyenne. D'où la dépendance directe — la fiche modifie une formule, il faut donc l'avoir. [ajout]

## Exemple minimal
Un poids $w$ constant redonne exactement l’utilité espérée ; un poids décroissant ajoute de l’aversion locale. [L3 slide 5, L3 slide 6]

## Geste de calcul type
Pour un petit risque de moyenne nulle, la prime vaut $\tfrac12\big[-u''/u'-2w'/w\big]\mathrm{Var}(\varepsilon)$ : les poids décroissants s’ajoutent à l’aversion, les croissants la réduisent. [L3 slide 6]

## Cesse d'être valide quand
Reste dans la famille d’intermédiarité : les courbes d’indifférence peuvent s’ouvrir ou se fermer en éventail, mais un goût pour la randomisation reste exclu. [L3 slide 6]
