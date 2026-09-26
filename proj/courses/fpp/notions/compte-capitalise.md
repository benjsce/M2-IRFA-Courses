---
id: fpp/compte-capitalise
nom: Compte capitalisé
symbole: $B(t_i,t_j)$
type: notion
statut: source
construite_a_partir_de:
- fpp/zero-coupon
alias:
- accumulated bank account
- placement renouvelé
- placement roulé
refs:
- §4.2.2
- Prop. 4
---

## Ce que c'est
Le produit des prix des zéro-coupons courts successifs entre deux dates, facteur d'actualisation d'un placement renouvelé à chaque période. [§4.2.2]

## Forme
$$B(t_i,t_j)=\prod_{k=i}^{j-1}P(t_k,t_{k+1})$$ [§4.2.2]

## Ce que les symboles modélisent
$B(t_i,t_j)$ est vu depuis $t_i$ : seul le premier facteur, $P(t_i,t_{i+1})$, y est connu ; les autres se découvrent un à un. Placer 1 en $t_i$ et renouveler le placement à chaque période rapporte $1/B(t_i,t_j)$ en $t_j$. Le poly l'appelle compte bancaire, bien que ce soit un facteur d'actualisation, inférieur à 1. Ce n'est ni le $B_t$ de la capitalisation ni le prix d'obligation $B(r^*,r)$. [§4.2.2, §2.1, Ex. 1]

## Ce qui la définit
Ce qui est **connu** aujourd'hui : le prix du zéro-coupon qui couvre la première période. Ce qui est **inconnu** : ceux des suivantes. Le zéro-coupon long $P(t_i,t_j)$ fixe tout le trajet dès le départ ; le compte capitalisé le découvre pas à pas. [§4.2.2, ajout]

Si les taux sont connus d'avance, les deux coïncident : $B(t,T)=P(t,T)$. [Prop. 4]

![Deux façons d'aller de t₀ à t₂. En haut, un seul zéro-coupon, P(t₀,t₂), connu dès t₀. En bas, deux placements successifs : P(t₀,t₁) est connu, P(t₁,t₂) ne le sera qu'en t₁ ; leur produit est B(t₀,t₂).](figures/compte-capitalise.svg) [ajout]

## Le chemin jusqu'ici
fpp/zero-coupon fournit chaque facteur, sur une période courte. Enchaîner ces périodes est de la capitalisation au sens de fpp/capitalisation, mais à des taux que l'on ne connaît pas encore. [ajout]

## Exemple minimal
Le zéro-coupon à six mois cote 0,9802 ; si, dans six mois, le taux à six mois est de 6 %, le suivant cotera 0,9704, et $B=0{,}9512$, contre 0,9608 pour le zéro-coupon à un an. [ajout]

## Geste de calcul type
Multiplier les zéro-coupons courts à mesure qu'ils sont connus ; l'inverse du produit est ce qu'est devenu 1 placé au départ : $1/0{,}9512=1{,}0513$. [§4.2.2, ajout]

## Cesse d'être valide quand
Quand les taux sont déterministes, le compte capitalisé n'apprend rien que le zéro-coupon ne sache déjà : $B=P$. [Prop. 4]
