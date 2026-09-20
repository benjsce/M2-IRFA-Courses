---
id: fpp/forward-de-change
nom: Forward de change
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: $\Phi=P(t,T)$, $D=P^f(t,T)$
construite_a_partir_de:
- fpp/taux-de-change
- fpp/facteur-actualisation
alias:
- forward FX
- parité des taux d’intérêt
refs:
- §2.4
---

## Ce que c'est
Le taux de change convenu aujourd’hui pour un échange de devises futur. [§2.4]

## Forme
$$K(t,T)=X_t\dfrac{P(t,T)}{P^f(t,T)}=X_te^{(R^f-R)\tau}$$ [§2.4]

## Ce qui la définit
Le seul endroit où les deux principes se rejoignent : c’est la composition du facteur temporel et du facteur de change. La parité des taux d’intérêt n’est pas un résultat de plus, c’est le portage avec le bon $\Phi$. [§2.4]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Valable parce que le sous-jacent *est* la devise de règlement. Dès qu’ils diffèrent, la corrélation entre $S$ et $X$ entre en jeu et la formule ne tient plus. [ajout]

## Origine
- exercice fpp/ex-03 : la formule à exposants exige de décider quelle devise est « locale », ce que l'énoncé ne dit jamais ; refaire la réplication en une ligne [ajout]
