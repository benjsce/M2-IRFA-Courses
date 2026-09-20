---
id: dup/ordre-concave
nom: Ordre concave
symbole: $F^*$
type: notion
statut: source
cas_de: dup/accroissement-de-risque
valeur: l’unanimité des agents concaves, énoncée sur l’intégrale
construite_a_partir_de:
- dup/aversion-au-risque
alias:
- concave order
- Definition A
refs:
- L1 slide 19
---

## Ce que c'est
À moyennes égales, $F^*$ est plus risquée que $F$ si tout agent averse au risque préfère $F$. [L1 slide 19]

## Forme
$$\int U(x)\,dF^*(x)\ \le\ \int U(x)\,dF(x)\qquad\text{pour toute }U\text{ concave}$$ [L1 slide 19]

## Ce qui la définit
Le critère est unanime : il ne retient que ce sur quoi tous les agents averses s’accordent, ce qui explique qu’il ne classe pas toute paire. [L1 slide 19]

## Le chemin jusqu'ici
Le socle commun mène à dup/aversion-au-risque, et c'est elle la clé. [ajout]

L'ordre concave ne dit pas « plus risqué selon moi » mais « plus risqué **selon tout agent averse** ». Il fallait donc disposer de l'aversion au risque comme classe d'agents, pas comme préférence individuelle. C'est un ordre partiel : à moyennes égales, beaucoup de paires restent incomparables, et c'est le prix de l'unanimité. [ajout]

## Exemple minimal
$\tilde y$ uniforme sur $\{20,40,60,80\}$ est plus risquée, au sens concave, que $\tilde x$ uniforme sur $\{40,60\}$, de même moyenne 50. [L1 slide 24]

## Geste de calcul type
Vérifier d’abord l’égalité des moyennes, sans quoi la définition ne s’applique pas. Puis, plutôt que de tester toutes les $U$ concaves, utiliser l’une des trois autres caractérisations : elles sont équivalentes. [L1 slide 19, L1 slide 23]

## Cesse d'être valide quand
À moyennes égales il coïncide avec la dominance stochastique du second ordre dans le bon sens ; à moyennes différentes l’énoncé ne s’applique pas tel quel. [L1 slide 19]
