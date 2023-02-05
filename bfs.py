from collections import deque


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
            neighbours = graph.next(graph.initial())
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:
            if n not in known:
                known.add(n)
                frontier.append(n)
    return known

def predicate_finder(
        graph,
        predicate=lambda n: False):
    def check_predicate(s, n, a):
        # increment the count
        a[2] += 1
        # check predicate-
        a[1] = predicate(n)
        # return true if predicate is true - stop the traversal
        return a[1]

    return bfs_with_accepting(graph, [predicate, False, 0, None], on_entry=check_predicate)

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

def bfs_with_accepting(graph,
        acc,
        on_entry,
        on_known=None,
        on_exit = None):
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        source = None
        if at_start:
            neighbours = graph.roots()
            at_start = False
        else:
            source = frontier.popleft()
            neighbours = graph.next(source)

        if neighbours is not None:
            for n in neighbours:
                if n not in known:
                    known.add(n)
                    frontier.append(n)
                    if on_entry is not None:
                        on_entry(source, n, acc)
                else:
                    if on_known is not None:
                        on_known(source, n, acc)
            if on_exit is not None:
                on_exit(source, n, acc)
    return acc, known


def get_trace(dict, target, initial):
    status = target
    if not status:
        print("No path found")
        return None
    print(initial, target)

    current_Node = target
    trace = [current_Node]
    while current_Node not in initial:
        current_Node = dict[current_Node]
        trace.append(current_Node)

    print("Trace : ", trace);