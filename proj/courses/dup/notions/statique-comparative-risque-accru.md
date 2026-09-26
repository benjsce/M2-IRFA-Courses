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

## Ce que les symboles modélisent
$a$ est la variable de décision de l'agent et $x$ le résultat aléatoire ; $U(x,a)$ rend l'utilité du résultat $x$ quand on a choisi $a$. $F(x;r)$ est la loi de $x$, et $r$ un indice de risque : plus il est élevé, plus la loi est risquée. $a^*$ est le choix optimal. [L1 slide 26, ajout]

Les indices notent des dérivées partielles : $U_a$ est le paiement marginal du choix, et $U_{xxa}$ la dérivée seconde en $x$ de ce paiement marginal, dont le signe dit s'il est concave ou convexe en $x$. [L1 slide 26, ajout]

## Ce qui la définit
Ce n’est pas la concavité de $U$ en $x$ qui décide, mais celle du paiement marginal $U_a$ : si $U_a$ est concave en $x$, un accroissement de risque abaisse la condition du premier ordre, et avec $U_{aa}<0$ il faut baisser $a$ pour la rétablir. [L1 slide 26]

Le signe s’inverse quand $U_{xxa}>0$. [L1 slide 27]

## Le chemin jusqu'ici
Le socle tient tout entier dans dup/accroissement-de-risque, la famille des façons de dire qu'une loterie est plus risquée qu'une autre. [ajout]

Une fois cet ordre partiel disponible, la question devient celle d'un déplacement : où va l'optimum quand le risque augmente ? Il fallait donc l'ordre avant le déplacement, et c'est le seul prérequis. [ajout]

## Exemple minimal
Une part $a$ de la richesse est placée dans un actif dont le rendement, en excès du placement sûr, est $x$ ; avec $U(x,a)=\ln(1+ax)$, on a $U_a=x/(1+ax)$ et $U_{xxa}=-2a/(1+ax)^3<0$. Si $x$ vaut $-40\,\%$ ou $+60\,\%$ à chances égales, la condition du premier ordre $\tfrac12\frac{-0{,}4}{1-0{,}4a}+\tfrac12\frac{0{,}6}{1+0{,}6a}=0$ donne $a^*=5/12\approx0{,}42$. Si chaque résultat s'étale de 50 points de part et d'autre, $x$ vaut $-90\,\%$, $+10\,\%$, $+10\,\%$ ou $+110\,\%$ avec probabilité $1/4$ chacun, même moyenne de 10 % : $a^*$ tombe à 0,20. C'est le même geste que l'étalement de $\{40,60\}$ vers $\{20,40,60,80\}$, mais sur un rendement qui peut être négatif : si $x$ était toujours positif, placer davantage rapporterait toujours plus, et il n'y aurait pas d'optimum. [ajout]

## Geste de calcul type
Calculer $U_{xxa}$ et lire son signe : négatif, un accroissement de risque fait baisser $a^*$ ; positif, il le fait monter. Vérifier au passage que $U_{aa}<0$. [L1 slide 26, L1 slide 27]

## Cesse d'être valide quand
Le résultat vaut sous les conditions de régularité de l’article et suppose $U_{aa}<0$ : sans concavité en $a$, la condition du premier ordre ne caractérise plus l’optimum. [L1 slide 26, L1 slide 27]
