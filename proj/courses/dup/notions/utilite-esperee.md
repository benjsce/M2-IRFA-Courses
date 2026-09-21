---
id: dup/utilite-esperee
nom: Utilité espérée
symbole: $V_{EU}$
type: notion
statut: source
cas_de: dup/axiome-independance
construite_a_partir_de:
- dup/loterie
- dup/fonction-utilite
alias:
- expected utility
- EU
- von Neumann-Morgenstern
refs:
- L1 slide 3
- L1 slide 4
- L1 slide 6
---

## Ce que c'est
La valeur d’une loterie est la moyenne des utilités de ses résultats, pondérée par leurs probabilités. [L1 slide 3]

## Forme
$$V_{\mathrm{EU}}(P)=\sum_{i=1}^{n}p_i\,u(x_i),\qquad V(F)=\mathbb{E}[U(\tilde x)]=\int U(x)\,dF(x)$$ [L1 slide 3, L1 slide 6]

## Ce que les symboles modélisent
$V_{EU}$ prend une loterie entière et rend un nombre : c'est une fonctionnelle, non une fonction de montant. La distinction avec $u$ est celle du tout et de la partie — $u$ évalue un résultat, $V_{EU}$ évalue la distribution qui les porte tous. [L1 slide 3]

## Ce qui la définit
Les probabilités entrent linéairement et l’utilité ne dépend que du résultat : c’est cette double séparation qui donne au modèle ses prédictions tranchées. [L1 slide 3]

Une relation de préférence sur $\Delta(X)$ admet cette représentation si et seulement si elle est complète, transitive, continue en mélange et indépendante. [L1 slide 4]

## Le chemin jusqu'ici
Deux objets suffisent, et ils ne se parlent pas encore. dup/loterie décrit **ce qui peut arriver** : des gains, et les probabilités qu'on leur associe. dup/fonction-utilite décrit **ce que l'agent en pense** : une valeur attachée à chaque gain. [ajout]

L'utilité espérée est la façon la plus simple de les faire se rencontrer — appliquer $U$ à chaque issue, puis pondérer par les probabilités. Tout le cours consiste ensuite à demander si cette façon-là est la bonne. [ajout]

## Exemple minimal
Avec $u(x)=\sqrt{x}$ et $P=(0,\tfrac12;100,\tfrac12)$ : $V_{\mathrm{EU}}(P)=5$. [ajout]

## Geste de calcul type
Calculer $\sum_i p_i u(x_i)$ pour chaque loterie et comparer les nombres obtenus ; c’est l’espérance des utilités qui classe, jamais l’espérance des gains. [ajout]

## Cesse d'être valide quand
Elle échoue là où l’indépendance échoue : effet de conséquence commune, effet de rapport commun, effet d’isolement. [L1 slide 45, L1 slide 47, L1 slide 48]
