---
id: fpp/prime-de-risque
nom: Prime de risque
symbole: '$\pi_A$, $\pi_E$'
type: notion
statut: source
construite_a_partir_de:
- fpp/levier
alias:
- risk premium
- expected excess return
refs:
- Déf. 2
- §1.3
---

## Ce que c'est
Ce que rapporte un actif au-delà du rendement de la dette qui le finance, son coût de financement. [Déf. 2, §1.3]

## Forme
$$\tilde\pi_E=l\times\tilde\pi_A,\qquad \pi_E=\mathbb{E}(\tilde\pi_E)=l\,\pi_A$$ [§1.3]

## Ce que les symboles modélisent
$\pi$ désigne une prime de risque en général. Comme toute variation relative, elle s'exprime en pour cent par unité de temps, le plus souvent par an : une prime de 3 % veut dire 3 % par an. [§1.3, Rem. 1]

Le tilde marque la prime **réalisée** sur la période, que l'on ne connaît qu'à la fin : $\tilde\pi_A=\frac{\Delta A_t}{A_t}-\frac{\Delta D_t}{D_t}$ pour l'actif, $\tilde\pi_E=\frac{\Delta E_t}{E_t}-\frac{\Delta D_t}{D_t}$ pour les capitaux propres. Sans tilde, c'est sa moyenne, l'espérance : $\pi=\mathbb{E}(\tilde\pi)$. [§1.3]

$\pi_A$ est donc la prime espérée de l'actif, $\pi_E$ celle des capitaux propres ; $l$ est le levier, le rapport de l'actif aux capitaux propres. [§1.3, Déf. 1]

## Ce qui la définit
La prime est l'excès de rendement sur la dette ; sa moyenne, $\pi$, est la prime espérée, et c'est elle qu'on appelle d'ordinaire prime de risque. Un actif qui rapporte moins que la dette a une prime négative. [Déf. 2, §1.3]

**Connu** : la prime de l'actif et le levier. **Cherché** : la prime des capitaux propres. Elle vaut $l$ fois la première : à chaque période, l'excès réalisé des capitaux propres est $l$ fois celui de l'actif, par l'identité du bilan ; leur moyenne l'est donc aussi. [§1.3]

![L'actif de l'exemple, à 6 % de volatilité et 3 % de prime, et ses capitaux propres, à 20 % et 10 %. Le levier multiplie les deux coordonnées par 3,33 : le point glisse sur une droite issue de l'origine, et le rapport de la prime à la volatilité reste 0,5.](figures/prime-de-risque.svg) [ajout]

Le même argument multiplie l'écart type de la prime, la volatilité : $\sigma_E=l\,\sigma_A$. Prime et volatilité grandissent ensemble, et leur rapport ne change pas. [§1.3]

## Le chemin jusqu'ici
fpp/bilan pose l'identité actif = capitaux propres + dette, et fpp/levier la réécrit en rendements : l'écart des capitaux propres sur la dette vaut $l$ fois celui de l'actif. La prime de risque ne fait que nommer ces écarts, puis en prendre la moyenne. [ajout]

## Exemple minimal
Une prime d’actif de 3 % avec un levier de 3,33 donne une prime sur capitaux propres de 10 %. [ajout]

## Geste de calcul type
Multiplier par le levier : $3{,}33\times3\,\%=10\,\%$ pour la prime, $3{,}33\times6\,\%=20\,\%$ pour la volatilité ; le rapport reste $3/6=10/20=0{,}5$. [§1.3]

## Cesse d'être valide quand
L'égalité des excès réalisés ne cesse jamais : c'est l'identité du bilan, à condition de mesurer les deux excès au-dessus de ce que la dette a effectivement rapporté. [§1.3]

Ce qui cesse, c'est de lire ce rendement de la dette comme un coût fixé d'avance. Quand l'actif passe sous la dette, les capitaux propres sont plancherisés à zéro et c'est la dette qui encaisse la perte : son rendement devient aléatoire lui aussi, et la prime des capitaux propres n'est plus $l$ fois ce que l'actif rapporte au-delà d'un coût connu. [§1.4, ajout]

Passer de l'égalité réalisée à celle des moyennes suppose aussi un levier constant : la source modélise les primes comme des variables aléatoires stationnaires. [§1.3, ajout]
