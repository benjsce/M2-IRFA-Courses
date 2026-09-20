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
Trois flux de 100 en 1, 2 et 3 ans, courbe plate à 4 % : $\mathrm{NPV}(0)=277{,}08$. [ajout]

## Geste de calcul type
Actualiser flux par flux, puis sommer : trois flux de 100 à un, deux et trois ans sur une courbe plate à 4 % valent 277,08. Pour transporter la valeur en $t_k$, diviser par $P(t,t_k)$. [Déf. 4]

## Cesse d'être valide quand
Flux certains uniquement. [Déf. 4]

Dès qu’ils sont aléatoires, il faut passer sous $\mathbb{Q}$. [§5.1]
