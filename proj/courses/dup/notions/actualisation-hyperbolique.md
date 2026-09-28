---
id: dup/actualisation-hyperbolique
nom: Actualisation hyperbolique
symbole: '$\alpha$, $\gamma$'
type: notion
statut: source
cas_de: dup/utilite-actualisee
construite_a_partir_de:
- dup/biais-pour-le-present
alias:
- hyperbolic discounting
- impatience fortement décroissante
- strongly diminishing impatience
refs:
- L5 slide 15
---

## Ce que c'est
Une actualisation dont l'impatience diminue à chaque pas qu'on s'éloigne d'aujourd'hui, et non au seul premier pas. [L5 slide 15]

## Forme
$$D(\tau)=(1+\alpha\tau)^{-\gamma/\alpha},\qquad \alpha,\gamma>0$$ [L5 slide 15]

## Ce que les symboles modélisent
$\alpha$ règle la vitesse à laquelle l'impatience s'émousse avec le délai, $\gamma$ son niveau ; quand $\alpha$ tend vers 0, $D$ tend vers l'exponentielle $e^{-\gamma\tau}$. Ces deux lettres n'ont rien à voir avec l'aversion relative $\gamma$ de CRRA ni avec le coefficient $\alpha$ de l'utilité quadratique. [L5 slide 15, ajout]

## Ce qui la définit
Elle a une **impatience fortement décroissante** : le prix d'une attente de longueur $\tau$, $D(t)/D(t+\tau)$, décroît strictement avec la date $t$ où l'attente commence. C'est plus fort que le biais pour le présent, qui ne compare que $t=0$ et $t>0$. [L5 slide 15]

![Le prix d'une attente de quatre semaines, D(t)/D(t+4), selon la semaine t où elle commence, avec u(x) = x : au-dessus de 110/100, on prend 100 en t plutôt que 110 en t + 4 ; en dessous, on attend. Exponentiel à δ = 1 : toujours 1. Quasi-hyperbolique à β = ½, δ = 1 : 2 en 0, puis 1. Hyperbolique à α = γ = 0,05 : 1,19 à la semaine 1, 1,09 à la semaine 26 ; il baisse à chaque semaine, c'est l'impatience fortement décroissante](figures/actualisation-hyperbolique.svg) [ajout]

## Le chemin jusqu'ici
dup/biais-pour-le-present compare seulement l'attente qui part d'aujourd'hui aux autres. Des choix qui renversent aussi l'attente partant de la semaine 1 demandent que ce prix baisse encore ensuite, sur une fonction de dup/utilite-actualisee. dup/actualisation-exponentielle, que dup/inversion-des-preferences-dans-le-temps avait déjà mise en défaut, reste le cas limite où il ne baisse jamais, les utilités restant celles de dup/fonction-utilite. [L5 slide 15]

## Exemple minimal
Avec $\alpha=\gamma=0{,}05$ par semaine, $D(\tau)=1/(1+0{,}05\,\tau)$ : attendre de la semaine 1 à la semaine 5 coûte $D(1)/D(5)=1{,}25/1{,}05\approx1{,}19$, de la semaine 26 à la semaine 30 seulement $2{,}5/2{,}3\approx1{,}09$. [ajout]

## Geste de calcul type
Calculer $D(t)/D(t+\tau)=\left(\dfrac{1+\alpha(t+\tau)}{1+\alpha t}\right)^{\gamma/\alpha}$ aux deux dates de départ à comparer : le rapport est plus petit à la plus lointaine. [ajout]

## Cesse d'être valide quand
Elle n'est pas cohérente entre deux dates futures : la façon dont elle arbitre entre les semaines 26 et 30 change à mesure qu'elles approchent. Le cours lui préfère donc le modèle quasi-hyperbolique, qui n'en garde que le trait principal, le biais pour le présent. [L5 slide 15, L5 slide 42]
