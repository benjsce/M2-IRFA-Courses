---
id: fpp/levier
nom: Levier
symbole: $l_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/bilan
alias:
- leverage
- ratio de levier
refs:
- Déf. 1
- §1.3
---

## Ce que c'est
Le rapport des actifs aux capitaux propres, c'est-à-dire le nombre d'euros d'actifs que porte chaque euro apporté par les actionnaires. [Déf. 1]

## Forme
$$l_t = \frac{A_t}{E_t}$$ [Déf. 1]

## Ce que les symboles modélisent
$l_t$ est un nombre sans unité, daté : il vaut 1 pour une entreprise sans dette et grandit avec elle. Ce n'est pas le $l$ du modèle de Merton dans le livre d'exercices, qui rapporte la dette à la valeur forward de l'entreprise. [Déf. 1, exo. 16]

## Ce qui la définit
On connaît les actifs et les capitaux propres ; le levier dit par combien une variation relative des actifs est multipliée quand elle arrive aux capitaux propres. Si la dette ne bouge pas, $\Delta E_t = \Delta A_t$, donc $\dfrac{\Delta E_t}{E_t} = \dfrac{A_t}{E_t}\,\dfrac{\Delta A_t}{A_t} = l_t\,\dfrac{\Delta A_t}{A_t}$. [§1.3]

Quand la dette varie aussi, le poly écrit $\dfrac{\Delta E_t}{E_t} = l_t\,\dfrac{\Delta A_t}{A_t} - (l_t-1)\,\dfrac{\Delta D_t}{D_t}$. [§1.3]

![Avant et après un gain ΔA des actifs, dette inchangée : les capitaux propres gagnent aussi ΔA. En relatif, ΔA / E_t = (A_t / E_t) × ΔA / A_t = l_t × ΔA / A_t : le gain des actifs pèse l_t fois plus sur les capitaux propres.](figures/levier.svg) [ajout]

## Le chemin jusqu'ici
fpp/bilan fait des capitaux propres ce qui reste une fois la dette déduite des actifs. Le levier mesure la minceur de cette couche restante par rapport à ce qu'elle porte : plus elle est mince, plus un mouvement des actifs pèse sur elle. [ajout]

## Exemple minimal
Des actifs de 100 et des capitaux propres de 20 : le levier vaut 5. [ajout]

## Geste de calcul type
Calculer $l_t = A_t/E_t$, puis multiplier par $l_t$ une variation relative des actifs pour obtenir celle des capitaux propres, dette inchangée : $+10\,\%$ sur les actifs donne $+50\,\%$ sur les capitaux propres. [§1.3, ajout]

## Cesse d'être valide quand
Le levier est daté. Après le choc, il ne vaut plus 5 mais $110/30 \approx 3{,}67$ : la règle « $l_t$ fois » vaut pour une variation à partir d'un bilan donné, pas pour une suite de variations. Et il n'a plus de sens quand les capitaux propres tombent à zéro. [§1.3, §1.4, ajout]
