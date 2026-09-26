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

Ce critère est minimal, prédicteurs standardisés et réponse centrée, en $\hat\beta^{\text{ridge}}=(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$. [slide 57]

## Ce que les symboles modélisent
$\lambda$, positif ou nul, règle la force de la pénalité : à zéro on retrouve les moindres carrés, très grand on écrase tous les coefficients vers zéro. [slide 49, slide 50, slide 51]

$\ell_2$ nomme la forme de la pénalité, la somme des carrés. Elle est lisse en zéro : sa pente y est nulle, donc rien ne pousse un petit coefficient jusqu'à zéro exactement. [slide 63, ajout]

$\mathbf{X}$ est la matrice $n\times p$ des prédicteurs standardisés, une ligne par observation, $\mathbf{y}$ la colonne des réponses centrées, $\mathbf{I}$ l'identité $p\times p$. Une fois tout centré, $\beta_0$ disparaît : il vaut la moyenne de la réponse. [slide 52, slide 57, ajout]

## Ce qui la définit
On connaît les coefficients des moindres carrés : ils ajustent au mieux les données d'apprentissage, mais changent beaucoup d'un échantillon à l'autre. On cherche des coefficients un peu biaisés et plus stables. Ridge les obtient en ajoutant une constante positive à la diagonale de $\mathbf{X}^T\mathbf{X}$ avant de l'inverser. [slide 53, slide 57]

Cette constante rend le problème non singulier : ridge a encore une solution unique quand $p>n$, là où les moindres carrés n'en ont plus. [slide 56, slide 57]

Les moindres carrés ne dépendent pas de l'échelle des prédicteurs, ridge si : multiplier un prédicteur par une constante change la solution. D'où la standardisation préalable. [slide 52]

Pour un $\lambda$ donné, un seul ajustement suffit, là où le meilleur sous-ensemble en demande un nombre exponentiel. Et sous forme contrainte, $\sum_j\beta_j^2\le t$, la région est une boule sans coin : c'est la raison géométrique pour laquelle aucun coefficient n'atteint exactement zéro. [slide 49, slide 56, slide 66]

## Le chemin jusqu'ici
Ridge modifie une fonction et une seule : la somme des carrés des erreurs que dss/moindres-carres-ordinaires rend minimale, pour ajuster au mieux les couples observés de dss/apprentissage-supervise. [ajout]

La raison de la modifier vient de dss/compromis-biais-variance : l'erreur que mesure dss/erreur-de-test, sur des données non vues, additionne le carré du biais, la variance et un bruit irréductible, et un peu de biais peut acheter beaucoup de variance. Sans ce compromis, ajouter du biais serait une dégradation pure. [ajout]

## Exemple minimal
Sur les 20 clients, prédicteurs standardisés : à $\lambda$ presque nul, l'endettement et le revenu ont leurs coefficients des moindres carrés, 0,86 et −0,80 ; à $\lambda=10$, 0,40 et −0,40 ; à $\lambda=10\,000$, tous les coefficients valent moins de 0,002. [ajout]

![Les coefficients standardisés des 20 clients quand $\lambda$ grandit, sur une échelle logarithmique. À gauche, ceux des moindres carrés ; à droite, tous tendent vers zéro, le modèle nul, sans l'atteindre. Ils ne rétrécissent pas au même rythme : celui de x3, la variable sans lien que le hasard a liée à la perte, grandit d'abord, puis rejoint celui de l'endettement.](figures/regression-ridge.svg) [ajout]

## Geste de calcul type
Standardiser les prédicteurs, choisir une grille de $\lambda$, résoudre $(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$ pour chacun, puis trancher par validation croisée. [slide 52, slide 57, slide 68]

## Cesse d'être valide quand
La pénalité ne force jamais un coefficient à valoir exactement zéro : le modèle final contient les $p$ prédicteurs, ce qui pose un problème d'interprétation. [slide 62]

Et le rétrécissement ne paie que si les moindres carrés ont une forte variance. Sur les 20 clients, il ne paie pas : l'erreur mesurée sur 20 000 clients nouveaux vaut 1,83 à $\lambda=0$, 2,00 à $\lambda=1$ et 2,70 à $\lambda=10$. [slide 55, ajout]
