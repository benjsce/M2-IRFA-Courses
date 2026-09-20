---
id: dss/smote
nom: SMOTE
type: notion
statut: source
construite_a_partir_de:
- dss/preparation-des-donnees
alias:
- SMOTE
- synthetic minority over-sampling technique
refs:
- slide 229
---

## Ce que c'est
Sur-échantillonner la classe minoritaire en fabriquant des observations synthétiques. [slide 229]

## Ce qui la définit
Le déséquilibre des classes est un problème de préparation, pas de modèle : un classifieur entraîné sur un jeu où une classe est rare apprend surtout à prédire l'autre. [ajout]

La technique ne duplique pas les observations rares, elle en construit de nouvelles. C'est ce qui la sépare d'un simple sur-échantillonnage. [slide 229]

Dans l'étude sur les biais, elle sert à rendre comparables des sous-échantillons de tailles très inégales avant de tester si une variable protégée est prédictible. [slide 227, slide 229]


## Le chemin jusqu'ici
dss/apprentissage-supervise, dss/reseau-de-neurones-artificiel, puis dss/preparation-des-donnees. [ajout]

SMOTE est une opération de préparation et non un modèle : elle agit sur le jeu avant l'apprentissage, ce qui explique qu'elle hérite de ce chemin plutôt que de celui des méthodes. [ajout]

## Cesse d'être valide quand
Les observations synthétiques n'apportent aucune information nouvelle : elles rééquilibrent le compte, elles ne remplacent pas des données manquantes. Le cours ne discute pas ce que cela fait aux mesures de performance. [ajout]
