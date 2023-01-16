# This is a sample Python script.
from collections import deque

from Graph import Graph
from bfs import bfs_with_accepting

# TODO: predicat 2 graphe qui fonctionne

g1 = Graph({
    "1": ["2", "3"],
    "2": ["5", "6"],
    "3": [],
    "4": ["4", "6"],
    "5": ["4"],
    "6": ["6"]
}, "1")

g2 = Graph({
    "0": ["1", "3"],
    "1": ["2"],
    "2": ["0"],
    "3": ["3", "4"],
    "4": ["1", "5"],
    "5": []
}, "0")

graph1 = {
    "1": ["2", "3"],
    "2": ["5", "6"],
    "3": [],
    "4": ["4", "6"],
    "5": ["4"],
    "6": ["6"]
}


def ftest1(source, n, acc):
    if n is acc:
        print("target %s" % n)


def ftest2(source, acc):
    acc[0] += 1


def ftest3(source, n, acc):
    pass


def ftest4(source, acc):
    pass


print(bfs_with_accepting(g1, "4", ftest1, ftest1, ftest4))
