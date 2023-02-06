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
        return getattr(self.operand, attr)

    def initial(self):
        return self.operand.initial()


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict = {}):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        neighbors = self.operand.roots()

    def next(self, source):
        neighbors = self.operand.next(source)
        for n in neighbors:
            if n not in self.parent:
                self.dict[n] = source, None
        return neighbors


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
            R.extend(r)
        return R

    def initial(self):
        return self.operand.initialConfigurations()




class IsAcceptingProxy(IdentityProxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate

    def isAccepting(self, c):
        return self.predicate(c)