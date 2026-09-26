---
id: dup/utilite-logarithmique
nom: Utilité logarithmique
type: notion
statut: source
cas_de: dup/famille-hara
valeur: le cas $\gamma=1$ de CRRA
construite_a_partir_de:
- dup/fonction-utilite
alias:
- utilité logarithmique
refs:
- L1 slide 35
---

## Ce que c'est
Le cas limite de CRRA quand l’aversion relative vaut un. [L1 slide 35]

## Forme
$$u(z)=\ln z\ \implies\ A(z)=\dfrac{1}{z}$$ [L1 slide 35]

## Ce que les symboles modélisent
$z$ est un niveau de richesse, strictement positif pour que $\ln$, le logarithme népérien, soit défini. $A(z)$ rend l'aversion absolue à cette richesse ; elle est inversement proportionnelle à $z$, de sorte que l'aversion relative ne dépend pas de la richesse. [L1 slide 35, ajout]

## Ce qui la définit
Elle sert de référence dans tout le cours : DARA, aversion relative égale à un, et une prime qui se calcule à la main. [L1 slide 35, ajout]

## Le chemin jusqu'ici
Elle ne suppose que dup/fonction-utilite. [ajout]

Elle se définit directement, sans passer par CRRA — c'est un choix de grain, pas un oubli : le logarithme est le cas limite quand l'aversion relative vaut un, et un cas limite s'obtient par passage à la limite, non par instanciation. Le lien avec CRRA est une propriété, pas une dépendance. [ajout]

## Exemple minimal
À une richesse de 100 : $A=0{,}01$, et la prime d’un pari de $\pm10\,\%$ vaut $0{,}5\,\%$. [L1 slide 37]

## Geste de calcul type
Utiliser $A(z)=1/z$ dans l’approximation d’Arrow-Pratt : la prime relative vaut environ la moitié de la variance relative. [L1 slide 32]

## Cesse d'être valide quand
Elle n’est pas définie en zéro et y tend vers $-\infty$ : elle interdit la ruine, ce qui est une hypothèse de comportement, pas un fait. [ajout]
