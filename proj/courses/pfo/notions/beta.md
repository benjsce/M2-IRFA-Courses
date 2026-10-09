---
id: pfo/beta
nom: Bêta
symbole: '$\beta_i$, $R_m$'
type: notion
statut: source
construite_a_partir_de:
- pfo/portefeuille-de-marche
- pfo/matrice-de-covariance
alias:
- beta
- bêta de marché
- coefficient bêta
- risque systématique
- systematic risk
refs:
- §4.2.1
- p. 59
- p. 76
---

## Ce que c'est
La covariance du rendement d'un actif avec celui du marché, divisée par la variance du marché : la sensibilité de l'actif aux mouvements du marché. [§4.2.1, p. 59]

## Forme
$$\beta_i=\frac{\mathrm{Cov}(R_i,R_m)}{\mathrm{Var}(R_m)}$$ [p. 59]

## Ce que les symboles modélisent
$R_i$ est le rendement de l'actif $i$, $R_m$ celui du portefeuille de marché ; tous deux sont aléatoires. $\beta_i$ est un nombre sans unité, puisqu'il divise une covariance par une variance : il ne mesure pas le risque total de l'actif, seulement la part de ce risque qui bouge avec le marché. [§4.2.1, p. 59]

## Ce qui la définit
**Connus** : la variance du marché et la covariance de l'actif avec lui. **Cherché** : de combien l'actif bouge, en moyenne, quand le marché bouge de 1 %. Un bêta de 1,2 associe à un mouvement du marché de 1 % un mouvement d'environ 1,2 % de l'actif, toutes choses égales par ailleurs. [p. 76, p. 68]

Supérieur à 1, l'actif est plus sensible au marché que le marché lui-même ; inférieur à 1, il l'est moins. Le cours dit aussi qu'il mesure la contribution de l'actif au risque de marché : pondérés par les poids du marché, les bêtas font exactement 1. [p. 59, p. 76, ajout]

![Les deux actifs du marché à deux tiers et un tiers. Chaque barre a pour largeur le poids de l'actif dans le marché et pour hauteur son bêta, Cov(R_i, R_m) / Var(R_m) : 0,75 et 1,5. Son aire est la part du risque du marché que l'actif porte, la moitié chacun, et les aires font 1, le bêta du marché, en pointillé. Dessous, la Forme : β_i = Cov(R_i, R_m) / Var(R_m).](figures/beta.svg) [ajout]

C'est la seule part du risque qui ne disparaît pas quand on diversifie : on l'appelle le risque systématique. [§4.1, p. 59]

## Le chemin jusqu'ici
Le bêta compare un actif à un portefeuille de référence, et ce portefeuille est pfo/portefeuille-de-marche ; son rendement se calcule comme une moyenne pondérée, ce que pfo/piege-d-agregation réserve à pfo/rendement-arithmetique, et refuse à pfo/rendement-logarithmique. [ajout]

La covariance et la variance du quotient se lisent dans pfo/matrice-de-covariance. La variance du marché y est la forme quadratique des poids ; sa diagonale porte le carré de fpp/volatilite, et fpp/echelonnement-de-la-variance permet d'y passer d'une fréquence à l'autre sans changer le bêta, qui est un quotient de deux grandeurs annualisées de la même façon. [ajout]

## Exemple minimal
Sur le marché à deux tiers et un tiers des deux actifs non corrélés du chapitre 3, de volatilités 10 % et 20 %, le premier a un bêta de 0,75 et le second de 1,5. [ajout]

## Geste de calcul type
$\mathrm{Var}(R_m)=\tfrac49\times0{,}01+\tfrac19\times0{,}04=0{,}00889$. Les actifs n'étant pas corrélés, $\mathrm{Cov}(R_2,R_m)=\tfrac13\times0{,}04=0{,}01333$, d'où $\beta_2=0{,}01333/0{,}00889=1{,}5$ ; de même $\beta_1=\tfrac23\times0{,}01/0{,}00889=0{,}75$. Contrôle : $\tfrac23\times0{,}75+\tfrac13\times1{,}5=1$. [ajout]

En pratique on ne connaît pas ces moments : on estime $\beta_i$ comme la pente de la régression du rendement de l'actif sur celui du marché. [p. 59, p. 76]

## Cesse d'être valide quand
Un bêta élevé n'annonce pas un rendement élevé : il mesure une sensibilité au facteur de marché, pas une performance future. [p. 77]

Le bêta est relatif au portefeuille de marché choisi ; mesuré contre un indice qui en tient lieu, comme le S&P 500, il change avec l'indice. [p. 67, ajout]

## Origine
- exercice pfo/ex-07 : comparer les bêtas de AAPL, MSFT et JPM pour savoir laquelle est la plus exposée au risque de marché [p. 75, p. 77]
