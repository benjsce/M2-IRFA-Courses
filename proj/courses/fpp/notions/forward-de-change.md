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

## Ce que les symboles modélisent
$P^f(t,T)$ est le zéro-coupon de l'autre devise : le prix, exprimé en monnaie étrangère, d'une unité étrangère payée en $T$. L'exposant ne marque pas une puissance, il marque le pays. [§2.4]

## Ce qui la définit
La devise locale s’apprécie à terme si le taux étranger est supérieur au taux local. [§2.4]

C’est le seul endroit où les deux principes se rejoignent : la composition du facteur temporel et du facteur de change. La parité des taux d’intérêt n’est pas un résultat de plus, c’est le portage avec le bon $\Phi$. [ajout]

## Le chemin jusqu'ici
fpp/taux-de-change fournit l'objet, et fpp/facteur-actualisation — bâti sur fpp/convention-capitalisation — le coût du temps. [ajout]

La seule idée propre à cette fiche est qu'il y a **deux** facteurs d'actualisation, un par devise, et que le forward est leur rapport. La devise étrangère se porte comme un actif qui verse un rendement : son taux joue le rôle du portage. [ajout]

## Exemple minimal
$X_t=1{,}10$ USD par EUR, $P(0,1)=0{,}9608$ (EUR à 4 %), $P^f(0,1)=0{,}9802$ (USD à 2 %) : $K(0,1)=1{,}0782$. [ajout]

## Geste de calcul type
Poser quelle devise est locale, puis appliquer $K=X_tP/P^f$ : avec $X_t=1{,}10$, $P=0{,}9608$ et $P^f=0{,}9802$, on obtient 1,0782. Contrôler le sens par les taux — le taux étranger plus bas fait baisser le forward. [§2.4]

## Cesse d'être valide quand
Valable parce que le sous-jacent *est* la devise de règlement. Dès qu’ils diffèrent, la corrélation entre $S$ et $X$ entre en jeu et la formule ne tient plus. [ajout]

## Origine
- exercice fpp/ex-03 : la formule à exposants exige de décider quelle devise est « locale », ce que l'énoncé ne dit jamais ; refaire la réplication en une ligne [ajout]
- exercice fpp/ex-06 : les deux couvertures, forward et marché monétaire, diffèrent de 1,8 pour cent mille — exactement l'arrondi de la cotation à 1,112 au lieu de 1,112019 [exo. 6]
- exercice fpp/ex-13 : le sens des variations se retrouve sans la formule — la devise qui rapporte le plus se déprécie à terme [exo. 13]
- exercice fpp/ex-19 : le change forward et le taux forward sont la même construction dans deux coordonnées ; la condition de gain a la même forme, $Z(T)<F(0,T)$ contre $r(t,T)<f(t,T)$ [exo. 19]
