from bfs import predicate_model_checker
from model import STR2TR
from soup import SoupProgram, Rule, SoupSemantics


class AliceBobConfig:
    def __init__(self):
        self.ProgramCounter_Alice = 0
        self.ProgramCounter_Bob = 0

    def __hash__(self):
        return hash(self.ProgramCounter_Alice + self.ProgramCounter_Bob)

    def __eq__(self, other):
        return self.ProgramCounter_Alice == other.ProgramCounter_Alice and self.ProgramCounter_Bob == other.ProgramCounter_Bob

    def __repr__(self):
        return str(self.ProgramCounter_Alice) + str(self.ProgramCounter_Bob)


def AliceBob():
    soup = SoupProgram(AliceBobConfig())

    def ItoSC_alice(c):
        c.ProgramCounter_Alice = 1

    soup.add(Rule("ItoSC_alice", lambda c: c.ProgramCounter_Alice == 0, ItoSC_alice))

    def SCtoI_alice(c):
        c.ProgramCounter_Alice = 0

    soup.add(Rule("SCtoI_alice", lambda c: c.ProgramCounter_Alice == 1, SCtoI_alice))


    def ItoSC_alice(c):
        c.ProgramCounter_Alice = 1

    soup.add(Rule("ItoSC_alice", lambda c: c.ProgramCounter_Bob == 0, ItoSC_alice))

    def SCtoI_bob(c):
        c.ProgramCounter_Bob = 0

    soup.add(Rule("SCtoI_bob", lambda c: c.ProgramCounter_Bob == 1, SCtoI_bob))

    return soup


if __name__ == '__main__':
    semantic = SoupSemantics(AliceBob())
    tr = STR2TR(semantic)
    r = predicate_model_checker(semantic, lambda c: c.ProgramCounter_Alice == 1 and c.ProgramCounter_Bob == 1)
    print(r)
    #r = predicate_model_checker(semantic, lambda c: len(semantic.actions(c)) == 0)
    #print(r)