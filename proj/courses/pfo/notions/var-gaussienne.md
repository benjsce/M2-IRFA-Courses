---
id: pfo/var-gaussienne
nom: VaR gaussienne
symbole: '$z_\alpha$, $\varphi$'
type: notion
statut: source
cas_de: pfo/modele-de-risque
valeur: la loi normale de moyenne et d'écart type estimés
construite_a_partir_de:
- pfo/valeur-a-risque-conditionnelle
alias:
- VaR paramétrique
- parametric VaR
- VaR normale
- CVaR gaussienne
- Gaussian VaR
refs:
- p. 33
- Listing 2.2
---

## Ce que c'est
La VaR et la CVaR calculées en supposant les rendements normaux, à partir de leur seule moyenne et de leur seul écart type. [Listing 2.2]

## Forme
$$\mathrm{VaR}_\alpha = -\left(\mu + z_\alpha\,\sigma\right) \times \text{capital}, \qquad \mathrm{CVaR}_\alpha = -\left(\mu - \sigma\,\dfrac{\varphi(z_\alpha)}{\alpha}\right) \times \text{capital}$$ [Listing 2.2]

## Ce que les symboles modélisent
$z_\alpha$ est le quantile d'ordre $\alpha$ de la loi normale centrée réduite, `stats.norm.ppf(alpha)`, environ −1,6448 pour 5 %. C'est un nombre d'écarts types, négatif, et non un rendement : il le devient une fois multiplié par $\sigma$ et ajouté à $\mu$. [p. 33, Listing 2.2]

$\varphi$ est la densité de la loi normale centrée réduite, `stats.norm.pdf`. Le rapport $\varphi(z_\alpha)/\alpha$ est la distance moyenne, en écarts types, d'une variable normale centrée réduite conditionnée à tomber sous $z_\alpha$. [Listing 2.2]

## Ce qui la définit
La méthode remplace la loi des rendements par la loi normale de même moyenne et de même écart type : la VaR se situe alors à $|z_\alpha|$ écarts types sous la moyenne, et la CVaR, moyenne de la queue gaussienne, un peu plus loin. [Listing 2.2]

## Le chemin jusqu'ici
pfo/valeur-a-risque demande un quantile et pfo/valeur-a-risque-conditionnelle une moyenne de queue. Sous l'hypothèse normale, les deux ont une formule fermée, et deux nombres, la moyenne et l'écart type, suffisent à les calculer. [ajout]

## Exemple minimal
Avec $\mu = 0{,}05\,\%$ et $\sigma = 2\,\%$ par jour, au seuil de 5 % et pour un capital de 1 000 000, la VaR gaussienne vaut 32 397 et la CVaR gaussienne 40 754. [ajout]

## Geste de calcul type
$z_\alpha = -1{,}6449$, donc $\mathrm{VaR} = -(0{,}0005 - 1{,}6449 \times 0{,}02) \times 10^6 = 32\,397$ ; puis $\varphi(z_\alpha)/\alpha = 0{,}1031/0{,}05 = 2{,}0627$, donc $\mathrm{CVaR} = -(0{,}0005 - 0{,}02 \times 2{,}0627) \times 10^6 = 40\,754$. [ajout]

## Cesse d'être valide quand
Elle repose sur l'hypothèse que le chapitre réfute : des rendements normaux. [p. 19, §2.1]

Avec des queues épaisses et une asymétrie négative, elle sous-estime la perte extrême, et d'autant plus que le seuil est loin dans la queue. [ajout]
