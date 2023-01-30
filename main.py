# This is a sample Python script.
from collections import deque

from Graph import Graph
from NBits import NBits
from bfs import bfs_with_accepting,predicate_finder
import matplotlib.pyplot as plt

def main_hanoi():
    pass

def main_alice_bob_v1():
    pass

def main_alice_bob_v2():
    pass

if __name__ == "__main__":
    print("Liste des mains")
    print("1: Hanoi")
    print("2: AliceBob V1")
    print("3: AliceBob V2")

    option = input("Quel est votre choix? ")

    if option == '1':
        main_hanoi()
    elif option == '2':
        main_alice_bob_v1()
    elif option == '3':
        main_alice_bob_v2()