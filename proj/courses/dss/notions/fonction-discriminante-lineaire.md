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
L'hyperplan qui sépare deux classes dans l'espace des attributs. [slide 135]

## Forme
$$f(X)=w_0+w_1x_1+w_2x_2=0,\qquad f>0\Rightarrow A,\quad f<0\Rightarrow B$$ [slide 135]

## Ce qui la définit
Chaque exemple est un point de l'espace des attributs, chaque classe un amas de points. La fonction range un point selon le signe qu'elle y prend. [slide 134, slide 135]

La difficulté est posée immédiatement, et c'est elle qui appelle l'apprentissage : la forme de la frontière est connue, les valeurs de $w_0$, $w_1$, $w_2$ ne le sont pas. [slide 136]


## Le chemin jusqu'ici
dss/apprentissage-supervise, puis dss/apprentissage-inductif, qui pose la question de la famille d'hypothèses. [ajout]

La fonction discriminante linéaire est la réponse la plus simple à cette question, et le cours la choisit précisément pour pouvoir en montrer aussitôt les limites. [ajout]

## Exemple minimal
Avec $w_0=-1$, $w_1=1$ et $w_2=1$, la frontière est la droite $x_1+x_2=1$ et l'ordonnée à l'origine vaut $-w_0/w_2=1$. [slide 135]

![La droite de l'exemple, $x_1+x_2=1$, qui coupe l'axe vertical en $-w_0/w_2=1$. D'un côté $f>0$ et le point va dans la classe A ; de l'autre $f<0$, classe B.](figures/fonction-discriminante-lineaire.svg) [ajout]

## Geste de calcul type
Pour visualiser ce qu'un réseau a appris, tracer la frontière dans l'espace des attributs plutôt que de lire les poids : le cours y revient à chaque étape. [slide 146]

## Cesse d'être valide quand
Elle ne sépare que des classes linéairement séparables ; la plupart des fonctions ne le sont pas. [slide 148]
