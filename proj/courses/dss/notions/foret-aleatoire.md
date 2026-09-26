---
id: dss/foret-aleatoire
nom: Forêt aléatoire
symbole: $m$
type: notion
statut: source
cas_de: dss/methode-d-ensemble
valeur: des arbres décorrélés par un tirage de prédicteurs à chaque coupure
construite_a_partir_de:
- dss/variance-d-une-moyenne-correlee
alias:
- random forest
- RF
refs:
- slide 110
- slide 111
- slide 112
- slide 113
- slide 115
- slide 116
- slide 119
- slide 121
---

## Ce que c'est
Du bagging où, à chaque coupure, seuls $m$ prédicteurs tirés au hasard sont candidats, pour que les arbres cessent de se ressembler. [slide 112, slide 113]

## Ce que les symboles modélisent
$m$ est le nombre de prédicteurs candidats **à chaque coupure** : le tirage se refait à chaque nœud, pas une fois par arbre. Il se lit face à $p$, le nombre total de prédicteurs ; à $m=p$, tous sont candidats et l'on retrouve exactement le bagging. Ce n'est pas le $m$ qui, plus loin dans le cours, compte les exemples d'apprentissage. [slide 113, ajout]

## Ce qui la définit
**Connu** : moyenner des arbres corrélés ne fait pas descendre la variance sous un plancher fixé par leur corrélation. **Cherché** : un moyen de rendre les arbres moins corrélés. La cause est nommée avant le remède : s'il existe un prédicteur très fort, tous les arbres du bagging le placent en haut, et ils se ressemblent. [slide 109, slide 110]

Restreindre les prédicteurs ne suffit pas : si l'on garde toujours les mêmes, les arbres restent corrélés. Il faut tirer le sous-ensemble au hasard, à chaque coupure. [slide 111, slide 112]

Ajouter des arbres ne fait pas surajuster la forêt : leur nombre $B$ n'augmente pas la souplesse du modèle. [slide 121]

## Le chemin jusqu'ici
dss/bagging moyenne des arbres ajustés sur des tirages de dss/bootstrap, pour réduire la variance d'un arbre sans toucher à son biais, l'échange que décrit dss/compromis-biais-variance. dss/apprentissage-supervise fournit les clients dont on connaît la perte, et dss/erreur-de-test mesure ce que l'on y gagne. [ajout]

dss/variance-d-une-moyenne-correlee montre où ce gain s'arrête : la variance de la moyenne bute sur un plancher fixé par la corrélation entre arbres. La forêt aléatoire s'attaque à ce plancher, et à rien d'autre. [ajout]

## Exemple minimal
Sur les 20 clients, $p=5$ et $m=2$ : un prédicteur donné est candidat à une coupure deux fois sur cinq. Sur 500 arbres, la variable sans lien x3, que le hasard a liée à la perte, fait la première coupure de 45 % des arbres du bagging, et de 30 % des arbres de la forêt. [ajout]

![Les 20 clients, 500 arbres. Chaque barre donne la part des arbres dont la première coupure porte sur un prédicteur : l'endettement x1, le revenu x2, les trois variables sans lien. En bagging, les 5 prédicteurs sont candidats, et près de la moitié des arbres commencent par x3. En forêt, 2 seulement le sont : x3 n'est candidate que deux fois sur cinq, et les premières coupures se répartissent.](figures/foret-aleatoire.svg) [ajout]

## Geste de calcul type
La chance qu'un prédicteur donné soit candidat à une coupure vaut $m/p$ : 2/5 sur les 20 clients. [ajout]

Pour choisir $m$, partir des valeurs recommandées par les inventeurs — $m=\sqrt{p}$ et taille de nœud minimale 1 en classification, $m=p/3$ et taille 5 en régression —, puis les traiter comme des paramètres à régler, en suivant l'erreur out-of-bag. [slide 116]

## Cesse d'être valide quand
Quand les prédicteurs sont nombreux et les pertinents rares, un $m$ petit fait mal travailler la forêt : à une coupure, la chance qu'un prédicteur pertinent soit candidat devient faible. [slide 119]

La slide la chiffre à environ 0,25 pour 3 prédicteurs pertinents parmi 103, sans dire quel $m$ elle suppose ; avec $m=10$, proche de $\sqrt{103}$, on trouve 0,27. [slide 119, ajout]
