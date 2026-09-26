---
id: fpp/effet-de-levier
nom: Effet de levier
symbole: '$\sigma_A$, $\sigma_E$'
type: notion
statut: source
construite_a_partir_de:
- fpp/levier
- fpp/prime-de-risque
- fpp/volatilite
alias:
- leverage effect
- amplification par le levier
refs:
- §1.3
---

## Ce que c'est
Le levier multiplie par le même facteur la prime de risque espérée et la volatilité des capitaux propres par rapport à celles des actifs. [§1.3]

## Forme
$$\tilde\pi_E = l_t\,\tilde\pi_A,\qquad \pi_E = l_t\,\pi_A,\qquad \sigma_E = l_t\,\sigma_A$$ [§1.3]

## Ce que les symboles modélisent
$\sigma_A$ et $\sigma_E$ sont les volatilités des primes de risque des actifs et des capitaux propres ; $\pi_A$ et $\pi_E$ leurs primes espérées ; $l_t$ le levier, connu au début de la période. [§1.3]

## Retrouver la formule
Prenons le bilan du cours : 100 d'actifs, 80 de dette, 20 de capitaux propres, un levier de 5. Sur l'année, les actifs rapportent 6 et la dette coûte 4 %, soit 3,2. Les capitaux propres gagnent la différence, 2,8, soit 14 % de 20. [ajout]

Au-delà du coût de la dette, les actifs rapportent $6-4=2$ points, les capitaux propres $14-4=10$ points : cinq fois plus, exactement le levier. [ajout]

En lettres, l'égalité du bilan donne $\Delta E_t = \Delta A_t - \Delta D_t$. Divisée par $E_t$, elle devient $\dfrac{\Delta E_t}{E_t} = l_t\dfrac{\Delta A_t}{A_t} - (l_t-1)\dfrac{\Delta D_t}{D_t}$, puisque $D_t/E_t = l_t-1$. [§1.3]

Retrancher $\Delta D_t/D_t$ des deux côtés fait apparaître les deux primes, et le levier se met en facteur. Comme $l_t$ est connu au début de la période, il sort de l'espérance et de l'écart type : [§1.3]

$$\tilde\pi_E = l_t\,\tilde\pi_A \;\Longrightarrow\; \pi_E = l_t\,\pi_A,\quad \sigma_E = l_t\,\sigma_A$$ [§1.3]

## Ce qui la définit
On connaît le levier et les deux statistiques des actifs ; on cherche celles des capitaux propres. Toutes deux sont multipliées par $l_t$ : les capitaux propres sont une version plus risquée et mieux rémunérée du même pari, et le rapport de la prime à la volatilité ne change pas. [§1.3, ajout]

Le levier amplifie dans les deux sens : un actif dont la prime espérée est négative donne des capitaux propres dont la prime espérée est $l_t$ fois plus négative. [§1.3]

![Les actifs et les capitaux propres dans le plan volatilité–prime : avec un levier de 5, le point des capitaux propres est cinq fois plus loin sur la même demi-droite issue de l'origine.](figures/effet-de-levier.svg) [ajout]

## Le chemin jusqu'ici
fpp/bilan fournit l'égalité des variations, d'où toute la formule sort par une division. fpp/levier y apparaît comme le rapport qui convertit un mouvement des actifs en mouvement des capitaux propres. [ajout]

Ce que ce rapport multiplie, ce sont les deux nombres qui résument un actif risqué : sa prime espérée, définie par fpp/prime-de-risque comme l'écart au coût de la dette, et sa dispersion, que fpp/volatilite mesure. [ajout]

## Exemple minimal
Un levier de 5, une prime espérée des actifs de 2 % et une volatilité de 4 % : les capitaux propres ont une prime espérée de 10 % et une volatilité de 20 %. [ajout]

## Geste de calcul type
Multiplier par le levier pour passer des actifs aux capitaux propres ; diviser pour faire le chemin inverse, par exemple retrouver la volatilité des actifs, $20\,\%/5=4\,\%$, à partir de celle d'une action et du levier de l'entreprise. [§1.3, ajout]

## Cesse d'être valide quand
Les égalités supposent que les capitaux propres peuvent perdre sans limite. Sous responsabilité limitée, ils ne descendent pas sous zéro, et $\tilde\pi_E = l_t\,\tilde\pi_A$ cesse de tenir pour les grandes pertes des actifs. [§1.4]
