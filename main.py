# This is a sample Python script.
import inspect
from collections import deque

from Graph import Graph
from NBits import NBits
from bfs import bfs_with_accepting,predicate_finder

from hanoi import Hanoi, actionFunc, soup_hanoi, guarde
from model import ParentTraceProxy, STR2TR
from soup import SoupSemantics


def main_hanoi():
    print("============= Hanoi Main ===============")
    new_hanoi = ParentTraceProxy(Hanoi(3, 3))

    for i, j in [(0, 1), (0, 2), (2, 1)]:
        init = new_hanoi.initial()[0]
        guarde_1 = guarde(i, j)
        action = actionFunc(i, j)
        g = guarde_1(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("============= Hanoi Soup ===============")
    soup = soup_hanoi(3, 3)
    soup_semantic = SoupSemantics(soup)
    init = soup_semantic.initial()[0]

    print("Etat initial: ", init)
    actions = soup_semantic.actions(init)

    if actions:
        for action in actions:
            execute = soup_semantic.execute(init, action)
            print("Execute : ", execute)

    print("======== STR2TR ==========")

    str = STR2TR(soup_semantic)
    init = str.initial()[0]
    next = str.next(init)

    print("States after ", init, "are", next)

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