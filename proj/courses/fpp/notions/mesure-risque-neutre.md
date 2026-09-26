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
La probabilité sous laquelle le prix d'un flux est simplement son espérance, actualisée par le zéro-coupon. [Prop. 5, Prop. 6]

## Forme
$$\Pi_t\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big]$$ [Prop. 6]

## Ce que les symboles modélisent
$\mathbb{Q}$ est une probabilité, mais pas celle des fréquences observées : c'est un instrument de calcul sous lequel actualiser suffit à donner le prix. Elle ne prédit rien — deux agents en désaccord complet sur l'avenir peuvent s'accorder sur elle. [§5.1]

$\Pi_t$ note le prix aujourd'hui d'un flux payé plus tard ; $g(S_T)$ est un flux payé en $T$ qui dépend du prix de l'action à cette date, comme l'action elle-même ou un call. Le poly date la Forme en $0$, avec $P(0,T)$ ; elle vaut à toute date $t$. [Prop. 6, ajout]

## Retrouver la formule
![Trois états du monde, pour l'exemple. À gauche, les prix d'aujourd'hui des flux qui paient 1 dans un seul état : tous positifs, et leur somme est le prix de l'euro certain, P(t,t+1) = 0,9608. À droite, les mêmes prix divisés par 0,9608 : des nombres positifs de somme 1, c'est-à-dire une probabilité, Q.](figures/mesure-risque-neutre.svg) [ajout]

**Connus aujourd'hui** : le prix de chaque flux, dont celui de l'euro certain, $P(t,T)$, et le prix à terme $F(t,T)$ de l'action. **Cherché** : une probabilité sous laquelle tout prix est une espérance actualisée. [§5.1, ajout]

On part d'un prix linéaire, écrit comme une moyenne pondérée des états du monde : $\Pi_t(X)=k\,\mathbb{E}^{\mathbb{Q}}(X)$, où $k$ est un nombre et $\mathbb{Q}$ une pondération dont on ne sait encore rien, pas même qu'elle est positive. [§5.1]

Un flux qui paie 1 dans un seul état et 0 ailleurs ne peut que rapporter : son prix, qu'on appelle prix d'état, est strictement positif, sinon ce serait un gain sans mise. Chaque état a donc un poids positif ; on met $\mathbb{Q}$ à l'échelle pour que ces poids fassent 1, et c'est une probabilité. [§5.1]

Le flux qui paie 1 dans tous les états est l'euro certain : son prix est $k\,\mathbb{E}^{\mathbb{Q}}(1)=k$, et c'est aussi $P(t,T)$. Donc $k=P(t,T)$ : sur la figure, les prix d'états font 0,9608, et divisés par 0,9608 ils deviennent les probabilités. [§5.1]

Enfin, un contrat à terme ne coûte rien : $\Pi_t\big(S_T-F(t,T)\big)=0$, soit $P(t,T)\big(\mathbb{E}^{\mathbb{Q}}(S_T)-F(t,T)\big)=0$. Sous $\mathbb{Q}$, l'espérance de l'action est donc son prix à terme. [§5.1, Prop. 6]

$$\Pi_t\big(g(S_T)\big)=P(t,T)\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\big],\qquad \mathbb{E}^{\mathbb{Q}}[S_T]=F(t,T)$$ [Prop. 6]

## Ce qui la définit
$\mathbb{Q}$ n’est pas choisie, elle est contrainte par le marché à terme : sous elle, l'espérance de chaque actif est son prix à terme. [Prop. 5, Prop. 6]

## Le chemin jusqu'ici
Le socle est en réalité une seule ligne. fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, et l'ensemble aboutit à fpp/prix-a-terme. [ajout]

La mesure risque-neutre est ce qu'on obtient en relisant ce prix à l'envers : si le prix à terme est le comptant capitalisé, alors il existe une probabilité sous laquelle tout prix est simplement l'espérance actualisée du flux. Aucune probabilité n'apparaît dans le socle — c'est la réplication qui l'engendre, pas une hypothèse. [ajout]

## Exemple minimal
Action à 100 sans dividende, $P(t,t+1)=0{,}9608$ : $\mathbb{E}^{\mathbb{Q}}[S_{t+1}]=104{,}08$, quelle que soit la dérive historique. [ajout]

## Geste de calcul type
Ne pas chercher $\mathbb{Q}$, la lire sur le marché à terme : $\mathbb{E}^{\mathbb{Q}}[S_T]=F(t,T)$. Puis actualiser l’espérance du payoff par $P(t,T)$, jamais par un taux ajusté du risque. [Prop. 6]

## Cesse d'être valide quand
Unique seulement en marché complet. Et elle ne dit rien de la dérive réelle : sous $\mathbb{Q}$, une action sans dividende croît en moyenne au taux sans risque, quelle que soit sa dérive historique. [§5.2.1, ajout]

## Origine
- exercice fpp/ex-13 : geste manquant — identifier le drift risque-neutre en écrivant « forward = espérance » et en résolvant, sans changement de mesure explicite [ajout]
