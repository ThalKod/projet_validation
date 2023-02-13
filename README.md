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
Une représentation graphique de l'exemple de graphe précèdent est la suivante :

<p align = "center">
    <img src ="https://user-images.githubusercontent.com/81907955/218487563-0c180124-3824-4d54-80b2-0bd7752597bd.png">
</p>

## Hanoi
Avant de réaliser la classe de **Hanoi**, nous avons commencé par écrire la classe nBits qui permet de recenser le nombre de configurations possibles a partir d’un état (configuration) initial.
Cette classe prend en entrée un état initial et le nombre de bits constituant cet etat initial et nous donne en sorite tous les états voisins possibles.

**Exemple :** entrée ```[0,1,0]``` et nBits=3, la sortie est : ```[[1, 1, 0], [0, 0, 0], [0, 1, 1]]```

La classe ```Hanoi``` permet de résoudre le problème de la tour de Hanoi en passant par une configuration de départ qui précise le nombre de disques et de tours. 

<p align = "center">
    <img src ="https://user-images.githubusercontent.com/81907955/218492186-d85d2ee5-33fc-459c-9aed-46eb3fb7aba9.png">
</p>

## Alice et Bob
Nous avons implémenté le fameux problème d’Alice et de Bob vu dans le cours précèdent de Vérification. 

Il s’agit de deux personnes qui souhaitent accéder a une section critique mais pas en même temps.
Nous avons trois versions qui représentent trois niveaux de complexité du problème.

#### Version 1 :
Version la plus simple du problème où Alice et Bob souhaitent accéder à la section critique sans contraintes supplémentaires.
<p align = "center">
    <img src ="https://user-images.githubusercontent.com/81907955/218495240-b5ac0c11-989a-4517-a108-fced0f53718d.PNG" width=70%>
</p>

#### Version 2:
Version un peu plus complexe que la première version. Dans cette version on introduit un état en plus le **Waiting**

#### Version 3:
Version la plus complexe entre les trois. 
Dans cette version on introduit en plus de l'état **waiting** la notion de **flag**. Chaque personne dispose d'un drapeau qui doit être levé pour indiquer le souhait de la personne d'accéder à la section critique. Ce drapeau reste levé tant que la personne est dans la zone critique et ne descend pas que quand cette personne revient chez elle.
<p align = "center">
    <img src ="https://user-images.githubusercontent.com/81907955/218498563-567e815f-570e-4ca4-a8c3-b7c9a6997e5c.PNG" width=70%>
</p>

