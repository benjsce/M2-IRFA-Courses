---
id: dup/accroissement-de-risque
nom: Accroissement de risque
type: abstraite
statut: source
cas_de: dup/principe-d-unanimite
valeur: l’accord de tous les agents averses, à moyennes égales
parametre: la caractérisation par laquelle on le définit
construite_a_partir_de: []
alias:
- increasing risk
- Rothschild-Stiglitz
refs:
- L1 slide 18
- L1 slide 23
- L1 slide 28
---

## Ce que c'est
L’ordre partiel sur lequel tous les agents averses au risque à utilité espérée sont d’accord. [L1 slide 18]

## Ce que les membres partagent
Rothschild et Stiglitz établissent que ces définitions coïncident pour deux distributions de même moyenne : ordre concave, bruit équitable, étalement préservant la moyenne, répartition intégrée. [L1 slide 23]

C’est un ordre partiel : certaines distributions de même moyenne restent incomparables parce que deux fonctions concaves les classent différemment. La relation ne classe pas toute paire, mais elle est transitive. [L1 slide 18]

Le cours met en regard trois façons de parler du risque : l’utilité concave demande si un pari est préféré à sa moyenne ; l’écart type mesure la dispersion autour de la moyenne ; l’accroissement de risque demande si tous les agents averses sont d’accord. [L1 slide 28]

Trois critères se ressemblent sur le papier et se distinguent par la classe d'agents qui doit être d'accord. Pour les deux derniers, $U$ n'apparaît pas dans la condition : elle est dans l'équivalence qui relie la condition à la classe. [ajout]

| critère | condition sur $F^*$, la loi la moins bonne ou la plus risquée, face à $F$ | agents qui préfèrent tous $F$ |
|---|---|---|
| dominance du premier ordre | $F^*(x)\ge F(x)$ pour tout $x$ | toutes les $U$ croissantes |
| dominance du second ordre | $\int_0^x\big[F^*(t)-F(t)\big]\,dt\ge0$ pour tout $x$ | toutes les $U$ croissantes et concaves |
| accroissement de risque | la même intégrale, positive pour tout $x$ **et nulle en $x=M$** | toutes les $U$ concaves |
[L1 slide 6, L1 slide 19, L1 slide 22, L1 slide 23, ajout]

La deuxième ligne n'est pas énoncée par le cours, qui ne nomme la dominance du second ordre que pour dire qu'à moyennes égales elle coïncide avec l'ordre concave. Elle est ajoutée ici pour situer la troisième. [L1 slide 19, ajout]

Les deux dernières lignes ne diffèrent que par l'égalité en $M$. L'intégrale de $F^*-F$ de 0 à $M$ vaut la moyenne de $F$ moins celle de $F^*$ : l'égalité impose donc des moyennes égales. À moyennes égales, un agent neutre, dont $U$ est linéaire, est indifférent, et le sens de variation de $U$ ne départage plus rien ; seule la concavité compte, et la classe s'élargit à toutes les $U$ concaves. Sans l'égalité, $F$ peut avoir une moyenne plus haute que $F^*$, et il faut alors que $U$ soit croissante pour que tous préfèrent $F$. [ajout]

## Pourquoi ce niveau existe
Le cours donne séparément les définitions A, B, C et la répartition intégrée, puis démontre qu’elles coïncident. Les garder séparées sans les réunir ferait de l’équivalence de Rothschild-Stiglitz un résultat sans objet. [L1 slide 23]

## Cesse d'être valide quand
Une variance plus grande ne suffit pas : $\mathrm{Var}(\tilde y)\ge\mathrm{Var}(\tilde x)$ découle de l’accroissement de risque, mais la réciproque échoue en général. [L1 slide 25]
