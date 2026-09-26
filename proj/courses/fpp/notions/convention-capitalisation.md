---
id: fpp/convention-capitalisation
nom: Convention de capitalisation
type: notion
statut: source
construite_a_partir_de: []
refs:
- §2.1
---

## Ce que c'est
La coordonnée dans laquelle on écrit un facteur d’actualisation : linéaire, périodique, continue, actuarielle. [§2.1]

## Forme
$$\left(1+\frac{rt}{n}\right)^{n}\xrightarrow[n\to\infty]{}e^{rt}$$ [§2.1]

## Ce qui la définit
Ce sont quatre écritures bijectives du même objet, sans aucun contenu économique. [§2.1]

## Exemple minimal
$r=5\%$ sur deux ans : facteur linéaire $1{,}10$, trimestriel $1{,}1038$, continu $1{,}1052$, actuariel $1{,}1052$. [ajout]

![Le facteur $(1+rt/n)^n$ pour $rt=0{,}10$, à mesure que le nombre de périodes grandit. Une période donne le facteur linéaire 1,10, huit trimestres 1,1038, et la limite continue vaut 1,1052 : chaque point est une convention, toutes pour le même placement.](figures/convention-capitalisation.svg) [ajout]

## Geste de calcul type
Avant tout calcul, fixer la convention : le même « 5 % sur deux ans » donne un facteur de 1,10 en linéaire et de 1,1052 en continu, soit 52 points de base d’écart. L’erreur est silencieuse et se propage à tout le reste. [§2.1]

## Cesse d'être valide quand
Aucune — mais oublier de la fixer rend toute formule inévaluable, et le choix borne la fréquence d’actualisation possible. Le continu est la seule convention sans plancher. [§2.1]

## Origine
- exercice fpp/ex-11 : sur un an à 5 %, l'escompte $1-r$, le linéaire $1/(1+r)$ et le continu $e^{-r}$ séparent les réponses de plus de 10 % (26,25 · 23,81 · 24,99). La convention y décide de la réponse [exo. 11]
