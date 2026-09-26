---
id: fpp/parcours-strategies
ordre: 7
titre: Assembler des options en produits
source: poly, §9
---

## Point de départ
Un épargnant place 100 et veut profiter d'une hausse de l'action sans risquer sa mise. Aucun call ni aucun put ne lui donne cela seul. [§9.2]

Avec un zéro-coupon à un an à 0,9608, il lui suffit de 96,08 pour garantir ses 100 : il lui reste 3,92 pour s'exposer à la hausse. [ajout]

## À savoir avant
- fpp/payoff : c'est ce qu'on assemble ; un produit se décrit d'abord par ce qu'il paiera. [§9.1]
- fpp/call : c'est la brique qui donne la hausse, dans le produit protégé comme dans la vente de calls. [§9.2, §9.3]
- fpp/put : c'est l'autre brique qu'on peut vendre pour encaisser une prime ; l'histoire vend un call, mais vendre un put relève de la même amélioration de rendement. [§9.3]
- fpp/facteur-actualisation : c'est le prix du zéro-coupon qui rend la mise dans le produit protégé. [§9.2]

## Étapes
1. fpp/strategie-optionnelle
   Des briques élémentaires, on peut tirer des profils de gain qu'aucune ne donne seule, et leur prix s'additionne. [§9.1]
   Histoire : « Aucun call ni aucun put ne lui donne cela seul » — Assemblés, avec un zéro-coupon ou l'action, ils peuvent le faire : le profil d'un assemblage est la somme des profils de ses briques, et son prix la somme de leurs prix. [ajout]

2. fpp/produit-a-capital-protege
   Le produit du point de départ se construit avec deux de ces briques. [§9.2]
   Histoire : « il lui reste 3,92 pour s'exposer à la hausse » — Les 96,08 placés en zéro-coupon rendent 100 dans un an ; les 3,92 achètent des calls de strike 100, à 9,93 l'unité, soit environ 0,39 call. L'épargnant reçoit ainsi 39 % de la hausse au-delà de 100, et jamais moins que sa mise. [ajout]

3. fpp/amelioration-de-rendement
   Et du côté de celui qui vend ces briques, que gagne-t-on, et en échange de quoi ? [§9.3]
   Suite : De l'autre côté, un investisseur qui détient déjà l'action accepterait de renoncer à une partie de la hausse contre un revenu certain, touché aujourd'hui. Que peut-il vendre, et que gagne-t-il ? [ajout]
   Histoire : « Que peut-il vendre, et que gagne-t-il » — Il vend le call à la monnaie, c'est-à-dire de strike égal au cours actuel, 100, et encaisse 9,93 tout de suite ; en échange, il abandonne toute la hausse au-delà de 100. La hausse que l'épargnant achète d'un côté, c'est ce vendeur qui la cède de l'autre. [ajout]

## Point d'arrivée
Un produit structuré se lit comme une somme de briques ; son prix est la somme de leurs prix, et ce qui est protégé d'un côté est porté de l'autre. [§9.1, §9.3]
