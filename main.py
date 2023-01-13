# This is a sample Python script.
from collections import deque
from projet_validation.Graph import Graph

#TODO: predicat 2 graphe qui fonctionne

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


def parcour_graph_largeur(graph, initial):
    visited = []
    stack = [initial]
    visited.append(initial)

    while stack:
        current_node = stack.pop(0)

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

    return visited


def bfs_simple(graph, i):
    known = set()
    frontier = deque()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = graph[i]
            at_start = False
        else:
            source = frontier.popleft()
            neighbours = graph[source]

        for n in neighbours:
            if n not in known:
                known.add(n)
                frontier.append(n)

    return known

def bfs_iter_graph(graph):
    known = set()
    frontier = deque()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:

            if n not in known:
                known.add(n)
                frontier.append(n)

    return known

def bfs_with_target(graph, target):
    known = set()
    frontier = deque()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:

            if n not in known:
                if n == target:
                    return known
                known.add(n)
                frontier.append(n)

    return known

def bfs_with_accepting(graph, acc, on_known, on_entry, on_exit):
    knowns = set()
    frontier = deque()
    at_start = True
    while frontier or at_start :
        source = None
        if at_start :
            neighbours = graph.initial()
            at_start = False
        else :
            source = frontier.popleft()
            neighbours = graph.next(source)
        for n in neighbours:
            if n in knowns :
                on_known(source, n, acc)
                continue
            on_entry(source, n, acc)
            knowns.add(n)
            frontier.append(n)
        on_exit(source, acc)
    return knowns

def ftest1(source, n, acc):
    if n is acc :
        print("target %s" % n)

def ftest2(source, acc):
    acc[0] += 1

def ftest3(source, n, acc):
    pass

def ftest4(source, acc):
    pass


print(bfs_with_accepting(g1, "4", ftest1, ftest1, ftest4))




