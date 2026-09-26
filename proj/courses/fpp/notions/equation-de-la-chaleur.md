---
id: fpp/equation-de-la-chaleur
nom: Réduction à l’équation de la chaleur
type: notion
statut: source
construite_a_partir_de:
- fpp/feynman-kac
alias:
- heat equation
refs:
- §7.2.2
- éq. 20
- éq. 21
---

## Ce que c'est
Passer aux valeurs forward, puis au logarithme, ramène l’équation de Black et Scholes à l’équation de la chaleur, qui n'a plus ni actualisation ni dérive. [§7.2.2]

## Forme
$$\dfrac{\partial C}{\partial t}+\tfrac12\sigma^2\dfrac{\partial^2C}{\partial x^2}=0,\qquad C(T,x)=(e^x-K)^+$$ [éq. 20, éq. 21]

## Ce que les symboles modélisent
Le $C$ de cette équation n'est plus le prix de l'option : c'est sa valeur forward, le prix multiplié par $e^{r(T-t)}$, vue comme une fonction de la date $t$ et de $x$. La lettre est restée celle de l'équation de départ, mais la fonction a changé. [§7.2.2, ajout]

$x$ n'est plus le prix du sous-jacent. Le poly en fait le logarithme de son prix forward ; pour que l'équation soit exactement celle-ci, il faut encore le décaler de $\tfrac12\sigma^2(T-t)$ (voir « Retrouver la formule »). [§7.2.2, ajout]

À l'échéance $T$, le forward et le comptant coïncident et le décalage est nul, si bien que $e^x$ y est le prix du sous-jacent et que la condition terminale reste le payoff du call de strike $K$. $\sigma$ est la même volatilité qu'avant ; le taux $r$ a disparu de l'équation, absorbé par le passage au forward. [§7.2.2, ajout]

## Retrouver la formule
On part de l'équation de Black et Scholes, $\partial_tC+rS\,\partial_SC+\tfrac12\sigma^2S^2\,\partial^2_SC=rC$ : un terme de temps, un terme de dérive $rS\,\partial_SC$, un terme de diffusion, un terme d'actualisation $rC$. L'équation de la chaleur n'a que le premier et le troisième ; chaque geste en retire un. [éq. 16]

Premier geste : passer à la valeur forward de l'option, $e^{r(T-t)}C$. Les dérivées en $S$ sont simplement multipliées par $e^{r(T-t)}$ ; la dérivée en temps, elle, gagne $-r\,e^{r(T-t)}C$, qui compense exactement $rC$. Le terme d'actualisation disparaît : $\partial_tC+rS\,\partial_SC+\tfrac12\sigma^2S^2\,\partial^2_SC=0$, le $C$ désignant désormais la valeur forward. [§7.2.2]

Deuxième geste : prendre pour variable le prix forward du sous-jacent, $f=Se^{r(T-t)}$, au lieu du comptant. À $S$ fixé, $f$ monte avec le temps au taux $r$ : la dérivée en temps à $S$ fixé est celle à $f$ fixé moins $rf\,\partial_fC$, et ce terme compense exactement la dérive, puisque $rS\,\partial_SC=rf\,\partial_fC$. Il reste $\partial_tC+\tfrac12\sigma^2f^2\,\partial^2_fC=0$. [§7.2.2, ajout]

Troisième geste : prendre le logarithme, $x=\ln f$, pour que la diffusion ne dépende plus du niveau. Mais $f^2\,\partial^2_f=\partial^2_x-\partial_x$ : le logarithme recrée une dérive, $\partial_tC+\tfrac12\sigma^2\big(\partial^2_xC-\partial_xC\big)=0$. C'est l'équation qu'on obtient avec les seuls changements que le poly annonce ; l'éq. 20 omet ce terme $-\tfrac12\sigma^2\,\partial_xC$. [§7.2.2, ajout]

Quatrième geste, que le poly ne fait pas : décaler $x$ de ce que cette dérive accumule jusqu'à l'échéance, $x-\tfrac12\sigma^2(T-t)$. La dérivée en temps à $x$ fixé devient celle à la nouvelle variable fixée plus $\tfrac12\sigma^2\,\partial_xC$, qui annule le terme de trop ; en $T$ le décalage est nul et la condition terminale ne change pas. [ajout]

$$\dfrac{\partial C}{\partial t}+\tfrac12\sigma^2\dfrac{\partial^2C}{\partial x^2}=0,\qquad C(T,x)=(e^x-K)^+$$ [éq. 20, éq. 21]

## Ce qui la définit
Chaque geste retire un terme : la valeur forward de l'option retire l'actualisation, le forward du sous-jacent retire la dérive, le logarithme rend la diffusion indépendante du niveau, et le décalage retire la dérive que le logarithme a recréée. Le poly annonce les trois premiers ; le quatrième est nécessaire pour arriver exactement à l'éq. 20. [§7.2.2, ajout]

## Le chemin jusqu'ici
C'est le socle le plus long du cours, et il n'est long que parce que cette fiche est la dernière. [ajout]

**Le prix.** fpp/replication-statique donne la méthode, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) en chiffrent les deux jambes, d'où fpp/prix-a-terme puis fpp/mesure-risque-neutre. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps ; avec fpp/transformee-de-laplace-gaussienne, on obtient fpp/modele-black-scholes. [ajout]

**L'équation.** fpp/compte-capitalise ouvre fpp/replication-dynamique, d'où fpp/edp-black-scholes, dont fpp/feynman-kac fournit la lecture probabiliste. [ajout]

Rien n'est ajouté ici sur le plan financier : des changements de variables, et l'équation devient celle de la chaleur. Il a fallu tout construire pour y arriver ; cette fiche, elle, ne fait que la réécrire. C'est la seule étape purement mathématique. [ajout]

## Exemple minimal
À un an, avec un taux de 4 % et une volatilité de 20 %, le facteur du passage au forward est $e^{r(T-t)}=1{,}0408$, et le décalage du dernier geste vaut $\tfrac12\sigma^2(T-t)=0{,}02$. [ajout]

## Geste de calcul type
Pour reconnaître un problème de Black et Scholes déguisé : chercher si un passage au forward annule le terme d’ordre zéro et le terme de dérive, puis si un passage au logarithme, suivi d'un décalage, rend les coefficients constants. [§7.2.2, ajout]

## Cesse d'être valide quand
La réduction suppose $r$ et $\sigma$ constants. Avec des coefficients dépendant du temps il reste une équation de la chaleur à temps changé ; avec des coefficients dépendant du niveau, elle ne tient plus. [ajout]
