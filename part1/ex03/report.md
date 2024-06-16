Preuve de la complexité polynomiale :
La complexité de l'algorithme est dominée par le tri des positions des maisons, ce qui est O(n log n). Les autres opérations (calcul des temps d'attente et construction de l'ordre optimal) sont linéaires en fonction du nombre de maisons, donc en O(n). Par conséquent, l'algorithme global est en O(n log n), ce qui est bien polynomial par rapport au nombre de maisons.

Pour conclure, cette approche offre une solution efficace pour minimiser le temps d'attente moyen des maisons nettoyées par un chasse-neige, en comparaison avec des méthodes gloutonnes ou basées sur le tri simple des positions des maisons.