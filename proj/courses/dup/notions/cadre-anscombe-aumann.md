---
id: dup/cadre-anscombe-aumann
nom: Cadre d’Anscombe-Aumann
symbole: $\mathcal{F}$
type: notion
statut: source
construite_a_partir_de:
- dup/acte
- dup/loterie
alias:
- Anscombe-Aumann
- actes à valeurs dans les loteries
refs:
- L4 slide 43
- L4 slide 44
---

## Ce que c'est
Un acte associe à chaque état non plus un résultat mais une loterie, ce qui place une randomisation objective à l’intérieur de chaque état. [L4 slide 43]

## Forme
$$\mathcal{F}=\{f:S\to\Delta(X)\},\qquad \big(\alpha f+(1-\alpha)g\big)(s)=\alpha f(s)+(1-\alpha)g(s)$$ [L4 slide 43]

## Ce que les symboles modélisent
$\mathcal{F}$ est l'ensemble des actes de ce cadre : des fonctions qui vont des états vers les loteries, et non vers les résultats. $\ell$ désigne une loterie et, du même coup, l'acte qui la donne dans tous les états ; c'est ce double emploi qui permet de comparer un acte à une loterie. [L4 slide 43]

$\mathcal{F}$ tient le rôle que $F$ tenait chez Savage, sous une autre lettre. [ajout]

## Ce qui la définit
Le mélange se fait état par état, sur les loteries : c’est une randomisation objective, distincte de l’incertitude sur l’état. Une loterie $\ell$ désigne aussi l’acte constant qui la donne dans tous les états, ce qui permet de comparer $f(s)$ et $g(s)$ comme deux actes constants et donne un sens à la comparaison état par état. [L4 slide 43]

Quatre axiomes sont communs à tous les modèles écrits dans ce cadre : l’ordre faible, la continuité par mélange, la non-dégénérescence et la monotonie. La monotonie est celle qui fait travailler la structure : si $f(s)$ est au moins aussi bon que $g(s)$ dans chaque état, alors $f$ est au moins aussi bon que $g$. [L4 slide 44]

## Le chemin jusqu'ici
dup/acte donne l’application des états vers les conséquences, et dup/loterie l’objet probabiliste posé sur ces conséquences. Le cadre les emboîte l’un dans l’autre au lieu de les juxtaposer. [ajout]

C’est ce qui en fait un cadre de travail plutôt qu’une notion de plus : l’enrichissement des conséquences donne prise au mélange, et le mélange est l’outil qui permettra d’écrire les axiomes sous forme d’égalités de préférence. Sans les deux amonts, la définition ne dirait rien. [ajout]

## Exemple minimal
Sur $S=\{R,B\}$, l’acte qui donne « 100 ou 0 à pile ou face » si la boule est rouge et 50 pour sûr si elle est bleue est un élément de $\mathcal{F}$, alors qu’il n’en est pas un au sens de dup/acte. [ajout]

## Geste de calcul type
Distinguer les deux randomisations : celle qui porte sur l’état, inconnue et ambiguë, et celle qui porte sur la conséquence, objective et donnée par la loterie. [L4 slide 43]

## Cesse d'être valide quand
Le cadre suppose qu’on sait mélanger objectivement les conséquences, c’est-à-dire qu’un dispositif de hasard non ambigu est disponible. C’est une hypothèse de richesse du décor, absente du cadre de Savage. [ajout]
