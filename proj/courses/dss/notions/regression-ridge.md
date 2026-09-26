---
id: dss/regression-ridge
nom: Régression ridge
symbole: $\lambda$
type: notion
statut: source
cas_de: dss/regularisation
valeur: la norme $\ell_2$, somme des carrés des coefficients
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/compromis-biais-variance
alias:
- ridge regression
refs:
- slide 48
- slide 49
- slide 50
- slide 51
- slide 52
- slide 56
- slide 57
---

## Ce que c'est
Les moindres carrés avec une pénalité proportionnelle à la somme des carrés des coefficients. [slide 48]

## Forme
$$\sum_{i=1}^{n}\Big(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\Big)^2+\lambda\sum_{j=1}^{p}\beta_j^2=\mathrm{RSS}+\lambda\sum_{j=1}^{p}\beta_j^2$$ [slide 48]

$$\hat\beta^{\text{ridge}}=(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$$ [slide 57]

## Ce que les symboles modélisent
$\lambda$ règle la force de la pénalité et décide seul du compromis : à zéro on retrouve les moindres carrés, très grand on écrase tous les coefficients. $\ell_2$ en nomme la forme, la somme des carrés — arrondie en zéro, elle rapproche les coefficients de zéro sans jamais les y poser. [slide 50, slide 63]

## Ce qui la définit
La forme matricielle dit tout : on ajoute une constante positive à la diagonale de $\mathbf{X}^T\mathbf{X}$ avant de l'inverser, ce qui rend le problème non singulier. C'est pourquoi la méthode fonctionne encore quand $p>n$, cas où les moindres carrés n'ont même pas de solution unique. [slide 56, slide 57]

Écriture équivalente sous contrainte : minimiser la RSS sous $\sum_j\beta_j^2\le t$. La région de contrainte est une boule, sans coin, et c'est la raison géométrique pour laquelle aucun coefficient n'atteint exactement zéro. [slide 49, slide 66]

Les estimateurs des moindres carrés sont équivariants par changement d'échelle, ceux de ridge ne le sont pas : multiplier un prédicteur par une constante change la solution. D'où la standardisation préalable. [slide 52]

Un seul ajustement suffit pour un $\lambda$ donné, là où le meilleur sous-ensemble en demande un nombre exponentiel. [slide 56]


## Le chemin jusqu'ici
Deux fils. dss/apprentissage-supervise donne dss/moindres-carres-ordinaires, la fonction à modifier ; dss/erreur-de-test donne dss/compromis-biais-variance, la raison de la modifier. [ajout]

Ridge est l'addition d'un seul terme à la première, justifiée par le second. Sans le compromis, ajouter du biais serait une dégradation pure et personne n'y verrait un progrès. [ajout]

## Exemple minimal
À $\lambda=0$ la solution est celle des moindres carrés ; quand $\lambda$ devient très grand, tous les coefficients standardisés sont proches de zéro, ce qui est le modèle nul. [slide 51]

![Les coefficients standardisés des 20 clients quand $\lambda$ grandit, sur une échelle logarithmique. À gauche, ceux des moindres carrés ; à droite, tous tendent vers zéro sans l'atteindre. Les trois variables sans lien ne partent pas de zéro : sur 20 clients, le hasard leur donne un coefficient, que la pénalité réduit comme les autres.](figures/regression-ridge.svg) [ajout]

## Geste de calcul type
Standardiser les prédicteurs, choisir une grille de $\lambda$, résoudre $(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$ pour chacun, puis trancher par validation croisée. [slide 52, slide 57, slide 68]

## Cesse d'être valide quand
La pénalité ne force jamais un coefficient à valoir exactement zéro : le modèle final contient les $p$ prédicteurs, ce qui pose un problème d'interprétation. [slide 62]
