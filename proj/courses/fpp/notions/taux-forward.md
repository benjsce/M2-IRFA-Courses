---
id: fpp/taux-forward
nom: Taux forward
symbole: $F(t,T,S)$, $f(t,T)$
type: notion
statut: source
construite_a_partir_de:
- fpp/taux-zero-coupon
alias:
- forward rate
- taux instantané
refs:
- §2.3
---

## Ce que c'est
Le taux d'une période future $[T,S]$ que les prix d'aujourd'hui impliquent, et qu'on peut donc s'assurer dès aujourd'hui. [§2.3]

## Forme
$$F(t,T,S)=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce que les symboles modélisent
$F(t,T,S)$ prend trois dates : $t$, aujourd'hui, d'où l'on parle ; $T$ et $S$, le début et la fin de la période future. Il rend un taux annualisé en capitalisation continue, comme le taux zéro-coupon $R(t,T)$. Ici $S$ est une date, pas le prix d'une action. [§2.3, ajout]

$f(t,T)$ est ce même taux quand la période se réduit à un instant, $S$ tendant vers $T$ : un taux instantané. Il ne sert pas à calculer $F$ ; il sert à décrire toute la courbe d'un seul trait, à la fin de « Ce qui la définit ». [§2.3, ajout]

## Retrouver la formule
![Un euro placé en $t$ jusqu'en $S$, par deux chemins. En haut, d'un coup : il devient $1/P(t,S)$. En bas, jusqu'en $T$, où il devient $1/P(t,T)$, puis replacé de $T$ à $S$ au taux $F$ : il devient $e^{F(S-T)}/P(t,T)$. Le taux forward est celui qui fait arriver les deux chemins au même montant.](figures/taux-forward-retrouver.svg) [ajout]

L'idée tient en une phrase : un euro placé de $t$ à $S$ doit rapporter autant, qu'on le place d'un coup ou en deux temps, en s'arrêtant en $T$. Sinon, on emprunterait par le chemin qui rapporte le moins pour placer par celui qui rapporte le plus, et l'on gagnerait sans risque. [ajout]

Sur des chiffres d'abord. Placer deux ans d'un coup à 5 % par an rapporte 10 % ; placer un an à 4 %, puis un an au taux $F$, rapporte $4\,\%+F$, puisqu'en capitalisation continue les taux s'ajoutent d'une période à l'autre. D'où $F=10\,\%-4\,\%=6\,\%$. [ajout]

En lettres maintenant. D'un coup : un zéro-coupon d'échéance $S$ coûte $P(t,S)$ et rend $1$ en $S$ ; avec un euro, on en achète $1/P(t,S)$, qui rendent $1/P(t,S)$. [ajout]

En deux temps : de la même façon, un euro devient $1/P(t,T)$ en $T$ ; placé ensuite pendant $S-T$ au taux continu $F$, ce montant est multiplié par $e^{F(S-T)}$. [ajout]

Les deux montants sont égaux. On prend le logarithme des deux côtés, puis on divise par $S-T$. [ajout]

$$\dfrac{1}{P(t,S)}=\dfrac{e^{F(S-T)}}{P(t,T)}\quad\Longleftrightarrow\quad F(t,T,S)=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}$$ [§2.3]

## Ce qui la définit
Le taux forward n'est pas une prévision du taux qu'il fera en $T$ : il se lit dans les prix d'aujourd'hui, sans aucune hypothèse sur l'avenir. [ajout]

La même égalité s'écrit avec les taux zéro-coupon au lieu des prix : puisque $P(t,T)=e^{-R(t,T)(T-t)}$, elle devient $R(t,S)(S-t)=R(t,T)(T-t)+F(t,T,S)(S-T)$. Le taux long est la moyenne des taux des périodes successives, pondérée par leurs durées : $5\,\%\times2=4\,\%\times1+6\,\%\times1$. [§2.3]

![La même égalité, lue en aires : 4 % sur la première année et 6 % sur la seconde font la même aire que 5 % sur deux ans. Le forward est le taux qui complète l'aire du taux court jusqu'à celle du taux long.](figures/taux-forward.svg) [ajout]

Pour aller plus loin, le taux instantané. En resserrant la période sur un instant, on obtient $f(t,T)=-\partial\ln P(t,T)/\partial T$ : la vitesse à laquelle le prix du zéro-coupon baisse quand l'échéance recule. Mis bout à bout, ces taux redonnent le prix de n'importe quelle échéance, $P(t,T)=\exp\left(-\int_t^T f(t,u)\,du\right)$ : toute la courbe est faite de ses forwards. [§2.3]

## Le chemin jusqu'ici
fpp/convention-capitalisation dit comment un taux devient un facteur, et pourquoi, en capitalisation continue, les taux s'ajoutent d'une période à l'autre. fpp/facteur-actualisation donne les prix $P(t,T)$, et fpp/taux-zero-coupon les réécrit en taux, un par échéance. [ajout]

Le taux forward pose la question suivante : que dit cette courbe d'une période qui ne commence que plus tard ? [ajout]

## Exemple minimal
$P(0,1)=0{,}9608$ et $P(0,2)=0{,}9048$, soit des taux zéro-coupon de 4 % à un an et de 5 % à deux ans : le taux forward de la deuxième année vaut $F(0,1,2)=6\%$. [ajout]

## Geste de calcul type
Pour une période entre deux échéances cotées, diviser le prix court par le prix long, prendre le logarithme, puis diviser par la durée de la période : $\ln(0{,}9608/0{,}9048)/1\approx6\,\%$. Vérifier avec les taux : $5\,\%\times2-4\,\%\times1=6\,\%$. [§2.3]

## Cesse d'être valide quand
On ne peut s'assurer ce taux que si l'on peut prêter et emprunter aux deux échéances $T$ et $S$ ; sinon, il reste un nombre lu dans la courbe, sans moyen de l'obtenir. [ajout]

## Origine
- exercice fpp/ex-04 : un rapport de deux prix à terme de change est un rapport de facteurs d'actualisation forward [ajout]
- exercice fpp/ex-19 : la matrice complète des forwards se remplit avec une seule formule, $\big(r(T)T-r(t)t\big)/(T-t)$, où $r$ est le taux zéro-coupon et où $t$ est une échéance, non la date d'aujourd'hui ; elle se lit comme le taux qu'il faudra réaliser pour qu'un refinancement soit neutre [exo. 19]
