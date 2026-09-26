---
id: dss/bagging
nom: Bagging
symbole: $B$
type: notion
statut: source
cas_de: dss/methode-d-ensemble
valeur: des arbres tirés en parallèle, puis moyennés
construite_a_partir_de:
- dss/bootstrap
- dss/compromis-biais-variance
alias:
- bagging
- bootstrap aggregating
refs:
- slide 98
- slide 99
- slide 100
- slide 101
- slide 103
---

## Ce que c'est
Construire un arbre sur chaque échantillon bootstrap, puis moyenner les prédictions. [slide 98]

## Forme
$$\hat f_{\text{avg}}(x)=\frac{1}{B}\sum_{b=1}^{B}\hat f^{\,b}(x)$$ [slide 99]

## Ce que les symboles modélisent
$B$ est le nombre d'arbres agrégés : un paramètre de calcul, pas un paramètre de modèle, dont le coût est du temps. $\hat f^{\,b}(x)$ est la prédiction au point $x$ de l'arbre construit sur le $b$-ième échantillon bootstrap, et $\hat f_{\text{avg}}(x)$ la moyenne de ces $B$ prédictions. [slide 99]

## Ce qui la définit
Le problème qu'il traite est nommé : découper les données autrement donne un arbre différent, donc la variance est forte. Moyenner des estimations incertaines donne un résultat moins incertain. [slide 98]

Les arbres sont construits sans élagage, par centaines, et l'on moyenne. En classification, la moyenne est remplacée par un vote majoritaire. [slide 99, slide 100]

La méthode réduit la variance, pas le biais ; elle s'applique surtout aux arbres, et se parallélise sans difficulté puisque les arbres sont indépendants du point de vue du calcul. [slide 103, slide 108]


## Le chemin jusqu'ici
dss/bootstrap fournit le moyen : plusieurs échantillons fabriqués à partir d'un seul, donc plusieurs arbres. dss/compromis-biais-variance fournit la raison de les moyenner : un arbre ajusté sur les couples observés de dss/apprentissage-supervise a une forte variance, et elle pèse dans l'erreur que mesure dss/erreur-de-test. [ajout]

## Exemple minimal
Sur les 20 clients, on tire 500 échantillons de 20 clients avec remise, on construit un arbre sur chacun, et la perte prédite pour un nouveau client est la moyenne des 500 pertes prédites. Si ces 500 arbres étaient indépendants, la variance de leur moyenne serait 500 fois plus petite que celle d'un arbre ; ils ne le sont pas, puisqu'ils sont bâtis sur les mêmes 20 clients. [slide 109, ajout]

## Geste de calcul type
Ne pas élaguer les arbres : c'est la moyenne qui contrôle la variance, l'élagage ne ferait qu'ajouter du biais à chacun. [slide 99]

## Cesse d'être valide quand
L'erreur de test ne remonte pas quand $B$ augmente : le bagging ne surajuste pas par le nombre d'arbres. Ce qui plafonne le gain est ailleurs, dans la corrélation entre les arbres. [slide 100, slide 109]
