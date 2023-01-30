# This is a sample Python script.
import inspect
from collections import deque

import copy

from Graph import Graph
from NBits import NBits
from bfs import bfs_with_accepting, predicate_finder, get_trace

from hanoi import Hanoi, actionFunc, soup_hanoi, guarde, HanoiConfiguration, change, createStack
from model import ParentTraceProxy, STR2TR, IdentityProxy
from soup import SoupSemantics, SoupProgram, Rule


def hanoi_on_entry1(n):
   conf = n.conf
   i = 0
   while i < n.taille() - 1:
       if conf[i] != []:
           return False
       i = i + 1
   double = copy.deepcopy(conf[-1])
   if double.sort() == conf[-1]:
       return False
   print("GAGNE")
   return True


def main_hanoi():
    print("============= Hanoi Main ===============")
    num_of_disks = 4
    hanoi_tower = IdentityProxy(Hanoi(3, 3))
    init = hanoi_tower.initial()[0]
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        guard = guarde(i, j)
        action = actionFunc(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("-------------------------")
    print("Soup")
    soup = soup_hanoi(3, 3)
    soup_semantic = SoupSemantics(soup)
    init = soup_semantic.initialConfigurations()[0]
    print("First State: ", init)
    actions = soup_semantic.enabledActions(init)

    if actions:
        for action in actions:
            execute = soup_semantic.execute(init, action)
            print("Output : ", execute)

    str = STR2TR(soup_semantic)
    init = str.roots()[0]
    next = str.next(init)
    print("After ", init, ": ", next)


def main_alice_bob_v1():
    pass

def main_alice_bob_v2():
    pass

if __name__ == "__main__":
    print("Liste des mains")
    print("1: Hanoi")
    print("2: Hanoi Simple")
    print("3: AliceBob V1")
    print("4: AliceBob V2")

    option = input("Quel est votre choix? ")

    if option == '1':
        main_hanoi()
    elif option == '2':
        main_alice_bob_v1()
    elif option == '3':
        main_alice_bob_v2()