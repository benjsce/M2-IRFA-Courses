---
id: fpp/edp-black-scholes
nom: Équation de Black et Scholes
type: notion
statut: source
construite_a_partir_de:
- fpp/modele-black-scholes
- fpp/replication-dynamique
alias:
- B&S PDE
- équation aux dérivées partielles des options
refs:
- §7.1
- éq. 16
---

## Ce que c'est
L’équation que satisfait tout prix d’option quand on peut couvrir le risque en continu. [§7.1]

## Forme
$$\dfrac{\partial C}{\partial t}+rS\dfrac{\partial C}{\partial S}+\tfrac12\sigma^2S^2\dfrac{\partial^2C}{\partial S^2}=rC,\qquad C(T,x)=(x-K)^+$$ [éq. 16]

## Ce qui la définit
Le geste est en trois temps : écrire $dC$ par la formule d’Itô, former le portefeuille d’une option et de $\delta$ actions, puis choisir $\delta=-\partial C/\partial S$ pour annuler le terme brownien. [§7.1]

Le portefeuille ne porte alors plus de risque entre $t$ et $t+dt$ : son rendement instantané doit valoir $r\,dt$, sinon il y a arbitrage. La dérive $\mu$ disparaît de l’équation — c’est le résultat central du chapitre. [§7.1]

## Exemple minimal
Pour $C(t,S)=S$, l’équation se réduit à $rS=rS$ : une action est bien son propre prix. [ajout]

## Geste de calcul type
Pour vérifier qu’une formule candidate est un prix : la dériver une fois en $t$, deux fois en $S$, reporter dans l’équation, puis contrôler la condition terminale. [éq. 16]

## Cesse d'être valide quand
Exige un rééquilibrage continu et sans friction, une volatilité constante et un taux déterministe. C’est l’hypothèse la plus fragile de tout l’édifice. [ajout]
