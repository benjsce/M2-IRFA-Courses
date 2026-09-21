---
id: dup/crra
nom: CRRA
symbole: $\gamma$
type: notion
statut: source
cas_de: dup/famille-hara
valeur: une aversion relative constante
construite_a_partir_de:
- dup/fonction-utilite
alias:
- crra
refs:
- L1 slide 35
---

## Ce que c'est
L’utilité dont l’aversion relative $zA(z)$ ne dépend pas de la richesse. [L1 slide 35]

## Forme
$$u(z)=\dfrac{z^{1-\gamma}}{1-\gamma}\ \implies\ A(z)=\dfrac{\gamma}{z}$$ [L1 slide 35]

## Ce que les symboles modélisent
$\gamma$ est l'aversion **relative** : l'aversion absolue multipliée par la richesse, donc un nombre sans unité. La différence avec le coefficient de CARA est celle d'un pari libellé en euros et d'un pari libellé en pourcentage de fortune — $\gamma$ constant veut dire que l'agent voit les risques en proportion. [L1 slide 35]

## Ce qui la définit
C’est la forme que le cours retient pour toutes ses calibrations, parce que la prime y est proportionnelle à la richesse et donc exprimable en pourcentage. [L1 slide 35, L1 slide 36]

## Le chemin jusqu'ici
Rien d'autre au socle que dup/fonction-utilite. [ajout]

Comme CARA, c'est une contrainte sur la forme de $U$, posée avant toute loterie. La différence tient au fait qu'on normalise par la richesse au lieu de la laisser hors du calcul : c'est ce qui rend CRRA naturelle dès qu'on raisonne en rendements plutôt qu'en montants. [ajout]

## Exemple minimal
Avec $\gamma=4$ et un pari de $\pm30\,\%$ de la richesse à pile ou face : la prime vaut $16{,}0\,\%$. [L1 slide 37]

## Geste de calcul type
Poser l’équation $u(100(1-\pi))=\tfrac12u(100(1-\alpha))+\tfrac12u(100(1+\alpha))$ et résoudre en $\pi$ : c’est ainsi que le cours estime $\gamma$ sur une réponse individuelle. [L1 slide 36]

## Cesse d'être valide quand
Elle est DARA, ce qui est souhaité, mais impose l’aversion relative constante, ce qui est une hypothèse forte et démentie par la comparaison des échelles de risque. [L1 slide 34, L2 slide 33]
