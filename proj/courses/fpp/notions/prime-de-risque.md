---
id: fpp/prime-de-risque
nom: Prime de risque
symbole: '$\pi_A$, $\pi_E$'
type: notion
statut: source
construite_a_partir_de:
- fpp/levier
alias:
- risk premium
- expected excess return
refs:
- Déf. 2
- §1.3
---

## Ce que c'est
Le rendement d’un actif au-delà de son coût de financement. [Déf. 2]

## Forme
$$\tilde\pi_E=l\times\tilde\pi_A,\qquad \pi_E=\mathbb{E}(\tilde\pi_E)=l\,\pi_A$$ [§1.3]

## Ce qui la définit
La moyenne prospective de cet excès est la prime de risque espérée ; le levier la multiplie exactement, comme il multiplie la volatilité. [Déf. 2, §1.3]

## Le chemin jusqu'ici
fpp/bilan pose l'identité, fpp/levier en tire le rapport actif sur capitaux propres. [ajout]

La prime de risque est ce que le levier multiplie. Deux notions suffisent parce qu'on reste dans l'identité comptable : rien ici ne suppose un modèle de marché, seulement que la dette est sans risque — et c'est exactement là que la fiche cessera d'être valide. [ajout]

## Exemple minimal
Une prime d’actif de 3 % avec un levier de 3,33 donne une prime sur capitaux propres de 10 %. [ajout]

## Geste de calcul type
Multiplier la prime de l’actif par le levier ; la même multiplication vaut pour l’écart type, donc le rapport prime sur volatilité est inchangé par le levier. [§1.3]

## Cesse d'être valide quand
La linéarité suppose la dette sans risque ; dès que la dette peut faire défaut, la relation cesse d’être exacte. [§1.4]
