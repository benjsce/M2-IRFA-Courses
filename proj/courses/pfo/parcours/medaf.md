---
id: pfo/parcours-medaf
ordre: 7
titre: Le rendement d'un actif est-il justifié par son risque ?
source: poly, chapitre 4, §4.1 à §4.3
---

## Point de départ
L'investisseur du récit précédent a retenu deux tiers dans le premier actif, qui rapporte 6 % avec une volatilité de 10 %, et un tiers dans le second, qui rapporte 10 % avec une volatilité de 20 %. Sur son marché, seuls ces deux actifs sont cotés : le premier compte 2 milliards d'actions à 10 €, le second 500 millions d'actions à 20 €. Il se demande ce que donnerait une règle qui ne calcule rien : détenir tout le marché, chaque actif dans la proportion où il existe. Combien mettrait-il alors dans chacun ? [ajout]

## À savoir avant
- pfo/piege-d-agregation : il autorise à écrire le rendement du marché comme la moyenne pondérée des rendements de ses deux actifs. [§1.2.2]
- pfo/matrice-de-covariance : elle fournit la covariance de chaque actif avec le marché et la variance du marché, dont le récit fait le rapport. [§1.5]
- pfo/portefeuille-tangent : c'est le mélange que l'investisseur a retenu au récit précédent ; ce récit montre qu'il coïncide ici avec le marché. [p. 40]
- dss/moindres-carres-ordinaires : le cours de data science en donne la méthode, choisir la droite qui rend minimale la somme des carrés des écarts ; le récit l'applique à des rendements. [ajout]
- pfo/p-valeur : elle traduit en probabilité l'écart d'une estimation à zéro, et dit si l'on peut rejeter un coefficient nul. [p. 26]

## Étapes
1. pfo/portefeuille-de-marche
   Le récit précédent a optimisé ; celui-ci part d'une règle qui ne demande ni rendement espéré ni covariance. [p. 57]
   Histoire : « détenir tout le marché, chaque actif dans la proportion où il existe » — Le marché vaut 20 + 10 = 30 milliards : le premier actif en pèse deux tiers, le second un tiers, alors que son action coûte deux fois plus cher. C'est exactement le mélange que l'optimisation lui avait donné. [ajout]

2. pfo/beta
   Le marché devient la référence ; reste à situer chaque actif par rapport à elle. [§4.2.1]
   Suite : Le second actif est bien plus volatil que le premier. Quand le marché monte de 1 %, de combien monte-t-il en moyenne ? [ajout]
   Histoire : « Quand le marché monte de 1 %, de combien monte-t-il en moyenne » — De 1,5 % : sa covariance avec le marché, $\tfrac13\times0{,}04=0{,}01333$, divisée par la variance du marché, $\tfrac49\times0{,}01+\tfrac19\times0{,}04=0{,}00889$, vaut 1,5. Le premier n'en suit que 0,75 %. [ajout]

3. pfo/medaf
   Le second actif porte plus de risque de marché ; il rapporte aussi davantage. [§4.2.1]
   Suite : Il rapporte 10 %, quatre points de plus que le premier. Ce surcroît est-il justifié par le risque qu'il fait porter ? [ajout]
   Histoire : « Ce surcroît est-il justifié par le risque qu'il fait porter » — Exactement. Le marché rapporte $\tfrac23\times6+\tfrac13\times10=7{,}33\,\%$, soit 5,33 points au-delà des 2 % ; un bêta de 1,5 en exige $2+1{,}5\times5{,}33=10\,\%$, un bêta de 0,75, 6 %. Les quatre points rémunèrent les 0,75 de bêta en plus, et non la volatilité propre du second actif. [ajout]

4. pfo/regression-du-medaf
   Ces chiffres supposent connus les vrais rendements espérés et les vrais bêtas. [p. 59]
   Suite : Or l'investisseur n'a que soixante mois de rendements des deux actifs. Comment en tirer le bêta du second ? [ajout]
   Histoire : « Comment en tirer le bêta du second » — En plaçant chaque mois comme un point, le rendement du marché au-delà du taux sans risque en abscisse, celui du second actif en ordonnée, et en ajustant la droite des moindres carrés : sa pente vaut 1,56, près du vrai 1,5. Sa hauteur en zéro, elle, n'est pas nulle. [ajout]

5. pfo/alpha-de-jensen
   Le MEDAF prédit une droite qui passe par zéro ; celle des données passe au-dessus. [p. 59]
   Suite : Sur ces soixante mois, le second actif a rapporté en moyenne 0,94 % par mois au-delà du taux sans risque, alors que son bêta ne lui en valait que 0,35 %. De combien a-t-il battu ce que le marché lui promettait ? [ajout]
   Histoire : « De combien a-t-il battu ce que le marché lui promettait » — De $0{,}938-1{,}556\times0{,}224=0{,}59\,\%$ par mois, environ 7 % par an : c'est la hauteur de la droite en zéro, ce que l'actif a gagné au-delà de son exposition au marché. [ajout]

6. pfo/statistique-t
   Un tel écart ferait du second actif une affaire, s'il était réel. [p. 76]
   Suite : Mais soixante mois, c'est peu. Cet écart est-il réel, ou le hasard des soixante mois ? [ajout]
   Histoire : « Cet écart est-il réel, ou le hasard des soixante mois » — Rien ne permet de l'affirmer : l'estimation, 0,59 %, ne fait que 0,97 fois son erreur type de 0,61 %, loin des 2 qu'exige un test à 5 %. La pente, elle, en fait 7,45 : le bêta est solidement établi, l'alpha ne l'est pas. [ajout]

7. pfo/coefficient-de-determination
   La droite situe bien l'actif, mais les mois s'en écartent beaucoup. [p. 63]
   Suite : Quelle part des variations du second actif le marché explique-t-il ? [ajout]
   Histoire : « Quelle part des variations du second actif le marché explique-t-il » — La moitié environ : la dispersion de ses rendements autour de leur moyenne vaut 2 477, et il en reste 1 266 autour de la droite, soit $1-1\,266/2\,477=0{,}49$. L'autre moitié est son risque propre, celui que le MEDAF ne rémunère pas. [ajout]

## Point d'arrivée
Sur ce marché, le second actif rapporte plus que le premier parce qu'il porte plus de risque de marché, un bêta de 1,5, et le MEDAF justifie ses 10 % au point près. Mesuré sur soixante mois, le bêta se retrouve à 1,56 avec assurance ; l'alpha de 0,59 % par mois ne se distingue pas de zéro ; et le marché n'explique que la moitié des variations de l'actif. [ajout]

Reste à savoir si cette autre moitié lui est vraiment propre. [ajout]
