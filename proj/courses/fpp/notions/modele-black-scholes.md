---
id: fpp/modele-black-scholes
nom: Modèle de Black et Scholes
symbole: $W_t$
type: notion
statut: source
construite_a_partir_de:
- fpp/mesure-risque-neutre
- fpp/transformee-de-laplace-gaussienne
- fpp/echelonnement-de-la-variance
alias:
- Black and Scholes model
- diffusion log-normale
refs:
- §5.4
---

## Ce que c'est
Le sous-jacent suit une diffusion log-normale et le taux est constant. [§5.4]

## Forme
$$dS_t=S_t\big(\mu\,dt+\sigma\,dW_t^{\mathbb{P}}\big)=S_t\big(r\,dt+\sigma\,dW_t^{\mathbb{Q}}\big)$$ [§5.4]

## Ce que les symboles modélisent
$\mu$ est la dérive du sous-jacent sous la probabilité **historique**, celle des fréquences observées : c'est précisément la grandeur qui disparaîtra du prix de l'option. $W_t$ est un mouvement brownien, le hasard élémentaire du modèle — de moyenne nulle, et de variance égale au temps écoulé. [§5.4]

## Ce qui la définit
Le passage de $\mathbb{P}$ à $\mathbb{Q}$ ne change que la dérive, jamais la volatilité : $\mu$ devient $r$, et $\sigma$ reste. [§5.4]

$$S_t=S_0e^{(\mu-\frac{\sigma^2}{2})t+\sigma W_t^{\mathbb{P}}},\qquad \mathbb{E}^{\mathbb{Q}}(S_t)=S_0e^{rt}$$ [§5.4]

## Le chemin jusqu'ici
Trois fils entrent ici, et c'est le nœud du cours. [ajout]

**Le prix.** fpp/replication-statique, fpp/portage et fpp/facteur-actualisation (bâti sur fpp/convention-capitalisation) se combinent en fpp/prix-a-terme, puis fpp/mesure-risque-neutre : un prix est une espérance actualisée. [ajout]

**L'aléa.** fpp/volatilite puis fpp/echelonnement-de-la-variance disent comment l'incertitude grandit avec le temps. [ajout]

**Le calcul.** fpp/transformee-de-laplace-gaussienne donne la seule identité dont on aura besoin pour mener l'espérance jusqu'au bout. [ajout]

Le modèle est le choix minimal qui referme les trois : une diffusion log-normale et un taux constant. Rien de plus n'est dans le socle, et c'est ce qui rend ses limites faciles à nommer. [ajout]

## Exemple minimal
Avec $S_0=100$, $r=4\%$ et un an : $\mathbb{E}^{\mathbb{Q}}(S_1)=104{,}08$, quelle que soit $\sigma$. [ajout]

## Geste de calcul type
Écrire $S_T$ sous forme exponentielle, reconnaître une gaussienne à l’exposant, puis appliquer la transformée de Laplace : c’est le chemin le plus court vers toute espérance sous $\mathbb{Q}$. [§5.4, Th. 1]

## Cesse d'être valide quand
Volatilité constante et taux déterministes : les deux hypothèses sont fausses en pratique, et c’est de là que viennent le smile et les modèles à volatilité stochastique. [ajout]
