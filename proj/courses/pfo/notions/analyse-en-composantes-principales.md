---
id: pfo/analyse-en-composantes-principales
nom: Analyse en composantes principales
symbole: '$\lambda_k$, $V_k$'
type: notion
statut: source
construite_a_partir_de:
- pfo/matrice-de-covariance
alias:
- ACP
- PCA
- principal component analysis
- variance expliquée
- explained variance ratio
- diagonalisation de la covariance
refs:
- §4.2.3
- p. 60
- p. 61
- p. 63
- p. 70
---

## Ce que c'est
La diagonalisation de la matrice de covariance des rendements, qui en tire les directions de plus grande variance commune et la part de variance que porte chacune. [§4.2.3, p. 60]

## Forme
$$\boldsymbol{\Sigma}\,V_k=\lambda_k\,V_k,\qquad \text{part de la composante }k=\frac{\lambda_k}{\sum_{j=1}^{N}\lambda_j}$$ [p. 60, p. 61]

## Ce que les symboles modélisent
$V_k$ est un vecteur propre de $\boldsymbol{\Sigma}$, de norme un : une direction dans l'espace des rendements, qui dit dans quelle proportion chaque actif entre dans la composante $k$. $\lambda_k$ est la valeur propre associée, la variance des rendements le long de cette direction ; leur somme est la variance totale des $N$ actifs. [p. 60, p. 61]

## Ce qui la définit
**Connue** : la matrice de covariance des rendements. **Cherchées** : les directions que la matrice étire sans les tourner, et de combien. La première est celle de plus grande variance ; la deuxième, la plus grande variance restante, orthogonale à la première ; et ainsi de suite. [p. 60, p. 61]

![Deux actifs de volatilités journalières 1 % et 2 %, corrélés à 0,5, annualisées : l'ellipse d'un écart type. Σ étire V_1 = (0,29 ; 0,96) de λ_1 = 0,108 et V_2 de λ_2 = 0,018 sans les tourner : ce sont les axes du nuage, et V_1 porte 86 % de la variance. Une direction quelconque u ressort tournée. Dessous, la Forme : Σ V_k = λ_k V_k, et la part de V_k est λ_k / Σ_j λ_j.](figures/analyse-en-composantes-principales.svg) [ajout]

C'est une méthode statistique descriptive, non paramétrique : à la différence du MEDAF ou du modèle de Fama et French, elle n'impose aucun facteur défini à l'avance par une théorie économique. Elle cherche seulement les directions qui expliquent le plus de variance dans les rendements observés. [§4.2.3, p. 61]

En Python, `PCA(n_components=k)` de `sklearn.decomposition` fixe le nombre de composantes gardées ; `.fit()` centre les rendements, extrait les axes par une décomposition en valeurs singulières et les range par valeur propre décroissante ; `explained_variance_ratio_` donne les parts. [p. 63, p. 70]

## Le chemin jusqu'ici
Tout part de pfo/matrice-de-covariance, la seule donnée que l'analyse consulte : ses vecteurs propres sont les composantes, ses valeurs propres leurs variances. Elle est faite de rendements de pfo/rendement-logarithmique dans l'exemple, porte le carré de fpp/volatilite sur sa diagonale, et fpp/echelonnement-de-la-variance l'annualise sans changer ses directions propres, puisqu'il multiplie toute la matrice par le même nombre. [ajout]

## Exemple minimal
Pour la matrice annualisée $\begin{pmatrix}0{,}0252&0{,}0252\\0{,}0252&0{,}1008\end{pmatrix}$, les valeurs propres sont 0,108 et 0,018 : la première composante porte 86 % de la variance totale. [ajout]

## Geste de calcul type
Pour une matrice $2\times2$ de termes $a$, $c$, $d$ : $\lambda=\tfrac12\big(a+d\pm\sqrt{(a-d)^2+4c^2}\big)$. Ici $a+d=0{,}126$ et $\sqrt{0{,}0756^2+4\times0{,}0252^2}=0{,}0909$, d'où $\lambda_1=0{,}1084$ et $\lambda_2=0{,}0176$, et $0{,}1084/0{,}126=86\,\%$. Le vecteur propre $V_1$ est proportionnel à $(c\,;\lambda_1-a)=(0{,}0252\,;0{,}0832)$, soit $(0{,}29\,;0{,}96)$ une fois normé. [ajout]

## Cesse d'être valide quand
Sur la matrice de covariance, la première composante suit surtout l'actif le plus volatil : ici 0,96 sur le second contre 0,29 sur le premier. Sur les rendements standardisés, c'est-à-dire sur la matrice de corrélation, les deux actifs pèsent autant, 0,71 chacun, et la première composante ne porte plus que 75 % de la variance. Le cours fait l'un et l'autre : le script ne standardise pas, l'exercice 2 dit la standardisation obligatoire. [p. 70, p. 74, ajout]

L'analyse ne voit que des covariances, donc des relations linéaires, et la variance d'une composante n'en dit pas le sens économique. [p. 62, ajout]

## Origine
- exercice pfo/ex-06 : sur quatre actifs mus par un facteur commun et standardisés, la première composante porte 81 % de la variance [p. 74, ajout]
- exercice pfo/ex-09 : trois composantes sur huit actions, 2021–2025 [p. 88]
