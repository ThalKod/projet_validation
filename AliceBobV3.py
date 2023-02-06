from bfs import predicate_model_checker
from model import STR2TR, IsAcceptingProxy
from soup import SoupProgram, SoupSemantics, Rule


class AliceBobConfiguration:
    def __init__(self):
        self.ProgramCounter_Alice = 0
        self.ProgramCounter_Bob = 0

    def __hash__(self):
        return hash(self.ProgramCounter_Alice + self.ProgramCounter_Bob)

    def __eq__(self, other):
        return self.ProgramCounter_Alice == other.ProgramCounter_Alice and self.ProgramCounter_Bob == other.ProgramCounter_Bob

    def __repr__(self):
        return str(self.ProgramCounter_Alice) + str(self.ProgramCounter_Bob)


def counterState():
    soup = SoupProgram(AliceBobConfiguration())

    def InitialToWaiting_Alice(c):
        c.ProgramCounter_Alice = 1

    soup.add(Rule("InitialToWaiting_Alice", lambda c: c.ProgramCounter_Alice == 0, InitialToWaiting_Alice))

    def WaitingToCriticalSection_Alice(c):
        return 1

    soup.add(Rule("WaitingToCriticalSection_Alice", lambda c: c.ProgramCounter_Bob == 0 and c.ProgramCounter_Alice == 1, WaitingToCriticalSection_Alice))

    def CriticalSectionToInitial_Alice(c):
        c.ProgramCounter_Alice = 0

    soup.add(Rule("CriticalSectionToInitial_Alice", lambda c: c.ProgramCounter_Alice == 1, CriticalSectionToInitial_Alice))

    def InitialToWaiting_Bob(c):
        c.ProgramCounter_Bob = 1

    soup.add(Rule("InitialToWaiting_Bob", lambda c: c.ProgramCounter_Bob == 0, InitialToWaiting_Bob))

    def WaitingToCriticalSection_Bob(c):
        return 1

    soup.add(Rule("WaitingToCriticalSection_Bob", lambda c: c.ProgramCounter_Alice == 0 and c.ProgramCounter_Bob == 1, WaitingToCriticalSection_Bob))

    def CriticalSectionToInitial_Bob(c):
        c.ProgramCounter_Bob = 0

    soup.add(Rule("CriticalSectionToInitial_Bob", lambda c: c.ProgramCounter_Bob == 1, CriticalSectionToInitial_Bob))

    return soup


if __name__ == '__main__':
    semantic = SoupSemantics(counterState())
    tr = STR2TR(semantic)
    tr = IsAcceptingProxy(tr, lambda c: c.ProgramCounter_Alice == 0)
    print(tr.initial())
    print(tr.next(tr.initial()[0]))
    r = predicate_model_checker(semantic, lambda c: c.ProgramCounter_Alice == 1 and c.ProgramCounter_Bob == 1)
    print(r)
