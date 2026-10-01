---
id: cs/espace-l2-progressif
nom: Espace des processus progressifs de carré intégrable
symbole: '$L^2_{prog}(\Omega\times[0,T])$'
type: notion
statut: source
construite_a_partir_de:
- cs/espace-l2-des-processus
- cs/processus-progressivement-mesurable
alias:
- L²_prog(Ω × [0, T])
- processus progressifs de carré intégrable
refs:
- Déf. 0.5.11
---

## Ce que c'est
Les processus de carré intégrable sur $[0,T]$ qui, en plus, sont progressivement mesurables : ceux qui ne regardent pas l'avenir et dont la taille est finie. [Déf. 0.5.11]

## Forme
$$L^2_{prog}(\Omega\times[0,T])=\Big\{(X_t)_{t\in[0,T]}\ \text{progressivement mesurable} ;\ E\Big[\int_0^TX_s^2\,ds\Big]<\infty\Big\}$$ [Déf. 0.5.11]

## Ce que les symboles modélisent
$L^2_{prog}(\Omega\times[0,T])$ est une partie de $L^2(\Omega\times[0,T])$, avec la même norme, $\big(E\big[\int_0^TX_s^2\,ds\big]\big)^{1/2}$ ; l'indice $prog$ rappelle la contrainte d'information. [Déf. 0.5.11, ajout]

## Ce qui la définit
**On garde** la norme de $L^2(\Omega\times[0,T])$, qui mesure la taille d'un processus. **On restreint** aux processus progressivement mesurables, ceux qu'on saura intégrer contre le hasard sans regarder l'avenir. C'est l'espace des intégrandes de l'intégrale stochastique. [Déf. 0.5.11, ajout]

## Le chemin jusqu'ici
cs/espace-l2-des-processus fournit la norme et la structure d'espace de Hilbert, pour tout cs/processus-mesurable. cs/processus-progressivement-mesurable y ajoute la contrainte d'information : un cs/processus-stochastique lu avec cs/filtration, adapté au sens de cs/processus-adapte, et mesurable en $(t,\omega)$ sur chaque $[0,T]$ ; cs/processus-continu en donne le critère pratique. [Déf. 0.5.7, Déf. 0.5.10, Prop. 0.5.1]

L'espace réunit la norme et la contrainte, et la question devient de savoir s'il est encore complet. [Th. 0.5.2]

## Exemple minimal
La mise du joueur, $1$ sur $[0,\tfrac12[$ puis $2$ ou $0$ : elle est progressivement mesurable et de norme au carré $1{,}5$, donc dans $L^2_{prog}(\Omega\times[0,1])$. [ajout]

## Geste de calcul type
Vérifier les deux conditions séparément : la mesurabilité progressive, par le critère « continu et adapté » ou par la forme élémentaire ; puis la finitude de $E\big[\int_0^TX_s^2\,ds\big]$, en échangeant espérance et intégrale. [Prop. 0.5.1, ajout]

## Cesse d'être valide quand
Le processus regarde l'avenir, même s'il est de carré intégrable : il est dans $L^2(\Omega\times[0,T])$ mais pas dans $L^2_{prog}$. [Déf. 0.5.11, ajout]
