---
id: fpp/fra
nom: Forward Rate Agreement
symbole: FRA
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: sous-jacent $P(\cdot,S)$, strike écrit en taux
construite_a_partir_de:
- fpp/taux-forward
alias:
- forward rate agreement
refs:
- §2.3
- Déf. 7
---

## Ce que c'est
Un contrat qui échange en $S$ l'intérêt d'une période future au taux $K$, fixé aujourd'hui, contre l'intérêt au taux $R(T,S)$, qui ne sera connu qu'en $T$. [Déf. 7]

## Forme
$$P(t,T)=P(t,S)\,e^{K(S-T)}\quad\Longrightarrow\quad K=F(t,T,S)$$ [Déf. 7, §2.3]

## Ce que les symboles modélisent
FRA n'est pas une grandeur mais un contrat, désigné par son sigle anglais, *forward rate agreement*. Il porte sur trois dates : $t$, la signature ; $T$, le début de la période future ; $S$, sa fin et la date du paiement. [Déf. 7]

$K$ est le taux fixe inscrit au contrat, en capitalisation continue, choisi à la signature. $R(T,S)$ est le taux zéro-coupon de $T$ à $S$, tel qu'il sera constaté en $T$ : le même objet que $R(t,T)$, mais vu depuis une date future, donc inconnu aujourd'hui. On se place du côté de celui qui paie le fixe : l'emprunteur qui veut connaître dès aujourd'hui le taux de son emprunt futur. [Déf. 7, §2.3, ajout]

## Retrouver la formule
![En $S$, celui qui paie le fixe paie $e^{K(S-T)}$, fixé aujourd'hui, et reçoit $e^{R(T,S)(S-T)}$, inconnu aujourd'hui. Ce second flux vaut pourtant 1 en $T$, quel que soit le taux, donc $P(t,T)$ en $t$ ; le premier vaut $P(t,S)e^{K(S-T)}$ en $t$. Le contrat ne coûtant rien, les deux sont égaux, et $K$ est le taux forward.](figures/fra.svg) [ajout]

Sur un nominal de 1, le FRA fait recevoir en $S$ la somme $e^{R(T,S)(S-T)}$, capital et intérêts au taux du moment, et payer $e^{K(S-T)}$, capital et intérêts au taux fixe ; les deux capitaux se compensent, seuls les intérêts s'échangent. [Déf. 7, ajout]

Prenons $T$ dans un an et $S$ dans deux. **Connus aujourd'hui** : les prix $P(t,T)=0{,}9608$ et $P(t,S)=0{,}9048$. **Inconnu** : le taux $R(T,S)$, qui ne sera fixé que dans un an. **Cherché** : le $K$ pour lequel le contrat ne coûte rien à la signature. [ajout]

La jambe fixe est un montant connu, payé en $S$ : ramenée en $t$ par le zéro-coupon d'échéance $S$, elle vaut $0{,}9048\,e^{K}$. [ajout]

La jambe flottante a un montant inconnu, mais sa valeur, elle, est connue. Recevoir $e^{R(T,S)(S-T)}$ en $S$, c'est recevoir exactement ce que devient 1 placé en $T$ jusqu'en $S$ au taux du moment : en $T$, ce flux vaut donc 1, quel que soit ce taux. Et 1 payé en $T$ vaut aujourd'hui $P(t,T)=0{,}9608$. [§2.3, ajout]

Le contrat ne coûte rien à la signature, donc les deux jambes valent autant : $0{,}9608=0{,}9048\,e^{K}$, d'où $K=\ln(0{,}9608/0{,}9048)\approx6\,\%$. [Déf. 7]

C'est la formule du taux forward, au chiffre et à la lettre près : le taux fixe du FRA est le taux forward de la courbe. [§2.3]

$$P(t,T)=P(t,S)\,e^{K(S-T)}\quad\Longleftrightarrow\quad K=\dfrac{1}{S-T}\ln\dfrac{P(t,T)}{P(t,S)}=F(t,T,S)$$ [Déf. 7, §2.3]

## Ce qui la définit
Le taux forward est un nombre lu dans la courbe ; le FRA est l'engagement de le payer. Il ne prévoit pas le taux de $T$ à $S$ : il remplace le taux inconnu $R(T,S)$ par le taux $F(t,T,S)$, connu aujourd'hui, quel que soit le taux qui se fixera. [§2.3, ajout]

Vu comme un prix à terme, son sous-jacent est le zéro-coupon d'échéance $S$, livré en $T$ : son prix à terme vaut $P(t,S)/P(t,T)=e^{-K(S-T)}$, et le FRA l'écrit en taux. [ajout]

## Le chemin jusqu'ici
fpp/facteur-actualisation cote aujourd'hui un euro payé en $T$ et un euro payé en $S$ : ce sont les deux prix connus du contrat. fpp/convention-capitalisation fixe la capitalisation continue, où capital et intérêts d'une période s'écrivent $e^{K(S-T)}$. [ajout]

fpp/taux-zero-coupon relit ces prix en taux, et fournit aussi le taux inconnu $R(T,S)$, un taux zéro-coupon vu depuis $T$. fpp/taux-forward tire des deux prix le taux de la période de $T$ à $S$ : le FRA est le contrat qui le garantit. [ajout]

## Exemple minimal
Un emprunteur qui empruntera un euro dans un an, pour un an, signe aujourd'hui un FRA : il paiera 6 %, quel que soit le taux à un an constaté dans un an. [ajout]

## Geste de calcul type
Lire $K$ sur les deux prix : $\ln(0{,}9608/0{,}9048)\approx6\,\%$, et vérifier que le contrat ne coûte rien, $0{,}9048\times e^{0{,}06}=0{,}9608$. Si, dans un an, le taux à un an s'est fixé à 7 %, celui qui paie le fixe reçoit en $S$ la différence $e^{0{,}07}-e^{0{,}06}\approx0{,}0107$ : ce qu'il gagne sur le contrat compense ce qu'il paie de plus sur son emprunt. [ajout]

## Cesse d'être valide quand
Rien ne permet de placer ou d'emprunter de $T$ à $S$ au taux $R(T,S)$ : la jambe flottante ne vaut alors plus 1 en $T$. Et le taux ne se garantit sans rien payer que si l'on peut aujourd'hui prêter et emprunter aux deux échéances $T$ et $S$. [ajout]

## Origine
- exercice fpp/ex-19 : verrouiller aujourd'hui le taux d'un emprunt futur, ce que décrit la question (b), est un FRA — le mot n'apparaît pas dans l'exercice [ajout]
