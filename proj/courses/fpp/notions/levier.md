---
id: fpp/levier
nom: Levier
symbole: $l_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/bilan
alias:
- leverage
refs:
- Déf. 1
- §1.3
---

## Ce que c'est
Le rapport de l’actif aux capitaux propres, qui multiplie sur les capitaux propres l’écart entre le rendement de l’actif et celui de la dette. [Déf. 1, §1.3]

## Forme
$$l_t\equiv\dfrac{A_t}{E_t},\qquad \dfrac{\Delta E_t}{E_t}-\dfrac{\Delta D_t}{D_t}=l_t\Big(\dfrac{\Delta A_t}{A_t}-\dfrac{\Delta D_t}{D_t}\Big)$$ [Déf. 1, §1.3]

## Ce que les symboles modélisent
$l_t$ est un rapport entre deux montants du bilan, sans unité. Ce n'est pas un taux d'endettement au sens courant : il vaut un quand il n'y a aucune dette, et croît sans borne à mesure que les capitaux propres s'amenuisent. [Déf. 1]

$\Delta$ note la variation entre $t$ et $t+\Delta t$ ; $\Delta A_t/A_t$ est donc le rendement de l'actif sur la période, et de même pour les capitaux propres et la dette. [§1.3]

## Retrouver la formule
![Le bilan de l'exemple avant et après une baisse de 10 % de l'actif, choisie pour le dessin. Connu : le choc sur l'actif, et la dette, qui ne bouge pas. Cherché : ce que perdent les capitaux propres. Toute la perte tombe sur eux, de 30 à 20 : $-33\,\%$, soit 3,33 fois $-10\,\%$.](figures/levier.svg) [ajout]

Un actif de 100, financé par 30 de capitaux propres et 70 de dette. L'actif perd 10 %, soit 10 ; la dette est due quoi qu'il arrive et ne bouge pas. **Connu** : ces deux variations. **Cherché** : ce que perdent les capitaux propres, en pour cent. [ajout]

Le bilan tient toujours : $\Delta A=\Delta E+\Delta D$, donc $-10=\Delta E+0$. Les capitaux propres perdent les 10, mais sur une base de 30 : $-10/30=-33\,\%$. [§1.3]

C'est $3{,}33$ fois la perte de l'actif, parce que la même perte en euros se rapporte à une base $3{,}33$ fois plus petite : $l=100/30$. [ajout]

En lettres, $\Delta E=\Delta A-\Delta D$ ; on divise par $E$, et on fait apparaître les rendements : $\frac{\Delta E}{E}=\frac{A}{E}\frac{\Delta A}{A}-\frac{D}{E}\frac{\Delta D}{D}=l\,\frac{\Delta A}{A}-(l-1)\frac{\Delta D}{D}$, puisque $D/E=(A-E)/E=l-1$. [§1.3]

On retranche des deux côtés le rendement de la dette, et l'écart des capitaux propres sur la dette apparaît comme $l$ fois celui de l'actif. [§1.3]

$$\dfrac{\Delta E_t}{E_t}-\dfrac{\Delta D_t}{D_t}=l_t\Big(\dfrac{\Delta A_t}{A_t}-\dfrac{\Delta D_t}{D_t}\Big)$$ [§1.3]

## Ce qui la définit
C'est une identité, pas une hypothèse : elle ne tient qu'au bilan, et vaut pour n'importe quel choc. Quand la dette ne rapporte rien sur la période, elle se lit simplement : les capitaux propres varient, en pour cent, de $l$ fois ce que varie l'actif. [§1.3, ajout]

## Le chemin jusqu'ici
fpp/bilan fournit l'identité actif = capitaux propres + dette. Le levier est le rapport de deux de ses termes, et l'amplification n'est que cette identité, divisée par les capitaux propres. [ajout]

## Exemple minimal
Un actif de 100 sur 30 de capitaux propres et 70 de dette : $l=3{,}33$. [ajout]

## Geste de calcul type
L'actif rapporte 5 % sur l'année, la dette 2 %. L'actif gagne 5, les créanciers reçoivent $70\times2\,\%=1{,}4$, il reste $3{,}6$ aux actionnaires, soit 12 % de 30. Par la formule : $12\,\%-2\,\%=3{,}33\times(5\,\%-2\,\%)=10\,\%$. [ajout]

## Cesse d'être valide quand
L'identité, jamais. Mais sa lecture « la dette ne bouge pas » cesse quand les pertes dépassent les capitaux propres : ceux-ci ne peuvent pas passer sous zéro, et c'est alors la dette qui perd. [§1.4]

## Origine
- exercice fpp/ex-16 : **collision de symbole entre les deux documents du cours.** Le poly pose $l_t=A_t/E_t\in[1,\infty)$ (Déf. 1) ; le livre d'exercices pose $l=D/F_T\in[0,1]$. Même lettre, même mot. Voir `notation.yml`, section collisions [exo. 16]
