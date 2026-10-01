---
id: cs/espace-l2-des-processus
nom: Espace des processus de carré intégrable
symbole: '$L^2(\Omega\times[0,T])$'
type: notion
statut: source
construite_a_partir_de:
- cs/processus-mesurable
alias:
- L²(Ω × [0, T])
- squared integrable stochastic processes
- processus de carré intégrable
refs:
- Déf. 0.5.7
---

## Ce que c'est
L'ensemble des processus mesurables dont le carré, intégré en temps sur $[0,T]$ puis en espérance, est fini ; c'est un espace de Hilbert. [Déf. 0.5.7]

## Forme
$$L^2(\Omega\times[0,T])=\Big\{(X_t)_{t\in[0,T]}\ \text{mesurable} ;\ E\Big[\int_0^TX_s^2\,ds\Big]<\infty\Big\}$$ [Déf. 0.5.7]

## Ce que les symboles modélisent
$L^2(\Omega\times[0,T])$ est l'espace des fonctions de carré intégrable sur le produit de l'aléa et du temps, pour la mesure $P\otimes ds$. La quantité $E\big[\int_0^TX_s^2\,ds\big]$ est le carré de la norme du processus, une seule mesure de taille qui somme les carrés sur toutes les dates et dans tous les mondes. [Déf. 0.5.7, ajout]

## Ce qui la définit
**On connaît** un processus mesurable. **On cherche** une distance entre processus, pour pouvoir parler d'approximation et de limite. La norme $\big(E\big[\int_0^TX_s^2\,ds\big]\big)^{1/2}$ la donne, et le produit scalaire $E\big[\int_0^TX_sY_s\,ds\big]$ fait de l'espace un espace de Hilbert, où les suites de Cauchy convergent. [Déf. 0.5.7, ajout]

## Le chemin jusqu'ici
cs/processus-stochastique donne une valeur par date et par monde ; cs/processus-mesurable rend légitime l'intégrale $\int_0^TX_s^2\,ds$, trajectoire par trajectoire, comme une variable aléatoire. On peut alors en prendre l'espérance, et la finitude de cette espérance définit l'espace. [Déf. 0.5.1, Déf. 0.5.6, Déf. 0.5.7]

## Exemple minimal
Sur $[0,1]$ avec la mesure de Lebesgue, $X_t(\omega)=\omega+t$ : $E\big[\int_0^1(\omega+s)^2\,ds\big]=\tfrac76$, fini ; $X$ est dans $L^2(\Omega\times[0,1])$. [ajout]

## Geste de calcul type
Échanger l'espérance et l'intégrale en temps, ce que permet Fubini pour une fonction positive mesurable, puis calculer $\int_0^TE[X_s^2]\,ds$. Ici $E[(\omega+s)^2]=\tfrac13+s+s^2$, et $\int_0^1\big(\tfrac13+s+s^2\big)ds=\tfrac13+\tfrac12+\tfrac13=\tfrac76$. [ajout]

## Cesse d'être valide quand
Le processus n'est pas mesurable : $\int_0^TX_s^2\,ds$ n'est alors pas une variable aléatoire, et la norme n'a pas de sens. Deux processus qui ne diffèrent que sur un ensemble de mesure $P\otimes ds$ nulle sont un même élément de l'espace. [Déf. 0.5.7, ajout]
