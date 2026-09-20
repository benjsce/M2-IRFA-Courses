---
id: fpp/portage
nom: Portage
symbole: $\Phi$
type: notion
statut: source
construite_a_partir_de: []
alias:
- cost of carry
- carry
refs:
- §3.2
- §5.2.1
---

## Ce que c'est
La fraction de sous-jacent qu’il faut détenir aujourd’hui pour en avoir exactement une unité à l’échéance. [§3.2, §5.2.1]

## Ce qui la définit
Un actif qui verse quelque chose pendant qu’on le détient allège son propre portage. [§3.2, §5.2.1]

Le « dividende » d’une devise est son taux d’intérêt. [§2.4]

Pour une matière première ce serait le convenience yield : la source ne le traite pas. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| ce que verse le sous-jacent | rien | $\Phi=1$ |
| ce que verse le sous-jacent | dividendes proportionnels aux dates $T_i$ | $\Phi=1-\sum_i d_i$ |
| ce que verse le sous-jacent | rendement continu $q$ | $\Phi=e^{-q\tau}$ |
| ce que verse le sous-jacent | taux d’intérêt (devise) | $\Phi=P(t,T)$ |
[§3.2, §5.2.1, §2.4]

## Cesse d'être valide quand
Le portage cesse d’être un scalaire si les dividendes sont en montant fixe : $F=\frac{S_t-\sum_i D_iP(t,T_i)}{P(t,T)}$, et les dates de détachement réapparaissent. [ajout]

## Origine
- exercice fpp/ex-01 (c)(d) : « 8 % de la valeur de l'action » ne fixe pas la convention cum/ex ; $\Phi=1-d$ (cours) donne 59,97, $\Phi=1/(1+d)$ (corrigé) donne 59,59 [ajout]
- exercice fpp/ex-02 (c) : deuxième instance de l'ambiguïté cum/ex — $\Phi=1-d$ (cours, §3.2) donne 79,73, $\Phi=1/(1+d)$ (corrigé) donne 79,86. Ce n'est donc pas une coquille isolée mais la convention constante du livre d'exercices [exo. 1]
- exercice fpp/ex-05 : un dividende versé juste avant l'échéance ne s'actualise pas ; sa date n'entre pas dans le calcul, au contraire d'un montant versé en cours de vie [exo. 5]
- exercice fpp/ex-07 : un future ne coûte rien à porter, ce qui s'écrit $\Phi=e^{-r\tau}$ ; c'est le sens du « dividende = taux » du corrigé [exo. 7]
- exercice fpp/ex-08 : avec un dividende en montant, le retirer du comptant **avant** d'entrer dans la formule, jamais après [ajout]
- exercice fpp/ex-13 : une devise étrangère est un sous-jacent à rendement continu, $\Phi=e^{-r_f\tau}$ — le seul cas de la table où $\Phi$ est un taux et non un flux [exo. 13]
