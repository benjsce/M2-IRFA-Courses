---
id: dss/selection-de-variables
nom: Sélection de variables
type: principe
statut: source
construite_a_partir_de:
- dss/moindres-carres-ordinaires
- dss/interpretabilite
alias:
- feature selection
- variable selection
refs:
- slide 27
- slide 28
---

## Ce que c'est
Remplacer l'ajustement par moindres carrés sur tous les prédicteurs par une procédure qui en réduit le nombre effectif. [slide 25, slide 28]

## Ce qui la définit
Aux deux vrais prédicteurs des 20 clients, l'endettement et le revenu, on ajoute trois variables tirées au hasard. **Ce qui est connu** : l'erreur moyenne sur ces 20 clients, qui baisse à chaque variable ajoutée, de 1,12 à 0,98. **Ce qu'on cherche** : l'erreur sur des clients nouveaux, qu'on ne voit pas ; mesurée sur 20 000, elle monte de 1,16 à 1,83. Sélectionner, c'est choisir les variables sans voir ce trou. [ajout]

Le cours le dit ainsi : des variables bien choisies améliorent le modèle, trop de variables le font surapprendre. [slide 27]

Deux raisons, et elles ne sont pas de même nature : la précision de prédiction, qui se dégrade quand $n$ n'est pas beaucoup plus grand que $p$, et l'interprétabilité, qui se dégrade dès que des variables sans effet restent dans le modèle. [slide 25, slide 26]

Le cours range les méthodes en familles sur une seule slide, et toutes réduisent le nombre effectif de prédicteurs : en en retirant, en tirant leurs coefficients vers zéro, ou en projetant les prédicteurs sur quelques combinaisons. [slide 28]

## Le chemin jusqu'ici
Deux fils y mènent. dss/moindres-carres-ordinaires, ajustés sur les couples de prédicteurs et de réponse que fournit dss/apprentissage-supervise, sont la méthode à améliorer ; dss/interpretabilite apporte la seconde raison de le faire, la lecture du modèle. [ajout]

## Cesse d'être valide quand
La sélection pas à pas ne garantit pas de trouver le meilleur sous-ensemble ; la recherche exhaustive, qui ajuste toutes les combinaisons, le garantit à chaque taille, mais son coût explose avec $p$. Dans tous les cas, le choix final repose sur une estimation de l'erreur de test. [slide 29, slide 36, slide 56, ajout]
