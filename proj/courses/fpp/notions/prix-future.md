---
id: fpp/prix-future
nom: Prix future
symbole: $H_t$
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: $D=B(t,T)$, aléatoire
construite_a_partir_de:
- fpp/replication-dynamique
alias:
- futures
- contrat à terme margé
refs:
- §4.2
- Prop. 3
- Prop. 4
---

## Ce que c'est
Le prix d’un contrat à terme réglé par appels de marge quotidiens. [§4.2, Prop. 3, Prop. 4]

## Forme
$$H_t=\Pi_t\!\left(\dfrac{S_T}{B(t,T)}\right)$$ [§4.2, Prop. 3]

## Ce que les symboles modélisent
$H_t$ est un prix qui se réajuste chaque jour, et non la valeur d'un contrat : c'est le niveau auquel les appels de marge se calculent. Un future vaut zéro juste après chaque règlement, et c'est ce qui le sépare d'un forward. [§4.2]

$\Pi_t(X)$ se lit « le prix aujourd'hui du flux $X$ payé plus tard » : la Forme dit que $H_t$ est ce que coûte aujourd'hui le droit de recevoir $S_T/B(t,T)$ en $T$. $B(t,T)$ est le compte capitalisé, le produit des zéro-coupons courts de $t$ à $T$, dont seul le premier est connu en $t$. [Prop. 3, ajout]

## Retrouver la formule
![En haut, le forward se règle en une fois, en $T$. En bas, la stratégie qui réplique le future : on place aujourd'hui $H_t$, le montant cherché ; à chaque règlement, un appel de marge de montant inconnu en $t$ est encaissé ou payé, puis replacé jusqu'en $T$ à un taux lui aussi inconnu en $t$ ; le nombre de contrats est ajusté à chaque règlement, et en $T$ le tout vaut $S_T/B(t,T)$. Les hauteurs ne viennent d'aucune donnée.](figures/prix-future.svg) [ajout]

**Connus aujourd'hui** : le comptant et le taux court de la première période. **Inconnus** : les appels de marge et les taux auxquels chacun sera replacé. **Cherché** : $H_t$. On ne peut donc pas, comme pour un forward, ramener en $t$ deux jambes connues ; on construit une stratégie dont on connaît le coût et la valeur finale. [§4.2, ajout]

La stratégie : placer $H_t$ au taux court et tenir des futures, dont l'entrée ne coûte rien. Elle coûte donc $H_t$. [§4.2.2]

Un pas, du règlement $t_i$ au suivant $t_{i+1}$. Si la richesse vaut $H_{t_i}/B(t,t_i)$, la placer une période au taux court la divise par $P(t_i,t_{i+1})$ : elle devient $H_{t_i}/B(t,t_{i+1})$. Tenir $1/B(t,t_{i+1})$ contrats y ajoute l'appel de marge $(H_{t_{i+1}}-H_{t_i})/B(t,t_{i+1})$. La richesse devient $H_{t_{i+1}}/B(t,t_{i+1})$ : même forme, un pas plus loin. Le nombre de contrats est connu en $t_i$, puisque seul le taux de la période qui commence y entre. [§4.2.2]

Au départ, la richesse est $H_t$, soit $H_t/B(t,t)$. À l'échéance, le future vaut le comptant, $H_T=S_T$ : la stratégie vaut $S_T/B(t,T)$. [§4.2.2]

Elle coûte $H_t$ aujourd'hui et paie $S_T/B(t,T)$ en $T$ : deux flux identiques ont le même prix, donc $H_t$ est le prix aujourd'hui de $S_T/B(t,T)$. [Prop. 3]

$$H_t=\Pi_t\!\left(\dfrac{S_T}{B(t,T)}\right)$$ [Prop. 3]

## Ce qui la définit
Chaque variation est encaissée le jour même et doit être replacée à un taux inconnu : c'est pourquoi le facteur n'est plus le zéro-coupon $P(t,T)$, connu aujourd'hui, mais le compte capitalisé $B(t,T)$, qui ne l'est pas. [§4.2, Prop. 3]

## Le chemin jusqu'ici
fpp/convention-capitalisation et fpp/facteur-actualisation fixent le prix du temps ; fpp/compte-capitalise donne celui de l'argent réinvesti au jour le jour ; fpp/replication-dynamique dit comment le répliquer. [ajout]

Le future se distingue du forward par une seule chose : les appels de marge quotidiens, donc un réglage à chaque pas. C'est pourquoi son socle passe par le compte capitalisé alors que celui du forward n'en a pas besoin. Les deux prix coïncident quand les taux sont déterministes — et le socle montre exactement où cette hypothèse entre. [ajout]

## Exemple minimal
Sous-jacent à 100, taux déterministes, $B(t,t+1)=P(t,t+1)=0{,}9608$ : $H_t=104{,}08$, égal au forward. [ajout]

## Geste de calcul type
Vérifier d’abord si les taux sont déterministes : si oui, $B=P$ et le future vaut le forward, 104,08. Sinon il n’y a pas de forme fermée et il faut un modèle de taux. [Prop. 4]

## Cesse d'être valide quand
La Forme suppose que chaque appel de marge peut être replacé au taux court du moment. Hors du cas de taux déterministes, elle ne se ramène plus au prix forward. [§4.2.2, Prop. 4]

## Origine
- exercice fpp/ex-07 : une option sur future se price avec la formule du cours en posant $q=r$, sans rien redémontrer [exo. 7]
- exercice fpp/ex-14 : le prix forward est une martingale sous $\mathbb{Q}$ — c'est pourquoi la formule de Black n'a pas de terme de dérive [exo. 14]
- exercice fpp/ex-20 : à taux nuls, future = comptant, et deux stratégies distinctes deviennent indiscernables (Prop. 4 sur un cas réel) [exo. 20]
