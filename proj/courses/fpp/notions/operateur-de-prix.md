---
id: fpp/operateur-de-prix
nom: Opérateur de prix
type: abstraite
statut: ajout
cas_de: fpp/absence-arbitrage
parametre: la nature des flux
construite_a_partir_de: []
refs:
- §5.1
---

## Ce que c'est
L’application $\Pi_t$ qui associe à un flux payé plus tard son prix aujourd'hui, en $t$. [ajout]

## Ce que les symboles modélisent
$\Pi_t$ prend un flux, un montant payé à une date future et qui peut dépendre de ce qui se sera passé d'ici là, et rend un nombre : ce que coûte ce flux en $t$. On écrit $\Pi_t(X)$ pour le prix aujourd'hui du flux $X$. [§5.1, ajout]

Le poly écrit ce prix « Price » au §5.1 et $\pi(S_0)$ au §6.2 ; le dépôt le note $\Pi_t$, parce que $\pi$ y désigne déjà la prime de risque, qui est un écart de rendement et non un prix. [§5.1, §6.2, ajout]

## Ce que les membres partagent
Deux propriétés, toutes deux imposées par l’absence d’arbitrage. Linéarité : le prix d'une somme de flux est la somme de leurs prix, $\Pi_t(aX+bY)=a\,\Pi_t(X)+b\,\Pi_t(Y)$ ; sinon, acheter les morceaux et vendre le tout rapporterait sans mise. Positivité : un flux qui ne peut que rapporter, et rapporte dans au moins un état du monde, a un prix strictement positif. [§5.1, ajout]

Deux exemples avec les chiffres du cours : l'euro certain payé dans un an, $\Pi_t(1)=P(t,t+1)=0{,}9608$ ; l'action sans dividende livrée dans un an, $\Pi_t(S_{t+1})=S_t=100$. [§5.1, ajout]

## Pourquoi ce niveau existe
La valeur actuelle nette et le prix risque-neutre sont le même opérateur : l'un sur des flux certains, l'autre sur des flux aléatoires. Le cours ne fait pas le rapprochement ; ce niveau le fait. [ajout]

## Cesse d'être valide quand
rien dans le périmètre du cours [ajout]

## Origine
- exercice fpp/ex-14 : c'est la **linéarité** qui autorise à évaluer une somme de payoffs terme à terme ; sans elle, la démonstration de la parité s'arrête à la première ligne [exo. 14]
