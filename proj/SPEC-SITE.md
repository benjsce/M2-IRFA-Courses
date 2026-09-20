# SPEC-SITE — architecture d'information et générateur

Le site est **généré** depuis `courses/` par `tools/build.py`. Il est statique : des
fichiers HTML dans `site/`, sans serveur. Il s'ouvre en double-cliquant `site/index.html`
et se publie tel quel sur GitHub Pages.

## 1. Le problème à résoudre

Un cours entier compte 100 à 300 notions. Afficher le graphe complet, ou une page
défilante, est inutilisable : la charge de repérage écrase la charge d'apprentissage.
L'architecture d'information sert à une seule chose : **que la personne ne voie jamais
plus que ce qu'elle cherche, et trouve en un clic ce qu'elle cherchera ensuite.**

## 2. Règles de charge cognitive

Ces règles sont des contraintes du générateur, pas des conseils.

1. **Une notion par écran.** La fiche est la page. Tout le reste est à un clic.
2. **Jamais le graphe entier.** Aucune vue ne dessine plus que : le voisinage de dépendance
   à rayon 1 d'une notion, ou l'arbre d'abstraction d'un cours replié au-delà de deux
   niveaux.
3. **Les rubriques dans le même ordre partout**, avec les mêmes intitulés, y compris
   quand elles sont vides (omises, mais jamais réordonnées). La prévisibilité supprime le
   coût de repérage.
4. **Sept éléments par liste au plus.** Au-delà, regrouper (par niveau, par cours, par
   type) et replier les groupes.
5. **Divulgation progressive.** À l'ouverture d'une fiche : « Ce que c'est », « Forme »,
   « Ce qui la définit ». Les autres rubriques sont repliées, dans l'ordre, et se
   déplient d'un clic. L'état de pliage est mémorisé par navigateur (`localStorage`).
6. **Le socle est une liste, jamais un graphe.** Plat, ordonné par niveau croissant, avec
   un état « déjà su » persistant par navigateur, et le compteur « n notions, k à voir ».
7. **Deux relations, deux traitements visuels**, jamais confondus : la dépendance est une
   liste de pastilles ; l'abstraction est un arbre. Aucune arête d'abstraction n'apparaît
   dans une vue de dépendance et réciproquement.
8. **Les ajouts sont distinguables et masquables.** Une notion `ajout` ou un paragraphe
   `[ajout]` porte une marque visible ; un interrupteur global les masque ; la projection
   qui reste est valide (A11).
9. **Recherche instantanée** sur nom, alias, symbole, depuis toute page, sans rechargement.
10. **Aucune animation** sauf celles qui répondent à un geste (ouvrir, plier, filtrer).

## 3. Les pages

```
site/
  index.html                      sélecteur de cours + recherche globale
  <code>/index.html               carte du cours : principes, abstractions de niveau 1,
                                  composants sans généralisation, dette ; recherche
  <code>/n/<slug>.html            la fiche
  <code>/arbre.html               arbre d'abstraction pliable (replié > 2 niveaux)
  <code>/inventaire.html          la couverture de la source, pour l'audit hebdomadaire
  <code>/exercices/<slug>.html    énoncé, solution officielle, résolution, fiches touchées
  rapports/<date>.html            les rapports d'ingestion
```

### 3.1 La fiche `<code>/n/<slug>.html`

Dans cet ordre, sans exception :

1. En-tête : nom, symbole, type, cours, niveau, références principales, marque `ajout`.
2. Ce que c'est.
3. Forme.
4. Ce qui la définit / Ce que les membres partagent.
5. *(abstraite)* Le paramètre qui les distingue — table membre → valeur, **générée**.
6. *(abstraite)* Pourquoi ce niveau existe.
7. Cas particulier de — une pastille, **générée**, avec la mention « autre relation :
   ce n'est pas un prérequis ».
8. Construite à partir de — pastilles, depuis le front matter.
9. Socle complet — liste **générée**, ordonnée par niveau, cases « déjà su », compteur.
10. Exemple minimal.
11. Geste de calcul type.
12. Ce qui reste libre.
13. Cesse d'être valide quand — visuellement distinguée (bordure), c'est la rubrique
    la plus lue.
14. Sert ensuite à — pastilles, **générée** ($D^{-1}$).
15. Membres — *(abstraite)* pastilles, **générée** ($A^{-1}$).
16. Origine.
17. Voisinage — petit schéma **généré** : la notion au centre, ses dépendances directes
    à gauche, ses dépendants directs à droite. Rayon 1, jamais plus.

Les pastilles sont des liens. Un lien vers une notion d'un autre cours porte le code du
cours. Un lien vers un id `a-venir` est rendu comme texte barré avec la mention « à
venir », jamais comme lien mort.

### 3.2 La carte du cours `<code>/index.html`

Ce qu'on voit : les principes (en tête), puis pour chaque principe ses abstractions
directes avec leur nombre de membres, puis « Composants » (notions sans `cas_de` et sans
type principe), puis un bandeau « Dette » (liens à venir, gestes à venir, inventaire à
venir). Rien d'autre. Le détail est à un clic.

### 3.3 L'arbre `<code>/arbre.html`

Voir §5 pour l'algorithme. Un seul type d'arête. Replié au-delà de deux niveaux à
l'ouverture. Cliquer un nœud ouvre la fiche. Boutons : tout déplier, tout replier, zoom,
masquer les ajouts. Le canevas se déplace au glisser (souris et tactile). Les nœuds
`ajout` sont marqués. Sous l'arbre : la liste « notions sans généralisation », qui est une
information et non un oubli.

