---
id: fpp/formule-black-scholes
nom: Formule de Black et Scholes
symbole: '$N(\cdot)$, $d_1$, $d_2$, $q$'
type: notion
statut: source
construite_a_partir_de:
- fpp/modele-black-scholes
- fpp/option
alias:
- B&S formula
- formule de Black
refs:
- §6.4
- §6.5
---

## Ce que c'est
Le prix fermé d’un call et d’un put sous diffusion log-normale et taux constant. [§6.4]

## Forme
$$C=S_0N(d_1)-Ke^{-rT}N(d_2),\qquad P=Ke^{-rT}N(-d_2)-S_0N(-d_1)$$
$$d_1=\dfrac{\ln(S_0/K)+\big(r+\tfrac{\sigma^2}{2}\big)T}{\sigma\sqrt{T}},\qquad d_2=d_1-\sigma\sqrt{T}$$ [éq. 3, éq. 4, éq. 5, éq. 6]

## Ce qui la définit
Une seule formule, trois jeux d’entrées. La version en forward et zéro-coupon — la formule de Black — est la plus générale : les deux autres s’en déduisent en remplaçant $F$ par $S_0$ ou $S_0e^{-qT}$. [§6.4, §6.5]

## Le chemin jusqu'ici
Trois fils se nouent ici, et c'est l'aboutissement du cours. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue. [ajout]

Autrement dit : tout était prêt pour calculer, il ne manquait que de dire *quoi*. L'espérance risque-neutre du payoff d'une option, sous la diffusion log-normale, se mène jusqu'au bout grâce à la transformée de Laplace gaussienne — et c'est pourquoi la formule a une forme fermée alors que la plupart des payoffs n'en ont pas. [ajout]

## Exemple minimal
$S_0=100$, $K=100$, $r=4\%$, $\sigma=20\%$, $T=1$ : le call vaut 9,925 et le put 6,005. [ajout]

## Geste de calcul type
Calculer $d_1$, en déduire $d_2=d_1-\sigma\sqrt T$, lire $N(d_1)$ et $N(d_2)$, puis assembler. Pour un sous-jacent quelconque, utiliser la formule de Black avec le forward en entrée. [§6.4, §6.5]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| entrées | sans dividende | $C=S_0N(d_1)-Ke^{-rT}N(d_2)$ |
| entrées | dividende continu $q$ | $C=S_0e^{-qT}N(d_1)-Ke^{-rT}N(d_2)$, $d_1$ porte $r-q$ |
| entrées | forward et zéro-coupon | $C=P(0,T)\big(FN(d_1)-KN(d_2)\big)$, $d_1$ porte $\ln(F/K)$ |
[éq. 7, éq. 8, éq. 9, éq. 10, éq. 11, éq. 12, éq. 13, éq. 14]

## Cesse d'être valide quand
Volatilité constante, taux déterministe, exercice européen, pas de friction. La volatilité implicite du marché varie avec le strike — le smile — ce qui contredit directement la première hypothèse. [ajout]

## Origine
- exercice fpp/ex-07 : la limite gênante n'est pas « taux constant » mais l'égalité prix future = prix forward, qui suppose la corrélation taux–sous-jacent nulle [ajout]
- exercice fpp/ex-09 : le taux étranger entre comme un rendement de dividende continu ; une seule formule sert aux actions à dividende, aux futures et au change [exo. 9]
- exercice fpp/ex-17 : le rendement continu $q$ du §5.2 représente aussi le détachement d'un indice — troisième emploi du même paramètre [exo. 17]
