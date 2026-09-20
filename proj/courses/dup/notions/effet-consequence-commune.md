---
id: dup/effet-consequence-commune
nom: Effet de conséquence commune
type: notion
statut: source
cas_de: dup/violation-de-l-independance
valeur: une conséquence commune que l’on remplace par une autre
construite_a_partir_de:
- dup/utilite-esperee
alias:
- paradoxe d'Allais
- Allais paradox
- common consequence effect
refs:
- L1 slide 42
- L1 slide 43
- L2 slide 5
- L2 slide 6
---

## Ce que c'est
Remplacer une conséquence commune aux deux options par une autre renverse le choix, alors que l’indépendance l’interdit. [L1 slide 42]

## Forme
$$a_1\succ a_2\iff .11\,U(1)>.10\,U(5)+.01\,U(0),\qquad a_3\succ a_4\iff .10\,U(5)+.01\,U(0)>.11\,U(1)$$ [L1 slide 43]

## Ce qui la définit
Les deux inégalités finales se contredisent exactement : le même terme apparaît des deux côtés avec le sens opposé. Aucune fonction $U$ ne peut satisfaire les deux. [L1 slide 43]

Le trait qui déclenche la violation est le passage de la certitude à une petite chance de ne rien avoir : c’est l’effet de certitude. [L1 slide 43]

## Le chemin jusqu'ici
Il faut d'abord disposer de la théorie que l'effet met en défaut : dup/loterie, dup/fonction-utilite, et dup/utilite-esperee qui les combine. [ajout]

Ici se joue quelque chose qui vaut pour toute la série des paradoxes : **une violation a besoin de la théorie qu'elle viole.** L'effet de conséquence commune n'est pas un fait brut sur des choix ; c'est un écart, et un écart se mesure par rapport à une prédiction. L'utilité espérée est au socle comme la règle graduée est au socle d'une mesure d'erreur. [ajout]

## Exemple minimal
Beaucoup préfèrent 1 M sûr à $(5\text{M},{,}10;1\text{M},{,}89;0,{,}01)$, et pourtant $(5\text{M},{,}10;0,{,}90)$ à $(1\text{M},{,}11;0,{,}89)$. [L1 slide 42]

## Geste de calcul type
Écrire les quatre loteries avec la même conséquence commune de probabilité 0,89, l’effacer des deux côtés, et constater que les deux préférences donnent deux inégalités opposées sur les mêmes trois termes. [L1 slide 43]

## Cesse d'être valide quand
C’est un fait expérimental, pas un théorème : la question ouverte est de savoir quelle pièce du modèle il faut relâcher pour en rendre compte. [L1 slide 70]
