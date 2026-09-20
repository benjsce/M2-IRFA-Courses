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

## Ce qui la définit
Il amplifie exactement, et linéairement, l’écart de rendement entre l’actif et la dette : $\frac{\Delta E_t}{E_t}-\frac{\Delta D_t}{D_t}=l_t\big(\frac{\Delta A_t}{A_t}-\frac{\Delta D_t}{D_t}\big)$. [§1.3]

## Exemple minimal
Un actif de 100 sur 30 de capitaux propres : $l=3{,}33$. [ajout]

## Geste de calcul type
Pour lire l’effet du levier, écrire l’excès de rendement des capitaux propres sur la dette comme $l$ fois l’excès de rendement de l’actif sur la dette — c’est une identité, pas une hypothèse. [§1.3]

## Cesse d'être valide quand
L’amplification est symétrique : elle joue autant à la baisse, et c’est la responsabilité limitée qui en borne l’effet. [§1.4]
