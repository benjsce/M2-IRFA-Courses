---
id: dup/aversion-a-la-deception-generalisee
nom: Aversion à la déception généralisée
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-a-la-deception
alias:
- generalized disappointment aversion
- Routledge et Zin
refs:
- L3 slide 12
---

## Ce que c'est
La déception ne commence qu’en dessous d’une fraction de l’équivalent certain, et non à l’équivalent certain lui-même. [L3 slide 12]

## Forme
$$u\big(c(P)\big)=\mathbb{E}_P[u(x)]-\theta\,\mathbb{E}_P\big[\big(u(\delta c(P))-u(x)\big)_+\big],\qquad \theta\ge0,\ \delta\in(0,1]$$ [L3 slide 12]

## Ce qui la définit
Deux paramètres séparent ce que le modèle de Gul confondait : $\theta$ dit la force de la pénalité, $\delta$ dit à partir d’où elle s’applique. [L3 slide 12]

Avec $\delta<1$, seuls les résultats suffisamment mauvais déclenchent la pénalité : l’aversion se concentre sur la queue basse. [L3 slide 12]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite se combinent en dup/utilite-esperee, dont on tire dup/equivalent-certain — sans équivalent certain, aucun seuil de déception n'est définissable. dup/aversion-a-la-deception place ce seuil exactement à l'équivalent certain. [ajout]

La généralisation tient en un paramètre : le seuil de déception n'est plus l'équivalent certain lui-même mais une fraction de celui-ci. Il fallait donc la version à seuil fixe avant de pouvoir le faire glisser. C'est ce paramètre libre qui permettra d'accommoder l'aversion du premier ordre. [ajout]

## Exemple minimal
$\delta=1$ redonne le modèle de Gul, $\theta=0$ redonne l’utilité espérée. [L3 slide 12]

## Geste de calcul type
Fixer $\delta$, poser le seuil à $\delta c(P)$, et résoudre le point fixe comme pour Gul — le seuil est simplement déplacé. [L3 slide 12]

## Cesse d'être valide quand
Reste dans la classe d’intermédiarité de Chew-Dekel, avec les restrictions adaptées au seuil ; l’indépendance complète n’y est pas imposée. [L3 slide 12]
