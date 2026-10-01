---
id: cs/processus-de-meme-loi
nom: Processus de même loi
symbole: '$\underset{\mathcal D}{=}$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-stochastique
alias:
- equidistributed processes
- processus équidistribués
- lois fini-dimensionnelles
refs:
- Déf. 0.5.2
---

## Ce que c'est
Deux processus ont même loi quand, pour tout choix d'un nombre fini de dates, leurs valeurs à ces dates ont la même loi jointe. [Déf. 0.5.2]

## Forme
$$\forall n\in\mathbb N^*,\ \forall(t_1,\dots,t_n)\in T^n :\qquad(X_{t_1},\dots,X_{t_n})\underset{\mathcal D}{=}(Y_{t_1},\dots,Y_{t_n})$$ [Déf. 0.5.2]

## Ce que les symboles modélisent
$\underset{\mathcal D}{=}$ est l'égalité en loi : deux vecteurs aléatoires qui donnent la même probabilité à chaque événement, sans être égaux pour autant. Les lois des vecteurs $(X_{t_1},\dots,X_{t_n})$ s'appellent les lois fini-dimensionnelles du processus. [Déf. 0.5.2, ajout]

## Ce qui la définit
C'est la plus faible des trois façons de dire que deux processus se ressemblent : elle ne compare que des probabilités, jamais les valeurs prises dans un même monde $\omega$. Deux processus peuvent même avoir la même loi sans être définis sur le même espace. [Déf. 0.5.2, §0.5 slide 3, ajout]

## Le chemin jusqu'ici
cs/processus-stochastique fournit, à chaque date, une variable aléatoire ; la loi du processus se lit alors sur un nombre fini de dates à la fois, par les lois jointes de ces variables. [Déf. 0.5.1, Déf. 0.5.2]

## Exemple minimal
Sur $[0,1]$ avec la mesure de Lebesgue, $X_t(\omega)=\omega+t$ et $X'_t(\omega)=(1-\omega)+t$ ont même loi, puisque $1-\omega$ est encore uniforme sur $[0,1]$ ; pourtant $X_t-X'_t=2\omega-1$ n'est presque jamais nul. [ajout]

## Geste de calcul type
Pour montrer que deux processus ont même loi, écrire chacun comme la même fonction du temps et d'une variable aléatoire, puis vérifier que les deux variables ont même loi : ici $\omega$ et $1-\omega$, toutes deux uniformes. [ajout]

## Cesse d'être valide quand
On veut comparer les valeurs dans un même monde $\omega$ : même loi ne dit rien de $X_t(\omega)-Y_t(\omega)$, comme le montre $X$ et $X'$ ci-dessus. Il faut alors une version (cs/version-d-un-processus). [§0.5 slide 3, ajout]
