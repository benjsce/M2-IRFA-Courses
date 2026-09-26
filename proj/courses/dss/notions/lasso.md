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
$\ell_1$ ne nomme pas la pénalité mais sa **forme** : la taille d'un vecteur de coefficients mesurée par la somme des valeurs absolues. Elle est anguleuse en zéro, et c'est ce coin qui pose des coefficients exactement à zéro au lieu de les en approcher. $\ell_2$, la somme des carrés, est la forme de la pénalité de ridge, lisse en zéro. [slide 63]

## Ce qui la définit
Un seul terme change par rapport à ridge, et il change tout : la pénalité $\ell_1$ force certains coefficients à valoir exactement zéro dès que $\lambda$ est assez grand. Le lasso fait donc de la sélection de variables, ce que ridge ne fait jamais. [slide 63]

La raison est géométrique. Sous forme contrainte, la région du lasso est $\sum_j|\beta_j|\le s$, un losange à coins sur les axes ; celle de ridge est un disque. La solution est le premier point où une ellipse de RSS touche la région, et une ellipse touche un losange par un coin. [slide 65, slide 66]

![Les mêmes courbes de niveau de la RSS dans les deux cadres, autour de l'estimation des moindres carrés. La solution est le point où la première d'entre elles, en partant du centre, touche la région, en noir : un point du bord du disque où aucun coefficient n'est nul, pour ridge ; un coin du losange, sur l'axe, où $\beta_2=0$, pour le lasso. Les ellipses sont choisies pour le dessin ; les points de contact sont calculés.](figures/lasso.svg) [ajout]

## Le chemin jusqu'ici
Le lasso reprend le critère de dss/regression-ridge et n'en change que la pénalité : le cours l'introduit en énonçant ce que ridge ne fait pas, mettre un coefficient exactement à zéro. C'est pourquoi il en dépend directement au lieu de repartir des moindres carrés. [ajout]

Il hérite donc de ridge tout le reste : la somme des carrés des erreurs de dss/moindres-carres-ordinaires, qui ajuste les couples observés de dss/apprentissage-supervise, et la raison de la pénaliser, dss/compromis-biais-variance, qui accepte un peu de biais pour faire baisser la variance et avec elle l'erreur que mesure dss/erreur-de-test. [ajout]

## Exemple minimal
Sur les 20 clients, prédicteurs standardisés, les coefficients rétrécissent quand $\lambda$ croît, puis s'annulent exactement, chacun à son $\lambda$ : x4 vers $\lambda=5$, le revenu vers 16, x5 vers 20, l'endettement vers 24, et x3, la variable sans lien que le hasard a liée à la perte, en dernier, vers 30. [ajout]

Le cours montre la même chose sur des données de crédit, où les coefficients du revenu, de la limite de crédit, de la note de crédit et du statut d'étudiant finissent tous à zéro exactement, à des $\lambda$ différents. [slide 64]

## Geste de calcul type
Le comparer à ridge par validation croisée sur le même jeu : le cours ne tranche pas a priori entre les deux, il dit de mesurer. [slide 67]

## Cesse d'être valide quand
Il n'est pas uniformément meilleur : il produit des modèles plus simples et plus interprétables, et se comporte qualitativement comme ridge quant au biais et à la variance. Lequel prédit le mieux dépend du jeu de données. [slide 67]

Et ce qu'il garde n'est pas forcément un vrai prédicteur : sur les 20 clients, le dernier coefficient non nul est celui de x3, sans lien avec la perte. Réglé par validation croisée, vers $\lambda=2{,}5$, il laisse l'erreur mesurée sur 20 000 clients nouveaux à 1,87, contre 1,83 pour les moindres carrés. [ajout]