## 4. Contraintes du générateur

- **Python 3.10+**, dépendances : `pyyaml` seulement. Un seul point d'entrée :
  `python tools/build.py`. Idempotent. Tourne à l'identique sur macOS et Windows.
- **Le site doit s'ouvrir en `file://`.** Donc : aucune requête `fetch` vers un fichier
  local. Les données d'une page sont incorporées dans la page. L'index de recherche est
  un script inclus dans chaque page ou un unique fichier chargé par balise `<script>`.
- **Formules** : MathJax 3, sortie SVG, chargé depuis un CDN par défaut ; option
  `--offline` qui copie MathJax dans `site/vendor/` pour un usage sans réseau. Les fontes
  du texte sont des fontes système ; aucune dépendance externe autre que MathJax.
- **Une page = un fichier autonome** (CSS et JS inclus), ≤ 300 ko hors MathJax.
- **Thème clair / sombre** suivant le système, commutable, mémorisé.
- **Responsive** : lisible sur un téléphone en portrait. L'arbre y est utilisable au doigt.
- **Accessibilité minimale** : navigation au clavier, focus visible, contrastes
  suffisants, animations désactivées si `prefers-reduced-motion`.
- **Aucune donnée personnelle** ne quitte le navigateur. `localStorage` sert aux états
  « déjà su », pliage, thème ; tout accès est protégé par `try/catch`.
- **`build.py` échoue si `validate.py` échoue.** Il ne génère jamais depuis un graphe
  invalide.

## 5. L'arbre d'abstraction : algorithme et garantie

Disposition en colonnes par profondeur, cartes de largeur fixe $w$, colonnes espacées de
$c > w$, hauteur des cartes mesurée une fois toutes cartes visibles (une carte masquée
mesure zéro ; on ne mesure jamais une carte masquée), écart vertical $g$.

Pour chaque colonne $d$, une ordonnée $y^{\text{next}}_d$, initialement 0, **jamais
décroissante**. Placement récursif d'un nœud $n$ de profondeur $d$ :

1. si $n$ n'a pas d'enfant visible : $\text{top}(n) = y^{\text{next}}_d$ ;
2. sinon, placer d'abord ses enfants ; soit $m$ le milieu vertical entre le premier et le
   dernier ; $\text{top}(n) = \max\!\big(y^{\text{next}}_d,\ m - h(n)/2\big)$ ; si le
   maximum a joué, soit $\delta$ l'écart : décaler tout le sous-arbre de $\delta$ vers le
   bas et avancer de $\delta$ les $y^{\text{next}}_{d'}$ des seules colonnes $d'$ que le
   sous-arbre occupe ;
3. $y^{\text{next}}_d \leftarrow \text{top}(n) + h(n) + g$.

Les racines sont placées l'une après l'autre, chaque nouvelle racine démarrant sous le
maximum de tous les $y^{\text{next}}$.

**Propriétés garanties**, chacune avec sa raison :
- *Aucune superposition dans une colonne* : les tops d'une colonne sont posés au plus tôt
  à $y^{\text{next}}_d$, avancé de la hauteur après chaque pose ; le décalage d'un
  sous-arbre n'augmente que des écarts et avance les compteurs des colonnes concernées.
- *Aucune superposition entre colonnes* : bandes verticales disjointes puisque $c > w$.
- *Aucune arête ne traverse une carte* : chaque arête est une courbe de Bézier dont les
  points de contrôle ont pour abscisse le milieu de l'entre-colonne ; son abscisse reste
  donc dans la bande vide entre le bord droit du parent et le bord gauche de l'enfant.
- *Parent centré sur ses enfants* : restauré par le décalage exact de l'étape 2.

**Test de propriété obligatoire** (`tools/tests/test_layout.py`, exécuté par `build.py`) :
pour au moins 1 000 configurations de pliage tirées au hasard sur chaque arbre de cours,
et pour 3 jeux de hauteurs aléatoires par configuration, vérifier que (i) tous les
rectangles visibles sont deux à deux disjoints, (ii) l'abscisse de chaque arête est
comprise entre le bord droit de son parent et le bord gauche de son enfant, (iii) chaque
parent visible a son ordonnée entre celles de son premier et de son dernier enfant
visible. Le build échoue si un test échoue. En complément, la page elle-même exécute la
vérification (i) après chaque re-disposition et l'écrit dans la console du navigateur.

Ce que l'algorithme ne garantit pas : la compacité. Un arbre de dix niveaux et deux cents
nœuds est large. C'est pourquoi la règle 2 impose le repli par défaut : la garantie de
non-chevauchement vaut pour toute taille, la lisibilité non.

## 6. Publication

`site/` est commité. GitHub Pages est configuré sur le dossier `site/` de la branche
principale. Le site est alors accessible à une adresse publique depuis n'importe quel
appareil. Un `.nojekyll` vide est présent dans `site/` pour que GitHub ne retraite pas
les fichiers.

## 7. Point d'export prévu (non construit)

`tools/export_cards.py` : pour chaque fiche, produire des germes de cartes (recto proposé,
verso, fiche d'origine) au format attendu par le dépôt de flashcards. Pas dans le
périmètre initial ; l'interface est : une fiche → zéro ou plusieurs germes, jamais
l'inverse.
