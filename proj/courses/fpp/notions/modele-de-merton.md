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
$S_T$ n'est pas ici le cours d'une action, mais la valeur de toute la firme à l'échéance de sa dette, aléatoire ; $F_T$ est sa valeur forward, connue aujourd'hui. [exos §2.1]

$D$ est le notionnel de la dette zéro-coupon, remboursé en $T$, et $l$, égal à $D/F_T$, le rapporte à la firme : c'est la mesure du levier dans ce modèle, nulle pour une firme sans dette. Ce n'est pas le levier $l_t=A_t/E_t$ du poly, qui vaut 1 pour une firme sans dette. [exos §2.1, ajout]

$E_0$ est la valeur des fonds propres aujourd'hui, et $D^r$ celle de la dette risquée, ce que les créanciers paient pour elle ; $s$ est le spread de crédit, l'écart entre le taux auquel la firme emprunte et le taux sans risque, tel que $D^r=De^{-(r+s)T}$. [exos §2.1, exo. 16]

$P(T,F_T)$ est, dans le livre, le prix du put de strike $D$ sur la firme : malgré ses deux arguments, ce n'est pas un zéro-coupon $P(t,T)$. [exo. 16, ajout]

## Retrouver la formule
![La valeur finale de la firme partagée entre créanciers et actionnaires, avec une dette de 80 pour une firme de valeur forward 100. La bande du bas est la dette, qui reçoit au plus $D$ ; celle du haut, les fonds propres, a le payoff d'un call de strike $D$ ; leur somme est la diagonale, le bilan. En haut à gauche, le trou : ce que la dette perd sous $D$ en cas de faillite, $(D-S_T)^+$, le payoff d'un put vendu aux actionnaires.](figures/modele-de-merton.svg) [ajout]

Ce qui est **connu** : la valeur forward de la firme, $F_T=100$ ; la dette promise, $D=80$, due dans un an ; la volatilité de la firme, 20 % ; un taux nul. Ce qu'on **cherche** : le spread $s$, le supplément de taux qui paie le risque de faillite. [exo. 16, ajout]

La firme est financée par des fonds propres et par une seule dette zéro-coupon ; elle fait faillite si $S_T<D$. Les créanciers sont payés en premier : $D$, ou toute la firme en cas de faillite. Les actionnaires reçoivent le reste, $(S_T-D)^+$ : le payoff d'un call de strike $D$ sur la firme. [exos §2.1, exo. 16]

Les créanciers reçoivent donc $\min(S_T,D)$, que la figure lit comme la dette promise moins ce qu'elle perd sous $D$ : $D-(D-S_T)^+$. Détenir la dette risquée, c'est détenir la dette sans risque et avoir vendu aux actionnaires un put de strike $D$ ; ce put est le trou. [exo. 16]

Par la formule de Black et Scholes, ce put vaut 1,186. La dette risquée vaut donc $D^r=80-1{,}186=78{,}814$, au lieu des 80 qu'elle vaudrait sans risque de faillite. [ajout]

Le spread est ce manque exprimé en taux : $80\,e^{-s}=78{,}814$, soit $s=\ln(80/78{,}814)=1{,}49\,\%$. [ajout]

En lettres : $D^r=De^{-rT}-P(T,F_T)$, avec $P(T,F_T)=e^{-rT}F_T\big[l\,N(-d_2)-N(-d_1)\big]$ par la formule de Black. On égale à $De^{-(r+s)T}$ et on divise par $De^{-rT}=e^{-rT}lF_T$ : $e^{-sT}=1-N(-d_2)+\frac{1}{l}N(-d_1)=N(d_2)+\frac{1}{l}N(-d_1)$. [exo. 16]

$$s=-\frac{1}{T}\ln\!\Big(N(d_2)+\frac{1}{l}N(-d_1)\Big)$$ [exo. 16]

## Ce qui la définit
Le modèle n'invente aucun contrat : il lit le bilan en options. Les fonds propres sont un call de strike $D$ sur la firme, que la formule de Black et Scholes évalue en $E_0$ ; la dette risquée est la dette sans risque moins un put ; le spread est le prix de ce put, réexprimé en taux. [exo. 16]

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

Le livre affirme que $s\to+\infty$ quand $l\to1$ ; sa propre formule donne pourtant un spread fini en $l=1$, 8,3 % pour $\sigma=20\,\%$ et $T=1$, et ne diverge que quand $l\to\infty$, comme $\ln l/T$. [exo. 16, ajout]
