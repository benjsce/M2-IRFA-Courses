---
id: fpp/levier
nom: Levier
symbole: $l_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/bilan
alias:
- leverage
refs:
- Déf. 1
- §1.3
---

## Ce que c'est
Le rapport entre l’actif et les capitaux propres. [Déf. 1]

## Forme
$$l_t\equiv\dfrac{A_t}{E_t}$$ [Déf. 1]

## Ce que les symboles modélisent
$l_t$ est un rapport entre deux montants du bilan, sans unité. Ce n'est pas un taux d'endettement au sens courant : il vaut un quand il n'y a aucune dette, et croît sans borne à mesure que les capitaux propres s'amenuisent. [Déf. 1]

## Ce qui la définit
Il amplifie exactement, et linéairement, l’écart de rendement entre l’actif et la dette : $\frac{\Delta E_t}{E_t}-\frac{\Delta D_t}{D_t}=l_t\big(\frac{\Delta A_t}{A_t}-\frac{\Delta D_t}{D_t}\big)$. [§1.3]

## Le chemin jusqu'ici
Tout repose sur fpp/bilan, et sur son identité actif = capitaux propres + dette. [ajout]

Le levier n'ajoute aucune hypothèse : c'est un rapport entre deux termes de cette identité. Tout ce qu'il dira ensuite — amplification de la prime, de la volatilité, seuil de faillite — se déduit de l'identité comptable, pas d'un modèle. [ajout]

## Exemple minimal
Un actif de 100 sur 30 de capitaux propres : $l=3{,}33$. [ajout]

## Geste de calcul type
Pour lire l’effet du levier, écrire l’excès de rendement des capitaux propres sur la dette comme $l$ fois l’excès de rendement de l’actif sur la dette — c’est une identité, pas une hypothèse. [§1.3]

## Cesse d'être valide quand
L’amplification est symétrique : elle joue autant à la baisse, et c’est la responsabilité limitée qui en borne l’effet. [§1.4]

## Origine
- exercice fpp/ex-16 : **collision de symbole entre les deux documents du cours.** Le poly pose $l_t=A_t/E_t\in[1,\infty)$ (Déf. 1) ; le livre d'exercices pose $l=D/F_T\in[0,1]$. Même lettre, même mot. Voir `notation.yml`, section collisions [exo. 16]
