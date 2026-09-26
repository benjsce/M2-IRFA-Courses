---
id: dss/lasso
nom: Lasso
symbole: $\ell_1$, $\ell_2$
type: notion
statut: source
cas_de: dss/regularisation
valeur: la norme $\ell_1$, somme des valeurs absolues des coefficients
construite_a_partir_de:
- dss/regression-ridge
alias:
- the lasso
- LASSO
refs:
- slide 62
- slide 63
- slide 64
- slide 65
- slide 66
- slide 67
---

## Ce que c'est
La régularisation avec une pénalité en valeur absolue, qui met certains coefficients exactement à zéro. [slide 63]

## Forme
$$\sum_{i=1}^{n}\Big(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\Big)^2+\lambda\sum_{j=1}^{p}|\beta_j|=\mathrm{RSS}+\lambda\sum_{j=1}^{p}|\beta_j|$$ [slide 63]

## Ce que les symboles modélisent
$\ell_1$ ne nomme pas la pénalité mais sa **forme** : la façon de mesurer la taille d'un vecteur de coefficients, ici par la somme des valeurs absolues. C'est cette forme, anguleuse en zéro, qui met des coefficients exactement à zéro au lieu de les en approcher. [slide 63]

## Ce qui la définit
Un seul terme change par rapport à ridge, et il change tout : la pénalité $\ell_1$ force certains coefficients à valoir exactement zéro dès que $\lambda$ est assez grand. Le lasso fait donc de la sélection de variables, ce que ridge ne fait jamais. [slide 63]

La raison est géométrique. Sous forme contrainte, la région du lasso est $\sum_j|\beta_j|\le s$, un losange à coins sur les axes ; celle de ridge est un disque. La solution est le premier point où une ellipse de RSS touche la région, et une ellipse touche un losange par un coin. [slide 65, slide 66]

![La même ellipse de RSS face aux deux régions. Elle touche le disque de ridge en un point de son bord où aucun coefficient n'est nul, et le losange du lasso en un coin, sur l'axe, où $\beta_2=0$. L'ellipse est choisie pour le dessin ; les points de contact sont calculés.](figures/lasso.svg) [ajout]

## Le chemin jusqu'ici
Le chemin passe par dss/apprentissage-supervise et dss/moindres-carres-ordinaires d'un côté, dss/erreur-de-test et dss/compromis-biais-variance de l'autre, qui se rejoignent dans dss/regression-ridge. [ajout]

Le lasso ne se comprend que contre ridge : le cours l'introduit en énonçant ce que ridge ne fait pas, mettre un coefficient exactement à zéro. C'est pourquoi il en dépend directement au lieu de repartir des moindres carrés. [ajout]

## Exemple minimal
Sur les données Credit, quand $\lambda$ croît, les coefficients d'Income, Limit, Rating et Student tombent à zéro l'un après l'autre, et non progressivement. [slide 64]

## Geste de calcul type
Le comparer à ridge par validation croisée sur le même jeu : le cours ne tranche pas a priori entre les deux, il dit de mesurer. [slide 67]

## Cesse d'être valide quand
Il n'est pas uniformément meilleur : il produit des modèles plus simples et plus interprétables, et se comporte qualitativement comme ridge quant au biais et à la variance. Lequel prédit le mieux dépend du jeu de données. [slide 67]
