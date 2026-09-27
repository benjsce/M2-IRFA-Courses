---
id: fpp/dividendes-intermediaires
nom: Dividendes intermédiaires
symbole: '$d_i$, $T_i$'
type: notion
statut: source
construite_a_partir_de:
- fpp/prix-forward
alias:
- intermediate dividends
- dividende proportionnel
- dividende en numéraire
- dividende implicite
refs:
- §3.2
- exo. 1
- exo. 2
- exo. 5
---

## Ce que c'est
Les dividendes versés avant l'échéance abaissent le prix forward, parce qu'ils reviennent à celui qui porte l'action et allègent son financement. [§3.2]

## Forme
$$F(t,T)=\frac{S_t}{P(t,T)}\Big(1-\sum_i d_i\Big)\qquad\text{ou, pour des montants fixes,}\qquad F(t,T)=\frac{S_t-\text{valeur en }t\text{ des dividendes}}{P(t,T)}$$ [§3.2, exo. 1]

## Ce que les symboles modélisent
$T_i$ est la date du $i$-ième dividende, avant $T$. $d_i$ est une fraction : le dividende versé en $T_i$ vaut $d_i$ fois la valeur forward de l'action à cette date, $S_t/P(t,T_i)$. Ce ne sont ni les $d_1$, $d_2$ de la formule de Black et Scholes, ni le taux de dividende continu $d$. [§3.2, éq. 5, §5.2.1]

## Retrouver la formule
![Le cash-and-carry du vendeur à terme quand l'action verse en T₁ un dividende d₁ S_t / P(t,T₁). En t, il achète l'action S_t mais emprunte en deux fois : d₁ S_t jusqu'à T₁ seulement, que le dividende rembourse exactement, et (1 − d₁) S_t jusqu'à T. En T₁, dividende reçu et emprunt court remboursé s'annulent. En T, ses jambes se somment comme au cash-and-carry, avec un emprunt plus petit : vente à terme + (F − S_T), action portée à crédit + (S_T − (1 − d₁) S_t / P(t,T)), somme F − (1 − d₁) S_t / P(t,T), certaine et sans mise, donc nulle : F(t,T) = S_t / P(t,T) × (1 − d₁). Placer le dividende jusqu'en T, comme dans le texte, mène au même prix.](figures/dividendes-intermediaires.svg) [ajout]

Sans dividende, porter l'action un an coûte 104,08. [§3.1]

Dans six mois, la valeur forward de l'action est $100/0{,}9802=102{,}02$ ; un dividende de 2 % de cette valeur rapporte 2,04 à celui qui porte l'action. Placés jusqu'à l'échéance, ils deviennent $2{,}04\times0{,}9802/0{,}9608=2{,}08$. [§3.2, ajout]

Le prix de livraison baisse d'autant : $104{,}08-2{,}08=102{,}00$, soit $104{,}08\times(1-0{,}02)$. En lettres, chaque dividende vaut $\dfrac{S_t}{P(t,T_i)}d_i$ en $T_i$ et $\dfrac{S_t\,d_i}{P(t,T_i)}\cdot\dfrac{P(t,T_i)}{P(t,T)}$ en $T$ : [§3.2]

$$F(t,T)=\frac{S_t}{P(t,T)}-\sum_{i}\frac{S_t\,d_i}{P(t,T_i)}\frac{P(t,T_i)}{P(t,T)}=\frac{S_t}{P(t,T)}\Big(1-\sum_i d_i\Big)$$ [§3.2]

## Ce qui la définit
Ce qui est **connu** : le prix comptant, la courbe et les dividendes. Ce qu'on **cherche** : le prix de livraison. L'acheteur à terme ne reçoit pas les dividendes versés avant la livraison ; celui qui porte l'action, si. Le prix forward lui retire donc leur valeur capitalisée. [§3.2]

Un dividende proportionnel à la valeur forward de sa date ne dépend pas de cette date : 2 % dans trois mois ou dans six mois retirent le même 2 % du prix forward. Le livre d'exercices le montre, avec deux réponses égales pour un dividende de 8 % à trois mois et à six mois. [§3.2, exo. 2]

Pour un dividende d'un montant fixe, on retire sa valeur actuelle au prix comptant avant de capitaliser. Et un prix forward observé révèle le dividende que le marché attend : c'est le dividende implicite. [exo. 1, exo. 5]

## Le chemin jusqu'ici
fpp/prix-forward donne le prix quand l'action ne verse rien. fpp/cash-and-carry dit qui touche le dividende : celui qui porte l'action, pas l'acheteur à terme. Ce dividende se déplace dans le temps avec fpp/zero-coupon, selon la convention de fpp/capitalisation, et fpp/absence-d-arbitrage oblige le prix de livraison à le refléter entièrement. [ajout]

## Exemple minimal
L'action à 100, 4 % sur un an, un dividende de 2 % de la valeur forward dans six mois : le prix forward à un an vaut 102,00 ; pour un dividende fixe de 2 à la même date, 102,04. [ajout]

## Geste de calcul type
Dividende implicite : si le forward à un an cote 101, le dividende capitalisé que le marché attend vaut $104{,}08-101=3{,}08$ à l'échéance. [exo. 5, ajout]

## Cesse d'être valide quand
La formule du poly suppose des dividendes proportionnels à la valeur forward de leur date ; un dividende annoncé en euros se traite par la seconde écriture. Et elle suppose ces dividendes connus : un dividende incertain fait de $F$ une estimation, et c'est ce que l'exercice 5 du livre exploite. [§3.2, exo. 1, exo. 5]
