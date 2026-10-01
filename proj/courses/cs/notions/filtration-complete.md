---
id: cs/filtration-complete
nom: Filtration complète
symbole: '$\mathcal N$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-adapte
- cs/version-d-un-processus
alias:
- complete filtration
- complétion d'une filtration
- conditions habituelles
refs:
- Déf. 0.5.8
- Rem. 0.5.3
- Rem. 0.5.5
---

## Ce que c'est
Une filtration est complète quand chacune de ses tribus contient tous les événements négligeables ; le cours la suppose toujours complète, pour qu'un changement de probabilité nulle ne fasse rien perdre. [Déf. 0.5.8, Rem. 0.5.3]

## Forme
$$\forall t\in\mathbb R_+ :\ \mathcal N\subset\mathcal F_t,\qquad\mathcal N=\{N\subset\Omega ;\ \exists A\in\mathcal A,\ N\subset A,\ P(A)=0\}$$ [Déf. 0.5.8]

$$\text{sinon, on remplace }\mathcal F_t\text{ par }\sigma(\mathcal N\cup\mathcal F_t)$$ [Rem. 0.5.3]

## Ce que les symboles modélisent
$\mathcal N$ est l'ensemble des parties négligeables de $\Omega$ : celles qui sont contenues dans un événement de probabilité nulle. Les mettre dans $\mathcal F_t$, c'est décider qu'à toute date on « sait » qu'un événement impossible ne s'est pas produit. $\sigma(\mathcal N\cup\mathcal F_t)$ est la plus petite tribu qui contient à la fois l'information $\mathcal F_t$ et ces parties. [Déf. 0.5.8, Rem. 0.5.3, ajout]

## Ce qui la définit
**L'avantage**, selon les slides, est double. D'abord, si $X_t=Y_t$ presque sûrement et que $X_t$ est $\mathcal F_t$-mesurable, alors $Y_t$ l'est aussi : toute version d'un processus adapté est adaptée. Ensuite, une limite presque sûre de variables $\mathcal F_t$-mesurables est $\mathcal F_t$-mesurable. [Rem. 0.5.5]

Sans la complétion, modifier un processus sur un événement de probabilité nulle pourrait le rendre non adapté, alors que rien d'observable n'a changé. [Rem. 0.5.5, ajout]

## Le chemin jusqu'ici
cs/filtration fixe l'information de chaque date, et cs/processus-adapte demande qu'un cs/processus-stochastique soit lisible avec elle. De son côté, cs/version-d-un-processus fabrique des processus qui ont les mêmes valeurs presque sûrement à chaque date, donc la même loi au sens de cs/processus-de-meme-loi, mais qui diffèrent sur des ensembles négligeables. [Déf. 0.5.8, Déf. 0.5.9, Déf. 0.5.3]

La complétion fait que l'adaptation et la version s'accordent : une version d'un processus adapté reste adaptée. [Rem. 0.5.5]

## Exemple minimal
Avant tout lancer, l'information est vide, $\{\varnothing,\Omega\}$. Une mise qui vaut $5$ si la pièce va retomber sur la tranche, événement de probabilité nulle, et $1$ sinon, n'est pas mesurable pour cette tribu ; elle l'est pour sa complétion, qui contient l'événement négligeable « sur la tranche ». [ajout]

## Geste de calcul type
Devant une égalité presque sûre, conclure directement à la mesurabilité : si $Y_t=X_t$ p.s. et $X_t$ est $\mathcal F_t$-mesurable, $\{Y_t\in B\}$ ne diffère de $\{X_t\in B\}$ que par une partie négligeable, qui est dans $\mathcal F_t$. [Rem. 0.5.5, ajout]

## Cesse d'être valide quand
La filtration n'est pas complétée : les deux avantages tombent, et un énoncé du cours qui s'appuie sur eux demande alors une précaution supplémentaire. Le cours l'évite en complétant toujours. [Rem. 0.5.3, Rem. 0.5.5]
