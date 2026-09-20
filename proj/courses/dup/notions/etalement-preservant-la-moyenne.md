---
id: dup/etalement-preservant-la-moyenne
nom: Étalement préservant la moyenne
type: notion
statut: source
cas_de: dup/accroissement-de-risque
valeur: une suite d’étalements géométriques
construite_a_partir_de:
- dup/loterie
alias:
- mean-preserving spread
- MPS
- Definition C
refs:
- L1 slide 21
- L1 slide 24
---

## Ce que c'est
Déplacer de la probabilité du centre vers les queues en laissant la moyenne inchangée. [L1 slide 21]

## Ce qui la définit
$F^*$ est plus risquée que $F$ si elle s’obtient à partir de $F$ par une suite de tels étalements. [L1 slide 21]

## Le chemin jusqu'ici
Le socle se limite à dup/loterie. [ajout]

Déplacer de la probabilité vers les queues à moyenne constante est une opération sur la distribution, pas sur les préférences. Le socle s'arrête donc là. Que cela corresponde à « plus risqué » est un théorème, qui viendra quand l'utilité sera disponible. [ajout]

## Exemple minimal
De $\{40,60\}$ uniforme vers $\{20,40,60,80\}$ uniforme : la moyenne reste 50, la probabilité est partie vers les extrêmes. [L1 slide 24]

## Cesse d'être valide quand
Un seul étalement ne produit qu’un croisement des fonctions de répartition ; une suite en produit plusieurs, et la lecture graphique cesse d’être praticable. [L1 slide 22]
