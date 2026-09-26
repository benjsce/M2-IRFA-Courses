---
id: fpp/convention-capitalisation
nom: Convention de capitalisation
type: notion
statut: source
construite_a_partir_de: []
refs:
- §2.1
---

## Ce que c'est
La règle qui dit ce que devient un euro placé à un taux donné, selon le nombre de fois où l'intérêt est versé : linéaire, périodique, actuarielle, continue. [§2.1]

## Forme
$$\left(1+\frac{rt}{n}\right)^{n}\xrightarrow[n\to\infty]{}e^{rt}$$ [§2.1]

## Ce que les symboles modélisent
$r$ est le taux affiché, par an ; $t$ est la durée du placement, comptée en années, et non une date. $n$ est le nombre de fois où l'intérêt est versé sur cette durée, puis réinvesti : $n=1$ est la convention linéaire, un $n$ fini la convention périodique, et un versement par an, $n=t$, la convention actuarielle. [§2.1, ajout]

L'expression rend ce que devient un euro au bout de la durée $t$ ; ce qu'il faut placer aujourd'hui pour recevoir un euro en est l'inverse. [§2.1]

$r_a$ est le taux actuariel : celui qui, versé et réinvesti une fois par an, donne le même facteur, $(1+r_a)^t$. [§2.1]

## Retrouver la formule
![Ce que devient un euro placé deux ans à 5 % par an, selon le nombre de fois où l'intérêt est versé. Une fois, le facteur linéaire 1,1000 ; une fois par an, l'actuariel 1,1025 ; huit trimestres, 1,1045. Les points montent vers la limite continue 1,1052 sans l'atteindre : le même taux affiché fait autant de montants que de conventions.](figures/convention-capitalisation.svg) [ajout]

Le poly pose la question : à 5 % par an, que devient un euro au bout de deux ans ? **Connus** : le taux, 5 %, et la durée, deux ans. **Cherché** : le montant final. [§2.1]

Si l'intérêt est versé une seule fois, à la fin, il vaut $5\,\%\times2=10\,\%$ : l'euro devient $1+rt=1{,}10$. C'est la convention linéaire. [§2.1]

S'il est versé une fois par an, la première année rapporte 5 %, l'euro devient 1,05 ; la seconde année, ces 1,05 rapportent 5 % à leur tour, et l'euro devient $1{,}05\times1{,}05=1{,}1025$. Les 0,0025 de plus sont l'intérêt de la seconde année sur l'intérêt de la première. [§2.1, ajout]

Couper les deux ans en $n$ périodes, c'est verser $rt/n$ à chaque fin de période, puis le réinvestir : l'euro est multiplié $n$ fois par $1+rt/n$. Plus on coupe, plus l'intérêt produit d'intérêt, et le facteur monte, vers une limite : versé à chaque instant, l'intérêt fait $e^{rt}=1{,}1052$. [§2.1, ajout]

$$\left(1+\frac{rt}{n}\right)^{n}\xrightarrow[n\to\infty]{}e^{rt}$$ [§2.1]

## Ce qui la définit
Un taux seul ne désigne aucun placement : 5 % sur deux ans font 1,10 ou 1,1052 selon la convention, et tant qu'elle n'est pas dite, le chiffre ne se calcule pas. [§2.1]

Inversement, un même placement s'écrit avec un taux différent dans chaque convention : c'est une affaire d'écriture, sans contenu économique. Le poly le dit pour l'actuariel et le continu : ils décrivent le même placement quand le taux actuariel vaut $r_a=e^{r}-1$, soit 5,13 % actuariel pour 5 % continu. [§2.1]

## Exemple minimal
Un euro placé deux ans à 5 % par an devient 1,10 en linéaire, 1,1025 en actuariel, 1,1045 avec des intérêts trimestriels et 1,1052 en continu. [ajout]

## Geste de calcul type
Fixer la convention, puis écrire son facteur : pour des intérêts trimestriels sur deux ans, $n=8$ et $(1+0{,}10/8)^8=1{,}1045$ ; en continu, $e^{0{,}10}=1{,}1052$. Le prix aujourd'hui d'un euro payé dans deux ans est l'inverse du facteur : $1/1{,}1052=0{,}9048$ en continu. [§2.1]

## Cesse d'être valide quand
Une convention périodique ne sait pas actualiser sur moins d'une période : des intérêts mensuels ne disent rien d'un placement d'une semaine. Le continu n'a pas cette limite, et c'est pour cela que le cours l'emploie. [§2.1]

## Origine
- exercice fpp/ex-11 : sur un an à 5 %, l'escompte $1-r$, une convention que le poly ne liste pas, le linéaire $1/(1+r)$ et le continu $e^{-r}$ séparent les réponses de plus de 10 % (26,25 · 23,81 · 24,99). La convention y décide de la réponse [exo. 11]
