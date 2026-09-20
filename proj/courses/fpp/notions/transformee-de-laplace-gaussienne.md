---
id: fpp/transformee-de-laplace-gaussienne
nom: Transformée de Laplace gaussienne
type: notion
statut: source
construite_a_partir_de: []
alias:
- Gaussian Laplace transform
- lemme d'exponentielle gaussienne
refs:
- Th. 1
---

## Ce que c'est
L’espérance de l’exponentielle d’une gaussienne s’écrit en forme fermée. [Th. 1]

## Forme
$$X\sim\mathcal{N}(\mu,\sigma^2)\ \implies\ \mathbb{E}\big(e^{\lambda X}\big)=e^{\lambda\mu+\frac{\lambda^2\sigma^2}{2}}$$ [Th. 1]

## Ce qui la définit
C’est le seul calcul technique dont Black et Scholes ont besoin : il transforme une espérance de log-normale en exponentielle d’un polynôme. [Th. 1, §5.4]

## Exemple minimal
Avec $\mu=0$, $\sigma=1$ et $\lambda=1$ : $\mathbb{E}(e^X)=e^{0{,}5}=1{,}6487$. [ajout]

## Geste de calcul type
Pour $S_T=S_0e^{Y}$ avec $Y\sim\mathcal N(rT-\tfrac{\sigma^2T}{2},\sigma^2T)$, appliquer le théorème avec $\lambda=1$ : le terme $-\sigma^2T/2$ annule exactement le $+\lambda^2\sigma^2/2$, et il reste $\mathbb{E}(S_T)=S_0e^{rT}$. [§5.4]

## Cesse d'être valide quand
Vaut pour une gaussienne, et pour elle seule : c’est l’hypothèse de log-normalité qui entre ici dans le modèle. [Th. 1]
