---
id: fpp/probabilite-risque-neutre
nom: Probabilité risque-neutre
symbole: '$\mathbb{Q}$, $\mathbb{P}$'
type: notion
statut: source
cas_de: fpp/absence-d-arbitrage
construite_a_partir_de:
- fpp/prix-forward
- fpp/valeur-actuelle-nette
alias:
- risk neutral probability
- RNP
- théorème fondamental de l'évaluation
- fundamental pricing theorem
- mesure risque-neutre
refs:
- Prop. 6
- §5.1
- Prop. 5
---

## Ce que c'est
La probabilité sous laquelle le prix de tout flux aléatoire est son espérance actualisée, et l'espérance de tout actif son prix forward. [Prop. 6]

## Forme
$$\mathrm{Price}\big(g(\tilde S(T))\big)=P(0,T)\,E^{\mathbb Q}\big(g(\tilde S(T))\big),\qquad E^{\mathbb Q}\big(\tilde S(T)\big)=F(T)$$ [Prop. 6]

## Ce que les symboles modélisent
$\mathbb{Q}$ n'est la croyance de personne : c'est un outil de calcul des prix, fixé par les prix forward. $\mathbb{P}$, la probabilité historique, est celle du monde réel, et ce n'est pas sous elle qu'on calcule les prix. $\tilde S(T)$ est le prix aléatoire de l'actif en $T$, $g$ une fonction quelconque qui en fait un paiement, $F(T)$ son prix forward vu d'aujourd'hui, noté ailleurs $F(0,T)$. [Prop. 6, §6.1]

## Retrouver la formule
![Deux états du monde dans un an, l'action à 80 ou à 130. Sous la probabilité historique, la hausse a 60 % de chances et la moyenne vaut 110. Sous la probabilité risque-neutre, elle n'en a que 48 %, juste ce qu'il faut pour que la moyenne tombe sur le prix forward, 104,08.](figures/probabilite-risque-neutre.svg) [ajout]

Le poly cherche une règle de prix de la forme $\mathrm{Price}(\tilde X_T)=k\,E^{\mathbb Q}(\tilde X_T)$, avec un nombre $k$ et une mesure $\mathbb Q$ à déterminer. [§5.1]

Un titre qui paie 1 dans un seul état du monde et 0 ailleurs doit avoir un prix strictement positif, sinon ce serait un gain gratuit : $\mathbb Q$ donne un poids positif à chaque état, et on la normalise en probabilité. [§5.1]

Un titre qui paie 1 dans tous les états est le zéro-coupon : son prix est $k=P(0,T)$. Dans l'exemple, $k=0{,}9608$. [§5.1]

Enfin, un contrat à terme ne coûte rien : $\mathrm{Price}(\tilde S_T-F)=0$, donc $E^{\mathbb Q}(\tilde S_T)=F$. Dans l'exemple, la probabilité de hausse $q$ vérifie $130\,q+80(1-q)=104{,}08$, soit $q\approx0{,}48$. Il reste : [§5.1]

$$\mathrm{Price}\big(g(\tilde S(T))\big)=P(0,T)\,E^{\mathbb Q}\big(g(\tilde S(T))\big)$$ [Prop. 6]

## Ce qui la définit
En finance d'entreprise, on actualise l'espérance des flux à un taux qui dépend de leur classe de risque ; mais sous quelle probabilité prendre l'espérance ? Ce qui est **connu** : les zéro-coupons et les prix forward. Ce qu'on **cherche** : une probabilité qui donne un prix nul à tout flux de valeur actuelle nette nulle, en particulier à tout contrat à terme. C'est la probabilité risque-neutre, et elle existe en l'absence d'arbitrage. [§5.1, Prop. 5]

## Le chemin jusqu'ici
fpp/prix-forward fournit la contrainte qui fixe $\mathbb Q$ : l'espérance d'un actif doit tomber sur son prix forward. Ce prix sortait de fpp/cash-and-carry, avec un emprunt évalué par fpp/zero-coupon dans la convention de fpp/capitalisation. [ajout]

fpp/valeur-actuelle-nette actualisait des flux certains ; la probabilité risque-neutre étend le geste aux flux aléatoires, en actualisant leur espérance. Et c'est fpp/absence-d-arbitrage, par son second point, qui dit que cette espérance est le prix forward. [ajout]

## Exemple minimal
L'action vaut 100 et le taux à un an 4 % : $E^{\mathbb Q}(S_1)=104{,}08$, même si les investisseurs attendent en moyenne 108,33. [ajout]

## Geste de calcul type
Prix d'un paiement aléatoire : espérance sous $\mathbb Q$, puis actualisation. Dans l'arbre de l'exemple, le droit de recevoir $(S_1-100)^+$ vaut $0{,}9608\times0{,}48\times30\approx13{,}88$. [Prop. 6, ajout]

## Cesse d'être valide quand
Le poly suppose qu'une telle règle de prix existe et qu'elle est linéaire ; il ne dit rien de son unicité. Avec des taux aléatoires, l'actualisation par $P(0,T)$ ne se sépare plus de l'espérance. [§5.1, ajout]
