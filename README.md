# Projet de Validation
Ce projet a été réalisé par Yara HALLAK, Bachar HAJJAR et Thalul-De MARCELIN pendant notre cours de Validation a l’ENSTA Bretagne. 
Dans ce projet nous avons construit une simulation d’un model checker qui nous permet de réaliser des vérifications d’un modele en entrée et de valider son comportement.


## Graphes et parcours de graphes
Pour réaliser ce model checker, on a commencé par implémenter des fonctions en Python qui parcourent un graphe en entrée par la méthode du BFS (Breadth First Search).

Un graphe en entrée est une instance de la classe **Graphe** qui a la forme suivante :

```python
g1 = Graph({
    "1": ["2", "3"],
    "2": ["4", "6"],
    "3": [],
    "4": ["5", "6"],
    "5": ["4"],
    "6": ["6"]
}, "1")
```
  Une reperesentation graphique de l'exemple de graphe predent est la suivante:





