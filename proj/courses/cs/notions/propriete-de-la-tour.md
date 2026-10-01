---
id: cs/propriete-de-la-tour
nom: Propriété de la tour
symbole: '$\mathcal G''$'
type: notion
statut: source
construite_a_partir_de:
- cs/esperance-conditionnelle
alias:
- tower property
- conditionnements successifs
- emboîtement des espérances conditionnelles
refs:
- Prop. 0.4.2 a)
- Prop. 0.4.2 e)
---

## Ce que c'est
Prévoir d'abord avec une information riche, puis avec une information plus pauvre, revient à prévoir directement avec la plus pauvre : c'est la plus petite information qui l'emporte. [Prop. 0.4.2 e)]

## Forme
$$\mathcal G'\subset\mathcal G\ \Rightarrow\ E\big[E[X|\mathcal G]\,\big|\,\mathcal G'\big]=E[X|\mathcal G']\quad P\text{-p.s.}$$ [Prop. 0.4.2 e)]

$$E\big[E[X|\mathcal G]\big]=E[X]$$ [Prop. 0.4.2 a)]

## Ce que les symboles modélisent
$\mathcal G'$ est une sous-tribu de $\mathcal A$ contenue dans $\mathcal G$ : une information plus pauvre, qui distingue moins d'événements. La seconde forme est le cas où $\mathcal G'$ est l'information vide, $\{\varnothing,\Omega\}$, sachant laquelle prévoir c'est prendre l'espérance. [Prop. 0.4.2 e), Prop. 0.4.2 a), ajout]

## Retrouver la formule
![Deux chemins, même arrivée, sur les deux lancers : en haut, X (2, 1, 1, 0) est moyenné sur chaque atome du premier lancer, ce qui donne E(X|𝒢) = 1,5 ou 0,5, puis sur Ω entier, ce qui donne 1 ; en bas, X est moyenné directement sur Ω entier, et donne 1. E(E(X|𝒢)|𝒢') = E(X|𝒢'), avec 𝒢' l'information vide.](figures/propriete-de-la-tour.svg) [ajout]

Deux lancers, $X$ le nombre de piles, $\mathcal G$ le premier lancer. Sachant $\mathcal G$, la prévision vaut $1{,}5$ ou $0{,}5$, chacune avec probabilité ½. [ajout]

On moyenne cette prévision sans aucune information : $\tfrac12\times1{,}5+\tfrac12\times0{,}5=1$. Directement, $E[X]=\tfrac14(2+1+1+0)=1$ : les deux chemins arrivent au même nombre. [ajout]

En général, il faut vérifier que $E[X|\mathcal G']$ satisfait la définition de l'espérance conditionnelle de $E[X|\mathcal G]$ sachant $\mathcal G'$ : pour $U$ $\mathcal G'$-mesurable, $U$ est aussi $\mathcal G$-mesurable, donc $E\big[E[X|\mathcal G]\,U\big]=E[XU]=E\big[E[X|\mathcal G']\,U\big]$. L'unicité conclut : [Déf. 0.4.1, ajout]

$$E\big[E[X|\mathcal G]\,\big|\,\mathcal G'\big]=E[X|\mathcal G']$$ [Prop. 0.4.2 e)]

## Ce qui la définit
Quand on prévoit en deux temps, le détail que $\mathcal G$ apporte en plus de $\mathcal G'$ se perd au second temps, puisqu'on moyenne de nouveau sur ce que $\mathcal G'$ ne distingue pas. Ce qui reste est la prévision avec la seule information commune, $\mathcal G'$. [Prop. 0.4.2 e), ajout]

## Le chemin jusqu'ici
cs/esperance-conditionnelle fournit les égalités $E[XU]=E[ZU]$ qui caractérisent une prévision ; la propriété de la tour les applique deux fois, en remarquant qu'un pari écrit avec l'information pauvre peut aussi s'écrire avec la riche. [Déf. 0.4.1]

## Exemple minimal
Deux lancers : $E\big[E[X|\mathcal G]\big]=\tfrac12\times1{,}5+\tfrac12\times0{,}5=1=E[X]$. [ajout]

## Geste de calcul type
Pour calculer une espérance difficile, conditionner d'abord par une information qui la rend facile, puis prendre l'espérance du résultat : $E[X]=E\big[E[X|\mathcal G]\big]$. Pour l'ordre des conditionnements, retenir que le plus petit gagne, quel que soit l'ordre dans lequel on les écrit. [Prop. 0.4.2 a), Prop. 0.4.2 e), ajout]

## Cesse d'être valide quand
Les deux informations ne sont pas emboîtées : si $\mathcal G'\not\subset\mathcal G$, $E\big[E[X|\mathcal G]\big|\mathcal G'\big]$ n'a en général rien à voir avec $E[X|\mathcal G']$. [Prop. 0.4.2 e)]
