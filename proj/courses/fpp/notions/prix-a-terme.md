---
id: fpp/prix-a-terme
nom: Prix à terme
symbole: $K$
type: abstraite
statut: source
cas_de: fpp/absence-d-arbitrage
parametre: ce que le contrat livre à l'échéance
construite_a_partir_de:
- fpp/zero-coupon
alias:
- forward contract
- contrat forward
- forward
refs:
- §2
- §3
---

## Ce que c'est
Le montant K inscrit aujourd'hui dans un contrat qui échange plus tard quelque chose contre K, choisi pour que le contrat ne coûte rien à la signature. [§2, §3.1]

## Forme
$$\text{valeur en }t\text{ de ce qu'on paie, fixé par }K\;=\;\text{valeur en }t\text{ de ce qu'on reçoit}$$ [ajout]

## Ce que les symboles modélisent
$K$ est ce qui est écrit dans le contrat : le taux d'un FRA, le change d'un contrat de change à terme, le prix de livraison d'une action. Le poly emploie la même lettre pour le strike d'une option, qui est fixé lui aussi dans le contrat mais n'est pas choisi pour le rendre gratuit. [Déf. 7, §2.4, §3.1, Déf. 9]

## Ce que les membres partagent
Chaque membre répond à la même question : quel $K$ rend gratuit un contrat qui échange, à une date future, une chose contre $K$ ? Ce qui est **connu** : les prix du jour, zéro-coupons et prix comptant. Ce qu'on **cherche** : $K$. [§2.3, §2.4, §3.1]

La réponse suit toujours le même geste : écrire les deux jambes du contrat, ramener chacune en $t$ avec le zéro-coupon de sa devise et de sa date, et égaler, puisque le contrat ne coûte rien. [§2.3, §2.4, §3.1]

$K$ ne prévoit rien. Il ne dépend que des prix d'aujourd'hui, pas de ce que quiconque attend du futur. [§2.4, ajout]

## Pourquoi ce niveau existe
Le poly traite trois contrats l'un après l'autre, le FRA, le change à terme et le forward sur action, et les résout par le même geste. Le voir une fois dispense de retenir trois formules et permet d'en écrire une quatrième, pour une matière première ou un indice, sans rien apprendre de nouveau. La formule de Black ne demande d'ailleurs qu'un prix à terme, quel que soit le sous-jacent. [§2, §3, §6.5]

## Le chemin jusqu'ici
fpp/zero-coupon est l'outil qui ramène chaque jambe en $t$, dans sa devise et à sa date ; fpp/capitalisation dit pourquoi un même montant ne vaut pas la même chose selon la date où il est payé. [ajout]

## Exemple minimal
Dans le monde du cours, à un an : un taux de 6 % pour emprunter entre un et deux ans, un change de 1,1111 dollar par euro, un prix de livraison de 104,08 pour l'action. [ajout]

## Geste de calcul type
Écrire les deux jambes, les actualiser chacune avec le zéro-coupon de sa devise et de sa date, égaler, résoudre en $K$. [ajout]

## Cesse d'être valide quand
Si ce qui est livré verse quelque chose avant l'échéance, dividende ou coupon, il faut le compter dans la jambe livrée. Et si le contrat se règle chaque jour par appels de marge, comme un future, les deux jambes ne se ramènent plus en $t$ par un seul zéro-coupon connu. [§3.2, §4.2]
