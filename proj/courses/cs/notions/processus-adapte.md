---
id: cs/processus-adapte
nom: Processus adapté
type: notion
statut: source
construite_a_partir_de:
- cs/filtration
- cs/processus-stochastique
alias:
- adapted process
- processus adapté à une filtration
- non-anticipatif
refs:
- Déf. 0.5.9
---

## Ce que c'est
Un processus est adapté à une filtration quand, à chaque date, sa valeur est connue avec l'information disponible à cette date : il ne regarde pas l'avenir. [Déf. 0.5.9]

## Forme
$$\forall t\in\mathbb R_+ :\qquad X_t\ \text{ est }\ \mathcal F_t\text{-mesurable}$$ [Déf. 0.5.9]

## Ce que les symboles modélisent
« $X_t$ est $\mathcal F_t$-mesurable » se lit : connaître l'information $\mathcal F_t$ suffit pour connaître la valeur de $X_t$. Quand $\Omega$ est fini et que $\mathcal F_t$ le découpe en blocs, $X_t$ est constante sur chaque bloc. [Déf. 0.5.9, ajout]

## Ce qui la définit
**On connaît** l'information de chaque date, la filtration. **On demande** que la valeur du processus n'utilise jamais plus que cette information. C'est la condition qu'on imposera à une stratégie : décider à la date $t$ avec ce qu'on sait en $t$. [Déf. 0.5.9, ajout]

## Le chemin jusqu'ici
cs/processus-stochastique fournit une variable aléatoire par date, et cs/filtration une information par date ; être adapté, c'est que chacune de ces variables soit lisible avec l'information de sa propre date. [Déf. 0.5.1, Déf. 0.5.8, Déf. 0.5.9]

## Exemple minimal
Deux lancers, en $t=\tfrac12$ et $t=1$ ; un joueur mise $1$ sur $[0,\tfrac12[$, puis $2$ si le premier lancer donne pile et $0$ sinon : sa mise est adaptée. S'il misait déjà $2$ avant $\tfrac12$ quand le premier lancer va donner pile, elle ne le serait pas. [ajout]

## Geste de calcul type
Pour chaque date, se demander si la valeur de $X_t$ se calcule avec les seuls événements de $\mathcal F_t$ ; sur un $\Omega$ fini, vérifier que $X_t$ prend la même valeur sur toutes les issues d'un même bloc. [ajout]

## Cesse d'être valide quand
L'adaptation est une propriété date par date : elle ne dit rien de la mesurabilité en $(t,\omega)$ ensemble, et ne suffit pas, seule, à rendre $\int_0^tf(X_s)\,ds$ connue à la date $t$. Il faut pour cela la mesurabilité progressive. [Déf. 0.5.9, Déf. 0.5.10, ajout]
