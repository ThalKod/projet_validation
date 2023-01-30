from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class IdentityProxy():
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.get.rand, attr)


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        neighbors = self.operand.roots()

    def next(self, source):
        neighbors = self.operand.next(source)


class ReplaceRootsProxy(IdentityProxy):

    def __init__(self, operand, newRoots):
        super().__init__(operand)
        self.newRoots = newRoots

    def roots(self):
        return self.newRoots


class SemanticTransitionRelation:
    def intialConfigurations(self):
        pass

    def enabledActions(self, source):
        pass

    def execute(self, action, source):
        pass


class inputSemanticTransitionRelation():
    def initialConfigurations(self):
        pass

    def enabledActions(self, input, source):
        pass
    def execute(self, action, input, source):
        pass

class STR2TR(TransitionRelation):
    def __init__(self, op):
        self.operand = op

    def roots(self):
        return self.operand.intialConfigurations()

    def next(self, source):
        R = []
        for a in self.operand.enabledActions(source):
            r = self.operand.execute(source, a)
            R.append(r)
        return R


class StepSynchronousProduct(SemanticTransitionRelation):
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs
    def initial(self):
        r = []
        for lc in lhs.initial():
            for rc in rhs.initial():
                r.append((lc,rc))
        return r
    def enabledActions(self, source):
        ls, rs = source
        SyncA = []
        lhs_enA = self.lhs.enabledActions(ls)
        numActions = length(lhs_enA)
        pass