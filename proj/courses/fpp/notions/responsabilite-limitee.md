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

## Ce qui la définit
Quand l’actif passe sous la dette, les capitaux propres sont plancherisés à zéro et c’est la dette qui encaisse la perte : la faillite. [§1.4]

## Le chemin jusqu'ici
fpp/bilan puis fpp/levier donnent l'amplification, et elle joue dans les deux sens. [ajout]

La responsabilité limitée est ce qui l'arrête en bas : les capitaux propres ne passent pas sous zéro. Le seuil se lit directement sur le levier, $\pi_A=-1/l$. On n'a pas besoin de plus : c'est une contrainte juridique posée sur une identité comptable. [ajout]

## Exemple minimal
Avec un levier de 3,33, une chute de l’actif de 30 % suffit à effacer les capitaux propres. [ajout]

## Geste de calcul type
Le seuil de faillite est l’inverse du levier : $\pi_A=-1/l$. Plus le levier est grand, plus la marge est mince. [§1.4]

## Cesse d'être valide quand
Ce plancher est exactement une option de vente détenue par l’actionnaire sur l’actif de la firme ; le §1.4 ne le dit pas, mais toute la section 6 le permet. [ajout]

## Origine
- exercice fpp/ex-16 : ce que cette fiche avançait en `[ajout]` — « ce plancher est exactement une option de vente détenue par l'actionnaire » — est dit et nommé par la source : c'est le **modèle de Merton**. Les fonds propres sont un call sur la valeur de la firme, de strike la dette [exo. 16]
