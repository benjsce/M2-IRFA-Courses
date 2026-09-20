---
id: fpp/valeur-actuelle-nette
nom: Valeur actuelle nette
symbole: $\mathrm{NPV}$
type: notion
statut: source
cas_de: fpp/operateur-de-prix
valeur: flux certains
construite_a_partir_de:
- fpp/facteur-actualisation
alias:
- NPV
- net present value
refs:
- Déf. 4
---

## Ce que c'est
La somme d’un échéancier de flux certains, ramenés à une même date. [Déf. 4]

## Forme
$$\mathrm{NPV}(t)=\sum_i P(t,t_i)X_i$$ [Déf. 4]

## Ce qui la définit
Transportable à n’importe quelle date par division : $\mathrm{NPV}(t_k)=\mathrm{NPV}(t)/P(t,t_k)$. [Déf. 4]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Flux certains uniquement. Dès qu’ils sont aléatoires, il faut passer sous $\mathbb{Q}$. [Déf. 4]
