from ctypes import sizeof

from model import SemanticTransitionRelation


class MaybeStutter():
    pass


class Stutter(MaybeStutter):
    pass

class Action(MaybeStutter):
    def __init__(self,a):
        self.action = a

class Step(MaybeStutter):
    def __init__(self,source,action,target):
        self.source = source
        self.action = action
        self.target = target

class StepSynchronousProduct(SemanticTransitionRelation):
    def __int__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        r = []
        for lc in self.lhs.initial():
            for rc in self.rhs.initial():
                r.append((lc,rc))
        return r

    def enabledActions(self, source):
        ls, rs = source
        syncA = []
        lhs_enA = self.lhs.enabledActions(ls)
        nomActions = sizeof(lhs_enA)
        for la in lhs_enA:
            ltargets = self.lhs.execute(la, ls)
            if sizeof(ltargets) == 0:
                nomActions -= 1
            for lt in ltargets:
                rhs_enA = self.rhs.enabledActions(Step(ls, Action(la), lt), rs)
                syncA.extend(map(lambda re: (Step, re), rhs_enA))

        if nomActions == 0:
            step = Step(ls, Stutter(), ls)
            rhs_enA = self.rhs.enabledActions(Step, rs)
            syncA.extend(map(lambda ra: (Step, ra), rhs_enA))

        return syncA

    def execute(self, action, source):
        ls, rs = source
        step, ra = action
        r_T = self.rhs.execute(ra, step, rs)
        return map(lambda rt: (step.target, rt), r_T)


