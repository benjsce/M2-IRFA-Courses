---
id: fpp/option
nom: Option
type: abstraite
statut: source
cas_de: fpp/contrat-a-prime
valeur: un payoff convexe par morceaux, $(S_T-K)^+$ ou $(K-S_T)^+$
parametre: le sens du droit accordé au détenteur
construite_a_partir_de:
- fpp/payoff
alias:
- option
refs:
- Déf. 9
- Déf. 10
- §6.1
---

## Ce que c'est
Un contrat qui donne un droit d’échanger à prix fixé, sans l’obligation de l’exercer. [Déf. 9]

## Ce que les membres partagent
Le strike $K$ et la maturité $T$ sont fixés d’avance ; l’inconnue est la prime. C’est ce qui les sépare des contrats à prime nulle, où l’inconnue est le strike. [Déf. 9]

L’asymétrie du droit rend le payoff non linéaire, et c’est cette non-linéarité, et elle seule, qui interdit la réplication statique. [ajout]

## Pourquoi ce niveau existe
Deux contrats que le cours définit dans la même phrase et qui ne diffèrent que par le sens de l’échange, avec une relation exacte entre eux — la parité call-put. Les séparer sans les réunir ferait perdre cette relation. [Déf. 9, Prop. 7]

## Le chemin jusqu'ici
Une seule brique : fpp/payoff. Une option, c'est la possibilité de ne pas exercer — donc un payoff qui se coupe à zéro, ce que la partie positive $(\cdot)^+$ écrit. [ajout]

C'est le seul prérequis parce qu'à ce stade rien n'est encore évalué : on décrit un contrat, on ne le price pas. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| dates d’exercice | européenne | à la seule date $T$, sans paiement intermédiaire |
| dates d’exercice | américaine | à tout moment entre la première date et la maturité |
[Déf. 10]

## Cesse d'être valide quand
Le style d’exercice est un second paramètre, orthogonal au sens du droit : le cours ne valorise que l’européenne, et l’américaine n’a pas de forme fermée. [Déf. 10]
