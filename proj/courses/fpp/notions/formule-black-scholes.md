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

## Ce que les symboles modélisent
$N(\cdot)$ est la répartition de la loi normale centrée réduite : elle prend un nombre et rend une probabilité. $d_1$ et $d_2$ sont ses deux arguments, sans unité, et leur écart vaut la volatilité multipliée par la racine du temps restant. $q$ est un taux de dividende continu, la seule des quatre grandeurs à porter une dimension. [§6.4]

$N(d_2)$ est la probabilité, sous $\mathbb{Q}$, que le call soit exercé ; $N(d_1)$ ne l'est pas : c'est la même probabilité, calculée en pondérant chaque état par la valeur de l'action. Dans la Forme, $P$ est le prix du put ; dans la table plus bas, $P(0,T)$ est le zéro-coupon. [§6.4, ajout]

## Retrouver la formule
![La loi de $S_T$ sous $\mathbb{Q}$ pour l'exemple : action à 100, strike 100, taux 4 %, volatilité 20 %, un an. À gauche du strike, on n'exerce pas et le call ne paie rien. À droite, on exerce : on reçoit l'action et on paie le strike. L'aire ombrée est la probabilité d'exercer, $N(d_2)=0{,}5398$. Ramenés à aujourd'hui, ce qu'on reçoit vaut 61,791 et ce qu'on paie 51,866 : l'écart, 9,925, est le prix du call.](figures/formule-black-scholes.svg) [ajout]

Ce qui est **connu** : le contrat, un strike $K=100$ et une échéance d'un an ; le marché, l'action à $S_0=100$ et le taux $r=4\,\%$ ; et une hypothèse, la volatilité $\sigma=20\,\%$. Ce qu'on **cherche** : le prix du call, $C$. [§6.4, ajout]

Le prix est l'espérance du payoff sous $\mathbb{Q}$, actualisée. [Prop. 6]

Le call ne paie que si $S_T>K$, et dans ce cas il échange : on reçoit l'action, $S_T$, et on paie le strike, $K$. Son prix se coupe donc en deux termes : ce qu'on reçoit si l'on exerce, moins ce qu'on paie si l'on exerce, chacun ramené à aujourd'hui. [ajout]

Ce qu'on paie : $K$, multiplié par la probabilité d'exercer, puis actualisé. Sous $\mathbb{Q}$, $\ln S_T$ est gaussien, de moyenne $\ln S_0+(r-\sigma^2/2)T$ et d'écart type $\sigma\sqrt T$ ; $S_T>K$ revient à ce qu'une gaussienne centrée réduite dépasse $-d_2$, ce qui arrive avec la probabilité $N(d_2)$. Ici $N(0{,}1)=0{,}53983$, et le terme payé vaut $96{,}079\times0{,}53983=51{,}866$. [§5.4, ajout]

Ce qu'on reçoit : l'action, mais seulement dans les états où l'on exerce, qui sont ceux où elle vaut le plus. Pondérer chaque état par $S_T$ décale la gaussienne de $\sigma\sqrt T$ — c'est le calcul de la transformée de Laplace gaussienne, où l'on complète le carré. La probabilité devient $N(d_2+\sigma\sqrt T)=N(d_1)$, et le terme reçu vaut $S_0N(d_1)=100\times0{,}61791=61{,}791$. [Th. 1, ajout]

Le prix est leur différence : $61{,}791-51{,}866=9{,}925$. [ajout]

$$C=\underbrace{S_0N(d_1)}_{\text{reçu si l'on exerce}}-\underbrace{Ke^{-rT}N(d_2)}_{\text{payé si l'on exerce}}$$ [éq. 3]

## Ce qui la définit
Le prix du call se lit en deux termes : ce qu'on reçoit si l'on exerce, l'action, pondérée par $N(d_1)$, moins ce qu'on paie si l'on exerce, le strike actualisé, pondéré par $N(d_2)$, la probabilité risque-neutre d'exercer. Le put se lit de même, dans l'autre sens. [§6.4, ajout]

## Le chemin jusqu'ici
Trois fils se nouent ici, et c'est l'aboutissement du cours. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre : un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**Le contrat.** fpp/payoff puis fpp/option disent ce qu'on évalue. [ajout]

Autrement dit : tout était prêt pour calculer, il ne manquait que de dire *quoi*. L'espérance risque-neutre du payoff d'une option, sous la diffusion log-normale, se mène jusqu'au bout grâce à la transformée de Laplace gaussienne — et c'est pourquoi la formule a une forme fermée alors que la plupart des payoffs n'en ont pas. [ajout]

## Exemple minimal
$S_0=100$, $K=100$, $r=4\%$, $\sigma=20\%$, $T=1$ : le call vaut 9,925 et le put 6,004. [ajout]

## Geste de calcul type
Calculer $d_1$, en déduire $d_2=d_1-\sigma\sqrt T$, lire $N(d_1)$ et $N(d_2)$, puis assembler. Avec l'exemple : $d_1=\big(\ln(100/100)+(0{,}04+0{,}02)\times1\big)/0{,}2=0{,}3$ et $d_2=0{,}1$ ; $N(0{,}3)=0{,}61791$ et $N(0{,}1)=0{,}53983$ ; $C=100\times0{,}61791-96{,}079\times0{,}53983=9{,}925$. [§6.4, ajout]

Le put suit par la parité : $9{,}925-100+96{,}079=6{,}004$. Pour un sous-jacent quelconque, utiliser la formule de Black avec le forward en entrée. [Prop. 7, §6.5]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| entrées | sans dividende | $C=S_0N(d_1)-Ke^{-rT}N(d_2)$ |
| entrées | dividende continu $q$ | $C=S_0e^{-qT}N(d_1)-Ke^{-rT}N(d_2)$, $d_1$ porte $r-q$ |
| entrées | forward et zéro-coupon | $C=P(0,T)\big(FN(d_1)-KN(d_2)\big)$, $d_1$ porte $\ln(F/K)$ |
[éq. 7, éq. 8, éq. 9, éq. 10, éq. 11, éq. 12, éq. 13, éq. 14]

Les trois lignes sont une seule formule : dans celle de Black, $P(0,T)F$ vaut $S_0$ sans dividende et $S_0e^{-qT}$ avec un dividende continu. [§6.5, ajout]

## Cesse d'être valide quand
La formule suppose une volatilité constante, un taux déterministe, un exercice européen et l’absence de friction. La volatilité implicite du marché varie avec le strike — le smile — ce qui contredit directement la première hypothèse. [ajout]

## Origine
- exercice fpp/ex-07 : la limite gênante n'est pas « taux constant » mais l'égalité prix future = prix forward, qui suppose la corrélation taux–sous-jacent nulle [ajout]
- exercice fpp/ex-09 : le taux étranger entre comme un rendement de dividende continu ; une seule formule sert aux actions à dividende, aux futures et au change [exo. 9]
- exercice fpp/ex-17 : le rendement continu $q$ du §5.2 représente aussi le détachement d'un indice — troisième emploi du même paramètre [exo. 17]
