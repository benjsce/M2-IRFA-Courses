---
id: fpp/responsabilite-limitee
nom: Responsabilité limitée
type: notion
statut: source
construite_a_partir_de:
- fpp/levier
alias:
- limited liability
refs:
- §1.4
---

## Ce que c'est
La valeur des capitaux propres ne peut pas devenir négative : l’actionnaire ne perd jamais plus que sa mise. [§1.4]

## Forme
$$\pi_E\le-100\%\iff l\,\pi_A\le-1\iff \pi_A\le-\dfrac{1}{l}$$ [§1.4]

## Ce que les symboles modélisent
Ici, $\pi_E$ et $\pi_A$ sont de simples rendements réalisés sur la période, des capitaux propres et de l'actif : la source néglige le rendement de la dette. Un rendement de −100 % des capitaux propres est la perte de toute la mise. [§1.4, ajout]

$l$ est le levier, le rapport de l'actif aux capitaux propres, au moins égal à un. [Déf. 1]

## Retrouver la formule
![Le rendement des capitaux propres selon celui de l'actif, avec le levier de l'exemple. La droite de pente 3,33 atteint $-100\,\%$ quand l'actif perd 30 % ; en dessous, l'actionnaire ne perd pas plus que sa mise, et le pointillé est la perte qu'il aurait subie sans la responsabilité limitée.](figures/responsabilite-limitee.svg) [ajout]

Un actif de 100, financé par 30 de capitaux propres et 70 de dette, soit un levier de 3,33. **Connu** : ce bilan. **Cherché** : la baisse de l'actif qui efface les capitaux propres. [ajout]

La dette ne bouge pas : l'actif peut descendre jusqu'à 70 avant qu'elle ne soit touchée. Il perd alors 30 sur 100, soit 30 %, exactement la part de l'actif payée par les actionnaires, $E/A=1/l$. [ajout]

En rendements, les capitaux propres varient de $l$ fois ce que varie l'actif ; ils sont effacés quand ce rendement atteint −100 %, c'est-à-dire quand l'actif perd $1/l$. Au-delà, ils restent à zéro, et c'est la dette qui perd. [§1.4]

$$\pi_E\le-100\%\iff\pi_A\le-\dfrac{1}{l}$$ [§1.4]

## Ce qui la définit
Quand l’actif passe sous la dette, les capitaux propres sont plancherisés à zéro et c’est la dette qui encaisse la perte : la faillite. [§1.4]

## Le chemin jusqu'ici
L'amplification vient de fpp/levier, qui la tire de l'identité de fpp/bilan : les capitaux propres varient de $l$ fois ce que varie l'actif, à la baisse comme à la hausse. La responsabilité limitée l'arrête en bas, à la perte de la mise. C'est une contrainte juridique posée sur une identité comptable. [ajout]

## Exemple minimal
Avec un levier de 3,33, une chute de l’actif de 30 % suffit à effacer les capitaux propres. [ajout]

## Geste de calcul type
Le seuil est l'inverse du levier, $1/l=E/A$ : avec 30 de capitaux propres sur 100 d'actif, 30 % ; avec 10 sur 100, un levier de 10, il suffit de 10 %. Plus le levier est grand, plus la marge est mince. [§1.4, ajout]

## Cesse d'être valide quand
Le seuil $-1/l$ néglige le rendement de la dette. Si les 70 de dette portent 2 % d'intérêt, l'actif doit valoir au moins 71,4 à la fin de la période : il ne peut perdre que 28,6 %, et non 30 %. [§1.4, ajout]

## Origine
- exercice fpp/ex-16 : les capitaux propres se comportent comme un call sur l'actif de la firme, de strike la dette ; c'est le **modèle de Merton** [exo. 16]
