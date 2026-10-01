---
id: cs/processus-progressivement-mesurable
nom: Processus progressivement mesurable
type: notion
statut: source
construite_a_partir_de:
- cs/processus-mesurable
- cs/processus-adapte
- cs/processus-continu
alias:
- progressively measurable process
- mesurabilité progressive
refs:
- Déf. 0.5.10
- Rem. 0.5.6
- Prop. 0.5.1
- §0.5 slide 11
---

## Ce que c'est
Un processus est progressivement mesurable quand, sur chaque intervalle $[0,T]$, il est mesurable en $(t,\omega)$ avec la seule information disponible en $T$ ; c'est ce qui rend $\int_0^tf(X_s)\,ds$ connue en $t$. [Déf. 0.5.10, §0.5 slide 11]

## Forme
$$\forall T>0 :\qquad(t,\omega)\in\big([0,T],\mathcal B([0,T])\big)\times(\Omega,\mathcal F_T)\ \longmapsto\ X_t(\omega)\in\big(\mathbb R,\mathcal B(\mathbb R)\big)\ \text{ est mesurable}$$ [Déf. 0.5.10]

## Ce que les symboles modélisent
La différence avec un processus mesurable tient à la tribu du côté de $\omega$ : $\mathcal F_T$, l'information de la date $T$, au lieu de $\mathcal A$, toute l'information. Et la condition porte sur la restriction du processus à $[0,T]$, pour chaque date $T$. [Déf. 0.5.10, Déf. 0.5.6, ajout]

## Ce qui la définit
C'est la fusion des deux exigences précédentes : mesurable en $(t,\omega)$, comme un processus mesurable, et ne regardant pas l'avenir, comme un processus adapté — mais les deux à la fois, sur tout le passé. Un processus progressivement mesurable est mesurable et adapté. [Déf. 0.5.10, Rem. 0.5.6]

Le gain est l'intégrale en temps : si $X$ est progressivement mesurable et $f$ continue bornée, $Y_t=\int_0^tf(X_s)\,ds$ est adapté, par le théorème de Fubini appliqué sur $[0,t]\times\Omega$ avec la tribu $\mathcal B([0,t])\otimes\mathcal F_t$. [§0.5 slide 11]

Le critère qu'on utilise en pratique : un processus continu et adapté est progressivement mesurable. [Prop. 0.5.1]

## Le chemin jusqu'ici
cs/processus-mesurable permet d'intégrer un cs/processus-stochastique en temps, mais avec toute l'information $\mathcal A$ ; cs/processus-adapte respecte l'information de cs/filtration, mais date par date. La mesurabilité progressive demande les deux ensemble, sur chaque intervalle $[0,T]$ avec l'information $\mathcal F_T$. [Déf. 0.5.6, Déf. 0.5.8, Déf. 0.5.9]

cs/processus-continu fournit le moyen de la vérifier en pratique : continu et adapté suffit. [Prop. 0.5.1]

## Exemple minimal
Le joueur qui mise $1$ sur $[0,\tfrac12[$, puis $2$ ou $0$ selon le premier lancer : sa mise est progressivement mesurable, et sa mise cumulée $\int_0^tX_s\,ds$ vaut $t$ avant $\tfrac12$, puis $\tfrac12+2(t-\tfrac12)$ ou $\tfrac12$ selon le lancer, une quantité connue à chaque date. [§0.5 slide 11, ajout]

## Geste de calcul type
Pour l'établir, chercher d'abord le critère : le processus est-il continu et adapté ? Sinon, l'écrire comme limite de processus élémentaires, dont la mesurabilité progressive se vérifie terme à terme sur $[0,T]$. [Prop. 0.5.1, §0.5 slide 11, ajout]

## Cesse d'être valide quand
Les trajectoires ne sont pas continues : le critère de la Prop. 0.5.1 ne s'applique plus, et l'adaptation jointe à la mesurabilité ne donne pas directement la mesurabilité progressive. Il faut alors l'établir à la main. [Prop. 0.5.1, ajout]

## Origine
- exercice cs/ex-0-5-4 : la mesurabilité progressive rend $\int_0^tf(X_s)\,ds$ adaptée, par Fubini sur $[0,t]\times\Omega$ [ajout]
