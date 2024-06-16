## Partie 2 : Résolution du Problème de Correspondance Maximale dans un Graphe

### Introduction
Dans cette partie, nous nous intéressons à la résolution du problème de correspondance maximale dans un graphe généré aléatoirement. Le but est de comparer deux heuristiques différentes pour trouver des paires de nœuds connectés qui maximisent le nombre de correspondances.

### Méthodes Utilisées
Nous avons implémenté deux heuristiques pour résoudre le problème de correspondance maximale dans le graphe :
1. **Heuristique basée sur le degré décroissant** : Cette méthode consiste à apparier les nœuds en commençant par ceux ayant le plus haut degré, cherchant à maximiser le nombre d'arêtes couvertes.
2. **Heuristique basée sur le degré croissant** : À l'inverse de la première méthode, celle-ci commence par les nœuds ayant le plus bas degré et tente également de maximiser le nombre de correspondances.

### Implémentation
Nous avons utilisé la bibliothèque Python `networkx` pour générer un graphe aléatoire `G` avec 120 nœuds et une probabilité de lien de 0.04. Chaque heuristique est ensuite appliquée sur ce graphe pour évaluer ses performances. Nous avons également utilisé `matplotlib` pour visualiser les résultats et `time` pour mesurer les temps d'exécution.