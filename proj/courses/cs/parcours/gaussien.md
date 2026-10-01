---
id: cs/parcours-gaussien
ordre: 1
titre: Deux gaussiennes liées
source: slides, §0.3 Gaussian vectors (slides 1–5)
---

## Point de départ
On tire deux variables indépendantes $G_1$ et $G_2$ de loi $\mathcal N(0,1)$, et l'on fabrique $X_1=G_1$ et $X_2=1+\tfrac12G_1+\tfrac{\sqrt3}{2}G_2$. Chacune est une variable gaussienne, comme somme d'une constante et de gaussiennes indépendantes. Mais le couple $(X_1,X_2)$ est-il gaussien, lui aussi ? [§0.3 slide 2, ajout]

## Étapes
1. cs/vecteur-gaussien
   Pour un couple, « gaussien » ne peut pas vouloir dire seulement que chaque variable l'est. [Déf. 0.3.1]
   Histoire : « le couple $(X_1,X_2)$ est-il gaussien » — Oui : toute combinaison $x_1X_1+x_2X_2=x_2+\big(x_1+\tfrac12x_2\big)G_1+\tfrac{\sqrt3}{2}x_2G_2$ est une constante plus une combinaison de deux gaussiennes indépendantes, donc une gaussienne. Il aurait suffi d'une seule combinaison non gaussienne pour répondre non. [Déf. 0.3.1, ajout]

2. cs/loi-gaussienne-multivariee
   Le couple est gaussien ; on n'a encore rien dit de sa loi. [Prop. 0.3.1]
   Suite : Ses moyennes valent $0$ et $1$, ses variances $1$ et $\tfrac14+\tfrac34=1$, et la covariance de $X_1$ et $X_2$ vaut ½. Ces cinq nombres suffisent-ils à connaître la loi du couple ? [ajout]
   Histoire : « Ces cinq nombres suffisent-ils à connaître la loi du couple » — Oui : chaque combinaison est gaussienne, donc fixée par sa moyenne et sa variance, qui se calculent avec ces cinq nombres. La somme $X_1+X_2$ a pour moyenne $0+1=1$ et pour variance $1+1+2\times\tfrac12=3$ ; la loi du couple est $\mathcal N(m,\Sigma)$, avec $m=(0,1)$ et $\Sigma=\begin{pmatrix}1&\tfrac12\\\tfrac12&1\end{pmatrix}$. [Prop. 0.3.1, ajout]

3. cs/densite-gaussienne
   La loi est fixée, mais par une fonction caractéristique, qui ne dit pas directement la probabilité d'une région du plan. [Prop. 0.3.2]
   Suite : Le couple a-t-il une densité, qui permettrait de calculer ces probabilités par une intégrale ? [ajout]
   Histoire : « Le couple a-t-il une densité » — Oui, parce que $\det\Sigma=1-\tfrac14=\tfrac34$ n'est pas nul. Elle vaut $1/(\pi\sqrt3)\approx0{,}184$ au centre $(0,1)$ et décroît le long d'ellipses. Avec une covariance de $1$ au lieu de ½, on aurait $\det\Sigma=0$, $X_2-X_1=1$ avec probabilité un, et plus de densité. [Prop. 0.3.2, ajout]

4. cs/independance-gaussienne
   La covariance ½ lie les deux variables : connaître $X_1$ renseigne sur $X_2$. [Cor. 0.3.1]
   Suite : Peut-on isoler dans $X_2$ une part qui ne doive rien à $X_1$ ? [ajout]
   Histoire : « une part qui ne doive rien à $X_1$ » — $X_2-\tfrac12X_1$ : sa covariance avec $X_1$ vaut $\tfrac12-\tfrac12\times1=0$. Le couple $(X_1,\ X_2-\tfrac12X_1)$ est encore gaussien, et pour lui une covariance nulle suffit : $X_2-\tfrac12X_1$ est indépendante de $X_1$. C'est d'ailleurs $1+\tfrac{\sqrt3}{2}G_2$, qui ne contient pas $G_1$. [Cor. 0.3.1, ajout]

## Point d'arrivée
Un couple gaussien est décrit tout entier par ses moyennes et ses covariances : sa loi, sa densité quand $\det\Sigma\neq0$, et ses indépendances, qu'une covariance nulle suffit à établir. $X_2$ s'écrit $\tfrac12X_1$ plus une part indépendante de $X_1$, ce qui servira à prévoir $X_2$ quand on aura vu $X_1$. [ajout]
