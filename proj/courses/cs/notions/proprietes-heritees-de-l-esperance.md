---
id: cs/proprietes-heritees-de-l-esperance
nom: Propriétés héritées de l'espérance
symbole: '$\psi$'
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle
alias:
- classical properties of an expectation
- Jensen conditionnel
- convergence monotone conditionnelle
- Fatou conditionnel
- convergence dominée conditionnelle
refs:
- Prop. 0.4.1
- §0.4 slide 4
---

## Ce que c'est
L'espérance conditionnelle se calcule comme une espérance : positive, linéaire, croissante, et elle passe aux limites et sous une fonction convexe comme elle, à ceci près que chaque égalité ne vaut que presque sûrement. [Prop. 0.4.1]

## Forme
Pour $X$, $Y$ intégrables et $\mathcal G$ une sous-tribu de $\mathcal A$, $P$-presque sûrement : [Prop. 0.4.1]

- positivité : $X\ge0\Rightarrow E[X|\mathcal G]\ge0$ ; [Prop. 0.4.1 a)]
- linéarité : $E[\alpha X+\beta Y|\mathcal G]=\alpha E[X|\mathcal G]+\beta E[Y|\mathcal G]$ ; [Prop. 0.4.1 b)]
- monotonie : $X\ge Y\Rightarrow E[X|\mathcal G]\ge E[Y|\mathcal G]$ ; [Prop. 0.4.1 c)]
- Beppo-Lévy : $0\le X_n\uparrow X\Rightarrow E[X_n|\mathcal G]\uparrow E[X|\mathcal G]$ ; [Prop. 0.4.1 d)]
- Fatou : $X_n\ge0\Rightarrow E[\liminf_n X_n|\mathcal G]\le\liminf_n E[X_n|\mathcal G]$ ; [Prop. 0.4.1 e)]
- convergence dominée : $X_n\to X$ p.s. et $|X_n|\le Z\in L^1\Rightarrow E[X_n|\mathcal G]\to E[X|\mathcal G]$ p.s. et dans $L^1$ ; [Prop. 0.4.1 f)]
- Jensen : $\psi$ convexe et $\psi(X)\in L^1\Rightarrow\psi\big(E[X|\mathcal G]\big)\le E[\psi(X)|\mathcal G]$. [Prop. 0.4.1 g)]

## Ce que les symboles modélisent
$\psi$ est une fonction convexe de $\mathbb R$ dans $\mathbb R$, comme $x\mapsto x^2$ ou $x\mapsto|x|$ ; Jensen dit qu'appliquer $\psi$ après avoir prévu donne moins qu'appliquer $\psi$ puis prévoir. Ce n'est pas la fonction $\psi$ de la Prop. 0.4.3, qui porte la même lettre. $\alpha$ et $\beta$ sont deux réels quelconques, et dans la convergence dominée $Z$ est la variable qui majore toutes les $X_n$, pas une espérance conditionnelle. [Prop. 0.4.1, ajout]

## Ce qui la définit
Ces sept propriétés sont celles de l'espérance, recopiées : on peut calculer avec $E[\cdot|\mathcal G]$ sans réapprendre les règles. Deux différences seulement : le résultat est une variable aléatoire et non un nombre, et chaque égalité ou inégalité ne vaut que $P$-presque sûrement, puisque l'espérance conditionnelle n'est définie qu'à un événement négligeable près. [Prop. 0.4.1, Déf. 0.4.1]

La monotonie se démontre sur l'événement $\{E[Y|\mathcal G]-E[X|\mathcal G]\ge\varepsilon\}$, qui appartient à $\mathcal G$ : on l'utilise comme variable $U$ dans la définition, et sa probabilité est forcée à zéro. [Prop. 0.4.1 c)]

## Le chemin jusqu'ici
cs/esperance-conditionnelle caractérise la prévision par les égalités $E[XU]=E[ZU]$ ; chaque propriété se démontre en les vérifiant pour un candidat, puis en invoquant l'unicité. La linéarité, par exemple, vient de ce que $\alpha E[X|\mathcal G]+\beta E[Y|\mathcal G]$ satisfait ces égalités pour $\alpha X+\beta Y$. [Déf. 0.4.1, Prop. 0.4.1]

## Exemple minimal
Deux lancers, $X$ le nombre de piles, $\mathcal G$ le premier lancer, $\psi(x)=x^2$ : si le premier lancer donne pile, $\big(E[X|\mathcal G]\big)^2=1{,}5^2=2{,}25$ et $E[X^2|\mathcal G]=\tfrac12\times4+\tfrac12\times1=2{,}5$. Jensen se vérifie : $2{,}25\le2{,}5$. [ajout]

## Geste de calcul type
Découper ce qu'on conditionne en morceaux par linéarité, traiter chacun avec les propriétés propres au conditionnement — ce qui est connu sort, ce qui est indépendant se moyenne —, puis majorer avec Jensen ou passer à la limite avec la convergence dominée quand le calcul exact n'est pas possible. [Prop. 0.4.1, Prop. 0.4.2]

## Cesse d'être valide quand
Les hypothèses d'intégrabilité manquent : sans $\psi(X)\in L^1$, Jensen n'a pas de membre de droite ; sans variable dominante intégrable, la convergence p.s. des $X_n$ n'entraîne pas celle de leurs espérances conditionnelles. [Prop. 0.4.1 f), Prop. 0.4.1 g)]
