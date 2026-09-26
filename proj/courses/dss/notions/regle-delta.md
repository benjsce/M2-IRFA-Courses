---
id: dss/regle-delta
nom: Règle delta
symbole: $\eta$
type: notion
statut: source
construite_a_partir_de:
- dss/perceptron
alias:
- delta rule
- Widrow-Hoff
refs:
- slide 144
- slide 145
---

## Ce que c'est
Corriger chaque poids proportionnellement à l'erreur commise et à l'entrée qui l'a produite. [slide 145]

## Forme
$$w_i(t+1)=w_i(t)+\Delta w_i,\qquad \Delta w_i=\eta\,d\,x_i(t),\qquad d=t-y$$ [slide 145]

## Ce que les symboles modélisent
$\eta$ est le taux d'apprentissage : la fraction de la correction qu'on applique réellement. Il vit dans $]0,1]$ et vaut typiquement 0,1 ; trop petit, l'apprentissage traîne, trop grand, il oscille sans se poser. Ce n'est pas un paramètre du modèle mais un paramètre de la marche vers le modèle. [slide 145]

$d$ est le signal d'erreur, la sortie désirée $t$ moins la sortie obtenue $y$ : il vaut 1, 0 ou $-1$ pour un neurone à seuil. $x_i$ est l'entrée que porte le poids $w_i$, avec $x_0=1$ pour le seuil. [slide 145, ajout]

La lettre $t$ sert deux fois dans la même ligne, et la slide l'écrit ainsi : dans $w_i(t+1)$ et $x_i(t)$, elle numérote les pas de l'apprentissage ; dans $d=t-y$, elle est la sortie désirée, la cible. [slide 145, ajout]

## Ce qui la définit
**Connu** : l'entrée $x_i$, la sortie désirée $t$ et la sortie obtenue $y$. **Cherché** : de combien bouger chaque poids. La réponse : en proportion de l'erreur et de l'entrée. Le poids d'une entrée nulle ne bouge pas : seule une entrée active est tenue pour responsable. [slide 145]

L'algorithme du perceptron tient en quatre pas répétés : initialiser les poids, présenter un motif et sa sortie désirée, calculer la sortie, mettre à jour les poids. On recommence jusqu'à un niveau d'erreur acceptable. [slide 144]

## Le chemin jusqu'ici
dss/perceptron fixe ce qu'on corrige : les poids d'un neurone unique, qui réalise une dss/fonction-discriminante-lineaire, la famille d'hypothèses que dss/apprentissage-inductif demandait de choisir. dss/reseau-de-neurones-artificiel posait que ces poids s'apprennent, et dss/apprentissage-supervise fournit, pour chaque exemple, la sortie désirée à laquelle on compare la sortie obtenue. [ajout]

## Exemple minimal
Sur le OU logique, avec $\eta=0{,}1$ et des poids de départ $(w_0,w_1,w_2)=(-0{,}5\,;\,0{,}45\,;\,1)$ : au point $(1,0)$, dont la sortie désirée est 1, la somme vaut $-0{,}05$ et le neurone répond 0, d'où $d=1$. Les poids deviennent $(-0{,}4\,;\,0{,}55\,;\,1)$ ; $w_2$ ne bouge pas, parce que $x_2=0$. La somme au même point vaut alors $0{,}15$, et le neurone répond 1. [ajout]

![Les quatre points du OU, sorties désirées 1 pleines et 0 creuses, et la frontière du neurone, là où la somme pondérée s'annule. Avant, le point $(1,0)$ est du mauvais côté. Un pas de la règle, $\Delta w_i=0{,}1\times1\times x_i$, fait monter $w_0$ et $w_1$ et laisse $w_2$ en place : la frontière recule sous le point.](figures/regle-delta.svg) [ajout]

## Geste de calcul type
Vérifier le signe avant tout : si la sortie est trop basse, $d>0$ et les poids des entrées actives montent. Une erreur de signe fait diverger l'apprentissage sans autre symptôme. [ajout]

## Cesse d'être valide quand
Elle ne s'applique qu'à un neurone dont on connaît la sortie désirée. Pour un nœud caché, cette sortie n'existe pas — c'est précisément le problème que la rétropropagation résout. [slide 152]
