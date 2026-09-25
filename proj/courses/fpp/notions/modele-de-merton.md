---
id: fpp/modele-de-merton
nom: Modèle de Merton
symbole: '$s$, $l$, $D^r$, $F_T$'
type: notion
statut: source
construite_a_partir_de:
- fpp/responsabilite-limitee
- fpp/parite-call-put
- fpp/formule-black-scholes
alias:
- Merton model of the firm
- modèle structurel du crédit
refs:
- exos §2.1
- exo. 16
---

## Ce que c'est
Une lecture du bilan d'une entreprise endettée en options : les fonds propres sont un call sur la valeur de la firme, de strike la dette, et le risque de faillite devient un prix. [exos §2.1, exo. 16]

## Forme
$$E_0=e^{-rT}F_T\big[N(d_1)-l\,N(d_2)\big],\qquad s=-\frac{1}{T}\ln\!\Big(N(d_2)+\frac{1}{l}N(-d_1)\Big),\qquad d_{1,2}=\frac{-\ln l\pm\tfrac{\sigma^2T}{2}}{\sigma\sqrt T}$$ [exo. 16]

## Ce que les symboles modélisent
$F_T$ est la valeur forward de la firme à l'échéance de sa dette. $l$ rapporte à elle le notionnel $D$ de la dette, $l=D/F_T$ : c'est la mesure du levier dans ce modèle. [exos §2.1]

$E_0$ est la valeur des fonds propres aujourd'hui, et $D^r$ celle de la dette risquée, ce que les créanciers paient pour elle ; $s$ est le spread de crédit, l'écart entre le taux auquel la firme emprunte et le taux sans risque, tel que $D^r=De^{-(r+s)T}$. [exos §2.1, exo. 16]

## Ce qui la définit
La firme vaut $S_T$ à l'échéance ; elle est financée par des fonds propres et par une seule dette zéro-coupon de notionnel $D$ ; elle fait faillite si $S_T<D$. Les créanciers sont payés en premier : ils reçoivent $D$, ou toute la firme en cas de faillite. Les actionnaires reçoivent le reste, $(S_T-D)^+$. [exos §2.1]

Ce reste est le payoff d'un call sur la valeur de la firme, de strike la dette, et la formule de Black et Scholes en donne la valeur. [exo. 16]

L'identité du bilan force les créanciers à détenir le complément, $S_T-(S_T-D)^+$. La parité call-put le réécrit : détenir la dette risquée, c'est détenir la dette sans risque et avoir vendu un put aux actionnaires, $D^r=De^{-rT}-P(T,F_T)$. Le spread est le prix de ce put, réexprimé en taux. [exo. 16]

## Le chemin jusqu'ici
Trois fils du cours se rejoignent ici, et aucun outil nouveau ne s'y ajoute : le modèle reconnaît dans un bilan des contrats déjà connus. [ajout]

**L'entreprise.** fpp/bilan fait apparaître fpp/levier, que fpp/volatilite rend risqué pour l'actionnaire ; fpp/responsabilite-limitee pose un plancher sous sa perte, un profil d'option que rien ne permettait encore d'évaluer. [ajout]

**Les contrats.** fpp/payoff décrit ce que chacun reçoit ; fpp/option, fpp/call et fpp/put nomment les formes de ce paiement, et fpp/parite-call-put, qui actualise le strike par fpp/facteur-actualisation, bâti sur fpp/convention-capitalisation, découpe la dette en une part sûre et un put vendu. [ajout]

**Le prix.** fpp/replication-statique et fpp/portage conduisent à fpp/prix-a-terme puis à fpp/mesure-risque-neutre ; avec fpp/echelonnement-de-la-variance et fpp/transformee-de-laplace-gaussienne, on arrive à fpp/modele-black-scholes, dont fpp/formule-black-scholes chiffre chaque pièce du bilan. [ajout]

## Exemple minimal
Pour $\sigma=20\,\%$, $T=1$, $r=0$ et une dette égale à 80 % de la valeur forward de la firme, le spread vaut environ 149 points de base et les fonds propres 21,2 % de $F_T$. [ajout]

## Geste de calcul type
Avec $l=0{,}8$ et $\sigma\sqrt T=0{,}2$ : $d_1=(-\ln 0{,}8+0{,}02)/0{,}2=1{,}2157$ et $d_2=1{,}0157$, d'où $N(d_2)=0{,}8451$ et $N(-d_1)/l=0{,}1120/0{,}8=0{,}1401$. Leur somme vaut $0{,}9852$, et $s=-\ln 0{,}9852=1{,}49\,\%$. Contrôle par le bilan : fonds propres $0{,}2119\,F_T$ et dette risquée $0{,}7881\,F_T$ font bien $F_T$. [ajout]

## Ce qui reste libre
| paramètre | cas | effet |
|---|---|---|
| levier $l$ | $l\to0$ | $s\to0$ : la dette devient sans risque |
| volatilité $\sigma$ | $\sigma$ augmente | le call monte, donc les fonds propres ; le put aussi, donc la dette risquée baisse |
| dividende intermédiaire | versé aux actionnaires | la valeur forward baisse, le put monte, le spread monte |
[exo. 16]

Les actionnaires ont donc intérêt à ce que la firme prenne plus de risque, aux dépens des créanciers. [exo. 16]

## Cesse d'être valide quand
Le modèle suppose une dette unique, zéro-coupon, et une faillite qui ne peut survenir qu'à son échéance ; la valeur de la firme n'est pas observable, et sa volatilité non plus. [ajout]

Le livre affirme que $l=1$ correspond à une firme infiniment endettée et que $s\to+\infty$ quand $l\to1$. [exos §2.1, exo. 16]

Sa propre formule le dément : en $l=1$, $d_2=-d_1$ et le spread est fini. Il ne croît sans borne que quand $l\to\infty$, où il s'approche de $\ln l/T$. [ajout]

Le symbole $l$ désigne ici $D/F_T$, et non le levier $l_t=A_t/E_t$ du poly, qui vaut 1 pour une firme sans dette. [ajout]
