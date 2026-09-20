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
- §5.1
- Prop. 5
- Prop. 6
---

## Ce que c'est
La probabilité sous laquelle un prix est simplement l’espérance actualisée du flux. [Prop. 5, Prop. 6]

## Forme
$$\Pi\big(g(S_T)\big)=P(0,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$$ [Prop. 5, Prop. 6]

## Ce qui la définit
$\mathbb{Q}$ n’est pas choisie, elle est contrainte : $\mathbb{E}^{\mathbb{Q}}[S_T]=F(t,T)$. Le marché à terme la calibre. La positivité des prix d’états en fait une mesure positive, et le prix du flux certain 1 en fixe la constante à $P(0,T)$. [§5.1, Prop. 5, Prop. 6]

## Le chemin jusqu'ici
Le socle est en réalité une seule ligne. fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (sur fpp/convention-capitalisation) en chiffrent les deux jambes, et le tout donne fpp/prix-a-terme. [ajout]

La mesure risque-neutre est ce qu'on obtient en relisant ce prix à l'envers : si le prix à terme est le comptant capitalisé, alors il existe une probabilité sous laquelle tout prix est simplement l'espérance actualisée du flux. Aucune probabilité n'apparaît dans le socle — c'est la réplication qui l'engendre, pas une hypothèse. [ajout]

## Exemple minimal
Action à 100 sans dividende, $P(0,1)=0{,}9608$ : $\mathbb{E}^{\mathbb{Q}}[S_1]=104{,}08$, quelle que soit la dérive historique. [ajout]

## Geste de calcul type
Ne pas chercher $\mathbb{Q}$, la lire sur le marché à terme : $\mathbb{E}^{\mathbb{Q}}[S_T]=F(t,T)$. Puis actualiser l’espérance du payoff par $P(0,T)$, jamais par un taux ajusté du risque. [Prop. 6]

## Cesse d'être valide quand
Unique seulement en marché complet. Et elle ne dit rien de la probabilité historique $\mathbb{P}$ : les deux ne diffèrent que par la dérive. [ajout]

## Origine
- exercice fpp/ex-13 : geste manquant — identifier le drift risque-neutre en écrivant « forward = espérance » et en résolvant, sans changement de mesure explicite [ajout]
