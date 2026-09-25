---
id: pfo/rendement-arithmetique
nom: Rendement arithmétique
symbole: '$P_t$, $R_t$, $R_{0\to T}$'
type: notion
statut: source
cas_de: pfo/passage-aux-rendements
construite_a_partir_de: []
alias:
- arithmetic return
- rendement simple
- simple return
refs:
- §1.2.1
- éq. 1.4
---

## Ce que c'est
La variation relative du prix sur une période, rapportée au prix de départ. [éq. 1.4]

## Forme
$$R_{0\to T} = \dfrac{P_T - P_0}{P_0} = \prod_{t=1}^{T}(1+R_t) - 1$$ [éq. 1.4]

## Ce que les symboles modélisent
$P_t$ est le prix de l'actif à la date $t$ ; dans les listings du cours, c'est le prix de clôture ajusté des dividendes et des divisions d'actions, pas un prix affiché dans le carnet d'ordres. [§1.2, p. 11]

$R_t$ est le rendement d'une seule sous-période, $R_{0\to T}$ celui de la période entière. Le second ne s'obtient pas en additionnant les premiers mais en composant les facteurs $1+R_t$. [éq. 1.4]

La sous-période $t$ va de $t-1$ à $t$ : $R_t$ vaut $R_{t-1\to t}$, et non $R_{0\to t}$. [ajout]

$$R_t=\dfrac{P_t-P_{t-1}}{P_{t-1}},\qquad 1+R_t=\dfrac{P_t}{P_{t-1}}$$ [ajout]

Le produit donne bien le rendement de la période entière parce qu'il se télescope : chaque prix intermédiaire apparaît une fois au numérateur et une fois au dénominateur. [ajout]

$$\prod_{t=1}^{T}(1+R_t)=\dfrac{P_1}{P_0}\cdot\dfrac{P_2}{P_1}\cdots\dfrac{P_T}{P_{T-1}}=\dfrac{P_T}{P_0}$$ [ajout]

## Ce qui la définit
Le rendement arithmétique n'est pas additif dans le temps : le rendement de la période entière est le produit des facteurs de croissance, moins un, et non la somme des rendements. [§1.2.1, éq. 1.4]

En contrepartie, il s'agrège linéairement entre actifs : le rendement arithmétique d'un portefeuille est exactement la moyenne pondérée de ceux de ses composantes. [§1.2.2, éq. 1.7]

## Exemple minimal
Un prix qui passe de 100 à 110 puis à 99 fait +10 %, puis −10 %, et −1 % sur l'ensemble. [ajout]

## Geste de calcul type
Composer, ne pas additionner : $(1+0{,}10)(1-0{,}10)-1 = 0{,}99-1 = -1\,\%$, alors que la somme des deux rendements vaut 0. [ajout]

## Cesse d'être valide quand
Rien dans le périmètre du cours ne limite sa définition ; c'est son usage qui se trompe, dès qu'on additionne les rendements arithmétiques de périodes successives. [§1.2.1]
