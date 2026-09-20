---
id: dup/aversion-a-la-deception
nom: Aversion à la déception
type: notion
statut: source
cas_de: dup/famille-chew-dekel
valeur: une pénalité sur les résultats inférieurs à l’équivalent certain
construite_a_partir_de:
- dup/equivalent-certain
alias:
- disappointment aversion
- Gul
refs:
- L3 slide 9
- L3 slide 10
- L3 slide 11
---

## Ce que c'est
Les résultats inférieurs à l’équivalent certain de la loterie elle-même sont surpondérés. [L3 slide 9]

## Forme
$$V(P)=\mathbb{E}_P[u(x)]-\alpha\,\mathbb{E}_P\big[(V(P)-u(x))_+\big],\qquad (z)_+=\max\{z,0\}$$ [L3 slide 10]

## Ce qui la définit
Le seuil de déception est endogène : c’est la valeur de la loterie choisie, pas un point de référence donné de l’extérieur. [L3 slide 10]

Une conséquence commune peut changer quels résultats déçoivent ; l’indépendance n’a alors plus lieu d’être, ce qui autorise une attirance particulière pour la certitude. [L3 slide 9]

## Le chemin jusqu'ici
Le socle commun mène à dup/equivalent-certain, et le choix de cette dépendance est tout le contenu de la fiche. [ajout]

La déception se définit par rapport à l'équivalent certain **de la loterie elle-même**. Le point de référence est donc endogène : il dépend de ce qu'on évalue. C'est ce qui rend la fonctionnelle implicite, et ce qui la distingue d'une simple pondération. [ajout]

## Exemple minimal
Avec $u(x)=x$ et $\alpha=1$, les quatre loteries d’Allais valent 2 385,15, 2 400, 494,01 et 491,57 : $B\succ A$ et $C\succ D$, exactement le motif observé. [L3 slide 11]

## Geste de calcul type
Poser $V$ inconnue, identifier les résultats sous $V$, écrire la moyenne pondérée $\big(\sum p_iw_iu_i\big)/\big(\sum p_iw_i\big)$ avec $w=1+\alpha$ sous le seuil, puis résoudre. [L3 slide 10, L3 slide 11]

## Cesse d'être valide quand
$\alpha=0$ redonne l’utilité espérée. L’intermédiarité seule ne caractérise pas le modèle : il faut un axiome de symétrie en plus. [L3 slide 9, L3 slide 10]
