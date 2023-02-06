from bfs import predicate_model_checker
from model import STR2TR, IsAcceptingProxy
from soup import SoupProgram, SoupSemantics, Rule


class AliceBobConfiguration:
    def __init__(self):
        self.PC_alice = 0
        self.PC_bob = 0

    def __hash__(self):
        return hash(self.PC_alice + self.PC_bob)

    def __eq__(self, other):
        return self.PC_alice == other.PC_alice & self.PC_bob == other.PC_bob

    def __repr__(self):
        return str(self.PC_alice) + str(self.PC_bob)


def counterState():
    soup = SoupProgram(AliceBobConfiguration())

    def InitialToWaiting_Alice(c):
        c.PC_alice = 1

    soup.add(Rule("ItoSC_alice", lambda c: c.PC_alice == 0, InitialToWaiting_Alice))

    def WaitingToCriticalSection_Alice(c):
        return 1

    soup.add(Rule("WtoSC_alice", lambda c: c.PC_bob == 0 and c.PC_alice == 1, WaitingToCriticalSection_Alice))

    def CriticalSectionToInitial_Alice(c):
        c.PC_alice = 0

    soup.add(Rule("SCtoI_alice", lambda c: c.PC_alice == 1, CriticalSectionToInitial_Alice))

    def InitialToWaiting_Bob(c):
        c.PC_bob = 1

    soup.add(Rule("ItoW_bob", lambda c: c.PC_bob == 0, InitialToWaiting_Bob))

    def WaitingToCriticalSection_Bob(c):
        return 1

    soup.add(Rule("WtoSC_bob", lambda c: c.PC_alice == 0 and c.PC_bob == 1, WaitingToCriticalSection_Bob))

    def CriticalSectionToInitial_Bob(c):
        c.PC_bob = 0

    soup.add(Rule("SCtoI_bob", lambda c: c.PC_bob == 1, CriticalSectionToInitial_Bob))

    return soup


if __name__ == '__main__':
    semantic = SoupSemantics(counterState())
    tr = STR2TR(semantic)
    tr = IsAcceptingProxy(tr, lambda c: c.PC_alice == 0)
    print(tr.initial())
    print(tr.next(tr.initial()[0]))
    r = predicate_model_checker(semantic, lambda c: c.PC_alice == 1 and c.PC_bob == 1)
    print(r)
