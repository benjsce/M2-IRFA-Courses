---
id: dup/diversification
nom: Diversification
symbole: $\sigma_p$
type: notion
statut: source
construite_a_partir_de:
- dup/moyenne-variance
alias:
- diversification
- two risky assets
refs:
- L1 slide 13
---

## Ce que c'est
Combiner deux actifs risqués peut réduire l’écart type du portefeuille au-dessous de celui de chacun. [L1 slide 13]

## Forme
$$\sigma_p^2=a^2\sigma_1^2+(1-a)^2\sigma_2^2+2a(1-a)\,\mathrm{Cov}(\tilde r_1,\tilde r_2)$$ [L1 slide 13]

## Ce que les symboles modélisent
$\sigma_p$ est l'écart type du portefeuille entier, et non la somme de ceux des titres qui le composent. Toute la notion tient dans cette différence : la mesure porte sur le total, et le total peut être moins dispersé que chacune de ses parties. [L1 slide 13]

## Ce qui la définit
C’est la covariance, et non les variances, qui décide de la forme de l’ensemble atteignable dans le plan écart type-moyenne. [L1 slide 13]

## Le chemin jusqu'ici
Le socle s'arrête à dup/loterie et à sa réduction, dup/moyenne-variance. [ajout]

La diversification est un fait sur les deux nombres du résumé, pas sur les préférences : l'écart type d'un mélange peut tomber sous celui de ses composants dès que la corrélation est inférieure à un. Aucune utilité n'apparaît dans le socle, et c'est ce qui rend le résultat si général. [ajout]

## Exemple minimal
Deux actifs à $\sigma=20\%$, de covariance nulle, à parts égales : $\sigma_p=14{,}1\%$. [ajout]

## Geste de calcul type
Calculer $\sigma_p^2$ par la formule à trois termes, puis faire varier $a$ : le minimum de variance se trouve là où la dérivée s’annule, et il est d’autant plus bas que la covariance est faible. [L1 slide 13]

## Cesse d'être valide quand
Le gain disparaît quand les deux actifs sont parfaitement corrélés : l’écart type est alors la moyenne pondérée des écarts types. [ajout]
