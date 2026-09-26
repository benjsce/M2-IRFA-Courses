---
id: ods/expected-risk
nom: Expected risk
symbole: '$\mathcal{R}(\phi)$, $\ell$, $\mathbb{P}$, $\mathcal{F}$'
type: notion
statut: source
construite_a_partir_de:
- ods/optimization-problem
alias:
- risk
- true risk
- risk minimization
refs:
- §1.1.3
- p. 2
---

## Ce que c'est
The average loss that a prediction rule incurs on the pairs $(x,y)$ drawn from the distribution that generates the data, including the pairs not yet seen. [p. 2]

## Forme
$$\mathcal{R}(\phi)=\mathbb{E}_{(x,y)\sim\mathbb{P}}\,\ell\big(y,\phi(x)\big),\qquad\text{problem: }\ \inf_{\phi\in\mathcal{F}}\mathcal{R}(\phi)$$ [p. 2]

## Ce que les symboles modélisent
$\phi$ is the prediction rule: it takes an input $x$ and returns a predicted output. $\ell$ is the loss: it takes the true output and the predicted one, and returns the price of the mistake, for instance $\tfrac12\big(y-\phi(x)\big)^2$. [p. 2, ajout]

$\mathbb{P}$ is the probability measure on the pairs $(x,y)$: the whole population, not the sample. $\mathcal{F}$ is the class of prediction rules we allow ourselves, for instance the linear rules $\phi(x)=x^\top w$. [p. 2, ajout]

$\mathcal{R}(\phi)$ is one number per prediction rule: how much it loses on average, over the whole population. [p. 2]

## Ce qui la définit
Known: the loss and the class. Sought: the rule of the class with the smallest expected risk. The obstacle is that $\mathbb{P}$ is unknown, so $\mathcal{R}$ cannot be computed. [p. 2]

A Bayes predictor minimizes the expected risk over all measurable rules; a restricted class need not contain one, and the infimum over $\mathcal{F}$ need not be attained. [p. 2]

## Le chemin jusqu'ici
ods/optimization-problem supplies the template: here the unknown is a function $\phi$ rather than a vector, the domain is the class $\mathcal{F}$, and the objective is the expected risk. [p. 2]

## Exemple minimal
If the target is the second feature plus a noise of variance $0.1$, the weights $(0,1)$ have an expected squared-loss risk of $0.05$, even though they fit the four observations exactly. [ajout]

## Geste de calcul type
With $\ell(y,\phi(x))=\tfrac12(y-\phi(x))^2$, $\phi(x)=x_2$ and $y=x_2+\eta$ with $\mathbb{E}\,\eta=0$ and $\operatorname{Var}\eta=0.1$: the error is $\eta$, so $\mathcal{R}(\phi)=\tfrac12\,\mathbb{E}\,\eta^2=0.05$. No other rule does better here, since $\eta$ cannot be predicted from $x$. [ajout]

## Cesse d'être valide quand
In practice $\mathbb{P}$ is unknown and $\mathcal{R}$ cannot be evaluated: learning replaces it by its average on the sample, the empirical risk. Even with $\mathbb{P}$ known, the infimum over a restricted class may not be attained. [p. 2]
