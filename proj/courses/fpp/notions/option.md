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
Le strike $K$ et la maturité $T$ sont fixés d’avance. [Déf. 9]

Le détenteur a le droit sans l'obligation : en $T$, il n'exerce que si l'échange lui rapporte, et laisse tomber sinon. Le payoff est donc celui de l'échange, coupé à zéro, $(S_T-K)^+$ ou $(K-S_T)^+$. [Déf. 9, Déf. 11]

## Pourquoi ce niveau existe
Le cours définit le call, droit d'acheter, et le put, droit de vendre, dans la même définition, et ils ne diffèrent que par le sens de l’échange, avec une relation exacte entre eux — la parité call-put. Les séparer sans les réunir ferait perdre cette relation. [Déf. 9, Prop. 7]

## Le chemin jusqu'ici
Il n'y a qu'un prérequis, fpp/payoff : une option se décrit entièrement par ce qu'elle paie, et la partie positive $(\cdot)^+$ qu'il définit écrit la possibilité de ne pas exercer. À ce stade rien n'est encore évalué : on décrit un contrat, on ne le price pas. [ajout]

## Ce qui reste libre
| paramètre | cas | valeur |
|---|---|---|
| dates d’exercice | européenne | à la seule date $T$, sans paiement intermédiaire |
| dates d’exercice | américaine | à tout moment entre la première date et la maturité |
[Déf. 10]

## Cesse d'être valide quand
Le cours ne valorise que l'option européenne ; l'américaine, qu'on peut exercer à tout moment, n'a pas de forme fermée. [§6.2, ajout]
