---
id: pfo/parcours-nettoyage
ordre: 2
titre: Nettoyer les données avant de les croire
source: poly, §1.3, Listing 1.1
---

## Point de départ
On télécharge quatre ans de prix pour Apple, le CAC 40, le Nikkei et le Bitcoin. Le tableau a des trous les jours fériés de chaque place, et des sauts qui ne sont pas des mouvements de marché mais des erreurs. Tout modèle construit dessus en héritera. [p. 7, p. 10]

## À savoir avant
- pfo/rendement-logarithmique : c'est la série que le nettoyage protège. Le filtre ne regarde pas les prix mais les rendements, parce qu'eux seuls ont une moyenne locale stable. [Listing 1.1]

## Étapes
1. pfo/remplissage-des-valeurs-manquantes
   Premier défaut, avant tout calcul : des dates sans prix pour certains actifs. Que mettre à la place ? [p. 11, Listing 1.1]
   Histoire : « Le tableau a des trous les jours fériés de chaque place » — Un jour férié au Japon, le Nikkei n'a pas de prix alors que le Bitcoin en a un. On recopie le dernier prix connu : [100, NaN, NaN, 105] devient [100, 100, 100, 105], comme si le marché fermé n'avait pas bougé. [ajout]

2. pfo/score-z
   Second défaut, plus difficile : repérer une valeur aberrante demande de dire à partir de quand un écart est anormal. [§1.3.2, p. 9]
   Histoire : « des sauts qui ne sont pas des mouvements de marché mais des erreurs » — Pour dire qu'un saut est anormal, on le mesure en écarts types : un rendement de −4 % pour un actif de moyenne nulle et d'écart type 1 % est à 4 écarts types de sa moyenne, ce qui arrive rarement. [ajout]

3. pfo/filtre-z-score-glissant
   Appliqué aux rendements, l'outil doit suivre le marché : une moyenne et une dispersion calculées sur toute la série jugeraient mal les périodes agitées. [§1.3.2]
   Suite : Le Bitcoin varie bien plus que le CAC 40, et chacun s'agite plus en crise qu'en temps calme. Un même seuil peut-il juger toutes les périodes ? [ajout]
   Histoire : « Un même seuil peut-il juger toutes les périodes » — Oui, si la moyenne et l'écart type sont recalculés sur les vingt derniers rendements, et tout rendement à plus de trois écarts types de cette moyenne remplacé par 0. Pour une moyenne nulle, un −4 % dans une fenêtre qui, lui compris, a un écart type de 1 % est à 4 écarts types : il est effacé ; le même −4 % dans une fenêtre agitée, d'écart type 2 %, n'est qu'à 2 écarts types : il est gardé. [ajout]

4. pfo/pipeline-d-ingestion
   Il reste à enchaîner ces opérations, et l'ordre dans lequel on les fait n'est pas indifférent. [Listing 1.1]
   Histoire : « Tout modèle construit dessus en héritera » — La chaîne du cours télécharge les prix, comble les trous, calcule les rendements logarithmiques, puis filtre les sauts. L'ordre compte : combler avant de calculer, sinon chaque jour férié coupe la série ; filtrer après, parce que le filtre regarde les rendements et non les prix. [ajout]

## Point d'arrivée
Le cours sort de ce nettoyage une série de rendements sans trou ni saut aberrant, celle que les parcours suivants utiliseront. Le filtre a un prix : un vrai krach peut être effacé comme une erreur. [ajout]
