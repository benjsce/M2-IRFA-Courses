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
$$K=\dfrac{S_t\,\Phi}{D}$$ [ajout]

## Ce que les membres partagent
Tous sont le prix comptant d’un même objet : le payoff $S_T/D$. Le prix à terme n’est jamais une formule nouvelle, c’est un prix comptant amplifié par le coût de portage. [ajout]

## Pourquoi ce niveau existe
Quatre contrats que le cours présente séparément, sur quatre sections, alors qu’ils ne diffèrent que par deux paramètres qui commutent. C’est l’abstraction la plus rentable de la branche. [ajout]

## Le chemin jusqu'ici
Trois briques indépendantes se rejoignent ici. fpp/replication-statique donne la méthode — acheter aujourd'hui, porter, livrer — et c'est elle qui fait du prix à terme un prix démontré et non un pari sur l'avenir. [ajout]

Les deux autres chiffrent les deux jambes de cette réplication : fpp/facteur-actualisation (lui-même construit sur fpp/convention-capitalisation) dit ce que coûte l'argent qu'on immobilise, et fpp/portage ce que rapporte ou coûte la détention du sous-jacent pendant ce temps. [ajout]

$K=S_t\Phi/D$ n'est donc que la mise en équation du raisonnement : le prix à terme est le comptant, corrigé du financement et du portage. [ajout]

## Exemple minimal
$S_t=100$, $\Phi=1$, $D=P(0,1)=0{,}9608$ : $K=104{,}08$. [ajout]

## Geste de calcul type
Identifier les deux paramètres avant de calculer : le portage $\Phi$ et le facteur $D$. Avec $\Phi=1$ et $D=0{,}9608$, $K=104{,}08$. La formule se lit dans les deux sens : $S_t=KD/\Phi$. [Prop. 2, Prop. 3]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| portage $\Phi$ | action sans dividende | $1$ |
| portage $\Phi$ | dividendes discrets | $1-\sum_i d_i$ |
| portage $\Phi$ | rendement continu $q$ | $e^{-q\tau}$ |
| portage $\Phi$ | devise | $P(t,T)$ |
| facteur $D$ | règlement unique, devise locale | $P(t,T)$ |
| facteur $D$ | règlement unique, devise étrangère | $P^f(t,T)$ |
| facteur $D$ | appels de marge | $B(t,T)$ |
[Prop. 2, Prop. 3, Déf. 8, §2.4, §3.2]

## Cesse d'être valide quand
Deux ruptures : refinancement aléatoire (le future perd la forme fermée) ; sous-jacent et règlement dans deux devises différentes (quanto — la corrélation manque aux deux paramètres). La base $F-S$ n’est lisible comme coût de portage que hors de ces deux cas. [ajout]

## Origine
- exercice fpp/ex-01 : la fiche se lit à l'envers, $S_t=FD/\Phi$ [ajout]
- exercice fpp/ex-04 : deux forwards, spot inconnu — le spot se simplifie dans tout rapport de deux forwards, il reste un forward de taux [ajout]
