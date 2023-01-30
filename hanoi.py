import copy
import sys

from model import TransitionRelation
from soup import SoupProgram


def is_accepted(c):
    nb_disks = max(max(c))

    if len(c[-1]) != nb_disks:
        return False
    for k in range(nb_disks):
        if c[-1][k] != nb_disks - k:
            return False
    return True


class Hanoi(TransitionRelation):
    def __init__(self, nb_stacks, nb_disks):
        super().__init__()
        self.nbDisks = nb_disks
        self.nbStacks = nb_stacks

    def initial(self):
        return [HanoiConfiguration(self.nbStacks, self.nbDisks)]

    def next(self, n):
        next_states = []
        for i in range(self.nbStacks):
            new_node = copy.deepcopy(n)
            if new_node[i]:
                disk = new_node[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_node[j] or new_node[j][-1] > disk):
                        temp = copy.deepcopy(new_node)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states

    def on_entry(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nbDisks - k:
                return False
            k = k + 1
        return True


def guarde(s, t):
    return lambda c: len(c.stacks[s]) and len(c.stacks[t]) == 0 or c.stacks[s][-1] < c.stacks[t][-1]

def actionFunc(s, t):
    def action(c):
        disk = c.stacks[s].pop()
        c.stacks[t].append(disk)
        return action


def soup_hanoi(nb_stacks, nb_disks):
    h = HanoiConfiguration(nb_stacks, nb_disks)
    soup_program = SoupProgram(h)
    for i in range(nb_stacks):
        for j in range(nb_stacks):
            soup_program.add(f'{i}-{j}', guarde(i, j), actionFunc(i, j))
    return soup_program


class HanoiConfiguration(list):
    def __init__(self, nb_stacks, nb_disks):
        list.__init__(self, [[(nb_disks - i) for i in range(nb_disks)]] + [[] for _ in range(nb_stacks - 1)])

    def __hash__(self):
        hash = 0
        maxi = max(self)[0]
        for stack in self:
            hash += sum(stack) * maxi
            maxi *= 2
        return hash

    def __eq__(self, conf):
        if len(self) != len(conf):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(conf[i]):
                return False
        for j in range(len(self[i])):
            if conf[i][j] != self[i][j]:
                return False


