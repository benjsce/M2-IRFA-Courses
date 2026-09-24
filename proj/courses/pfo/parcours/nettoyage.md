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

2. pfo/score-z
   Second défaut, plus difficile : repérer une valeur aberrante demande de dire à partir de quand un écart est anormal. [§1.3.2, p. 9]

3. pfo/filtre-z-score-glissant
   Appliqué aux rendements, l'outil doit suivre le marché : une moyenne et une dispersion calculées sur toute la série jugeraient mal les périodes agitées. [§1.3.2]

4. pfo/pipeline-d-ingestion
   Il reste à enchaîner ces opérations, et l'ordre dans lequel on les fait n'est pas indifférent. [Listing 1.1]

## Point d'arrivée
Le cours sort de ce nettoyage une série de rendements sans trou ni saut aberrant, celle que les parcours suivants utiliseront. Le filtre a un prix : un vrai krach peut être effacé comme une erreur. [ajout]
