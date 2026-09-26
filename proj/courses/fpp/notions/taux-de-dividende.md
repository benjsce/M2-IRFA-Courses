---
id: fpp/taux-de-dividende
nom: Taux de dividende continu
symbole: '$d$, $q$'
type: notion
statut: source
construite_a_partir_de:
- fpp/dividendes-intermediaires
alias:
- continuous dividend yield
- dividend yield
- rendement du dividende
refs:
- §5.2.1
- éq. 7
- exo. 13
- exo. 17
---

## Ce que c'est
Un dividende versé en continu, à raison d'une fraction d du prix de l'action par an, qui abaisse d'autant la croissance du prix forward. [§5.2.1]

## Forme
$$F(t,T)=S_t\,e^{(r-d)(T-t)}$$ [§5.2.1, ajout]

## Ce que les symboles modélisent
$d$, au §5.2.1, et $q$, dans la formule de Black et Scholes, désignent le même taux, par an. Ce ne sont ni les proportions $d_i$ des dividendes datés, ni les $d_1$, $d_2$ de la formule. [§5.2.1, éq. 7]

## Ce qui la définit
Ce qui est **connu** : le prix comptant, le taux $r$ et le taux de dividende. Ce qu'on **cherche** : le prix forward. Répartis en une multitude de petits versements proportionnels, les dividendes retirent au prix forward non plus un facteur $1-\sum_i d_i$ mais $e^{-d(T-t)}$ : le portage coûte $r$ et rapporte $d$. [§3.2, §5.2.1, ajout]

Le livre d'exercices s'en sert pour un indice, le S&P 500 à 1,88 % par an, et pour une devise, dont le taux d'intérêt étranger joue le rôle du dividende. [exo. 17, exo. 13]

## Le chemin jusqu'ici
fpp/dividendes-intermediaires retirait du prix forward des dividendes datés ; le taux continu en est la limite quand ils deviennent nombreux et petits. Le reste vient de fpp/prix-forward : ce prix sort de fpp/cash-and-carry, un portage financé par un emprunt que fpp/zero-coupon évalue, dans la convention continue de fpp/capitalisation, et que fpp/absence-d-arbitrage rend unique. [ajout]

## Exemple minimal
L'action à 100, un taux de 4 %, un dividende continu de 2 % : le prix forward à un an vaut $100\,e^{0,02}=102{,}02$. [ajout]

## Geste de calcul type
Remplacer, dans une formule écrite sans dividende, $S_t$ par $S_t\,e^{-d(T-t)}$ : c'est ainsi que la formule de Black et Scholes avec dividendes se déduit de celle sans dividende. [éq. 7, ajout]

## Cesse d'être valide quand
Les dividendes réels sont datés et discrets ; le taux continu est une approximation, raisonnable pour un indice qui agrège beaucoup de versements, grossière pour une action seule. [ajout]
