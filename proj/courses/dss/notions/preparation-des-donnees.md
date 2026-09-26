---
id: dss/preparation-des-donnees
nom: Préparation des données
type: notion
statut: source
construite_a_partir_de:
- dss/reseau-de-neurones-artificiel
alias:
- data preparation
refs:
- slide 187
- slide 189
- slide 190
---

## Ce que c'est
Consolider, nettoyer, sélectionner et transformer les données avant de les présenter au réseau. [slide 187]

## Ce qui la définit
Le cours donne un chiffre qui situe l'enjeu : 50 % à 70 % du temps de développement d'un réseau est consacré à la préparation des données. [slide 187]

Trois étapes, dans cet ordre : consolidation et nettoyage, sélection et prétraitement, transformation et codage. [slide 187]

Le nettoyage comprend l'élimination ou l'estimation des valeurs manquantes, le retrait des valeurs aberrantes, et la détermination des probabilités a priori des catégories pour traiter le biais de volume. [slide 189]

Le biais de volume est le cas d'une catégorie bien plus fréquente que les autres, que le réseau apprendrait à prédire par défaut. [ajout]

Le prétraitement réduit la dimension — retirer les attributs redondants ou corrélés, les combiner — et réduit l'étendue des valeurs. [slide 190]


## Le chemin jusqu'ici
Le cours traite la préparation comme une contrainte du dss/reseau-de-neurones-artificiel et non comme une étape générale : c'est parce que le réseau n'accepte que des nombres continus que le codage devient un sujet à part entière. [ajout]

Les données qu'on prépare sont des exemples étiquetés, au sens de dss/apprentissage-supervise : un objet d'entrée et la sortie désirée. Les deux se préparent, les entrées comme les catégories à prédire, dont le volume relatif compte. [ajout]

## Cesse d'être valide quand
La formule que le cours met en tête est aussi sa limite : déchets à l'entrée, déchets à la sortie. Aucune préparation ne rattrape une donnée qui ne porte pas l'information. [slide 187]
