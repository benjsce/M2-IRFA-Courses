---
id: fpp/prix-a-terme
nom: Prix à terme
symbole: $F$, $K$, $H$
type: abstraite
statut: source
cas_de: fpp/contrat-prime-nulle
valeur: un actif ou un taux, livré à une date
parametre: le couple (portage $\Phi$, facteur d’actualisation $D$)
construite_a_partir_de:
- fpp/facteur-actualisation
- fpp/replication-statique
- fpp/portage
alias:
- forward price
- prix forward
- valeur forward
refs:
- Prop. 2
- Prop. 3
- Déf. 8
---

## Ce que c'est
Le prix fixé aujourd’hui pour un échange livré plus tard. [Prop. 2, Prop. 3, Déf. 8]

## Forme
$$K=F=\dfrac{S_t\,\Phi}{D}$$ [ajout]

## Ce que les symboles modélisent
$F$ est le prix à terme : celui qui rend le contrat de valeur nulle aujourd'hui, et c'est lui que donne la Forme. $K$ est le prix inscrit dans le contrat ; à la signature, on inscrit $K=F$. Ensuite $F$ bouge avec le marché, $K$ ne bouge plus. L'écart $F-S_t$ entre prix à terme et prix comptant s'appelle la base. [Déf. 8, §2.3]

$H$ est le prix à terme d'un future, contrat réglé chaque jour par appels de marge ; son $D$ n'est pas connu aujourd'hui, et la Forme ne lui donne pas de valeur. [§4.2]

$S_t$ est le prix comptant du sous-jacent. $\Phi$, le portage, dit quelle part de ce comptant paie la seule unité livrée en $T$ : le reste paie ce que la détention rapporte d'ici là (dividendes, intérêts d'une devise), que l'acheteur à terme ne touche pas. $D$ est le prix aujourd'hui d'une unité de la monnaie du règlement payée en $T$ : $P(t,T)$, $P^f(t,T)$ ou $B(t,T)$ selon le contrat. La Forme suppose $D$ connu en $t$. [§3.2, ajout]

## Retrouver la formule
Un contrat à terme a deux jambes : recevoir en $T$ une unité du sous-jacent, payer $K$ en $T$. **Connus aujourd'hui** : le comptant $S_t$, le portage $\Phi$ et le facteur $D$. **Cherché** : $K$. [ajout]

Jambe sous-jacent : recevoir une unité en $T$ vaut aujourd'hui le comptant, moins ce que la détention rapporte d'ici là et que l'acheteur à terme ne touche pas, soit $S_t\Phi$. [§3.2, ajout]

Jambe argent : $K$ payé en $T$ vaut aujourd'hui $KD$, puisque $D$ est le prix d'une unité payée en $T$. [ajout]

Le contrat ne coûte rien à la signature : les deux jambes valent autant, $KD=S_t\Phi$. Le $K$ qui l'assure est, par définition, le prix à terme $F$. [§3.1, ajout]

$$K=F=\dfrac{S_t\,\Phi}{D}$$ [ajout]

## Ce que les membres partagent
Tous sont le prix aujourd'hui d'un même flux : ce que coûte aujourd'hui le droit de recevoir $S_T/D$ en $T$. [Prop. 2, Prop. 3]

Quand $D$ est connu en $t$, ce prix se retrouve par le geste ci-dessus, les deux jambes ramenées en $t$ et égalées à la signature, et s'écrit $S_t\Phi/D$ ; d'un contrat à l'autre, seuls changent $\Phi$ et $D$. Quand $D$ ne l'est pas, comme $B(t,T)$ pour un future, le prix reste défini, mais sans formule fermée. [Prop. 2, Prop. 3, ajout]

## Pourquoi ce niveau existe
Le cours présente ces contrats séparément, sur autant de sections, alors qu’ils ne diffèrent que par deux paramètres, le portage $\Phi$ et le facteur $D$. Les réunir, c'est apprendre un geste au lieu de plusieurs. [ajout]

## Le chemin jusqu'ici
Plusieurs briques indépendantes se rejoignent ici. fpp/replication-statique donne la méthode — acheter aujourd'hui, porter, livrer — et c'est elle qui fait du prix à terme un prix démontré et non un pari sur l'avenir. [ajout]

Les deux autres chiffrent les deux jambes de cette réplication : fpp/facteur-actualisation (lui-même construit sur fpp/convention-capitalisation) dit ce que coûte l'argent qu'on immobilise, et fpp/portage ce que rapporte ou coûte la détention du sous-jacent pendant ce temps. [ajout]

$K=S_t\Phi/D$ n'est donc que la mise en équation du raisonnement : le prix à terme est le comptant, corrigé du financement et du portage. [ajout]

## Exemple minimal
$S_t=100$, $\Phi=1$, $D=P(t,t+1)=0{,}9608$ : $K=F=104{,}08$. [ajout]

## Geste de calcul type
Identifier les deux paramètres avant de calculer : le portage $\Phi$ et le facteur $D$. Avec $\Phi=1$ et $D=0{,}9608$, $K=104{,}08$. La formule se lit dans les deux sens : $S_t=KD/\Phi$. [Prop. 2, Prop. 3]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| portage $\Phi$ | action sans dividende | $1$ |
| portage $\Phi$ | dividendes discrets | $1-\sum_i d_i$ |
| portage $\Phi$ | rendement continu $q$ | $e^{-q\tau}$ |
| portage $\Phi$ | devise livrée | son zéro-coupon : $P(t,T)$ si c'est la devise locale |
| facteur $D$ | règlement unique, devise locale | $P(t,T)$ |
| facteur $D$ | règlement unique, devise étrangère | $P^f(t,T)$ |
| facteur $D$ | appels de marge | $B(t,T)$, inconnu en $t$ : pas de formule fermée |
[Prop. 2, Prop. 3, Déf. 8, §2.4, §3.2]

## Cesse d'être valide quand
Quand $D$ n'est pas connu aujourd'hui, parce que les appels de marge sont replacés à des taux futurs, la Forme ne donne plus de nombre : il faut un modèle de taux. Quand le sous-jacent est coté dans une devise et réglé dans une autre, $\Phi$ et $D$ ne suffisent plus. [§4.2, ajout]

## Origine
- exercice fpp/ex-01 : la fiche se lit à l'envers, $S_t=FD/\Phi$ [ajout]
- exercice fpp/ex-04 : deux forwards, spot inconnu — le spot se simplifie dans tout rapport de deux forwards, il reste un forward de taux [ajout]
