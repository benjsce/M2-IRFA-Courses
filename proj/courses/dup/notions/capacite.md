---
id: dup/capacite
nom: Capacité
symbole: $\mu$
type: notion
statut: source
construite_a_partir_de:
- dup/aversion-a-l-ambiguite
alias:
- capacity
- croyance non additive
- cœur d'une capacité
refs:
- L4 slide 56
- L4 slide 58
---

## Ce que c'est
Une mesure des événements qui respecte l’ordre d’inclusion sans exiger que les poids de deux événements disjoints s’ajoutent. [L4 slide 56]

## Forme
$$\mu(\varnothing)=0,\quad\mu(S)=1,\quad A\subseteq B\Rightarrow\mu(A)\le\mu(B)$$ [L4 slide 56]

## Ce que les symboles modélisent
$\mu$ prend un événement — une partie de l'espace des états — et rend un nombre entre zéro et un. C'est une croyance, mais ce n'est pas une probabilité : rien n'oblige $\mu(A)$ et $\mu$ du complémentaire à faire un, et c'est ce jeu qui loge l'ambiguïté. $C(\mu)$ est son cœur : l'ensemble des probabilités ordinaires qui la majorent sur chaque événement, donc les lectures probabilistes compatibles avec elle. [L4 slide 56]

## Ce qui la définit
Une capacité est dite convexe, ou supermodulaire, quand $\mu(A\cup B)+\mu(A\cap B)\ge\mu(A)+\mu(B)$ pour tous événements. Son cœur $C(\mu)$ rassemble les probabilités qui la majorent sur chaque événement ; pour une capacité convexe sur un espace d’états fini, ce cœur est non vide et l’intégrale de Choquet coïncide avec l’espérance minimale sur lui. [L4 slide 56]

La capacité ajustée sur l’urne d’Ellsberg rend compte des choix observés sans être convexe pour autant : avec $\mu(R)=1/3$, $\mu(B)=\mu(G)=1/4$, $\mu(B\cup G)=2/3$ et $\mu(R\cup B)=1/2$, on a $\mu(R\cup B)<\mu(R)+\mu(B)$. Rendre compte de ces choix-là ne suffit donc pas à établir l’axiome d’aversion à l’ambiguïté dans sa forme générale. [L4 slide 58]

## Le chemin jusqu'ici
Il faut d’abord la construction subjective : dup/acte et dup/fonction-utilite se combinent en dup/utilite-esperee-subjective, que dup/principe-de-la-chose-sure rend possible et que dup/paradoxe-d-ellsberg met en défaut, d’où dup/aversion-a-l-ambiguite. [ajout]

La capacité est l’objet qu’on fabrique pour loger ce comportement. Elle n’a pas d’intérêt propre : on ne renonce à l’additivité qu’une fois établi que l’additivité empêche de représenter les choix observés. C’est pourquoi elle dépend du diagnostic et non l’inverse. [ajout]

## Exemple minimal
La capacité d’Ellsberg donne $1/4$ au bleu et $1/4$ au vert, mais $2/3$ à leur réunion : les poids ne s’ajoutent pas. [L4 slide 58]

## Geste de calcul type
Vérifier la monotonie sur chaque inclusion, puis tester la convexité sur les paires d’événements qui se recouvrent ; le défaut d’additivité se lit le plus vite sur un événement et son complémentaire. [L4 slide 56, L4 slide 58]

## Cesse d'être valide quand
La monotonie seule ne donne rien : sans convexité, le cœur peut être vide et la lecture maxmin de la capacité tombe. [L4 slide 56, L4 slide 60]
