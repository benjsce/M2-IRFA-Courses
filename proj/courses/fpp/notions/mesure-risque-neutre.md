---
id: fpp/mesure-risque-neutre
nom: Mesure risque-neutre
symbole: $\mathbb{Q}$
type: notion
statut: source
cas_de: fpp/operateur-de-prix
valeur: flux aléatoires
construite_a_partir_de:
- fpp/prix-a-terme
alias:
- probabilité risque-neutre
- risk neutral probability
- mesure de pricing
refs:
- Prop. 5
- Prop. 6
---

## Ce que c'est
La probabilité sous laquelle un prix est simplement l’espérance actualisée du flux. [Prop. 5, Prop. 6]

## Forme
$$\Pi\big(g(S_T)\big)=P(0,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$$ [Prop. 5, Prop. 6]

## Ce qui la définit
$\mathbb{Q}$ n’est pas choisie, elle est contrainte : $\mathbb{E}^{\mathbb{Q}}[S_T]=F(t,T)$. Le marché à terme la calibre. La positivité des prix d’états en fait une mesure positive, et le prix du flux certain 1 en fixe la constante à $P(0,T)$. [Prop. 5, Prop. 6]

## Exemple minimal
à venir [ajout]

## Geste de calcul type
à venir [ajout]

## Cesse d'être valide quand
Unique seulement en marché complet. Et elle ne dit rien de la probabilité historique $\mathbb{P}$ : les deux ne diffèrent que par la dérive. [ajout]
