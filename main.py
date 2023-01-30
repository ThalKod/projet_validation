# This is a sample Python script.
import inspect
from collections import deque

import copy

from Graph import Graph
from NBits import NBits
from bfs import bfs_with_accepting, predicate_finder, get_trace

from hanoi import Hanoi, actionFunc, soup_hanoi, guarde, HanoiConfiguration, change, createStack
from model import ParentTraceProxy, STR2TR
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
    hanoi_configuration = HanoiConfiguration(3, 3)
    prog = SoupProgram(hanoi_configuration)

    for i in range(3):
        for j in range(3):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), guarde(i, j), change(i, j)))
    for k in range(len(prog.rules)):
        print(prog.rules[k])


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