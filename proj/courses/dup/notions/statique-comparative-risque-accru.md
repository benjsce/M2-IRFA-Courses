---
id: dup/statique-comparative-risque-accru
nom: Statique comparative sous risque accru
type: notion
statut: source
construite_a_partir_de:
- dup/accroissement-de-risque
alias:
- comparative statics under increasing risk
refs:
- L1 slide 26
- L1 slide 27
---

## Ce que c'est
Comment le choix optimal se déplace quand le risque augmente au sens de l’ordre partiel. [L1 slide 26]

## Forme
$$\int U_a(x,a)\,dF(x;r)=0,\qquad U_{xxa}(x,a)<0\ \implies\ a^*\ \text{baisse}$$ [L1 slide 26, L1 slide 27]

## Ce qui la définit
Ce n’est pas la concavité de $U$ en $x$ qui décide, mais celle du paiement marginal $U_a$ : si $U_a$ est concave en $x$, un accroissement de risque abaisse la condition du premier ordre, et avec $U_{aa}<0$ il faut baisser $a$ pour la rétablir. [L1 slide 26]

Le signe s’inverse quand $U_{xxa}>0$. [L1 slide 27]

## Exemple minimal
Pour $U(x,a)=\ln(1+ax)$ on a $U_{xxa}<0$ : passer de $x$ uniforme sur $\{40,60\}$ à $x$ uniforme sur $\{20,40,60,80\}$, de même moyenne 50, fait baisser le $a$ optimal. [ajout]

## Geste de calcul type
Calculer $U_{xxa}$ et lire son signe : négatif, un accroissement de risque fait baisser $a^*$ ; positif, il le fait monter. Vérifier au passage que $U_{aa}<0$. [L1 slide 26, L1 slide 27]

## Cesse d'être valide quand
Le résultat vaut sous les conditions de régularité de l’article et suppose $U_{aa}<0$ : sans concavité en $a$, la condition du premier ordre ne caractérise plus l’optimum. [L1 slide 26, L1 slide 27]
