from bfs import predicate_model_checker
from soup import SoupProgram, Rule, SoupSemantics


class AliceBobConfig:
    def __init__(self):
        self.ProgramCounter_Alice = 0
        self.Flag_Alice = 0
        self.Flag_Bob = 0
        self.ProgramCounter_Bob = 0

    def __hash__(self):
        return hash(self.ProgramCounter_Alice + self.ProgramCounter_Bob) + hash(self.Flag_Alice + self.Flag_Bob)

    def __eq__(self, other):
        if other is None:
            return False
        return self.ProgramCounter_Alice == self.ProgramCounter_Alice and self.ProgramCounter_Bob == other.ProgramCounter_Bob and self.Flag_Bob == other.Flag_Bob and self.Flag_Alice == other.Flag_Alice

    def __repr__(self):
        return str(self.ProgramCounter_Alice) + str(self.ProgramCounter_Bob)


def AliceBob():
    soup = SoupProgram(AliceBobConfig())

    def InitialToWaiting_Alice(c):
        c.ProgramCounter_Alice = 1
        c.Flag_Alice = 1

    soup.add(Rule("InitialToWaiting_Alice", lambda c: c.ProgramCounter_Alice == 0, InitialToWaiting_Alice))

    def WaitingToCriticalSection_Alice(c):
        c.ProgramCounter_Alice = 2
        c.Flag_Alice = 1

    soup.add(Rule("WaitingToCriticalSection_Alice", lambda c: c.ProgramCounter_Bob != 2 and c.ProgramCounter_Alice == 1, WaitingToCriticalSection_Alice))

    def CriticalSectionToInitial_Alice(c):
        c.ProgramCounter_Alice = 0
        c.Flag_Alice = 0

    soup.add(Rule("CriticalSectionToInitial_Alice", lambda c: c.ProgramCounter_Alice == 2, CriticalSectionToInitial_Alice))

    def InitialToWaiting_Bob(c):
        c.ProgramCounter_Bob = 1
        c.Flag_Bob = 1

    soup.add(Rule("InitialToWaiting_Bob", lambda c: c.ProgramCounter_Bob == 0, InitialToWaiting_Bob))

    def WaitingToCriticalSection_Bob(c):
        c.ProgramCounter_Bob = 2
        c.Flag_Bob = 1

    soup.add(Rule("WaitingToCriticalSection_Bob", lambda c: c.ProgramCounter_Bob == 1 and c.ProgramCounter_Alice != 2, WaitingToCriticalSection_Bob))

    def CriticalSectionToInitial_Bob(c):
        c.ProgramCounter_Bob = 0
        c.Flag_Bob = 0

    soup.add(Rule("CriticalSectionToInitial_Bob", lambda c: c.ProgramCounter_Bob == 2, CriticalSectionToInitial_Bob))

    return soup


def AliceInCriticalSection(c):
    return c.ProgramCounter_Alice == 2


def BobInCriticalSection(c):
    return c.ProgramCounter_Bob == 2


if __name__ == '__main__':
    sem = SoupSemantics(AliceBob())
    r = predicate_model_checker(sem, lambda c: c.ProgramCounter_Alice == 2 and c.ProgramCounter_Bob == 2)
    print(r)

