---
id: fpp/valeur-actuelle-nette
nom: Valeur actuelle nette
symbole: '$NPV(t)$, $X_i$'
type: notion
statut: source
construite_a_partir_de:
- fpp/zero-coupon
alias:
- net present value
- NPV
- VAN
- valeur actuelle
refs:
- Déf. 4
---

## Ce que c'est
La somme des flux futurs d'un titre, chacun multiplié par le prix du zéro-coupon de sa date. [Déf. 4]

## Forme
$$NPV(t)=\sum_i P(t,t_i)\,X_i,\qquad NPV(t_k)=\frac{NPV(t)}{P(t,t_k)}$$ [Déf. 4]

## Ce que les symboles modélisent
$X_i$ est le montant, certain, payé à la date $t_i$ ; le poly appelle $\tau$ l'ensemble des dates $t_1,\dots,t_n$, sans rapport avec la durée restante $\tau$ des grecques. $NPV(t)$ est la valeur de toute la suite en $t$ ; $NPV(t_k)$ la même valeur exprimée à une autre date $t_k$. [Déf. 4, §8.2]

## Retrouver la formule
![Un titre qui paie 5 dans un an et 105 dans deux ans : chaque flux revient en t par le zéro-coupon de sa date, 4,80 et 95,01, et leur somme est la valeur actuelle nette, 99,81.](figures/valeur-actuelle-nette.svg) [ajout]

Le flux de 5 dans un an, ce sont 5 zéro-coupons à un an : il vaut $5\times0{,}9608=4{,}80$. Celui de 105 dans deux ans, ce sont 105 zéro-coupons à deux ans : $105\times0{,}9048=95{,}01$. [ajout]

Le titre entier est ces deux paquets de zéro-coupons réunis ; son prix est la somme des deux prix, 99,81. [ajout]

Pour exprimer cette valeur à une autre date $t_k$, on la capitalise jusqu'à $t_k$, c'est-à-dire qu'on la divise par le zéro-coupon de $t_k$ : [Déf. 4]

$$NPV(t)=\sum_i P(t,t_i)\,X_i,\qquad NPV(t_k)=\frac{NPV(t)}{P(t,t_k)}$$ [Déf. 4]

## Ce qui la définit
On connaît les flux et la courbe du jour ; on cherche ce que vaut aujourd'hui toute la suite. La valeur actuelle nette ramène chaque flux en $t$ et additionne ; la même valeur peut ensuite se citer à n'importe quelle date. [Déf. 4]

## Le chemin jusqu'ici
fpp/zero-coupon donne le prix d'un flux pris isolément ; la valeur actuelle nette traite un titre comme une somme de zéro-coupons. fpp/capitalisation fournit l'idée qu'une même somme change de valeur avec sa date, et c'est elle qui sert à transporter le résultat en $t_k$. [ajout]

## Exemple minimal
Un titre qui paie 5 dans un an et 105 dans deux ans vaut 99,81 aujourd'hui. [ajout]

## Geste de calcul type
Actualiser chaque flux par son zéro-coupon, additionner ; pour citer la valeur dans deux ans, diviser par $P(t,t+2)$ : $99{,}81/0{,}9048\approx110{,}31$. [Déf. 4, ajout]

## Cesse d'être valide quand
Les flux doivent être certains et dans une même devise. Pour un flux aléatoire, la somme ne dit pas quel montant prendre pour $X_i$, ni sous quelle probabilité en prendre la moyenne : c'est la question du chapitre 5. [§5.1]
