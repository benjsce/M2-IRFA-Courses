---
id: fpp/contrat-prime-nulle
nom: Contrat à prime nulle
type: abstraite
statut: ajout
cas_de: fpp/contrat-derive
valeur: aucun flux à la signature
parametre: la nature du sous-jacent échangé
construite_a_partir_de:
- fpp/valeur-actuelle-nette
refs:
- §2.3
- §3.1
---

## Ce que c'est
Un échange qui ne coûte rien à la signature, comme un forward, un future, un FRA ou un swap : on n'y cherche pas son prix, qui est nul, mais le prix à inscrire dedans. [ajout]

## Ce que les membres partagent
Pour une option, on connaît le contrat et on cherche sa prime, ce qu'il faut payer pour l'avoir. Ici, c'est l'inverse : **la prime est connue, c'est zéro**, et **on cherche le prix $K$** à inscrire dans le contrat. [ajout]

Ce qui fixe $K$ : ce qu'on recevra et ce qu'on paiera, ramenés à aujourd'hui, valent autant, puisque la signature ne coûte rien. Pour une action à 100, livrée dans un an avec $P(t,t+1)=0{,}9608$, cette égalité donne $K=104{,}08$. [§3.1, ajout]

## Pourquoi ce niveau existe
Ces contrats n'échangent pas la même chose, une action, une devise, un taux, mais ils posent la même question : quel prix inscrire pour que l'échange ne coûte rien aujourd'hui ? Ce niveau la pose une fois pour tous. [ajout]

## Le chemin jusqu'ici
fpp/convention-capitalisation dit comment un taux fait grandir une somme avec le temps ; fpp/facteur-actualisation en tire le prix aujourd'hui d'un euro payé plus tard ; fpp/valeur-actuelle-nette additionne ces prix sur tous les flux d'un échange. [ajout]

Dire qu'un échange ne coûte rien à la signature, c'est dire que sa valeur actuelle nette est nulle : c'est cette équation, et elle seule, qui détermine $K$. [ajout]

## Cesse d'être valide quand
Dès que l'échange commence par un paiement, comme pour une option, la prime redevient l'inconnue et le prix inscrit dans le contrat est donné. [ajout]

## Origine
- exercice fpp/ex-11 : le strike qui annule la prime **est** le prix forward. Un forward est un call-put à strike bien choisi ; c'est la définition, lue depuis la parité [exo. 11]
