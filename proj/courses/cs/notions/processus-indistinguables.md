---
id: cs/processus-indistinguables
nom: Processus indistinguables
type: notion
statut: source
construite_a_partir_de:
- cs/version-d-un-processus
- cs/processus-continu
alias:
- indistinguishable processes
- indistinguabilité
refs:
- Déf. 0.5.4
- §0.5 slide 3
- §0.5 slide 4
---

## Ce que c'est
Deux processus sont indistinguables quand, presque sûrement, leurs trajectoires coïncident à toutes les dates à la fois. [Déf. 0.5.4]

## Forme
$$P\big(\{\omega : \forall t\in T,\ X_t(\omega)=Y_t(\omega)\}\big)=1$$ [Déf. 0.5.4]

## Ce que les symboles modélisent
L'événement $\{\omega : \forall t\in T,\ X_t(\omega)=Y_t(\omega)\}$ réunit les mondes où les deux trajectoires sont identiques d'un bout à l'autre. Le quantificateur « pour tout $t$ » est cette fois à l'intérieur de la probabilité : un seul ensemble négligeable, le même pour toutes les dates. [Déf. 0.5.4, ajout]

## Ce qui la définit
Les trois définitions du chapitre sont de plus en plus exigeantes : indistinguables entraîne version, qui entraîne même loi. La différence entre les deux dernières est la place du « pour tout $t$ » : hors de la probabilité pour une version, dedans pour des processus indistinguables. [§0.5 slide 3, Déf. 0.5.3, Déf. 0.5.4]

![L'exemple des slides avec a = 1 : X_t(ω) = ω + t, et Y égal à X sauf en t = ω, où il vaut 0. À t = 0,5 fixé, X et Y ne diffèrent que si ω = 0,5, avec probabilité 0 : Y est une version de X. Mais chaque trajectoire de Y a son trou, en t = ω, ici pour ω = 0,3 et 0,7 : P(X_t = Y_t pour tout t) = 0, et X et Y ne sont pas indistinguables.](figures/processus-indistinguables.svg) [§0.5 slide 4, ajout]

Pour des processus continus, l'écart disparaît : deux versions continues l'une de l'autre sont indistinguables. Elles coïncident presque sûrement à toutes les dates rationnelles à la fois, une réunion dénombrable d'ensembles négligeables étant négligeable, puis partout par continuité. [§0.5 slide 4]

## Le chemin jusqu'ici
Pour deux processus au sens de cs/processus-stochastique, le chapitre propose trois comparaisons de plus en plus fortes. cs/processus-de-meme-loi ne regarde que les lois ; cs/version-d-un-processus compare les valeurs date par date et laisse, à chaque date, son propre ensemble négligeable ; l'indistinguabilité demande un seul ensemble pour toutes les dates. [Déf. 0.5.2, Déf. 0.5.3, §0.5 slide 3]

cs/processus-continu dit quand la version suffit à l'indistinguabilité : des trajectoires continues sont fixées par une infinité dénombrable de dates. [Déf. 0.5.5, §0.5 slide 4]

## Exemple minimal
Sur $[0,1]$ avec la mesure de Lebesgue, $X_t(\omega)=\omega+t$ et sa version $Y$, nulle en $t=\omega$, ne sont pas indistinguables : leurs trajectoires ne coïncident que pour $\omega=0$, et $P(\{0\})=0$. [§0.5 slide 4]

## Geste de calcul type
Pour montrer que deux versions continues sont indistinguables : poser $N=\bigcup_{t\in T\cap\mathbb Q}\{X_t\neq Y_t\}$, négligeable comme réunion dénombrable ; hors de $N$ et de l'ensemble où une trajectoire n'est pas continue, les trajectoires coïncident aux rationnels, donc partout. [§0.5 slide 4, ajout]

## Cesse d'être valide quand
Les trajectoires ne sont pas continues : une version peut alors différer du processus en un instant différent pour chaque $\omega$, comme $Y$, et l'indistinguabilité échoue alors que chaque date, prise seule, ne voit rien. [§0.5 slide 4]

## Origine
- exercice cs/ex-0-5-1 : la continuité fait passer de version à indistinguable ; le contre-exemple $Y$ montre qu'il faut la continuité des deux processus [ajout]
