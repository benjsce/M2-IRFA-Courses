---
id: dup/utilite-esperee-subjective
nom: Utilité espérée subjective
type: notion
statut: source
cas_de: dup/separation-gouts-croyances
construite_a_partir_de:
- dup/acte
- dup/fonction-utilite
alias:
- SEU
- subjective expected utility
- Savage
refs:
- L1 slide 59
---

## Ce que c'est
La valeur d’un acte est l’espérance de l’utilité de ses conséquences sous une probabilité déduite des choix. [L1 slide 59]

## Forme
$$V(f)=\sum_{s\in S}\pi(s)\,U\big(f(s)\big)$$ [L1 slide 59]

## Ce que les symboles modélisent
$f$ est un acte : il associe à chaque état $s$ de $S$ une conséquence $f(s)$. $U$ prend une conséquence et rend son utilité, la même quel que soit l'état. $\pi(s)$ est la probabilité que l'agent attribue à l'état $s$ ; elle se déduit de ses choix, et n'est pas une fréquence donnée avec le problème. [L1 slide 59, ajout]

## Ce qui la définit
Deux objets sont inférés en même temps et à partir de la même donnée : $U$ représente les goûts, $\pi$ les croyances. Aucun des deux n’est supposé observable. [L1 slide 59]

C’est l’aboutissement de la séparation : Savage construit les probabilités à partir de préférences cohérentes sur les actes, au lieu de les postuler. [L1 slide 59]

## Le chemin jusqu'ici
dup/acte fournit l'objet — une conséquence par état du monde — et dup/fonction-utilite l'évaluation de ces conséquences. [ajout]

Remarquez ce qui **n'est pas** dans le socle : la probabilité. C'est tout le point de Savage. Elle n'est pas donnée avec le problème, elle se **déduit** des choix de l'agent. La loterie, elle, l'aurait fournie d'emblée — d'où des fiches distinctes pour deux constructions qui aboutissent à la même formule. [ajout]

## Exemple minimal
Un acte qui paie 100 si la boule est rouge et 0 sinon vaut $\pi(R)\,U(100)+(1-\pi(R))\,U(0)$. [ajout]

## Geste de calcul type
Pour tester si des choix admettent une représentation subjective, chercher une probabilité unique qui les rationalise tous : c’est ce que le paradoxe d’Ellsberg rend impossible. [L1 slide 63]

## Cesse d'être valide quand
Elle suppose une probabilité additive unique, et des goûts qui ne dépendent pas de l’état. Les deux hypothèses tombent, l’une chez Ellsberg, l’autre avec l’utilité dépendante de l’état. [L1 slide 61, L1 slide 63]
