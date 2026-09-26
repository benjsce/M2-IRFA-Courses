---
id: fpp/change-a-terme
nom: Change à terme
symbole: '$K(t,T)$, $P^f(t,T)$, $R^f(t,T)$'
type: notion
statut: source
cas_de: fpp/prix-a-terme
valeur: une devise
construite_a_partir_de:
- fpp/taux-de-change
- fpp/taux-zero-coupon
alias:
- forward exchange rate
- change forward
- taux de change à terme
- contrat de change à terme
refs:
- §2.4
- Ex. 3
- exo. 6
- exo. 13
- exo. 19
---

## Ce que c'est
Le change fixé aujourd'hui pour échanger en T une unité de devise locale contre K(t,T) unités étrangères, sans rien payer à la signature. [§2.4]

## Forme
$$K(t,T)=X_t\,\frac{P(t,T)}{P^f(t,T)}=X_t\,e^{\left(R^f(t,T)-R(t,T)\right)(T-t)}$$ [§2.4]

## Ce que les symboles modélisent
$K(t,T)$ s'exprime comme $X_t$, en unités étrangères pour une unité locale. $P^f(t,T)$ est le zéro-coupon étranger : ce que vaut en $t$, en devise étrangère, une unité étrangère payée en $T$. $R^f(t,T)$ est le taux zéro-coupon étranger ; l'exposant $f$ marque tout ce qui est étranger. [§2.4]

## Retrouver la formule
![Le contrat de change à terme sur deux lignes, la devise étrangère en haut, la locale en bas. On paie 1 unité locale en T et on reçoit K unités étrangères en T ; chaque flux revient en t par le zéro-coupon de sa devise, P(t,T) ou P^f(t,T), puis on convertit au change du jour X_t. Le contrat ne coûtant rien, K · P^f(t,T) / X_t = P(t,T).](figures/change-a-terme.svg) [§2.4, ajout]

Prenons l'euro comme devise locale, un change de 1,10 dollar par euro, un taux de 4 % sur l'euro et de 5 % sur le dollar, à un an. [ajout]

Le contrat fait payer 1 euro dans un an : aujourd'hui, cela vaut $P(t,T)=0{,}9608$ euro. [§2.4]

Il fait recevoir $K$ dollars dans un an : aujourd'hui, cela vaut $K\,P^f(t,T)=0{,}9512\,K$ dollars, soit $0{,}9512\,K/1{,}10$ euros au change du jour. [§2.4]

Le contrat ne coûte rien, donc les deux valeurs sont égales : $K=1{,}10\times0{,}9608/0{,}9512\approx1{,}1111$. En lettres, $K\,P^f(t,T)/X_t=P(t,T)$ : [§2.4]

$$K(t,T)=X_t\,\frac{P(t,T)}{P^f(t,T)}$$ [§2.4]

## Ce qui la définit
Ce qui est **connu** : le change du jour et les deux courbes. Ce qu'on **cherche** : le change à écrire au contrat. La devise qui rapporte le plus d'intérêts se vend moins cher à terme : ici le dollar rapporte 5 % contre 4 %, et un euro achète à terme plus de dollars qu'aujourd'hui. Le poly le dit du côté local : la devise locale s'apprécie à terme si le taux étranger est plus élevé. [§2.4]

Le livre d'exercices ajoute deux lectures. Emprunter des dollars, les changer aujourd'hui et placer les euros reproduit le contrat : c'est la couverture par le marché monétaire. Et emprunter dans une devise à taux bas pour placer dans une autre ne rapporte que si le change futur reste du bon côté du change à terme, qui est le point mort de l'opération. [exo. 6, exo. 19]

## Le chemin jusqu'ici
fpp/taux-de-change convertit les dollars en euros, mais seulement aujourd'hui. Pour ramener chaque flux en $t$, il faut le zéro-coupon de sa propre devise : fpp/zero-coupon pour l'euro, son homologue étranger pour le dollar, et fpp/taux-zero-coupon pour les écrire en taux. L'exponentielle de la seconde écriture vient de la convention continue de fpp/capitalisation. [ajout]

## Exemple minimal
Un change de 1,10 dollar par euro, 4 % sur l'euro, 5 % sur le dollar : le change à un an vaut 1,1111 dollar par euro. [ajout]

## Geste de calcul type
Retrouver un taux étranger à partir du change comptant et du change à terme : $R^f=R+\ln(K/X_t)/(T-t)=4\,\%+\ln(1{,}1111/1{,}10)=5\,\%$. Les exercices 3 et 4 du livre font ce calcul, dans l'autre convention de change. [§2.4, exo. 3, exo. 4]

## Cesse d'être valide quand
Si $X_t$ est le prix de la devise étrangère en devise locale, comme dans plusieurs exercices, les deux taux échangent leurs places : $X_t\,e^{(r_l-r_f)(T-t)}$. Et le change à terme ne prévoit pas le change futur : l'entreprise qui s'en sert fixe son taux, elle ne parie pas sur lui. [exo. 13, exo. 18]
