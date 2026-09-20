---
id: dup/bruit-equitable
nom: Bruit équitable
symbole: $\tilde\varepsilon$
type: notion
statut: source
cas_de: dup/accroissement-de-risque
valeur: l’ajout d’un bruit de moyenne conditionnelle nulle
construite_a_partir_de:
- dup/utilite-esperee
alias:
- additional fair noise
- Definition B
refs:
- L1 slide 20
---

## Ce que c'est
$F^*$ est plus risquée que $F$ si elle s’obtient en ajoutant un bruit de moyenne nulle conditionnellement au tirage. [L1 slide 20]

## Forme
$$\tilde y=\tilde x+\tilde\varepsilon,\qquad \mathbb{E}[\tilde\varepsilon\mid\tilde x]=0$$ [L1 slide 20]

## Ce qui la définit
Le bruit n’a pas besoin d’être indépendant de $\tilde x$ : sa variance conditionnelle peut varier avec $\tilde x$. [L1 slide 20]

L’inégalité de Jensen conditionnelle donne alors $\mathbb{E}[U(\tilde y)\mid\tilde x]\le U(\tilde x)$ pour $U$ concave, donc $\mathbb{E}U(\tilde y)\le\mathbb{E}U(\tilde x)$. [L1 slide 20]

## Le chemin jusqu'ici
Le socle commun : dup/loterie, dup/fonction-utilite, dup/utilite-esperee. [ajout]

Ajouter un bruit de moyenne nulle est une opération sur les loteries ; qu'elle corresponde à « plus risqué » est un énoncé sur les agents. Le socle contient les deux parce que la fiche relie les deux — c'est l'une des caractérisations équivalentes de l'accroissement de risque, et la plus intuitive. [ajout]

## Exemple minimal
Ajouter $\pm 20$ à pile ou face à $\tilde x$ uniforme sur $\{40,60\}$ donne $\{20,40,60,80\}$ uniforme, de même moyenne 50. [L1 slide 24]

## Geste de calcul type
Chercher à écrire $\tilde y=\tilde x+\tilde\varepsilon$ avec $\mathbb{E}[\tilde\varepsilon\mid\tilde x]=0$ : sur l’exemple du cours, $\pm20$ à pile ou face ajouté à $\{40,60\}$ donne exactement $\{20,40,60,80\}$. [L1 slide 20, L1 slide 24]

## Cesse d'être valide quand
La nullité de la moyenne conditionnelle est essentielle : un bruit de moyenne non nulle déplace la moyenne et sort du cadre. [L1 slide 20]
