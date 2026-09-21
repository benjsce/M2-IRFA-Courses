---
id: dup/moyenne-variance
nom: Analyse moyenne-variance
symbole: '$\mu$, $\sigma$'
type: notion
statut: source
construite_a_partir_de:
- dup/loterie
alias:
- mean-variance
- analyse moyenne-écart type
refs:
- L1 slide 11
---

## Ce que c'est
Représenter une perspective par deux nombres seulement, sa moyenne et son écart type. [L1 slide 11]

## Forme
$$\sigma^2=\mathrm{Var}(\tilde x)=\mathbb{E}\big[(\tilde x-\mathbb{E}\tilde x)^2\big],\qquad \sigma=\sqrt{\mathrm{Var}(\tilde x)}$$ [L1 slide 11]

## Ce que les symboles modélisent
$\tilde x$ est une richesse aléatoire, et le tilde marque qu'on parle du tirage et non de sa valeur. $\mu$ et $\sigma$ en sont les deux premiers moments, et la notion consiste précisément à ne garder que ceux-là : tout ce que la loi contient au-delà est jeté. [L1 slide 6, L1 slide 11]

## Ce qui la définit
Un avantage et un coût : les moments d’un portefeuille se calculent facilement, mais la réduction jette de l’information que l’utilité espérée, elle, utilise. [L1 slide 11]

## Le chemin jusqu'ici
Une seule notion précède celle-ci : dup/loterie. [ajout]

Résumer une distribution à deux nombres est une réduction faite sur la loterie elle-même, avant toute préférence. C'est pourquoi le socle est si court — et aussi pourquoi la critique viendra de loin : la question n'est pas de savoir si le résumé est calculable, mais si un agent peut légitimement s'y fier. [ajout]

## Exemple minimal
Le pari $(0,\tfrac12;100,\tfrac12)$ a $\mu=50$ et $\sigma=50$. [ajout]

## Geste de calcul type
Réduire chaque perspective à $(\mu,\sigma)$, puis les placer dans le plan. Avant de conclure, vérifier que la réduction est licite : elle ne l’est que sous utilité quadratique ou restriction des distributions. [L1 slide 11, L1 slide 14]

## Cesse d'être valide quand
Exacte seulement sous utilité quadratique ou sous restriction des distributions ; sinon elle peut déclarer indifférentes deux distributions dont l’une domine l’autre. [L1 slide 14, L1 slide 16]
