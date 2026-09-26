---
id: fpp/replication-dynamique
nom: Réplication dynamique
type: notion
statut: source
cas_de: fpp/replication
valeur: rééquilibrage à chaque pas
construite_a_partir_de:
- fpp/compte-capitalise
alias:
- delta hedging
- stratégie autofinançante
refs:
- §4.2.2
---

## Ce que c'est
Une stratégie en futures, ajustée à chaque appel de marge, qui coûte aujourd'hui le prix future et vaut à l'échéance le cours de l'action divisé par le compte capitalisé. [§4.2.2]

## Forme
$$\text{de }t_i\text{ à }t_{i+1},\ \text{détenir}\quad n_i=\dfrac{1}{B(t_0,t_{i+1})}\ \text{futures}\qquad\Longrightarrow\qquad H_{t_0}\ \text{aujourd'hui},\quad\dfrac{S_T}{B(t_0,T)}\ \text{à l'échéance}$$ [§4.2.2]

## Ce que les symboles modélisent
$t_0$ est aujourd'hui, $t_1,\dots,t_n=T$ les dates de règlement des appels de marge, en pratique chaque jour. $H_{t_i}$ est le prix future coté en $t_i$ : le niveau sur lequel se calcule l'appel de marge, qui verse $H_{t_{i+1}}-H_{t_i}$ par future détenu ; à l'échéance, il rejoint le cours de l'action, $H_T=S_T$. [§4.2, §4.2.2]

$n_i$ est le nombre de futures détenus entre $t_i$ et $t_{i+1}$ ; le poly n'a pas de lettre pour lui. $B(t_0,t_{i+1})=P(t_0,t_1)\cdots P(t_i,t_{i+1})$ est le compte capitalisé : aléatoire vu d'aujourd'hui, mais **connu en $t_i$**, puisque le dernier facteur, le zéro-coupon de la période qui commence, est coté ce jour-là. C'est ce qui rend $n_i$ calculable au moment où il faut le détenir. [§4.2.2, ajout]

## Retrouver la formule
![Un échéancier à trois dates, un règlement par an, à 4 % puis 6 %. Le prix future passe de 110 à 115, puis rejoint l'action à 122. En t₀ on place 110. À chaque date, la barre pleine est ce placement grossi au taux de la période, connu dès son début ; le cadre pointillé est le trou, bouché par l'appel de marge multiplié par le nombre de futures, 1,0408 puis 1,1052. La richesse finale, 134,83, est 122 divisé par le compte capitalisé 0,9048.](figures/replication-dynamique.svg) [ajout]

On cherche une stratégie qui coûte aujourd'hui le prix future $H_{t_0}$ et dont on sait dire la valeur finale. On la construit pour qu'à chaque date sa richesse soit $H_{t_i}/B(t_0,t_i)$ : c'est $H_{t_0}$ aujourd'hui, et $S_T/B(t_0,T)$ à l'échéance, où $H_T=S_T$. [§4.2.2]

En chiffres : 4 % la première année, 6 % la seconde, et un prix future de 110 aujourd'hui. Les futures ne coûtent rien à prendre : la stratégie coûte les 110 qu'on place à un an. Dans un an, ils sont devenus $110/0{,}9608=114{,}49$, montant **connu aujourd'hui**. [ajout]

Si le prix future est alors 115, on veut $115/0{,}9608=119{,}69$. Il manque $5{,}20$, c'est-à-dire $(115-110)/0{,}9608$ : l'appel de marge, 5, divisé par 0,9608. C'est le trou ; chaque future verse exactement l'appel de marge, il en faut donc $1/0{,}9608=1{,}0408$. [ajout]

Deuxième année, même raisonnement. Les 119,69 placés à 6 % deviennent $127{,}09$ ; pour atteindre $122/0{,}9048=134{,}83$, il faut $1/(0{,}9608\times0{,}9418)=1/0{,}9048=1{,}1052$ futures. Ce nombre dépend du taux de la seconde année, inconnu aujourd'hui, mais connu au début de cette année-là : juste à temps. [ajout]

En lettres. En $t_i$, la richesse $H_{t_i}/B(t_0,t_i)$ placée jusqu'en $t_{i+1}$ devient $H_{t_i}/B(t_0,t_{i+1})$, puisque $B(t_0,t_{i+1})=B(t_0,t_i)\,P(t_i,t_{i+1})$. Il manque $(H_{t_{i+1}}-H_{t_i})/B(t_0,t_{i+1})$ : l'appel de marge, divisé par $B(t_0,t_{i+1})$. [§4.2.2]

$$n_i=\dfrac{1}{B(t_0,t_{i+1})}\quad\Longrightarrow\quad\text{richesse en }t_i=\dfrac{H_{t_i}}{B(t_0,t_i)},\ \text{donc}\ \dfrac{S_T}{B(t_0,T)}\ \text{en }T$$ [§4.2.2]

## Ce qui la définit
Chaque appel de marge est replacé au taux du moment ; pour que la richesse finale ne dépende que de $S_T$, on grossit la position au rythme du compte capitalisé. [§4.2.2]

La ligne générale du poly écrit $1/B(t_0,t_i)$ futures en $t_i$ ; ses deux premiers pas, $1/P(0,1)$ en $t_0$ puis $1/\big(P(0,1)P(1,2)\big)$ en $t_1$, donnent bien $1/B(t_0,t_{i+1})$, et c'est ce que la fiche suit. [§4.2.2]

## Le chemin jusqu'ici
Tout le calcul tient dans fpp/compte-capitalise : ce que devient un euro replacé de période en période, à des taux qu'on n'apprend qu'au fur et à mesure. Il est lui-même un produit de zéro-coupons courts, les prix de fpp/facteur-actualisation, et c'est fpp/convention-capitalisation qui permet de les enchaîner en les multipliant. [ajout]

## Exemple minimal
À 4 % la première année puis 6 % la seconde : 1,0408 futures la première année, 1,1052 la seconde. [ajout]

## Geste de calcul type
Diviser 1 par le produit des zéro-coupons courts, celui de la période qui commence compris : $1/0{,}9608=1{,}0408$, puis $1/(0{,}9608\times0{,}9418)=1{,}1052$. [§4.2.2]

## Cesse d'être valide quand
Suppose qu'à chaque date de règlement on puisse placer ou emprunter au taux de la période qui commence, et ajuster sans frais le nombre de futures. [ajout]
