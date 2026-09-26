---
id: dss/fonction-discriminante-lineaire
nom: Fonction discriminante linéaire
type: notion
statut: source
construite_a_partir_de:
- dss/apprentissage-inductif
alias:
- linear discriminate function
refs:
- slide 134
- slide 135
- slide 136
- slide 146
---

## Ce que c'est
La fonction linéaire des attributs dont le signe range un exemple dans l'une de deux classes ; elle s'annule sur l'hyperplan qui les sépare. [slide 135]

## Forme
$$f(X)=w_0+w_1x_1+w_2x_2=0,\qquad f>0\Rightarrow A,\quad f<0\Rightarrow B$$ [slide 135]

## Ce que les symboles modélisent
$f$ prend un exemple, le point $X$ de coordonnées $x_1$ et $x_2$ dans l'espace des attributs, et rend un nombre réel dont seul le signe sert : positif, l'exemple va dans la classe $A$ ; négatif, dans la classe $B$. Sa valeur n'est pas une probabilité d'appartenance, et la frontière est l'ensemble des points où elle s'annule. [slide 135, ajout]

$x_1$ et $x_2$ sont deux attributs mesurés sur chaque exemple ; sur la slide, l'âge et la taille. $w_1$ et $w_2$ fixent l'orientation de la frontière, $w_0$ la déplace sans la tourner. Ces trois poids sont les inconnues que l'apprentissage doit trouver. [slide 135, slide 136, ajout]

La lettre $f$ change de sens d'une page à l'autre du cours, sans que la source le signale : ailleurs, elle désigne la fonction inconnue qu'on cherche à approcher, ou la fonction d'activation d'un neurone. Ici, c'est la fonction discriminante. [ajout]

## Ce qui la définit
Chaque exemple est un point de l'espace des attributs, chaque classe un amas de points. La fonction range un point selon le signe qu'elle y prend. [slide 134, slide 135]

La difficulté est posée immédiatement, et c'est elle qui appelle l'apprentissage : la forme de la frontière est connue, les valeurs de $w_0$, $w_1$, $w_2$ ne le sont pas. [slide 136]

## Le chemin jusqu'ici
dss/apprentissage-supervise fournit des exemples dont la classe est connue. dss/apprentissage-inductif demande de se donner d'abord une famille d'hypothèses, puis d'y chercher la meilleure : la fonction discriminante linéaire est la famille la plus simple, et le cours la choisit pour pouvoir en montrer aussitôt les limites. [ajout]

## Exemple minimal
Avec $w_0=-1$, $w_1=1$ et $w_2=1$, la frontière est la droite $x_1+x_2=1$ et l'ordonnée à l'origine vaut $-w_0/w_2=1$. [slide 135]

![La droite de l'exemple, $x_1+x_2=1$, qui coupe l'axe vertical en $-w_0/w_2=1$. D'un côté $f>0$ et le point va dans la classe A ; de l'autre $f<0$, classe B.](figures/fonction-discriminante-lineaire.svg) [ajout]

## Geste de calcul type
Pour classer un point, calculer $f$ et lire son signe. Avec les poids de l'exemple, le point $(1,1)$ donne $f=-1+1+1=1>0$, classe $A$ ; le point $(0{,}2\,;\,0{,}3)$ donne $f=-0{,}5<0$, classe $B$. [ajout]

## Cesse d'être valide quand
Elle ne sépare que des classes linéairement séparables ; la plupart des fonctions ne le sont pas. [slide 148]
