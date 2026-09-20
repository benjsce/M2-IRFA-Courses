---
id: fpp/volatilite
nom: Volatilité
symbole: '$\sigma$, $\sigma_A$'
type: notion
statut: source
construite_a_partir_de: []
alias:
- volatility
refs:
- Déf. 2
---

## Ce que c'est
L’écart type du rendement d’un actif. [Déf. 2]

## Forme
$$\sigma_E=\mathrm{stdev}(\tilde\pi_E)=l\,\sigma_A$$ [§1.3]

## Ce qui la définit
C’est la seule mesure de dispersion que le cours retient, et elle est amplifiée par le levier exactement comme la prime. [Déf. 2, §1.3]

## Exemple minimal
Une volatilité d’actif de 6 % avec un levier de 3,33 donne 20 % sur les capitaux propres. [ajout]

## Geste de calcul type
En temps continu, la volatilité porte une dimension $T^{-1/2}$ : une volatilité annuelle de 20 % vaut $20/\sqrt{12}=5{,}8\,\%$ par mois. [§5.3]

## Cesse d'être valide quand
Elle ne décrit complètement le risque que si le rendement est gaussien ; sinon elle ignore l’asymétrie et les queues. [ajout]
