---
id: dup/eu-locale
nom: Utilité espérée locale
symbole: $\Upsilon$
type: notion
statut: source
cas_de: dup/axiome-independance
valeur: une linéarité seulement locale, sans axiome de mélange global
construite_a_partir_de:
- dup/utilite-esperee
alias:
- local EU
- Machina
- utilité locale
refs:
- L1 slide 57
- L3 slide 13
- L3 slide 14
---

## Ce que c'est
Renoncer à l’indépendance globale et ne garder que la dérivabilité de la valeur en les probabilités. [L3 slide 13]

## Forme
$$V(P+\Delta P)-V(P)=\sum_i\Upsilon(x_i;P)\,\Delta p_i+o(\lVert\Delta P\rVert),\qquad \sum_i\Delta p_i=0$$ [L3 slide 13]

## Ce qui la définit
Les variations infinitésimales de probabilité s’évaluent comme sous utilité espérée, mais avec une utilité locale qui dépend de la loterie courante. Sous EU, $\Upsilon(x_i;P)=U(x_i)$ et la dépendance disparaît. [L3 slide 13, L1 slide 57]

C’est une approximation, jamais une indépendance exacte pour des mélanges finis : les courbes d’indifférence peuvent se courber. [L3 slide 13]

## Le chemin jusqu'ici
dup/loterie et dup/fonction-utilite donnent dup/utilite-esperee — les trois notions que presque tout ce cours suppose acquises. [ajout]

Même logique d'affaiblissement : on renonce à l'indépendance globale et on ne garde que la dérivabilité en les probabilités. L'utilité espérée reste au socle non comme hypothèse mais comme **point de comparaison** — localement, la fonctionnelle se comporte comme elle. [ajout]

## Exemple minimal
Pour $V(P)=\sum p_iu(x_i)+\tfrac{\eta}{2}\big(\sum p_iv(x_i)\big)^2$, l’utilité locale vaut $u(x_i)+\eta\big(\sum_j p_jv(x_j)\big)v(x_i)$, et $\eta=0$ redonne EU. [L3 slide 14]

## Geste de calcul type
Dériver $V$ par rapport à $p_i$ : le résultat est l’utilité locale, et c’est sur elle que se transposent tous les outils d’analyse du risque. [L3 slide 13, L1 slide 57]

## Cesse d'être valide quand
L’erreur d’approximation est quadratique en $\lVert\Delta P\rVert$ : le cadre est local, et ne dit rien des mélanges à poids finis. [L3 slide 14]
